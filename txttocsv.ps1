$lastnames = Get-Content "C:\Users\u0785\dumb.txt"
$emails    = Get-Content "C:\Users\u0785\emails.txt"

$result = for ($i = 0; $i -lt $lastnames.Count; $i++) {


    [PSCustomObject]@{
        LastName = $lastnames[$i]
        Email    = $emails[$i]
        Email = $String.Trim('"')
    }
}

$result | Export-Csv "C:\Users\u0785\printer_import.csv" -Encoding UTF8 -Delimiter ";"