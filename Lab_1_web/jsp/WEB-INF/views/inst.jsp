<%@ page language="java" contentType="text/html; charset=Windows-1251" pageEncoding="Windows-1251" %>


<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=Windows-1251">
    <title>Main page</title>
    <link rel="stylesheet" href="css/style.css" media="screen" type="text/css" />
</head>

<body class="main">
<form method="post" action="test2">
    <div id="login">
        <p><span class="fontawesome-user"></span><label>
            <input class="inputpr" name="title" type="text" value="������� ��������" onBlur="if(this.value == '') this.value = '������� ��������'" onFocus="if(this.value == '������� ��������') this.value = ''" required>
        </label></p>
        <p><span class="fontawesome-user"></span><label>
            <input class="inputpr" name="price" type="text" value="������� ����" onBlur="if(this.value == '') this.value = '������� ����'" onFocus="if(this.value == '������� ����') this.value = ''" required>
        </label></p>
    </div>
    <input type="submit" value="�������", align="center", class="bt1">
    <input type="submit" value="�����", align="center", class="bt1">
</form>
</body>
</html>
