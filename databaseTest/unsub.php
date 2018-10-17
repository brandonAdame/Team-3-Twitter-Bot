<?php

require "connect.php";

if(isset($_GET['id'])) {
$id = mysqli_real_escape_string($myConnection, $_GET['id']);
$sql = "SELECT * FROM events WHERE idNumber=$id LIMIT 1";
}else if (isset($_GET['twitterAccount'])){
$twitterAccount = mysqli_real_escape_string($myConnection, $_GET['twitterAccount']);
$sql = "SELECT * FROM events WHERE twitterAccount=\"$twitterAccount\"";
}else{
echo "No comand given, nothing was deleted.";
}

$count = 0;

$result = mysqli_query($myConnection, $sql) or die(mysqli_error($myConnection));
	while($row = mysqli_fetch_array($result)) {
	++$count;
		$id = $row['idNumber'];
		$eventType = $row['eventType'];
		$result = mysqli_query($myConnection, "DELETE FROM `events` WHERE `idNumber` = $id;") or die(mysqli_error($myConnection));

		if ($eventType == "localWeather"){
			$result = mysqli_query($myConnection, "DELETE FROM `localWeather` WHERE `idNumber` = $id;") or die(mysqli_error($myConnection));
		}else if ($eventType == "dailyStocks"){
			$result = mysqli_query($myConnection, "DELETE FROM `dailyStocks` WHERE `idNumber` = $id;") or die(mysqli_error($myConnection));
		}

	echo "Deleted event #$id ($eventType)\n";

	}

if ($count == 0){echo "No events matched query.  No events where deleted.";}

?>