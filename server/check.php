<?php
	
  DEFINE("DB_USER","");
  DEFINE("DB_PASS","");
  DEFINE("DB_NAME","");
  DEFINE("DB_HOST","");
  
	date_default_timezone_set("America/Chicago");
	
	$mysqli = new mysqli(DB_HOST,DB_USER,DB_PASS,DB_NAME);
	
  //example only, use proper sanitization
	$code = $_POST['code'];
	$location = $_POST['location'];
	$meal = $_POST['meal'];
	$date = $_POST['date'];
	$time = $_POST['time'];
	
	if ($mysqli->connect_errno OR !$meal OR !$code) {
   
    
   	$obj = new stdClass;
	  $obj->meal = $meal;
  	$obj->pass = TRUE;

		echo json_encode($obj);
    exit();
   
  }
	
    $obj = new stdClass;
	  $obj->meal = $meal;
    $obj->pass = TRUE;
    
	  if ($result = $mysqli->query("SELECT * FROM Scan.Meals WHERE meal='".$meal."' AND code='".$code."' and DATE(scantime)=CURDATE() ")) {
    	
    
    	
    if($result->num_rows>0){
        
        $uql ="INSERT IGNORE INTO Scan.Fails (`scantime`,`meal`,`location`,`code`) VALUES ('".date("Y-m-d H:i:s",strtotime($date." ".$time))."','".$meal."','".$location."','".$code."')";
    
        $mysqli->query($uql);
        
        $obj->pass = FALSE;
        
    }

    /* free result set */
    $result->close();
    
    }


    if($obj->pass == TRUE){

    $uql ="INSERT IGNORE INTO Scan.Meals (`scantime`,`meal`,`location`,`code`) VALUES ('".date("Y-m-d H:i:s",strtotime($date." ".$time))."','".$meal."','".$location."','".$code."')";
    
    $mysqli->query($uql);
    
    }
	
    echo json_encode($obj);
    exit;