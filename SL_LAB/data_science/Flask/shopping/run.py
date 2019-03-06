from flask import Flask, render_template, request, url_for, session, redirect

app=Flask(__name__)

app.secret_key = 'secret'

@app.route("/", methods=['GET', 'POST'])
def store():
	if(request.method=='GET'):
		return render_template('store.html')
	if(request.method=='POST'):
		for item in ['egg', 'milk', 'bread']:
			if(item not in session):
				session[item]=int(request.form[item])
			else:
				session[item]+=int(request.form[item])
		return(redirect(url_for('cart')))

@app.route("/cart", methods=['GET', 'POST'])
def cart():
	cart=list()
	for item in ['egg', 'milk', 'bread']:
		cart.append({ 'name':item,'quantity':session[item] })
	return (render_template('cart.html', cart=cart))

@app.route("/buy", methods=['GET', 'POST'])
def buy():
	amount=0
	cart=list()
	price=[5,12,22]
	index=0
	amount=0
	for item in ['egg', 'milk', 'bread']:
		cart.append({'name':item, 'quantity':session[item], 'price':session[item]*price[index]})
		amount+=session[item]*price[index]
		index+=1
	return (render_template('bill.html', cart=cart,amount=amount))

if(__name__=='__main__'):
	app.run(debug=True)