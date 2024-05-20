from flask import Flask, redirect, url_for, render_template, request, session, flash
from datetime import timedelta
import pyodbc 

app = Flask(__name__)

conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-OQEVQKM\SQLEXPRESS; DATABASE=QUAN_LY_KHACH_SAN; UID=danh; PWD=123456;')

@app.route("/")
def home():
    return render_template("Base_templates/hotel.html")

 #solve the room page
@app.route("/room")
def room():
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM dbo.PHONG_O')
    data = cursor.fetchall()   
    cursor.close()
    return render_template("Base_templates/room.html", phong = data)

@app.route("/addroom", methods=["POST", "GET"])
def addroom(): 
    if request.method == "POST":
        # Get the data from the form
        MA_PHONG = request.form["id_input"]
        LOAI_PHONG = request.form["type_room"]
        TINH_TRANG = request.form["condition"]
        SUC_CHUA = request.form["capicity"]
        GIA = request.form["cost"]
        # Insert data into the database
        cursor = conn.cursor()     
        cursor.execute("INSERT INTO dbo.PHONG_O (MA_PHONG, LOAI_PHONG, TINH_TRANG, SUC_CHUA, GIA) VALUES (?, ?, ?, ?, ?)", (MA_PHONG, LOAI_PHONG, TINH_TRANG, SUC_CHUA, GIA))
        conn.commit()
        return redirect(url_for("room"))
    return render_template("Add_Data/addroom.html")

@app.route("/deleteroom/<string:MA_PHONG>", methods=["POST", "GET"])
def deleteroom(MA_PHONG):
    cursor = conn.cursor()
    cursor.execute("DELETE FROM dbo.PHONG_O WHERE MA_PHONG = ?", (MA_PHONG,)) 
    conn.commit()
    return redirect(url_for("room"))
        


@app.route('/editroom/<string:MA_PHONG>', methods= ['GET','POST'])
def editroom(MA_PHONG):
    if request.method =='GET':
        cursor=conn.cursor()
        data =cursor.execute("SELECT * FROM PHONG_O WHERE MA_PHONG=?", (MA_PHONG))
        data = cursor.fetchall()
        conn.commit()
        cursor.close()
        return render_template("Edit_Data/editroom.html", data = data)    
    if request.method == "POST":
         LOAI_PHONG = request.form["type_room"]
         TINH_TRANG = request.form["condition"]
         SUC_CHUA = request.form["capicity"]
         GIA = request.form["cost"]   
         #MA_PHONG = request.form["id_input"]
         cursor = conn.cursor()
         cursor.execute("UPDATE dbo.PHONG_O SET LOAI_PHONG = ?, TINH_TRANG = ?, SUC_CHUA = ?, GIA = ? WHERE MA_PHONG = ?", (  LOAI_PHONG, TINH_TRANG, SUC_CHUA, GIA, MA_PHONG ))
         conn.commit()
         conn.close()
         return redirect(url_for("room"))
       
@app.route("/prosesroom", methods=["POST", "GET"])
def prosesroom():
    if request.method == "POST":
        MA_PHONG = request.form["id_input"]
        LOAI_PHONG = request.form["type_room"]
        TINH_TRANG = request.form["condition"]
        SUC_CHUA = request.form["capicity"]
        GIA = request.form["cost"]
        cursor = conn.cursor()
        cursor.execute("UPDATE dbo.PHONG_O SET LOAI_PHONG = ?, TINH_TRANG = ?, SUC_CHUA = ?, GIA = ? WHERE MA_PHONG = ?", (LOAI_PHONG, TINH_TRANG, SUC_CHUA, GIA, MA_PHONG))
        conn.commit()
        return redirect(url_for("room"))
    return render_template("Edit_Data/editroom.html")


   #solve the customer page

@app.route("/customer")
def customer():
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM dbo.KHACH_HANG')
    dataS = cursor.fetchall()   
    cursor.close()
    return render_template("Base_templates/customer.html" , khach_hang = dataS)

@app.route("/addcus", methods=["POST", "GET"])
def addcus(): 
    if request.method == "POST":
        # Get the data from the form
        MA_KH = request.form["id"]
        HOTEN = request.form["name"]
        Email = request.form["email"]
        QUOC_GIA = request.form["country"]
        DIA_CHI = request.form["address"]
        # Insert data into the database
        cursor = conn.cursor()
        
        cursor.execute("INSERT INTO dbo.KHACH_HANG (MA_KH, HOTEN, Email, QUOC_GIA, DIA_CHI ) VALUES (?, ?, ?, ?, ?)", (MA_KH, HOTEN, Email, QUOC_GIA, DIA_CHI))
        conn.commit()
        return redirect(url_for("customer"))
    return render_template("Add_Data/addcus.html")

