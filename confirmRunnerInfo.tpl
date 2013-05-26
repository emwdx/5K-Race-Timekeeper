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
<h2>Here is the information you entered:</h2>

<div class = "span8 offset3">
<div class = "row-fluid">
<form class="form-horizontal" action = "/insertRunner/" method = "POST">
  <div class="control-group">
    <label class="control-label" for="runnerID">Runner Number:</label>
    <div class="controls">
      <input type="text" id="runnerID" name = "runnerID" value = "{{runner[0]}}" readOnly="true">
    </div>
  </div>
  <div class="control-group">
    <label class="control-label" for="name">Name:</label>
    <div class="controls">
      <input type="text" id="name" name = "name" value = "{{runner[1]}}" readOnly="true" >
    </div>
  </div>
  <div class="control-group">
    <label class="control-label" for="gender">Gender:</label>
    <div class="controls">
      <input type="text" id="gender" name = "gender" value = "{{runner[2]}}" readOnly="true" >
    </div>
  </div>
  <div class="control-group">
    <label class="control-label" for="age">Age Category:</label>
    <div class="controls">
      <input type="text" id="age" name = "age" value = "{{runner[3]}}" readOnly="true" >
    </div>
  </div>
  <div class="control-group">
    <label class="control-label" for="category">Runner Category:</label>
    <div class="controls">
      <input type="text" id="category" name = "category" value = "{{runner[4]}}" readOnly="true" >
    </div>
  </div>
  <div class="form-actions">
  <button type="submit" class="btn btn-primary">Confirm</button>
  <a href = "/addRunner/"><button type="button" class="btn">Go Back</button></a>
</div>
  
</form>


</div></div>
</body>
</html>