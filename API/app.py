## declare libraries used in this API program

from flask import Flask,jsonify
import mysql.connector
from config import u_key,p_key,host_key,BD_key # you must have a file config.py with the credencialts to access de DB


#Define app to run api using Flask
app = Flask(__name__)

@app.route("/")
def home():
    return "<br> API\
            <br> \
            <br> \
            <a href='http://127.0.0.1:5000/api/get_info'> Get client's info</a><br>\
            <a href='http://127.0.0.1:5000/api/get_client_risk/1/2/3/4/5/6/7/8/9/10/11/12/13/14/15/16/17/18/19/20/21/22/23'>  Get Client's risk</a><br>\
            <br> Use this link as a guidance    -->      http://127.0.0.1:5000/api/get_client_risk/1/2/3/4/5/6/7/8/9/10/11/12/13/14/15/16/17/18/19/20/21/22/23 </a><br>"

# get_info API route; return a result of a predefined query, but with a conexion to cloud BD
@app.route("/api/get_info")
def get_info():

    cnx = mysql.connector.connect(user=u_key,
                              password=p_key,
                              host=host_key,
                              database=BD_key)

    cursor_ = cnx.cursor(buffered=True)

    # get X1,X3,X6, rows filtering by X2 and X5 (see below the values of this 2 parameters)
    query = ("SELECT ID,X1,X3,X6 FROM clients_info WHERE X2 = %s AND X5 = %s")

    x2_param = 2 # sexo masculino
    x5_param = 23 # edad

    cursor_.execute(query, (x2_param, x5_param))

    #Create dictionary to save results
    list_dict={}
 
    for row in cursor_:
        list_dict[row[0]]={"ID": row[0],
                                "X1": row[1],
                                "X3": row[2],
                                "X6": row[3]}

    cursor_.close()
    cnx.close()

    return jsonify(list_dict)


# get_client_risk API route; this route, gets 23 parameters, makes a conexion to cloud BD and INSERT them to the cloud BD 
@app.route("/api/get_client_risk/<X1>/<X2>/<X3>/<X4>/<X5>/<X6>/<X7>/<X8>/<X9>/<X10>/<X11>/<X12>/<X13>/<X14>/<X15>/<X16>/<X17>/<X18>/<X19>/<X20>/<X21>/<X22>/<X23>")       
def get_client_risk(X1,X2,X3,X4,X5,X6,X7,X8,X9,X10,X11,X12,X13,X14,X15,X16,X17,X18,X19,X20,X21,X22,X23):


    ##############################################################

    #    LONCHO'S MODEL CAN BE HERE

    ##############################################################

    cnx = mysql.connector.connect(user=u_key,
                              password=p_key,
                              host=host_key,
                              database=BD_key)

    cursor_select = cnx.cursor(buffered=True)
        
    # % 24 values, one per each table field (ID is assigned automaticaly by BD)
    insert_ = ("INSERT INTO  clients_info (X1,X2,X3,X4,X5,X6,X7,X8,X9,X10,X11,X12,X13,X14,X15,X16,X17,X18,X19,X20,X21,X22,X23,Y) values (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)")

    data_insert = (X1,X2,X3,X4,X5,X6,X7,X8,X9,X10,X11,X12,X13,X14,X15,X16,X17,X18,X19,X20,X21,X22,X23,0) # last parameter = Y (must be replaced with Loncho's Model)
    
    cursor_insert = cnx.cursor(buffered=True)
    cursor_insert.execute(insert_,(data_insert))    
    ID_no = cursor_insert.lastrowid # get the ID assigned, that the last row inserted

    cnx.commit() # commit into the DB to save the new row

    #Create dictionary to save results
    list_dict=[f"Insert Successful, ID {ID_no}"]
         
    cursor_insert.close()
    cnx.close()

    return jsonify(list_dict)

#Run app code
if __name__=="__main__":
    app.run(debug=True)