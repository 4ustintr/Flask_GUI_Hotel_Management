import pyodbc

# Connect to SQL Server
print(pyodbc.drivers())
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER=DESKTOP-OQEVQKM\SQLEXPRESS; DATABASE=QUAN_LY_KHACH_SAN; UID=danh; PWD=123456;')

# Create a cursor from the connection
cursor = conn.cursor()
data= cursor.execute('SELECT * FROM dbo.KHACH_SAN')
for row in data:
    print(row)

# Close the connection
conn.close()

