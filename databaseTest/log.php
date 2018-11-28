<?php
require "connect.php";

if(isset($_GET['lastActive'])) {
header('Content-Type: text/plain');
	$lastAction = mysqli_real_escape_string($myConnection, $_GET['lastActive']);
	$result = mysqli_query($myConnection, "SELECT * FROM `log` WHERE script='$lastAction' LIMIT 1") or die(mysqli_error($myConnection));
		while($row = mysqli_fetch_array($result)) {
		$date = $row['date'];
		echo $date;
		}

}else{

	if(isset($_GET['action'])) {$action = mysqli_real_escape_string($myConnection, $_GET['action']);}else{$action = "add";}

	if ($action == "add"){

		if(isset($_GET['script'])) {$script = mysqli_real_escape_string($myConnection, $_GET['script']);}
		else{$script = "main.py";}
		if(isset($_GET['type'])) {$type = mysqli_real_escape_string($myConnection, $_GET['type']);}
		else{$type = "Undefined";}
		if(isset($_GET['message'])) {$message = mysqli_real_escape_string($myConnection, $_GET['message']);

		$result = mysqli_query($myConnection, "INSERT INTO `log` (`script`, `type`, `message`) VALUES ('$script', '$type', '$message');") or die(mysqli_error($myConnection));

		echo "Added message to database";

		}else{
		echo "No message defined.  Nothing added to database.";
		}

	}else if ($action == "get"){

		$sql = "SELECT * FROM `log` WHERE TRUE";
		

		if(isset($_GET['script'])) {
			$script = mysqli_real_escape_string($myConnection, $_GET['script']);
			$sql = $sql . " AND `script` = '$script'";
		}
		if(isset($_GET['type'])) {
			$type = mysqli_real_escape_string($myConnection, $_GET['type']);
			$sql = $sql . " AND `type` = '$type'";
		}

		$sql = $sql . " ORDER BY `date` DESC LIMIT 25";

		echo"{\"log\":[";
	$i=0;
		$result = mysqli_query($myConnection, $sql) or die(mysqli_error($myConnection));
		while($row = mysqli_fetch_array($result)) {
			$id = $row['id'];
			$script = $row['script'];
			$type = $row['type'];
			$message = $row['message'];
			$date = $row['date'];
			if ($i != 0){echo",";}
			echo "{\"id\": \"$id\", \"date\" : \"$date\", \"type\" : \"$type\", \"script\" : \"$script\", \"message\" : \"$message\"}";
			$i = $i + 1;
		}

		echo "]}";
		header('Content-Type: application/json');

	}

}

?>