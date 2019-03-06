from flask import Flask,request,url_for,session,render_template,session,redirect

app=Flask(__name__)

app.secret_key="secret"

@app.route('/', methods=['GET','POST'])
def store():
	if(request.method=='GET'):
		return(render_template('shop.html'))
	if(request.method=='POST'):
		item=['biscuit', 'bread', 'jam', 'milk']
		for i in item:
			if(i not in session):
				session[i]=int(request.form[i])
			else:
				session[i]+=int(request.form[i])
	return(redirect(url_for('cart')))

@app.route('/cart',methods=['GET','POST'])
def cart():
	cart=[]
	item=['biscuit', 'bread', 'jam', 'milk']
	for i in item:
		cart.append({'name':i,'quantity':session[i]})
	return(render_template('cart.html',cart=cart))

@app.route('/bill',methods=['GET','POST'])
def bill():
	item=['biscuit', 'bread', 'jam', 'milk']
	price=[10,20,30,15]
	cart=[]
	index=0
	amt=0
	for i in item:
		amt=amt+session[i]*price[index]
		cart.append({'name':i, 'quantity':session[i], 'price':session[i]*price[index]})
		index+=1
	return(render_template('bill.html', cart=cart,amt=amt))

if(__name__=='__main__'):
	app.run(debug = True)
