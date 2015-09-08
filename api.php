<html>
	<head>
		<title>PHP api</title>
	</head>
	<body>
<?php 

	$color = htmlspecialchars($_GET["color"]);
	$op = htmlspecialchars($_GET["op"]);
	$consumed = htmlspecialchars($_GET["consumed"]);

	//print("Hello world<br>");

	// If an item was added to the fridge,
	if ($op == "Add") {
		if ($color == "green") {
			$fn = "../green_count.txt";
			$green = file($fn)[0];
			$green = $green+1;
			print("Green is now $green. <br>");
			$fh = file_put_contents($fn, $green);
		}
		if ($color == "red") {
			$fn = "../red_count.txt";
			$red = file($fn)[0];
			$red = $red+1;
			print("Red is now $red. <br>");
			$fh = file_put_contents($fn, $red);
		}
		if ($color == "blue") {
			$fn = "../blue_count.txt";
			$blue = file($fn)[0];
			$blue = $blue+1;
			print("blue is now $blue. <br>");
			$fh = file_put_contents($fn, $blue);
		}
	}
	// Else, an item was removed from the fridge.
	else if ($op == "Remove") {
		if ($color == "green") {
			$fn = "../green_count.txt";
			$green = file($fn)[0];
			$green = $green-1;
			print("Green is now $green. <br>");
			$fh = file_put_contents($fn, $green);
		}
		if ($color == "red") {
			$fn = "../red_count.txt";
			$red = file($fn)[0];
			$red = $red-1;
			print("Red is now $red. <br>");
			$fh = file_put_contents($fn, $red);
		}
		if ($color == "blue") {
			$fn = "../blue_count.txt";
			$blue = file($fn)[0];
			$blue = $blue-1;
			print("blue is now $blue. <br>");
			$fh = file_put_contents($fn, $blue);
		}
	}

	// Update the count of badly consumed (or thrown away) items.
	if ($consumed == "Bad") {
		if ($color == "green") {
			$fn = "../green_bad.txt";
			$green = file($fn)[0];
			$green = $green-1;
			print("Green is now $green. <br>");
			$fh = file_put_contents($fn, $green);
		}
		if ($color == "red") {
			$fn = "../red_bad.txt";
			$red = file($fn)[0];
			$red = $red-1;
			print("Red is now $red. <br>");
			$fh = file_put_contents($fn, $red);
		}
		if ($color == "blue") {
			$fn = "../blue_bad.txt";
			$blue = file($fn)[0];
			$blue = $blue-1;
			print("blue is now $blue. <br>");
			$fh = file_put_contents($fn, $blue);
		}
	}

?>

	</body>
</html>
