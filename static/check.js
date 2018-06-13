function check()	{
	var u, p;
	u = document.signin_form.uname.value;
	p = document.signin_form.pass.value;
	if(u == "")
		alert("No username");
	else if((u == "") && (p == ""))
		alert("No username and password");
	else if(p == "")
		alert("No password");

}