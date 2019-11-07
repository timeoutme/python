var now_year = new Date();
now_year = now_year.getFullYear();
var list = document.getElementsByName('age');
for(var i=0,l=list.length;i<l;i++){
	var j=list[i].innerHTML;
	parseInt(j);
	var age = now_year - j;
	list[i].innerHTML = age;
}