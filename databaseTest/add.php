<?php
require "connect.php";
//header('Content-Type: application/json');

$goodEventType = false;
$twitterAccount = mysqli_real_escape_string($myConnection, $_GET['twitterAccount']);
$eventType = mysqli_real_escape_string($myConnection, $_GET['eventType']);
$lastRunTime = "2000-01-01 00:00:00";
$nextRunTime = new DateTime('tomorrow');

if($eventType == "dailyStocks") {
	$nextRunTime->setTime(5,30,0);
	$symbol = mysqli_real_escape_string($myConnection, $_GET['symbol']);
	$goodEventType = true;
}else if ($eventType == "localWeather"){
	$location = mysqli_real_escape_string($myConnection, $_GET['location']);
	$sendTime = mysqli_real_escape_string($myConnection, $_GET['sendTime']);
	$sendTimeExplode = explode(":",$sendTime);
	$nextRunTime->setTime((int)$sendTimeExplode[0], (int)$sendTimeExplode[1], (int)$sendTimeExplode[2]);
	$goodEventType = true;
}else if ($eventType == "dailyQuote"){
	$nextRunTime->setTime(8, 0, 0);
	$goodEventType = true;
}else if ($eventType == "dailyWord"){
	$nextRunTime->setTime(9, 0, 0);
	$goodEventType = true;
}else{
	echo "Unknown event type.  Did not add to database.";
}

if ($goodEventType){
	$nextRunTime_formatted = date_format($nextRunTime, 'Y-m-d H:i:s');
	//echo "INSERT INTO `events` (`idNumber`, `twitterAccount`, `eventType`, `nextRunTime`, `lastRunTime`) VALUES (NULL, '$twitterAccount', '$eventType', '$lastRunTime', '$nextRunTime_formatted');";
		$result = mysqli_query($myConnection, "INSERT INTO `events` (`idNumber`, `twitterAccount`, `eventType`, `nextRunTime`, `lastRunTime`) VALUES (NULL, '$twitterAccount', '$eventType', '$nextRunTime_formatted', '$lastRunTime');") or die(mysqli_error($myConnection));
		$id = mysqli_insert_id($myConnection);
	if($eventType == "dailyStocks") {
			$result = mysqli_query($myConnection, "INSERT INTO `dailyStocks` (`idNumber`, `symbol`) VALUES ($id, '$symbol');") or die(mysqli_error($myConnection));
	}else if ($eventType == "localWeather"){
			$result = mysqli_query($myConnection, "INSERT INTO `localWeather` (`idNumber`, `location`, `sendTime`) VALUES ($id, '$location', '$sendTime');") or die(mysqli_error($myConnection));
	}



echo "{\"events\":[";
		echo "{\"id\": \"$id\", \"twitterAccount\": \"$twitterAccount\", \"eventType\": \"$eventType\", \"nextRunTime\": \"$nextRunTime_formatted\", \"lastRunTime\":\"$lastRunTime\"";
		if ($eventType == "localWeather"){echo", \"location\": \"$location\", \"sendTime\": \"$sendTime\"";
		}else if ($eventType == "dailyStocks"){	echo ", \"symbol\": \"$symbol\"";}
echo "}";
echo "]}";
header('Content-Type: application/json');



}
?>