@app.route("/deletecus/<string:MA_KH>", methods=["POST", "GET"])
def deletecus(MA_KH):
        cursor = conn.cursor()
        cursor.execute("DELETE FROM dbo.KHACH_HANG WHERE MA_KH = ?", (MA_KH))
        conn.commit()
        return redirect(url_for("customer"))

@app.route('/editcus/<string:MA_KH>', methods= ['GET','POST'])
def editcus(MA_KH):
    if request.method =='GET':
        cursor=conn.cursor()
        data =cursor.execute("SELECT * FROM KHACH_HANG WHERE MA_KH=?", (MA_KH))
        data = cursor.fetchall()
        conn.commit()
        cursor.close()
        return render_template("Edit_Data/editcus.html", data = data)    
    if request.method == "POST":
         HOTEN = request.form["name"]
         Email = request.form["email"]
         QUOC_GIA = request.form["country"]
         DIA_CHI= request.form["address"]
         cursor = conn.cursor()
         cursor.execute("UPDATE dbo.KHACH_HANG SET HOTEN = ?, Email = ?, QUOC_GIA = ?, DIA_CHI = ? WHERE MA_KH = ?", (  HOTEN, Email, QUOC_GIA, DIA_CHI, MA_KH ))
         conn.commit()
         conn.close()
         return redirect(url_for("customer"))
       
@app.route("/prosescus", methods=["POST", "GET"])
def prosescus():
    if request.method == "POST":
        MA_KH = request.form["id"]
        HOTEN = request.form["name"]
        Email = request.form["email"]
        QUOC_GIA = request.form["country"]
        DIA_CHI = request.form["address"]
        cursor = conn.cursor()
        cursor.execute("UPDATE dbo.KHACH_HANG SET HOTEN = ?, Email = ?, QUOC_GIA = ?, DIA_CHI = ? WHERE MA_KH = ?", (  HOTEN, Email, QUOC_GIA, DIA_CHI, MA_KH ))
        conn.commit()
        return redirect(url_for("customer"))
    return render_template("Edit_Data/editcus.html")

#solve the hotel page

@app.route("/hotel")
def hotel():
    cursor = conn.cursor()
    cursor.execute('SELECT * FROM dbo.KHACH_SAN')
    du_lieu = cursor.fetchall()   
    cursor.close()
    return render_template("Base_templates/hotel.html" , khach_san = du_lieu)

@app.route("/addhotel", methods=["POST", "GET"])
def addhotel():
    if request.method == "POST":
        # Get the data from the form
        Ma_KS = request.form["id"]
        Tên_KS = request.form["name"]
        DIA_CHI = request.form["address"]
        # Insert data into the database
        cursor = conn.cursor()
        cursor.execute("INSERT INTO dbo.KHACH_SAN (Ma_KS, Tên_KS, DIA_CHI ) VALUES (?, ?, ?)", (Ma_KS, Tên_KS, DIA_CHI))
        conn.commit()
        return redirect(url_for("hotel"))
    return render_template("Add_Data/addhotel.html")

@app.route("/deletehotel/<string:Ma_KS>", methods=["POST", "GET"])
def deletehotel(Ma_KS):
        cursor = conn.cursor()
        cursor.execute("DELETE FROM dbo.KHACH_SAN WHERE Ma_KS = ?", (Ma_KS))
        conn.commit()
        return redirect(url_for("hotel"))

@app.route('/edithotel/<string:Ma_KS>', methods= ['GET','POST'])
def edithotel(Ma_KS):
    if request.method =='GET':
        cursor=conn.cursor()
        data =cursor.execute("SELECT * FROM KHACH_SAN WHERE Ma_KS=?", (Ma_KS))
        data = cursor.fetchall()
        conn.commit()
        cursor.close()
        return render_template("Edit_Data/edithotel.html", data = data)    
    if request.method == "POST":
         Tên_KS = request.form["name"]
         DIA_CHI = request.form["address"]
         cursor = conn.cursor()
         cursor.execute("UPDATE dbo.KHACH_SAN SET Tên_KS = ?, DIA_CHI = ? WHERE Ma_KS = ?", (  Tên_KS, DIA_CHI, Ma_KS ))
         conn.commit()
         conn.close()
         return redirect(url_for("hotel"))

@app.route("/proseshotel", methods=["POST", "GET"])
def proseshotel():
    if request.method == "POST":
        Ma_KS = request.form["id"]
        Tên_KS = request.form["name"]
        DIA_CHI = request.form["address"]
        cursor = conn.cursor()
        cursor.execute("UPDATE dbo.KHACH_SAN SET Tên_KS = ?, DIA_CHI = ? WHERE Ma_KS = ?", (  Tên_KS, DIA_CHI, Ma_KS ))
        conn.commit()
        return redirect(url_for("hotel"))
    return render_template("Edit_Data/edithotel.html")


@app.route("/reservation")
def reservation():
    return render_template("Base_templates/reservation.html")



if __name__ == "__main__":
    app.run(debug=True)