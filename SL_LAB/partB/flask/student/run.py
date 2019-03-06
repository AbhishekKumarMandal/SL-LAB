from flask import Flask, render_template, request, url_for

import re
import datetime

app=Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
	if(request.method=='GET'):
		msg='Welcome Student'
		return render_template('student.html', msg=msg)
	if(request.method=='POST'):
		if(request.form['usn']==""  or  request.form['date']==""  or  request.form['m1']==""  or  request.form['m2']==""  or  request.form['m3']==""):
			msg="please specify the field"
			return (render_template('student.html', msg=msg))
		
		else:
			try:
				datetime.datetime.strptime(request.form['date'],'%d-%m-%Y')
			except ValueError:
				msg="date fromat invalid. Valid format should be DD-MM-YYYY"
				return(render_template('student.html',msg=msg))
			
			usn_pattern="^[1][A-Z][A-Z][0-9][0-9][A-Z][A-Z][0-9][0-9][0-9]$"

			if(not re.match(usn_pattern,request.form['usn'])):
				msg="invalid usn"
				return(render_template('student.html',msg=msg))
			m1=int(request.form['m1'])
			m2=int(request.form['m2'])
			m3=int(request.form['m3'])
			m=(m1+m2+m3)/3
			msg='average of marks is: '+str(round(m))
			return(render_template('student.html', msg=msg))
if(__name__=='__main__'):
	app.run(debug=True)			
