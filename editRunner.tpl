<!DOCTYPE html>
<html lang="en">

<head>
<title>2013 Dragon Run TimeKeeper</title>
<link rel="stylesheet" type="text/css" href="/static/bootstrap/css/bootstrap.css">

</head>

<body>
<div class = "container-fluid">
<div class = "row-fluid">
<p class = "text-center"><img src = "/static/timekeeper/small_drun.png"></p>
</div>
</div>


<hr>
<h2>Edit runner information below:</h2>

<form class = "form-horizontal" action = "/editRunner/" method = "POST">

<div class="control-group">
Runner Number:<input type = "text" name = "runnerID" class = "input-small" value = "{{runner[0]}}"/>
Name:<input type = "text" name = "name" class = "input-large" value = "{{runner[1]}}"/>
</div>
<div class="control-group">
Gender: <select name = 'gender'>
  <option value = 'M' {{runner[2][0]}}>M</option>
  <option value = 'F' {{runner[2][1]}}>F</option>
   
</select>
Age:
<select name = 'age'>
  <option value = 'LS' {{runner[3][0]}}>Lower School</option>
  <option value = 'MS' {{runner[3][1]}}>Middle School</option>
  <option value = 'HS' {{runner[3][2]}}>High School</option>
  <option value = 'A' {{runner[3][3]}}>Adult</option>
   
</select>
Category:
<select name = 'category'>
  <option value = '0' {{runner[4][0]}}>0</option>
  <option value = '1' {{runner[4][1]}}>1</option>
  <option value = '2' {{runner[4][2]}}>2</option>
  <option value = '3' {{runner[4][3]}}>3</option>
  <option value = '4' {{runner[4][4]}}>4</option>
  <option value = '5' {{runner[4][5]}}>Fun Run</option>
  
</select>
</div>

<div class="control-group">
Has Finished the race?
<input type = "checkbox" name = "hasFinished" {{runner[5]}}  /><p><p>

Finish Time:<input type = "text" name = "finishTime" class = "input-small" value = "{{runner[6]}}"/>
</div>
<button type = "submit" class = "btn">Submit</button>
</form>