<?php
$servername="localhost";
$username="root";
$password="";
$dbname="stroke data";
//Creating connection
$conn= new mysqli($servername,$username,$password,$dbname);
//Checking connection
if ($conn->Connect_error){
    die("Connection failed:".$conn->connect_error);
}
else
{
    echo "Connected successfully";
}
?>