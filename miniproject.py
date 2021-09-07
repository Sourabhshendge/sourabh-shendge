import MySQLdb

def database():
    print("")
    print("::::::::::::WELCOME TO TIRUPATI MOBILE SHOP:::::::::::: ")
    print("\t 1] Add products detail \n \t 2] Show products detail \n \t 3] Generate invoice (bill) \n \t 4] Exit ")
    print("")
    ch=int(input("\nEnter your choice : "))
   
    
    while (ch!=4):
        
        if ch==1: 
            print("\n Enter products information below ")
            
            try:
                mydb=MySQLdb.connect(host="localhost",user="root",passwd="",database="database")
                
                pname=(input("\nEnter Product name     : "))
                pid=(input("\nEnter product id       : "))
                pprice=(input("\nEnter Price of product : "))
                
                query="""INSERT INTO billing (p_id,p_name,p_price) VALUES ('{}', '{}', '{}');""".format(pid,pname,pprice)
                cur=mydb.cursor()
                
                cur.execute(query)
                mydb.commit()
                cur.close()
                database()
                print("\n Successfully addded............. ")
            
                break
            except:
                print("\t\tSomething went wrong while inserting......! ")
            
        if ch==2:
            print("\n \tShowing product ")
            try:
                mydb=MySQLdb.connect(host="localhost",user="root",passwd="",database="database")
                
                cur=mydb.cursor()
                
                query="select * from billing"
                cur.execute(query)
                
                tdata=cur.fetchall()
                print(" \n list of products are ")
                print("__________________________")
                for row in tdata:
                    print("\tProduct id    : ",row[0])
                    print("\tProduct name  : ",row[1])
                    print("\tProduct price : ",row[2])
                    print("\n ///////////////////////")
                database()
                break
            except:
                print("\t\tSomething went wrong while inserting......! ")

        if ch==3:
            print("\n\t........BILL............\n")
            pid=(input("\nEnter the mobile ID you want : "))

            try:

                mydb=MySQLdb.connect(host="localhost",user="root",passwd="",database="database")
                cur=mydb.cursor() 

                query="""select * from billing where p_id='{}'""".format(pid)
                cur.execute(query)

                data=cur.fetchall()
                print("::::::::::::WELCOME TO TIRUPATI MOBILE SHOP::::::::::::\n")
                for row in data:
                    print("Mobile Id    : ",row[0])
                    print("Mobile Name  : ",row[1])
                    print("")
                    print("Mobile Price : ",row[2]);print(" Rupees ")
                    print("")
                database()
                break

            except:
                print("Something went wrong while genarating bill.............!")

    if ch==4:
        print("........exit.......")
        
database()





