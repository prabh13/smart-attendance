<?php
ob_start();
include "db.php";
$header = '';
$data = '';
$company_name = $_GET['company'];

    {
        $header .= 'Sr No'."\t";
        $header .= 'TAGID'."\t";
        $header .= 'AMOUNT'."\t";
        $header .= 'TIME'."\t";
       
    }

$query="select * from readings where amtpay!=0";
$result = mysql_query($query);
$serial = 0;
while($info = mysql_fetch_array($result))
{
$serial++;

$time =$info['time'];
$tagid=$info['tagId'];
$amt=$info['amtpay'];



$data .= ''.$serial."\t";
$data .= ''.$tagid."\t";
$data .= ''.$amt."\t";
$data .= ''.$time."\t";

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
