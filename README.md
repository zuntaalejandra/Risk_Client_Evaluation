# Risk_Client_Evaluation

Until now, the first needed files to consolidate access to cloud DB:

1) TABLEAU file with basic graphs

2) google_colab to make a conexion to cloud BD and print the result of SELECT STATEMENT

3) app.py with 2 routes:
    a)  The first one,  makes a conexion to cloud BD and print the result of SELECT STATEMENT (it was used the code added in Google Colab file)
    b)  The second one, receives 23 parameters, makes a conexion to cloud BD, INSERT a new rows, using the 23 parameters and apply a commit to save the row into de BD.
        this app must to be used to include the excecution to the machine learning model.

4) BD files to upload demo data to the cloud DB
