$lastnames = Get-Content O:\dumb.txt

$result = foreach ($lname in $lastnames) {
    Get-ADUser -Filter "Surname -eq '$lname'" -Properties mail |
    Select-Object -Expandproperty mail
}
$result | Out-File "O:\emails.txt" -Encoding utf8
