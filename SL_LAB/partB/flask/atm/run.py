from flask import Flask, request, render_template, session, url_for

app=Flask(__name__)

app.secret_key="secret"
@app.route("/", methods=['GET', 'POST'])
def index():
	if(request.method=='GET'):
		session.clear()
		try:
			balance=session['balance']
			count=session['count']
		except KeyError:
			balance=session['balance']=8000
			count=session['count']=0
			msg="Welcome User"
			return(render_template('atm.html',msg=msg,balance=balance))
	
	if(request.method=='POST'):
		amt=request.form['amt']
		balance=session['balance']
		if(request.form['amt']==''):
			msg='please enter the ammount field.'
			return(render_template('atm.html',msg=msg,balance=balance))
		elif(int(amt)<0):
			msg='ammount cannot be negative.'
			return(render_template('atm.html',msg=msg,balance=session['balance']))
		elif(session['count']==5):
			msg ='your no of transactions: '+str(session['count'])+' you cannot make more than 5 transactions.'
			return(render_template('atm.html',msg=msg,balance=balance))
		
		else:
			if(request.form['action']=='withdraw'):
				if(int(amt)>5000):
					msg='you cannot withdraw more than 5000 at a time.'
					return(render_template('atm.html',msg=msg,balance=balance))
				elif(int(amt) > session['balance']):
					msg='your have less balance: ',session['balance']
					return(render_template('atm.html',msg=msg,balance=session['balance']))
				
				else:
					balance=session['balance']=session['balance']-int(amt)
					count=session['count']=session['count']+1
					msg='withdrawn successfully.'
					return(render_template('atm.html',msg=msg,balance=balance))
			
			if(request.form["action"]=='deposit'):
				if(int(amt)>100000):
					msg='you cannot deposit more than 100000 at a time'
					return(render_template('atm.html',msg=msg,balance=balance))
				else:
					balance=session['balance']=session['balance']+int(amt)
					count=session['count']=session['count']+1
					msg='deposited successfully'
					return(render_template('atm.html',msg=msg,balance=balance))
if(__name__=='__main__'):
	app.run(debug=True)
