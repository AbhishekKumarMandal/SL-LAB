window.onload=function(){
	
	document.getElementById('num').value="";
	document.getElementById('res').innerHTML="";
	document.getElementById('div3').checked = false;
	document.getElementById('div7').checked = false;
	};
	
	function fun1()
	{
		var num;
		num = document.getElementById("num").value;
		if(isNaN(num))
			document.getElementById('res').innerHTML="<br>"+"not a number"+"<br>";
		else if(num%3==0)
			document.getElementById('res').innerHTML="<br>"+"divisible by 3"+"<br>";
		else
			document.getElementById('res').innerHTML="<br>"+"not divisible by 3"+"<br>";
	}
	
	
	function fun2()
	{
		var num;
		num = document.getElementById("num").value;
		if(isNaN(num))
			document.getElementById('res').innerHTML="<br>"+"not a number"+"<br>";
		else if(num%7==0)
			document.getElementById('res').innerHTML="<br>"+"divisible by 7"+"<br>";
		else
			document.getElementById('res').innerHTML="<br>"+"not divisible by 7"+"<br>";
	}
