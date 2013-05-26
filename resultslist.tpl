<!DOCTYPE html>
<html lang="en">

<head>
<title>TimeKeeper</title>
<link rel="stylesheet" type="text/css" href="/static/bootstrap/css/bootstrap.css">
</head>


<body>

<div class = "container-fluid">
<div class = "row-fluid">
<p class = "text-center"><img src = "/static/timekeeper/small_drun.png"></p>
</div>



<div class = "row-fluid">
<h2><p class = "text-center">2013 5K Run Results - {{category}}</p></h2>
</div>
</div>

<div class = "results" style = "width:600px; margin-left:auto; margin-right:auto; margin-top: 30px;margin-bottom:30px; float: none; ">
<div class = "row-fluid">
<table class="table table-bordered table-hover">
<thead>
<tr><td>Rank</td><td>Runner #</td><td>Name</td><td>Finish Time</td></tr></thead>
<tbody>
%rank = 0
%for runner in runners:
%rank +=1
    <tr><td>
    <b>{{rank}}</b></td><td><b>{{runner[0]}}</b></td><td>{{runner[1]}}</td><td>{{runner[2]}}</td></tr>
%end
</tbody>
</table>
</div>
</div>

</body>
</html>
