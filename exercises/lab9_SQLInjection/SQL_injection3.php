<html>
<body>
<p>Welcome to SQL Injection Lab.</p>
<?php
    //$c = mysqli_connect("localhost", "root", "password", "users");
    $c = mysqli_connect("localhost", "root", "", "users");
    if(!$c){
 	echo('Could not connect to db. Contact someone who can help'. mysql_error());
    }

    $id = $_GET['id'] or die('<pre> id was not specified</pre>' );
    $stmt = mysqli_prepare($c, "SELECT first_name, last_name FROM t_users WHERE user_id=?"); 
    mysqli_stmt_bind_param($stmt, "i", $_GET['id']);
 
     echo("<p><b>Running query with bound parameters:</b></p>");
   // execute query
    if (!$stmt->execute()) {
        echo "Execute failed: (" . $stmt->errno . ") " . $stmt->error;
    }

    /* bind result variables */
    $first_name    = NULL;
    $last_name = NULL;
    if (!$stmt->bind_result($first_name, $last_name)) {
        echo "Binding output parameters failed: (" . $stmt->errno . ") " . $stmt->error;
    }

    while ($stmt->fetch()) {
    	echo("<p>Hello " . $first_name." ". $last_name . "!</p>");

    }

     /* close statement */
    mysqli_stmt_close($stmt);
    mysqli_close($c);
?>

</body>
</html>



