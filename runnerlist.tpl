<!DOCTYPE html>
<html lang="en">

<head>
<title>TimeKeeper</title>
<link rel="stylesheet" type="text/css" href="/static/bootstrap/css/bootstrap.css">

</head>

<body>

<div class = "span6 offset3">
<div class = "row-fluid">
<table class="table table-bordered table-hover">
%for runner in runners:
    <tr><td>
    <b>{{runner[0]}}</b></td><td>{{runner[1]}}</td><td>{{runner[2]}}</td><td><a href = "/stoptime/{{runner[0]}}"><button class = "btn">Stop Time</button></a></td></tr>
%end
</table>
</div>
</div>



<div class = "span6 offset3">
<div class = "row-fluid">
Finished Runners:
<table class="table table-bordered table-hover">
%for runner in finished:
    <tr><td>
    <b>{{runner[0]}}</b></td><td>{{runner[1]}}</td><td>{{runner[2]}}</td><td><a href = "/restarttime/{{runner[0]}}"><button class = "btn">Return to List</button></a></td></tr>
%end
</table>
</div>
</div>

</body>