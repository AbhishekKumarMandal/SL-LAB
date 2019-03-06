from flask import Flask, url_for, render_template, request,session

app=Flask(__name__)

app.secret_key = "secret"

balance=8000

@app.route("/",methods=['GET', 'POST'])
def index():
	if(request.method=='GET'):
		msg="Welcome User"
		return render_template('atm.html',balance=balance,msg=msg)
	if(request.method == 'POST'):
		amt=int(request.form['amt'])
		if(request.form['amt']==""):
			msg="please fill ammount field"
			return render_template('atm.html', balance=balance, msg=msg)
		if(amt<0):
			msg="ammount cannot be negative."
			return render_template('atm.html', balance=balance, msg=msg)
		 # if(session['count']==5):
		 # 	msg="5 transactions completed cannot process request."
		 # 	return render_template('atm.html', balance=balance, msg=msg)

@app.route("/dep",methods=['GET', 'POST'])
def deposit():
	if(request.method=='POST'):
		amt=int(request.form['amt'])
		if(amt>10000):
			msg="you cannot deposit more than 10000 at a time."
			return render_template('atm.html', balance=balance, msg=msg)
		else:
			balance=session['balance']+amt
			#session['count']=session['count']+1
			msg="your current balance is "+balance+" Rs/-"
			return render_template('atm.html', balance=balance, msg=msg)
			#if(request.form['action']=="withdraw"):
@app.route("/with", methods=['GET','POST'])
def withdraw():
	if(request.method=='POST'):
		amt=int(request.form['amt'])
		if(amt>5000):
			msg="cannot withdraw more than 5000 at a time."
			return render_template('atm.html', balance=balance, msg=msg)
		elif(amt>session['balance']):
			msg="you cannot withdraw "+amt+" your balance is "+session['balance']+"Rs/-"
			return render_template('atm.html',balance=balance, msg=msg)
		else:
			balance=session['balance']-amt
			session['count']=session['count']+1

if(__name__== '__main__'):
	app.run()