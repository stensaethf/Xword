document.getElementById("lf").disabled = false;
									document.getElementById("lf2").disabled = false;


									var dis1 = document.getElementById("lf");
									dis1.onchange = function () {
									   if (this.value != "" || this.value.length > 0) {
									      document.getElementById("lf2").disabled = true;
									      document.getElementById("lf2").style.backgroundColor="grey";
									   } else {
									      document.getElementById("lf2").disabled = false;
									      document.getElementById("lf2").style.backgroundColor="white";
									   }
									}

									var dis2 = document.getElementById("lf2");
									dis2.onchange = function () {
									   if (this.value != "" || this.value.length > 0) {
									      document.getElementById("lf").disabled = true;
									      document.getElementById("lf").style.backgroundColor="grey";
									   } else {
									      document.getElementById("lf").disabled = false;
									      document.getElementById("lf").style.backgroundColor="white";
									   }
									}