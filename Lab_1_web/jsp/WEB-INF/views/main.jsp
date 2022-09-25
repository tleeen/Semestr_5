<%@ page import="java.util.ArrayList" %>
<%@ page language="java" contentType="text/html; charset=Windows-1251" pageEncoding="Windows-1251" %>


<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
    <meta http-equiv="Content-Type" content="text/html; charset=Windows-1251">
    <title>Main page</title>
    <link rel="stylesheet" href="css/style.css" media="screen" type="text/css" />
</head>

 <body class="main">
  <form method="post" action="test">
      <div>
          <table class="table_dark", align="center">
              <tr>
                  <th class="aaa"></th>
                  <th>Номер</th>
                  <th>Название</th>
                  <th>Цена</th>
              </tr>
                  <%ArrayList<ArrayList<String>> arr = (ArrayList<ArrayList<String>>)session.getAttribute("arr");
                  int n = 0;
                      for (ArrayList<String> strings : arr) {
                          n = n + 1;
                  %>
              <%= "<tr>" %>
              <%= "<td class=\"aaa\">" + strings.get(0)  + "</td>" %>
              <%= "<td>" + n + "</td>" %>
              <%= "<td>" + strings.get(1) + "</td>" %>
              <%= "<td>" + strings.get(2) + "</td>" %>
              <%= "</tr>" %>
              <%}%>
          </table>
          <script>
              var tds = document.querySelectorAll('tr');
              var arr = [];
              for (i = 0; i < arr.length; i++){

              }
              tds.forEach(function(item)
              {
                  item.onclick = function()
                  {
                      var tdp = this.querySelectorAll('td');
                      a = tdp.item(0).textContent;
                      this.classList.toggle('back');
                      var n = 0;
                      for (i = 0; i < arr.length; i++){
                          if (a === arr[i]){
                              arr.splice(i, 1);
                              n = 1;
                              break;
                          }
                      }
                      if (n === 0){
                          arr.push(a);
                      }
                      var b = "";
                      for (i = 0; i < arr.length; i++){
                          b = b + arr[i] + " ";
                      }
                      document.querySelector('.span1').value = b;
                      console.log(arr);
                      console.log(document.querySelector('.span1').textContent)
                  };
              });
          </script>
      </div>
  </form>
  <div>
      <form method="post" action="test1" class="forms">
          <input type="submit" value="Добавить", align="center", class="bt">
      </form>
      <form method="post" action="test3" class="forms">
          <input type="text" class="span1" name="pozs" required>
          <input type="submit" value="Удалить", align="center", class="bt">
      </form>
  </div>
 </body>

</html>