<?php

require "connect.php";
//header('Content-Type: application/json');

if(isset($_GET['id'])) {
	$id = mysqli_real_escape_string($myConnection, $_GET['id']);

	$result = mysqli_query($myConnection, "SELECT * FROM events WHERE idNumber=$id LIMIT 1") or die(mysqli_error($myConnection));
	while($row = mysqli_fetch_array($result)) {
		$twitterAccount = $row['twitterAccount'];
		$eventType = $row['eventType'];
		$nextRunTime = $row['nextRunTime'];
		$lastRunTime = $row['lastRunTime'];
	}

	$now = new DateTime('now');
	$now_formatted = $now->format('Y-m-d H:i:s');

if(isset($_GET['nextSendTime'])) {

$newNextRunTime =  mysqli_real_escape_string($myConnection, $_GET['nextSendTime']);

}else{

	$tomorrow = new DateTime('today');
//	echo $tomorrow . "<br />";
	

	//echo $now->format('Y-m-d H:i:s') . "\n";

		if ($eventType == "localWeather"){
			$result = mysqli_query($myConnection, "SELECT * FROM localWeather WHERE idNumber=$id LIMIT 1") or die(mysqli_error($myConnection));
			while($row = mysqli_fetch_array($result)) {
				$sendTime = $row['sendTime'];
			}
			$newNextRunTime = $tomorrow->format('Y-m-d') . " " . $sendTime;
		}else if ($eventType == "dailyStocks"){
			$newNextRunTime = $tomorrow->format('Y-m-d') . " 17:30:00";
		}else if ($eventType == "dailyQuote"){
			$newNextRunTime = $tomorrow->format('Y-m-d') . " 8:00:00";
		}else{
			$newNextRunTime = $tomorrow->format('Y-m-d') . " " . $now->format('H:i:s');
		}

//echo ($tomorrow < $now);

	if ($tomorrow < $now){

	$tomorrow = new DateTime('tomorrow');

			if ($eventType == "localWeather"){
				$result = mysqli_query($myConnection, "SELECT * FROM localWeather WHERE idNumber=$id LIMIT 1") or die(mysqli_error($myConnection));
				while($row = mysqli_fetch_array($result)) {
					$sendTime = $row['sendTime'];
				}
				$newNextRunTime = $tomorrow->format('Y-m-d') . " " . $sendTime;
			}else if ($eventType == "dailyStocks"){
				$newNextRunTime = $tomorrow->format('Y-m-d') . " 17:30:00";
			}else if ($eventType == "dailyQuote"){
				$newNextRunTime = $tomorrow->format('Y-m-d') . " 8:00:00";
			}else{
				$newNextRunTime = $tomorrow->format('Y-m-d') . " " . $now->format('H:i:s');
			}

	}

}

	$result = mysqli_query($myConnection, "UPDATE events SET nextRunTime = '$newNextRunTime', lastRunTime= '$now_formatted' WHERE idNumber = $id") or die(mysqli_error($myConnection));

$sql = "SELECT * FROM events WHERE idNumber=$id LIMIT 1";
								echo "{\"events\":[";
								$count = 0;

								//Get basic info
								$result = mysqli_query($myConnection, $sql) or die(mysqli_error($myConnection));
									while($row = mysqli_fetch_array($result)) {
										$id = $row['idNumber'];
										$twitterAccount = $row['twitterAccount'];
										$eventType = $row['eventType'];
										$nextRunTime = $row['nextRunTime'];
										$lastRunTime = $row['lastRunTime'];
										
										if ($count != 0) {echo ",\n";}
										
										echo "{\"id\": \"$id\", \"twitterAccount\": \"$twitterAccount\", \"eventType\": \"$eventType\", \"nextRunTime\": \"$nextRunTime\", \"lastRunTime\":\"$lastRunTime\"";

								//Get special info
										if ($eventType == "localWeather"){
											$result2 = mysqli_query($myConnection, "SELECT * FROM localWeather WHERE idNumber=$id") or die(mysqli_error($myConnection));
												while($row = mysqli_fetch_array($result2)) {
													$location = $row['location'];
													$sendTime = $row['sendTime'];
												}
												echo", \"location\": \"$location\", \"sendTime\": \"$sendTime\"";
										}else if ($eventType == "dailyStocks"){
											$result2 = mysqli_query($myConnection, "SELECT * FROM dailyStocks WHERE idNumber=$id") or die(mysqli_error($myConnection));
												while($row = mysqli_fetch_array($result2)) {
													$symbol = $row['symbol'];
												}
												echo ", \"symbol\": \"$symbol\"";
										}
								echo "}";
								$count = $count + 1;
									}

								echo "]}";




}else{
echo "Run event requires you send an ID.";
}

?>