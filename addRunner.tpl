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
<h2>Enter all runner information below:</h2>

<form class = "form-horizontal" action = "/addRunner/" method = "POST">

<div class="control-group">
Runner Number:<input type = "text" name = "runnerID" class = "input-small" />
Name:<input type = "text" name = "name" class = "input-large"/>
</div>
<div class="control-group">
Gender: <select name = 'gender'>
  <option value = 'M' >M</option>
  <option value = 'F' >F</option>
   
</select>
Age:
<select name = 'age'>
  <option value = 'LS' >Lower School</option>
  <option value = 'MS' >Middle School</option>
  <option value = 'HS'>High School</option>
  <option value = 'A' >Adult</option>
   
</select>
Category:
<select name = 'category'>
  <option value = '0' >0</option>
  <option value = '1' >1</option>
  <option value = '2'>2</option>
  <option value = '3' >3</option>
  <option value = '4' >4</option>
  <option value = '5'>Fun Run</option>
  
</select>
</div>
<button type = "submit" class = "btn">Submit</button>
</form>