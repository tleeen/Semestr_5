package controller;

import controller.DB.DatabaseHandler;
import jakarta.servlet.http.HttpServlet;
import jakarta.servlet.http.HttpServletRequest;
import jakarta.servlet.http.HttpServletResponse;
import jakarta.servlet.http.HttpSession;

import java.util.ArrayList;

public class WebController extends HttpServlet {
	String login = "";
	String password = "";

	protected void doPost(HttpServletRequest request, HttpServletResponse response) {
		String url = request.getRequestURL().toString();
		url = url.substring(url.lastIndexOf("/"));
		HttpSession session = request.getSession(true);
		switch (url) {
			case "/test":
				try {
					String login = request.getParameter("login");
					String password = request.getParameter("password");
					this.login = login;
					this.password = password;
					DatabaseHandler DH = new DatabaseHandler();

					if (DH.getUser(login, password)) {

						ArrayList<ArrayList<String>> arr = DH.GetProduct(DH.GetId(login, password));

						session.setAttribute("arr", arr);
						String view = "main";
						request.getRequestDispatcher("/WEB-INF/views/" + view + ".jsp").forward(request, response);

					} else {
						String view = "index";
						request.getRequestDispatcher(view + ".jsp").forward(request, response);
					}

			  /*Object nn = session.getAttribute("n");
			  int n = 0;
			  if (nn != null) {
				  n = (Integer) nn;
			  }
			  n = n + 2;
			  session.setAttribute("n", n);


			  request.setAttribute("n", n);
			  String view = "main";
			  request.getRequestDispatcher("/WEB-INF/views/" + view + ".jsp").forward(request, response);

		  } catch (Exception ex) {
			  assert printWriter != null;
			  printWriter.println("Error: " + ex.getMessage());*/
				} catch (Exception e) {
					throw new RuntimeException(e);
				}
				break;
			case "/test1":
				try {
					String view1 = "inst";
					request.getRequestDispatcher("/WEB-INF/views/" + view1 + ".jsp").forward(request, response);
				} catch (Exception e) {
					throw new RuntimeException(e);
				}
				break;
			case "/test2":
				try {
					String title = request.getParameter("title");
					String price = request.getParameter("price");

					String login = this.login;
					String password = this.password;

					DatabaseHandler DH = new DatabaseHandler();
					DH.InsertProduct(DH.GetId(login, password), DH.GetPoz(DH.GetId(login, password)), title, price);
					ArrayList<ArrayList<String>> arr = DH.GetProduct(DH.GetId(login, password));

					session.setAttribute("arr", arr);

					String view1 = "main";
					request.getRequestDispatcher("/WEB-INF/views/" + view1 + ".jsp").forward(request, response);
				} catch (Exception e) {
					throw new RuntimeException(e);
				}
				break;
			case "/test3":
				try {
					String pozs = request.getParameter("pozs");

					char[] chars = pozs.toCharArray();
					ArrayList<String> array = new ArrayList<>();
					for (char aChar : chars) {
						if (!String.valueOf(aChar).equals(" ")) {
							array.add(String.valueOf(aChar));
						}
					}

					String login = this.login;
					String password = this.password;

					DatabaseHandler DH = new DatabaseHandler();
					for (String strings : array) {
						DH.DeleteProduct(strings, DH.GetId(login, password));
					}

					ArrayList<ArrayList<String>> arr = DH.GetProduct(DH.GetId(login, password));
					session.setAttribute("arr", arr);
					String view1 = "main";
					request.getRequestDispatcher("/WEB-INF/views/" + view1 + ".jsp").forward(request, response);
				} catch (Exception e) {
					throw new RuntimeException(e);
				}
				break;
		}
	}
}