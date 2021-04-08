<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta http-equiv="X-UA-Compatible" content="IE=edge">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Search for Admins</title>
</head>
<body>
    <form action="/" method="get">
        <input type="text" name="q" placeholder="Name..">
        <button type="submit">Search</button>
    <h1>
<?php
define("DB_SERVER", "localhost");
define("DB_USERNAME", "[DB_USERNAME]");
define("DB_PASSWORD", "[DB_PASSWORD]");
define("DB_DATABASE", "search_admin2");

$db = new mysqli(DB_SERVER, DB_USERNAME,DB_PASSWORD, DB_DATABASE);
$db -> set_charset("utf-8");

$search_value = $_GET["q"];

if (isset($search_value) && strlen($search_value) != 0 && strlen($search_value) < 15) {
    if ($db -> connect_error) {
        echo 'Connection Faild: '.$db->connect_error;
    } else {
        $query = "SELECT * from creds WHERE name='$search_value'";
        $res = $db->query($query);
        if(!$res) {
            $error = $db->error;
            echo $error;
        } else {
        if(mysqli_num_rows($res) > 0) {
            while($row = mysqli_fetch_assoc($res)) {
                    echo "Name: " . $row["name"] . " FLAG: " . $row["flag"];
            }
        } else {
            echo "0 results!";
        }
        }
    }
    mysqli_close($db);
}

?>
    </h1>
    </form>
</body>
</html>
