var now_year = new Date();
now_year = now_year.getFullYear();
var list = document.getElementsByName('age');
for(let i=0,l=list.length;i<l;i++){
	let j=list[i].innerHTML;
	parseInt(j);
	var age = now_year - j;
	list[i].innerHTML = age;
}
var list = document.getElementsByName('child_age'); 
for(let i=0,l=list.length;i<l;i++){ 	
	let j=list[i].innerHTML; 	
	parseInt(j); 	
	let age = now_year - j; 	
	list[i].innerHTML = age; 
}