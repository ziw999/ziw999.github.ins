{% comment %} <?

if($_POST["submit"])

{

    $email_admin = 'ziw999@yandex.ru'; if(!$email_admin) { $BAD = 'Поле $email_admin не заполнено'; }

    $subject = 'Сообщение с сайта - subject';

    if($_POST["name"]) { $name = strip_tags ($_POST["name"]); } else { $BAD = 'Поле name не заполнено'; }

    if($_POST["email"]) { $email = strip_tags ($_POST["email"]); } else { $BAD = 'Поле email не заполнено'; }

    if($_POST["message"])

    {

    $message = 'Пользователь ' .$name .' с емайлом ' .$email .' написал : <br> '. strip_tags ($_POST["message"]);

    }

    else { $BAD = 'Поле message не заполнено'; }

    if(!$BAD)

    {

       $send = @mail($email_admin, $subject, $message);

        if($send) { $info = 'Сообщение отправлено'; } else {$BAD = 'не удалось отправить сообщение'; }

    }

    if($BAD){ $info = '<red>'.$BAD .'</red>';}

}

?> {% endcomment %}


<?php
ini_set ('display errors', 'On');
error_reporting('E_All');

$to = 'ziw999@yandex.ru';
$sitename = $_SERVER['SERVER_NAME'];
$name = strip_tags($_POST['name']);
$phone = strip_tags($_POST['phone']);

if (isset($_POST['name'])) && !empty($_POST['name'])

{
    $subject = "[Zajavka s sajta '.$sitename.']";
    $headers = "From: mail@".$sitename."\r\n";
    $headers .= "MIME-Version: 1.0\r\n";
    $headers .= "Content-Type: text/html;charset = utf-8 \r\n" ;

    $msg = <html><body style = 'font-family:Arial,sans-serif;'>";
    $mag .= <h2 style = 'font-weight:bold;border-bottom:lpx dotted #ccc;>Новая заявка:'</h2>\r\n;
    if(isset($_POST['name']) && !empty($_POST['name'])){
        $smg .= "<p><strong>Имя:</strong>".$name."<p>\r\n";
    }
    if(isset($_POST['phone']) && !empty($_POST['$phone'])){
        $smg .= "<p><strong>Телефон:</strong>".$name."<p>\r\n";
    }
    $smg .= "</body></html>";

    mail($to, $subject, $headers);
}
else
{
    echo "false";
}
?>