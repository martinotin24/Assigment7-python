<?php
if (isset($_GET['numbers'])) {
    $numbers = $_GET['numbers'];
    // Use a default threshold of 0 if not provided
    $threshold = isset($_GET['threshold']) ? $_GET['threshold'] : 0;
    
    // Build the command to execute the Python script securely
    $command = escapeshellcmd("python3 bitwise_operations.py --numbers \"$numbers\" --threshold $threshold");
    $output = shell_exec($command);
    
    // Display the output, converting newlines to HTML breaks
    echo nl2br($output);
} else {
    echo "No numbers provided. Please input a comma-separated list of integers.";
}
?>
