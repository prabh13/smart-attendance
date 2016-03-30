<?php
ob_start();
include "db.php";
$header = '';
$data = '';
#$company_name = $_GET['company'];

    {
        $header .= 'Sr No'."\t";
        $header .= 'NAME'."\t";
        $header .= 'STAFF ID'."\t";
        $header .= 'DATE'."\t";
	$header .= 'NO OF HOURS'."\t";
       
    }

$query="SELECT users.name,users.surname,users.id,total_hours.date,total_hours.hours from users, total_hours, cards where users.id=cards.userId AND cards.tagId=total_hours.tagId";
$result = mysql_query($query);
$serial = 0;
while($info = mysql_fetch_array($result))
{
$serial++;

$name=$info['name']." ".$info[surname];
$id=$info['id'];
$date=$info['date'];
$hours=$info['hours'];




$data .= ''.$serial."\t";
$data .= ''.$name."\t";
$data .= ''.$id."\t";
$data .= ''.$date."\t";
$data .= ''.$hours."\t";

$data .= "\n";
}

    if ($data == "")
    {
        $data = "\n NO record found yet!\n";
    }
    $title ='ATTENDANCE_LIST_RVCE.xls';
    header('Content-Disposition: attachment; filename='.$title);
    header('Content-type: application/ms-excel');
    header("Pragma: no-cache");
    header("Expires: 0");
    print "$header\n$data";

ob_flush();
?>
