<!DOCTYPE html>
<html lang="en">

<head>
<title>2013 Dragon Run TimeKeeper</title>

<link rel="stylesheet" type="text/css" href="/static/bootstrap/css/bootstrap.css">
<script src = "/static/jquery/jquery-1.6.4.min.js"></script>

</head>

<body>
<div class = "container-fluid">
<div class = "row-fluid">
<p class = "text-center"><img src = "/static/timekeeper/small_drun.png"></p>
</div>
</div>
<div class = "container-fluid">
<div class = "row-fluid">
<h1>{{message}}</h1>
</div>
</div>
<div id = "lastRunners">
<p class = "text-info text-center"><h3>Last runners stopped: <table class="table table-bordered"><tr>{{!lastrunners}}</tr></table></h3></p>
</div>
<hr>
<h2>Enter the runner number: </h2>

<form action = "/stopTime/" id = "runnerEntry" method = "POST">

<input type = "text" name = "runnerID" id = "entry"/><p>
<button type = "submit" class = "btn" id = "stopRunner">Stop</button>


</form>
<a href = "/"><button type = "submit" class = "btn">Back to Main Menu</button></a>
</body>
</html>
<script>
$(document).ready(function($){
	
	$('#entry').focus();
		
});


	
function checkSubmit(e)
{
   if(e && e.keyCode == 13)
   {
      document.forms[0].submit();
   }
}
</script>