
$path = "C:\Users\u0785\AppData\Roaming\Vipaks\Domination Client\Profiles\"
$file = "nuser37.profile"
$index = 1

$file2 = "nuser37.8DE85AE48DCEB61"


for ($index = 1; $index -le 50; $index ++) {
	$output = "nuser${index}.profile"
	Copy-Item ($path + $file)  ($path + $output)

}