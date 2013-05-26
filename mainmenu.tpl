

<!DOCTYPE html>
<html lang="en">

<head>
<title>2013 Dragon Run TimeKeeper</title>
<link rel="stylesheet" type="text/css" href="/static/bootstrap/css/bootstrap.css">

</head>

<body>
<div class = "container">
<div class = "row-fluid">
<p class = "text-center"><img src = "/static/timekeeper/small_drun.png"></p>
</div>
</div>
<hr>
<div class = "container">
<div class = "row-fluid">
<div class = "buttons" style = "width:600px; margin-left:auto; margin-right:auto; margin-top: 30px;margin-bottom:30px; float: none; ">

<div class="btn-group ">
  <a href = "/mobile/"><button class="btn btn-primary"><h1>Mobile Site</h1></button></a>
   <a href = "/stopRunner/"><button class="btn btn-primary"><h1>Desktop Site</h1></button></a>
 
</div>
</div>
</div>
</div>
<hr>


<h1>Select runners:</h1>
<div class = "container">
<div class = "row-fluid">
<div class="btn-group ">
  <a href = "/men/"><button class="btn btn-primary"><h3>Men</h3></button></a>
  <a href = "/women/"><button class="btn btn-primary"><h3>Women</h3></button></a>
  <a href = "/HSmale/"><button class="btn btn-primary"><h3>HS Male</h3></button></a>
  <a href = "/HSfemale/"><button class= "btn btn-primary"><h3>HS Female</h3></button></a>
  <a href = "/MSmale/"><button class="btn btn-primary"><h3>MS Male</h3></button></a>
  <a href = "/MSfemale/"><button class= "btn btn-primary"><h3>MS Female</h3></button></a>
  <a href = "/LSmale/"><button class= "btn btn-primary"><h3>LS Male</h3></button></a>
  <a href = "/LSfemale/"><button class= "btn btn-primary"><h3>LS Female</h3></button></a>
</div>
</div>
</div>
<hr>

<h1>Race Results:</h1>

<div class = "container">
<div class = "row-fluid">

<div class="btn-group ">
  <a href = "/men/results/"><button class="btn btn-primary"><h3>Men</h3></button></a>
  <a href = "/women/results/"><button class="btn btn-primary"><h3>Women</h3></button></a>
  <a href = "/HSmale/results/"><button class="btn btn-primary"><h3>HS Male</h3></button></a>
  <a href = "/HSfemale/results/"><button class= "btn btn-primary"><h3>HS Female</h3></button></a>
  <a href = "/MSmale/results/"><button class="btn btn-primary"><h3>MS Male</h3></button></a>
  <a href = "/MSfemale/results/"><button class= "btn btn-primary"><h3>MS Female</h3></button></a>
  <a href = "/LSmale/results/"><button class= "btn btn-primary"><h3>LS Male</h3></button></a>
  <a href = "/LSfemale/results/"><button class= "btn btn-primary"><h3>LS Female</h3></button></a>
</div>
</div>
</div>

<hr>

<div class = "container">
<form class = "form-inline" action = "/admin/" method = "POST">
Enter race password:
<input type = "password" name = "password" class = "input-small" value = "notthepassword"/>
<select name = 'adminoption'>
  <option value = '1'>Start Race</option>
  <option value = '2'>Edit Runner</option>
  <option value = '3'>Add Runner</option>
  <option value = '4'>Load & Reset Data</option>
  <option value = '5'>Save Race Data</option>
  
</select>

<button type = "submit" class = "btn">Submit</button>
</form>

</div>
</div>


</div>

</div>
</body>