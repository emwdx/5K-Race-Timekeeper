
$(document).ready(function() { 
	if(runnerID==99999){
	//alert("Runner already stopped");
	}
	else if(runnerID==99998){
	
	//alert("Runner not found");
	
	}
	else if (runnerID ==99997){
	
	//alert("Welcome to the mobile site!");
	
	}
	else{
	msg = "Runner "+ runnerID + " stopped";
	//alert(msg);
	}
	
	$('.num').bind('touchend', function(){
	numText = $(this).text();
	currText = $('#stoptime').text();
	currText = currText.replace("Stop","")  + numText;
	
	
	
	
	$('#stoptime').text('Stop ' + currText);
	
	
	});
	
	
	$('.clr').bind('vclick',function(){
	$('#stoptime').text('Stop ');
	});
	
	$('.del').bind('vclick',function(){
	currText = $('#stoptime').text();
	
	
	$('#stoptime').text(currText.slice(0,-1));
	
	});
	
	$('#stoptime').touchend( function() {
	
	if($('#stoptime').text()=='Stop'){
	$('#stoptime').attr("href",'javascript:;')
	}
	else{	
	link = '/mobile/stoptime/' + $('#stoptime').text().replace("Stop", "").trim();
	
	$('#stoptime').attr("href",link);
	
	}
	});
	
	$('#stoptime').swipe( function(){
	$('#stoptime').text('Stop ');
	
	});
	
	
	
});