<html>
<body>
<p>Welcome to SQL Injection Lab.</p>
<?php
    //$c = mysqli_connect("localhost", "root", "password", "users");
    $c = mysqli_connect("localhost", "root", "", "users");
    if(!$c){
 	echo('Could not connect to db. Contact someone who can help'. mysql_error());
    }

    echo("Hi");

    $user = $_GET['user'] or die('<pre> user was not specified</pre>' );
    $pwd = $_GET['pwd'] or die('<pre> pwd was not specified</pre>' );

    //echo($id);

    $query = "SELECT first_name, last_name FROM t_users WHERE last_name = '".$user."' AND '".$pwd."' = 'p4$$w0rd'";
    echo($query);
 
    $result = mysqli_query($c, $query) or die('<pre>' . mysql_error() . '</pre>' );

    if ($result && mysqli_num_rows($result) != 0) {
    //     $row = mysqli_fetch_assoc($result);
    // 	echo("<p>Hello " . $row['first_name']." ". $row['last_name'] . "!</p>");
        while($row = mysqli_fetch_assoc($result)) {
    		echo("<p>Hello " . $row['first_name']." ". $row['last_name'] . "!</p>");
	}
    }
    mysqli_close($c);
?>

</body>
</html>


