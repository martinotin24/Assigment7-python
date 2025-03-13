<!DOCTYPE html>
<html>
<head>
  <title>Integer Bitwise Operations</title>
</head>
<body>
  <h1>SERVER 1/2 - MARTIN MUNOZ</h1>
  <h2>Enter Integers for Bitwise Operations</h2>
  <form action="process.php" method="GET">
    <label for="numbers">Integers (separated by commas):</label><br>
    <input type="text" name="numbers" id="numbers" placeholder="e.g., 3,5,7,9" required><br><br>
    
    <label for="threshold">Threshold:</label><br>
    <input type="number" name="threshold" id="threshold" placeholder="e.g., 4" required><br><br>
    
    <input type="submit" value="Submit">
  </form>
</body>
</html>
