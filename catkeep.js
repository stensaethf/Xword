
var cat1 = document.getElementById('dd1');
var cat2 = document.getElementById('dd2');
var cat3 = document.getElementById('dd3');
var cat4 = document.getElementById('dd4');
var cat5 = document.getElementById('dd5');

function forward(){
	if (cat1 != null){
		document.getElementById('Category1').value = "on";
	}
	if (cat2 != null){
		document.getElementById('Category2').value = "on";
	}
	if (cat3 != null){
		document.getElementById('Category3').value = "on";
	}
	if (cat4 != null){
		document.getElementById('Category4').value = "on";
	}
	if (cat5 != null){
		document.getElementById('Category5').value = "on";
	}
}