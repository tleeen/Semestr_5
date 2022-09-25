package controller.DB;

import java.sql.Connection;
import java.sql.DriverManager;
import java.sql.PreparedStatement;

import java.sql.ResultSet;
import java.util.ArrayList;

public class DatabaseHandler extends Configs {
    private Connection dbConnection;

    public Connection getDbConnection() {
        String connectionString = "jdbc:mysql://" + dbHost + ":" + dbPort + "/" + dbName + "?useSSL=false";
        try {
            Class.forName("com.mysql.cj.jdbc.Driver");
            dbConnection = DriverManager.getConnection(connectionString, dbUser, dbPass);
        } catch (Exception e) {
            e.printStackTrace();
        }
        return dbConnection;
    }

    public void closeConnection() {
        if (dbConnection != null) {
            try {
                dbConnection.close();
            } catch (Exception ignored) {
            }
        }
    }

    public Boolean getUser(String login, String password) {
        ResultSet resSet;

        String select = "SELECT * FROM " + Const.USER_TABLE + " WHERE " +
                Const.USER_LOGIN + "=? AND " + Const.USER_PASSWORD + "=?";

        try {
            PreparedStatement prSt = getDbConnection().prepareStatement(select);
            prSt.setString(1, login);
            prSt.setString(2, password);
            resSet = prSt.executeQuery();
            if (resSet.next()) {
                closeConnection();
                return true;
            }
        } catch (Exception e) {
            e.printStackTrace();
        }
        closeConnection();
        return false;
    }

    public void InsertProduct(String id_user, Integer product_poz, String product_title, String product_price) {
        String insert = "INSERT INTO " + Const.USER_PRODUCT_TABLE + "(" +
                Const.USER_PRODUCT_ID_USER + "," + Const.USER_PRODUCT_POZ + "," + Const.USER_PRODUCT_TITLE + "," + Const.USER_PRODUCT_PRICE + ")" +
                "VALUES(?,?,?,?)";

        try {
            PreparedStatement prSt = getDbConnection().prepareStatement(insert);
            prSt.setString(1, id_user);
            prSt.setString(2, String.valueOf(product_poz));
            prSt.setString(3, product_title);
            prSt.setString(4, product_price);
            prSt.executeUpdate();
        } catch (Exception e) {
            e.printStackTrace();
        }
        closeConnection();
    }

    public void DeleteProduct(String poz_product, String id_user) {



        String delete = "DELETE FROM " + Const.USER_PRODUCT_TABLE + " WHERE " +
                Const.USER_PRODUCT_POZ + "=? AND " + Const.USER_PRODUCT_ID_USER + "=?";
        try {
            PreparedStatement prSt = getDbConnection().prepareStatement(delete);
            prSt.setString(1, poz_product);
            prSt.setString(2, id_user);
            prSt.executeUpdate();
        } catch (Exception e) {
            e.printStackTrace();
        }
        closeConnection();
    }

    public ArrayList<ArrayList<String>> GetProduct(String id_user) {

        ResultSet resSet = null;

        String select = "(SELECT " + Const.USER_PRODUCT_POZ + ", " + Const.USER_PRODUCT_TITLE + ", " + Const.USER_PRODUCT_PRICE + " FROM " + Const.USER_PRODUCT_TABLE + " WHERE " +
                Const.USER_PRODUCT_ID_USER + "=?)";
        ArrayList<ArrayList<String>> products = new ArrayList<>();
        try {
            PreparedStatement prSt = getDbConnection().prepareStatement(select);
            prSt.setString(1, id_user);
            resSet = prSt.executeQuery();
            while (resSet.next()) {
                ArrayList<String> productArr = new ArrayList<String>();
                productArr.add(resSet.getString(Const.USER_PRODUCT_POZ));
                productArr.add(resSet.getString(Const.USER_PRODUCT_TITLE));
                productArr.add(resSet.getString(Const.USER_PRODUCT_PRICE));
                products.add(productArr);
            }
            closeConnection();
            return products;
        } catch (Exception e) {
            e.printStackTrace();
        }
        closeConnection();
        return products;
    }

    public String GetId(String login, String password) {

        ResultSet resSet = null;
        String id = "";

        String select = "SELECT " + Const.USER_ID + " FROM " + Const.USER_TABLE + " WHERE " +
                Const.USER_LOGIN + "=? AND " + Const.USER_PASSWORD + "=?";
        try {
            PreparedStatement prSt = getDbConnection().prepareStatement(select);
            prSt.setString(1, login);
            prSt.setString(2, password);
            resSet = prSt.executeQuery();
            while (resSet.next()) {
                id = resSet.getString(Const.USER_ID);
            }
            closeConnection();
            return id;
        } catch (Exception e) {
            e.printStackTrace();
        }
        closeConnection();
        return id;
    }

    public Integer GetPoz(String id_user) {

        ResultSet resSet = null;
        int n = 1;
        String select = "SELECT " + Const.USER_PRODUCT_POZ + " FROM " + Const.USER_PRODUCT_TABLE + " WHERE " +
                Const.USER_PRODUCT_ID_USER + "=?";

        try {
            PreparedStatement prSt = getDbConnection().prepareStatement(select);
            prSt.setString(1, id_user);
            resSet = prSt.executeQuery();
            while (resSet.next()) {
                n = n + 1;
            }
            prSt.executeUpdate();
        } catch (Exception e) {
            e.printStackTrace();
        }
        closeConnection();
        return n;
    }
}
