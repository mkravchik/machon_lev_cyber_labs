<html>
<body>
<p>Welcome to SQL Injection Lab.</p>
<?php
    //$c = mysqli_connect("localhost", "root", "password", "users");
    $c = mysqli_connect("localhost", "root", "", "users");
    if(!$c){
 	echo('Could not connect to db. Contact someone who can help'. mysqli_connect_error());
    }

    $id = $_GET['id'] or die('<pre> id was not specified</pre>' );

    //echo($id);

    $query = "SELECT first_name, last_name FROM t_users WHERE user_id = '".$id."'";
    echo($query);
 
    $result = mysqli_query($c, $query) or die('<pre>' . mysqli_error($c) . '</pre>' );

    if ($result && mysqli_num_rows($result) != 0) {
        while($row = mysqli_fetch_assoc($result)) {
    		echo("<p>Hello " . $row['first_name']." ". $row['last_name'] . "!</p>");
	}
    }
    mysqli_close($c);
?>

</body>
</html>



