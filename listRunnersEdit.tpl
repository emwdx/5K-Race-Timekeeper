<!DOCTYPE html>
<html lang="en">

<head>
<title>TimeKeeper</title>
<link rel="stylesheet" type="text/css" href="/static/bootstrap/css/bootstrap.css">
</head>

<body>
<h2>Select the runner you wish to edit:</h2>
<div class = "span6 offset3">
<div class = "row-fluid">
<table class="table table-bordered table-hover">
%for runner in runners:
    <tr><td>
    <b>{{runner[0]}}</b></td><td>{{runner[1]}}</td><td>{{runner[2]}}</td><td><a href = "/editRunner/{{runner[0]}}"><button class = "btn">Edit</button></a></td></tr>
%end
</table>
</div>
</div>


</body>