<?php 

$name=$_POST['name'];
$email=$_POST['email'];
$subject=$_POST['subject'];
$query=$_POST['message'];
$to="djacminfotech@gmail.com";
$header="From:".$email;
$message=" $query ";


$str_arr=str_split($email);
			$flag=0;
			    for($i=0;$i<strlen($email);$i++)
				{
					if($str_arr[$i]=='@')
					{
						for($j=$i;$j<strlen($email);$j++)
						{
							if($str_arr[$j]=='.')
							$flag=1;
						}	
					}
				}






if($flag==1)
{
mail($to,$subject,$message,$header);
echo 'Thank You For Contacting Us, We will Get Back To You Shortly.
<a href="http://www.djacm.in">DJSCOE-ACM</a>';
}


else
{
echo "Error. Please Fill In Correct Email Address.";
}
?>