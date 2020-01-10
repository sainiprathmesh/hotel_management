from datetime import datetime

import mysql.connector
from dateutil.parser import parse
from dateutil.relativedelta import relativedelta


def add_roomtype():
    print("Enter Details of Newly Created Room Type ")
    id1 = int(input("Enter ROOM TYPE ID "))
    type1 = input("Enter Type of Room ")
    cap = int(input("Enter Capacity "))
    rent = int(input("Enter Rent for Type of room "))
    try:
        connection = mysql.connector.connect(host='localhost', database='hotel', user='root', password='')
        sql_insert_query = (""" INSERT INTO roomtype(id,type,capacity,rentpd) VALUES (%d,%s,%d,%d)""" % (
            id1, "" + type1 + "", cap, rent))
        cursor = connection.cursor()
        result = cursor.execute(sql_insert_query)
        connection.commit()
        print("Record inserted successfully into python_users table")
    except mysql.connector.Error as error:
        connection.rollback()  # rollback if any exception occured
        print("Failed inserting record into python_users table {}".format(error))
    finally:
        # closing database connection.
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


def modify_roomtype_type():
    id1 = int(input("Enter ROOM TYPE ID for Modify "))
    print("Re Enter Details of Newly Created Room Type ")
    type1 = input("Enter Type of Room ")
    try:
        connection = mysql.connector.connect(host='localhost', database='hotel', user='root', password='')
        sql_update = (""" UPDATE ROOMTYPE SET TYPE=%s where id=%d""" % ("'" + type1 + "'", id1))
        cursor = connection.cursor()
        result = cursor.execute(sql_update)
        connection.commit()
        print("Record inserted successfully into python_users table")
    except mysql.connector.Error as error:
        connection.rollback()  # rollback if any exception occured
        print("Failed inserting record into python_users table {}".format(error))
    finally:
        # closing database connection.
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


def modify_roomtype_capacity():
    id1 = int(input("Enter ROOM TYPE ID for Modify "))
    print("Re Enter Details of Newly Created Room Type ")
    cap = int(input("Enter Capacity of Room "))
    try:
        connection = mysql.connector.connect(host='localhost', database='hotel', user='root', password='')
        sql_update = (""" UPDATE ROOMTYPE SET CAPACITY=%d where id=%d""" % (cap, id1))
        cursor = connection.cursor()
        result = cursor.execute(sql_update)
        connection.commit()
        print("Record inserted successfully into python_users table")
    except mysql.connector.Error as error:
        connection.rollback()  # rollback if any exception occured
        print("Failed inserting record into python_users table {}".format(error))
    finally:
        # closing database connection.
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


def modify_roomtype_rent():
    id1 = int(input("Enter ROOM TYPE ID for Modify "))
    print("Re Enter Details of Newly Created Room Type ")
    cap = int(input("Enter Rent of Room per day "))
    try:
        connection = mysql.connector.connect(host='localhost', database='hotel', user='root', password='')
        sql_update = (""" UPDATE ROOMTYPE SET RENTPD=%d where id=%d""" % (cap, id1))
        cursor = connection.cursor()
        result = cursor.execute(sql_update)
        connection.commit()
        print("Record inserted successfully into python_users table")
    except mysql.connector.Error as error:
        connection.rollback()  # rollback if any exception occured
        print("Failed inserting record into python_users table {}".format(error))
    finally:
        # closing database connection.
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


def add_guest():
    print("Enter Details of Newly Created Room Type ")
    id1 = int(input("Enter GUEST ID "))
    firstname = input("Enter First Name of Guest ")
    lastname = input("Enter Last Name of Guest ")
    mdate = input("Enter Date of membership of Guest ")
    address = input("Enter Address of Guest ")
    city = input("Enter City of Guest ")
    pincode = input("Enter Pincode of city of Guest ")
    mobileno = input("Enter Mobile No of city of Guest ")
    try:
        connection = mysql.connector.connect(host='localhost', database='hotel', user='root', password='')
        sql_insert_query = (
                """ INSERT INTO GUEST(id,FIRSTNAME,LASTNAME,MDATE,ADDRESS,CITY,PIN,MOBILENO) VALUES (%d,%s,%s,%s,%s,%s,%s,%s)""" % (
            id1, "'" + firstname + "'", "'" + lastname + "'", "'" + mdate + "'", "'" + address + "'", "'" + city + "'",
            "'" + pincode + "'", "'" + mobileno + "'"))
        print(sql_insert_query)
        cursor = connection.cursor()
        result = cursor.execute(sql_insert_query)
        connection.commit()
        print("Record inserted successfully into python_users table")
    except mysql.connector.Error as error:
        connection.rollback()  # rollback if any exception occured
        print("Failed inserting record into python_users table {}".format(error))
    finally:
        # closing database connection.
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


def modify_guest_firstname():
    id1 = int(input("Enter GUEST ID for Modify "))
    print("Re Enter Details of Guest ")
    firstname = input("Enter First Name of Guest ")
    try:
        connection = mysql.connector.connect(host='localhost', database='hotel', user='root', password='')
        sql_update = (""" UPDATE GUEST SET FIRSTNAME=%s whereid=%d""" % ("'" + firstname + "'", id1))
        cursor = connection.cursor()
        result = cursor.execute(sql_update)
        connection.commit()
        print("Record inserted successfully into python_users table")
    except mysql.connector.Error as error:
        connection.rollback()  # rollback if any exception occured
        print("Failed inserting record into python_users table {}".format(error))
    finally:
        # closing database connection.
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


def modify_guest_lastname():
    id1 = int(input("Enter GUEST ID for Modify "))
    print("Re Enter Details of Guest ")
    lastname = input("Enter Last Name of Guest ")
    try:
        connection = mysql.connector.connect(host='localhost', database='hotel', user='root', password='')
        sql_update = (""" UPDATE GUEST SET LASTNAME=%s where id=%d""" % ("'" + lastname + "'", id1))
        cursor = connection.cursor()
        result = cursor.execute(sql_update)
        connection.commit()
        print("Record inserted successfully into python_users table")
    except mysql.connector.Error as error:
        connection.rollback()  # rollback if any exception occured
        print("Failed inserting record into python_users table {}".format(error))
    finally:
        # closing database connection.
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


def modify_guest_mdate():
    id1 = int(input("Enter GUEST ID for Modify "))
    print("Re Enter Details of Guest ")
    mdate = input("Enter Date of Membership of Guest ")
    try:
        connection = mysql.connector.connect(host='localhost', database='hotel', user='root', password='')
        sql_update = (""" UPDATE GUEST SET MDATE=%s where id=%d""" % ("'" + mdate + "'", id1))
        cursor = connection.cursor()
        result = cursor.execute(sql_update)
        connection.commit()
        print("Record inserted successfully into python_users table")
    except mysql.connector.Error as error:
        connection.rollback()  # rollback if any exception occured
        print("Failed inserting record into python_users table {}".format(error))
    finally:
        # closing database connection.
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


def modify_guest_address():
    id1 = int(input("Enter GUEST ID for Modify "))
    print("Re Enter Details of Guest ")
    address = input("Enter Address of Guest ")
    try:
        connection = mysql.connector.connect(host='localhost', database='hotel', user='root', password='')
        sql_update = (""" UPDATE GUEST SET ADDRESS=%s where id=%d""" % ("'" + address + "'", id1))
        cursor = connection.cursor()
        result = cursor.execute(sql_update)
        connection.commit()
        print("Record inserted successfully into python_users table")
    except mysql.connector.Error as error:
        connection.rollback()  # rollback if any exception occured
        print("Failed inserting record into python_users table {}".format(error))
    finally:
        # closing database connection.
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


def modify_guest_city():
    id1 = int(input("Enter GUEST ID for Modify "))
    print("Re Enter Details of Guest ")
    city = input("Enter City of Guest ")
    try:
        connection = mysql.connector.connect(host='localhost', database='hotel', user='root', password='')
        sql_update = (""" UPDATE GUEST SET CITY=%s where id=%d""" % ("'" + city + "'", id1))
        cursor = connection.cursor()
        result = cursor.execute(sql_update)
        connection.commit()
        print("Record inserted successfully into python_users table")
    except mysql.connector.Error as error:
        connection.rollback()  # rollback if any exception occured
        print("Failed inserting record into python_users table {}".format(error))
    finally:
        # closing database connection.
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


def modify_guest_pincode():
    id1 = int(input("Enter GUEST ID for Modify "))
    print("Re Enter Details of Guest ")
    pin = input("Enter Pincode of Guest ")
    try:
        connection = mysql.connector.connect(host='localhost', database='hotel', user='root', password='')
        sql_update = (""" UPDATE GUEST SET PIN=%s where id=%d""" % ("'" + pin + "'", id1))
        cursor = connection.cursor()
        result = cursor.execute(sql_update)
        connection.commit()
        print("Record inserted successfully into python_users table")
    except mysql.connector.Error as error:
        connection.rollback()  # rollback if any exception occured
        print("Failed inserting record into python_users table {}".format(error))
    finally:
        # closing database connection.
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


def modify_guest_mobileno():
    id1 = int(input("Enter GUEST ID for Modify "))
    print("Re Enter Details of Guest ")
    mobileno = input("Enter Mobile No of Guest ")
    try:
        connection = mysql.connector.connect(host='localhost', database='hotel', user='root', password='')
        sql_update = (""" UPDATE GUEST SET MOBILENO=%s where id=%d""" % ("'" + mobileno + "'", id1))
        cursor = connection.cursor()
        result = cursor.execute(sql_update)
        connection.commit()
        print("Record inserted successfully into python_users table")
    except mysql.connector.Error as error:
        connection.rollback()  # rollback if any exception occured
        print("Failed inserting record into python_users table {}".format(error))
    finally:
        # closing database connection.
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


def add_room():
    print("Enter Details of Newly Created Room ")
    id1 = int(input("Enter ROOM ID "))
    roomno = int(input("Enter Newly Created Room No "))
    status = int(input("Enter Status 1 for working and 0 for not Working "))
    roomtypeid = int(input("Enter Room Type id which was created in room type  "))
    try:
        connection = mysql.connector.connect(host='localhost', database='hotel', user='root', password='')
        sql_insert_query = (""" INSERT INTO room (id,roomno,func_status,room_type_id)VALUES (%d,%d,%d,%d)""" % (
            id1, roomno, status, roomtypeid))
        cursor = connection.cursor()
        result = cursor.execute(sql_insert_query)
        connection.commit()
        print("Record inserted successfully into python_users table")
    except mysql.connector.Error as error:
        connection.rollback()  # rollback if any exception occured
        print("Failed inserting record into python_users table {}".format(error))
    finally:
        # closing database connection.
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


def modify_room_roomno():
    id1 = int(input("Enter ROOM ID for Modify "))
    print("Re Enter Details of ROOM ")
    roomno = int(input("Enter Room No of Room "))
    try:
        connection = mysql.connector.connect(host='localhost', database='hotel', user='root', password='')
        sql_update = (""" UPDATE ROOM SET ROOMNO=%d where id=%d""" % (roomno, id1))
        cursor = connection.cursor()
        result = cursor.execute(sql_update)
        connection.commit()
        print("Record inserted successfully into python_users table")
    except mysql.connector.Error as error:
        connection.rollback()  # rollback if any exception occured
        print("Failed inserting record into python_users table {}".format(error))
    finally:
        # closing database connection.
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


def modify_room_status():
    id1 = int(input("Enter ROOM ID for Modify "))
    print("Re Enter Details of ROOM ")
    status = int(input("Enter Status of Room 1 for WORKING AND 0 FOR NOT WORKING "))
    try:
        connection = mysql.connector.connect(host='localhost', database='hotel', user='root', password='')
        sql_update = (""" UPDATE ROOM SET func_status=%d where id=%d""" % (status, id1))
        cursor = connection.cursor()
        result = cursor.execute(sql_update)
        connection.commit()
        print("Record inserted successfully into python_users table")
    except mysql.connector.Error as error:
        connection.rollback()  # rollback if any exception occured
        print("Failed inserting record into python_users table {}".format(error))
    finally:
        # closing database connection.
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


def new_booking():
    print("Enter Details of New Booking ")
    id1 = int(input("Enter New Booking ID "))
    cindate2 = input("Enter Check In Date ")
    cindate = parse(cindate2)
    noofdaysstay = int(input("Enter No of Days Stay "))
    roomtypeid = int(input("Enter Room Type id for booking "))
    noofrooms = int(input("Enter No of Rooms "))
    guestid = int(input("Enter Guest id "))
    madeby = input("Enter Made By ")
    cindate1 = datetime.date(cindate)
    reservationdate = datetime.date(datetime.now())
    reservationdate1 = reservationdate.strftime('%Y-%m-%d')
    coutdate = cindate1 + relativedelta(days=noofdaysstay)
    coutdate2 = coutdate.strftime('%Y-%m-%d')
    print(cindate2)
    print(coutdate2)
    try:
        connection = mysql.connector.connect(host='localhost', database='hotel', user='root', password='')
        sql_insert_query = (
                """ INSERT INTO reservation(id,noofrooms,cindate,coutdate,madeby,guestid,reservationdate,no_of_days_stay,roomtypeid)VALUES(%d,%d,%s,%s,%s,%d,%s,%d,%d)""" % (
            id1, noofrooms, "'" + cindate2 + "'", "'" + coutdate2 + "'", "'" + madeby + "'", guestid,
            "'" + reservationdate1 + "'", noofdaysstay, roomtypeid))
        print(sql_insert_query)
        cursor = connection.cursor()
        result = cursor.execute(sql_insert_query)
        connection.commit()
        print("Record inserted successfully into python_users table")
    except mysql.connector.Error as error:
        connection.rollback()  # rollback if any exception occured
        print("Failed inserting record into python_users table {}".format(error))
    finally:
        # closing database connection.
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

    try:
        for i in range(0, noofrooms):
            id2 = int(input("Enter Room ID "))
            roomno2 = int(input("Enter Room No "))
            roomtypeid1 = roomtypeid
            reservationid1 = id1
            connection = mysql.connector.connect(host='localhost', database='hotel', user='root', password='')
            sql_insert_query = (
                    """ INSERT INTO reservedroom (id,roomno,roomtypeid,reservationid)VALUES (%d,%d,%d,%d)""" % (
                id2, roomno2, roomtypeid1, reservationid1))
            print(sql_insert_query)
            cursor = connection.cursor()
            result = cursor.execute(sql_insert_query)
            connection.commit()
            print("Record inserted successfully into python_users table")
    except mysql.connector.Error as error:
        connection.rollback()  # rollback if any exception occured
        print("Failed inserting record into python_users table {}".format(error))
    finally:
        # closing database connection.
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


def cancel_booking():
    id1 = int(input("Enter Reservation ID for Cancel Booking "))
    val = 1
    try:
        connection = mysql.connector.connect(host='localhost', database='hotel', user='root', password='')
        sql_update = (""" UPDATE RESERVATION SET cancelled=%d where id=%d""" % (val, id1))
        cursor = connection.cursor()
        result = cursor.execute(sql_update)
        connection.commit()
        print("Record inserted successfully into python_users table")
    except mysql.connector.Error as error:
        connection.rollback()  # rollback if any exception occured
        print("Failed inserting record into python_users table {}".format(error))
    finally:
        # closing database connection.
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
    cancelleddate = datetime.date(datetime.now())
    cancelleddate1 = cancelleddate.strftime('%Y-%m-%d')
    try:
        connection = mysql.connector.connect(host='localhost', database='hotel', user='root', password='')
        sql_update = (""" UPDATE RESERVATION SET cancelleddate=%s where id=%d""" % ("'" + cancelleddate1 + "'", id1))
        cursor = connection.cursor()
        result = cursor.execute(sql_update)
        connection.commit()
        print("Record inserted successfully into python_users table")
    except mysql.connector.Error as error:
        connection.rollback()  # rollback if any exception occured
        print("Failed inserting record into python_users table {}".format(error))
    finally:
        # closing database connection.
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
    val1 = 0
    try:
        connection = mysql.connector.connect(host='localhost', database='hotel', user='root', password='')
        sql_update = (""" UPDATE RESERVEDROOM SET STATUS=%d where RESERVATIONid=%d""" % (val1, id1))
        cursor = connection.cursor()
        result = cursor.execute(sql_update)
        connection.commit()
        print("Record inserted successfully into python_users table")
    except mysql.connector.Error as error:
        connection.rollback()  # rollback if any exception occured
        print("Failed inserting record into python_users table {}".format(error))
    finally:
        # closing database connection.
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


def guest_arrived():
    print("Enter Details of Guest at Check In Time ")
    id1 = int(input("Enter OCCUPIED ID "))
    cindate = input("Enter Check In Date ")
    cintime = input("Enter Check In Time ")
    roomid = int(input("Enter Room ID "))
    reservationid = int(input("Enter Reservation ID "))
    try:
        connection = mysql.connector.connect(host='localhost', database='hotel', user='root', password='')
        sql_insert_query = (
                """ INSERT INTO OCCUPIEDROOM (id,cindate,cintime,roomid,reservationid)VALUES (%d,%s,%s,%d,%d)""" % (
            id1, "'" + cindate + "'", "'" + cintime + "'", roomid, reservationid))
        print(sql_insert_query)
        cursor = connection.cursor()
        result = cursor.execute(sql_insert_query)
        connection.commit()
        print("Record inserted successfully into python_users table")
    except mysql.connector.Error as error:
        connection.rollback()  # rollback if any exception occured
        print("Failed inserting record into python_users table {}".format(error))
    finally:
        # closing database connection.
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


def guest_checkout():
    id1 = int(input("Enter Reservation ID for Check Out "))
    coutdate = input("Enter Check Out Date ")
    couttime = input("Enter Check Out Time ")
    val = 0
    try:
        connection = mysql.connector.connect(host='localhost', database='hotel', user='root', password='')
        sql_update = (""" UPDATE occupiedroom SET coutdate=%swhere reservationid=%d""" % ("'" + coutdate + "'", id1))
        cursor = connection.cursor()
        result = cursor.execute(sql_update)
        connection.commit()
        print("Record inserted successfully into python_users table")
    except mysql.connector.Error as error:
        connection.rollback()  # rollback if any exception occured
        print("Failed inserting record into python_users table {}".format(error))
    finally:
        # closing database connection.
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
    try:
        connection = mysql.connector.connect(host='localhost', database='hotel', user='root', password='')
        sql_update = (""" UPDATE occupiedroom SET couttime=%s where reservationid=%d""" % ("'" + couttime + "'", id1))
        cursor = connection.cursor()
        result = cursor.execute(sql_update)
        connection.commit()
        print("Record inserted successfully into python_users table")
    except mysql.connector.Error as error:
        connection.rollback()  # rollback if any exception occured
        print("Failed inserting record into python_users table {}".format(error))
    finally:
        # closing database connection.
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
    try:
        connection = mysql.connector.connect(host='localhost', database='hotel', user='root', password='')
        sql_update = (""" UPDATE reservation SET cancelled=%s where id=%d""" % (val, id1))
        cursor = connection.cursor()
        result = cursor.execute(sql_update)
        connection.commit()
        print("Record inserted successfully into python_users table")
    except mysql.connector.Error as error:
        connection.rollback()  # rollback if any exception occured
        print("Failed inserting record into python_users table {}".format(error))
    finally:
        # closing database connection.
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


def billing():
    try:
        connection = mysql.connector.connect(host='localhost', database='hotel', user='root', password='')
        # sql_select = ("SELECT * FROM RESERVEDROOM")
        # sql_select = ("SELECT id, GUESTID FROM RESERVEDROOM where cancelled=True and billpaid is null")
        # SELECT ID, GUESTID FROM RESERVATION WHERE CANCELLED=1 AND BILLPAID IS NULL
        sql_select = ("SELECT ID, GUESTID FROM RESERVATION WHERE CANCELLED=0 AND BILLPAID = 0")
        cursor = connection.cursor()
        cursor.execute(sql_select)
        result = cursor.fetchall()
        print("Bill going to generate ")
        print("Customer Id  Reservation Id ")
        for x in result:
            print(x[0], "	", x[1])
        # for x in result:
        # print(x[0],x[1],x[2],x[3])
        # generate_pdf()
    except mysql.connector.Error as error:
        connection.rollback()  # rollback if any exception occured
        print("Failed inserting record into python_users table {}".format(error))
    finally:
        # closing database connection.
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


def billpay():
    print("Do you want to Make Paymnet Y(1)")
    reservationid = int(input("Enter Reservation Id	:"))
    try:
        connection = mysql.connector.connect(host='localhost', database='hotel', user='root', password='')
        sql_select = (
                """SELECT G.FIRSTNAME,G.LASTNAME,RT.RENTPD,R.NO_OF_DAYS_STAY, R.CINDATE,R.COUTDATE FROM ROOMTYPE RT,RESERVEDROOM RR,RESERVATION R , GUEST G WHERE R.ID=%d AND R.ID=RR.RESERVATIONID AND RR.ROOMTYPEID=RT.ID AND G.ID=R.GUESTID""" % (
            reservationid))
        cursor = connection.cursor()
        cursor.execute(sql_select)
        result = cursor.fetchall()
        for x in result:
            fname = x[0]
            sname = x[1]
            rent = x[2]
            nod = x[3]
            cindate = x[4]
            coutdate = x[5]
            amtpayable = rent * nod
            gst = amtpayable * 18 / 100
            netamt = amtpayable + gst
            print("Mr / Mrs / Ms ", fname, " ", sname)
            print("Total Bill Payable:", netamt)
    except mysql.connector.Error as error:
        connection.rollback()  # rollback if any exception occured
        print("Failed inserting record into python_users table {}".format(error))
    finally:
        # closing database connection.
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")
    try:
        val = 1
        connection = mysql.connector.connect(host='localhost', database='hotel', user='root', password='')
        # sql_update_cancelled = (""" UPDATE RESERVATION SET cancelled=%d where id=%d"""%(val,reservationid))
        sql_update_billpaid = (""" UPDATE RESERVATION SET billpaid=%d where id=%d""" % (val, reservationid))
        cursor = connection.cursor()
        # result = cursor.execute(sql_update_cancelled)
        result = cursor.execute(sql_update_billpaid)
        connection.commit()
        print("Record inserted successfully into python_users table")
    except mysql.connector.Error as error:
        connection.rollback()  # rollback if any exception occured
        print("Failed inserting record into python_users table {}".format(error))
    finally:
        # closing database connection.
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


def generate_bill():
    try:
        connection = mysql.connector.connect(host='localhost', database='hotel', user='root', password='')
        # sql_select = ("SELECT * FROM RESERVEDROOM")
        # sql_select = ("SELECT id, GUESTID FROM RESERVEDROOM where cancelled=True and billpaid is null")
        # SELECT ID, GUESTID FROM RESERVATION WHERE CANCELLED=1 AND BILLPAID IS NULL
        sql_select = ("SELECT ID, GUESTID FROM RESERVATION WHERE CANCELLED=0 AND BILLPAID = 1")
        cursor = connection.cursor()
        cursor.execute(sql_select)
        result = cursor.fetchall()
        print("Bill going to generate ")
        print("Customer Id  Reservation Id ")
        for x in result:
            print(x[0], "	", x[1])
            # for x in result:
            # print(x[0],x[1],x[2],x[3])
            # generate_pdf()
    except mysql.connector.Error as error:
        connection.rollback()  # rollback if any exception occured
        print("Failed inserting record into python_users table {}".format(error))
    finally:
        # closing database connection.
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")

    print("Do you wnat to Make Paymnet Y(1)")
    reservationid = int(input("Enter Reservation Id	:"))
    try:
        connection = mysql.connector.connect(host='localhost', database='hotel', user='root', password='')
        sql_select = (
                """SELECT G.FIRSTNAME,G.LASTNAME,RT.RENTPD,R.NO_OF_DAYS_STAY, R.CINDATE,R.COUTDATE FROM ROOMTYPE RT,RESERVEDROOM RR,RESERVATION R , GUEST G WHERE R.ID=%d AND R.ID=RR.RESERVATIONID AND RR.ROOMTYPEID=RT.ID AND G.ID=R.GUESTID""" % (
            reservationid))
        cursor = connection.cursor()
        cursor.execute(sql_select)
        result = cursor.fetchall()
        for x in result:
            fname = x[0]
            sname = x[1]
            rent = x[2]
            nod = x[3]
            cindate = x[4]
            coutdate = x[5]
            amtpayable = rent * nod
            gst = amtpayable * 18 / 100
            netamt = amtpayable + gst
            print("Mr / Mrs / Ms ", fname, " ", sname)
            print("Total Bill Payable:", amtpayable)
            # generate_pdf()
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            pdf.cell(0, 5, "Hotel BHOPAL !", ln=0, align="L")
            pdf.cell(0, 5, "Receipt No." + str(reservationid), ln=1, align="R")
            pdf.cell(0, 5, "Station Road !", ln=0, align="l")
            pdf.cell(0, 5, "Date." + str(coutdate), ln=1, align="R")
            pdf.cell(0, 5, "BHOPAL M.P. !", ln=1, align="L")
            pdf.cell(0, 10, 'Invoice', 0, 1, align='C')
            pdf.cell(0, 0,
                     "----------------------------------------------------------------------------------------------------------------------------------------",
                     ln=1, align="L")
            pdf.cell(160, 10, "Guest Name", ln=0, align="L")
            pdf.cell(160, 10, fname + " " + sname, ln=1, align="L")
            pdf.cell(0, 0,
                     "----------------------------------------------------------------------------------------------------------------------------------------",
                     ln=1, align="L")
            pdf.cell(160, 10, "	Check In Date ", ln=0, align="L")
            pdf.cell(160, 10, str(cindate), ln=1, align="L")
            pdf.cell(160, 10, "	Check Out Date ", ln=0, align="L")
            pdf.cell(160, 10, str(coutdate), ln=1, align="L")
            pdf.cell(160, 10, "	Total Days	", ln=0, align="L")
            pdf.cell(160, 10, str(nod), ln=1, align="L")
            pdf.cell(160, 10, "	Rent Per day  ", ln=0, align="L")
            pdf.cell(160, 10, str(rent), ln=1, align="L")
            pdf.cell(160, 10, "	Rented Amount without Tax  ", ln=0, align="L")
            pdf.cell(160, 10, str(amtpayable), ln=1, align="L")
            pdf.cell(160, 10, "	SGST 9% & CGST 9%  ", ln=0, align="L")
            pdf.cell(160, 10, str(gst), ln=1, align="L")
            pdf.cell(160, 10, "	Total Amount Payable  ", ln=0, align="L")
            pdf.cell(160, 10, str(netamt), ln=1, align="L")
            pdf.cell(0, 0,
                     "----------------------------------------------------------------------------------------------------------------------------------------",
                     ln=1, align="L")
            pdf.cell(0, 100, "Signature ", ln=1, align="R")
            pdf.output("simple_demo.pdf")
            url = 'file:///G:/PERSONAL/SCHOOL/IN-SERVICE-COURSE/SPELL-2-BPL-NO-2/simple_demo.pdf'
            # chrome_path = 'C:/Program Files (x86)/Google/Chrome/Application/chrome.exe %s' webbrowser.open(url)
            pdf.cell(0, 0,
                     "----------------------------------------------------------------------------------------------------------------------------------------",
                     ln=1, align="L")
            pdf.cell(0, 100, "Signature ", ln=1, align="R")
    except mysql.connector.Error as error:
        connection.rollback()  # rollback if any exception occured
        print("Failed inserting record into python_users table {}".format(error))
    finally:
        # closing database connection.
        if (connection.is_connected()):
            cursor.close()
            connection.close()
            print("MySQL connection is closed")


while (True):
    while (True):
        print()
        print(
            "************************************************************************************ Main Menu ***********************************************************************")
        print()
        print("1. Room Type Details")
        print("2. Reservation")
        print("3. Guest Details")
        print("4. Room Details")
        print("5. Guest Arrival Check In")
        print("6. Guest Departure Check Out")
        print("7. Billing")
        print("8. Generate Old Bill")
        print("8. Exit")
        ch = int(input("Enter Choice from above"))
        if (ch < 1) or (ch >= 9):
            break
        elif (ch == 9):
            break
        elif (ch == 1):
            while (True):
                while (True):
                    print()
                    print(
                        "************************************************************************ Room Type Details Menu **************************************************************************")
                    print()
                    print("1. Add Room Type")
                    print("2. Modify Room Type")
                    print("3. Modify Room Capacity")
                    print("4. Modify Room Rent per Day ")
                    print("5. Exit")
                    ch1 = int(input("Enter Choice from above	"))
                    if (ch1 < 1 or ch1 >= 5):
                        break
                    elif (ch1 == 5):
                        break
                    elif (ch1 == 1):
                        add_roomtype()
                    elif (ch1 == 2):
                        modify_roomtype_type()
                    elif (ch1 == 3):
                        modify_roomtype_capacity()
                    elif (ch1 == 4):
                        modify_roomtype_rent()

        elif (ch == 3):
            while (True):
                while (True):
                    print()
                    print(
                        "************************************************************************ Guest Details Menu **************************************************************************")
                    print()
                    print("1. Add New Guest ")
                    print("2. Modify Guest First Name")
                    print("3. Modify Guest Last Name")
                    print("4. MOdify Guest Membership Date")
                    print("5. MOdify Guest Address")
                    print("6. Modify Guest City")
                    print("7. Modify Guest Pincode")
                    print("8. Modify Guest Mobile No")
                    print("9. Exit")
                    ch_guest = int(input("Enter Choice from above"))
                    if (ch_guest < 1 or ch_guest >= 9):
                        break
                    elif (ch_guest == 9):
                        break
                    elif (ch_guest == 1):
                        add_guest()
                    elif (ch_guest == 2):
                        modify_guest_firstname()
                    elif (ch_guest == 3):
                        modify_guest_lastname()
                    elif (ch_guest == 4):
                        modify_guest_mdate()
                    elif (ch_guest == 5):
                        modify_guest_address()
                    elif (ch_guest == 6):
                        modify_guest_city()
                    elif (ch_guest == 7):
                        modify_guest_pincode()
                    elif (ch_guest == 8):
                        modify_guest_mobileno()

        elif (ch == 4):
            while (True):
                while (True):
                    print()
                    print(
                        "************************************************************************ Room Details Menu **************************************************************************")
                    print()
                    print("1. Add New Room")
                    print("2. Modify Room No")
                    print("3. Modify Room Status")
                    print("4. Exit ")
                    ch_room = int(input("Enter Choice from above	"))
                    if (ch_room < 1 or ch_room >= 4):
                        break
                    elif (ch_room == 4):
                        break
                    elif (ch_room == 1):
                        add_room()
                    elif (ch_room == 2):
                        modify_room_roomno()
                    elif (ch_room == 3):
                        modify_room_status()

        elif (ch == 2):
            while (True):
                while (True):
                    print()
                    print(
                        "************************************************************************ Reservation Menu **************************************************************************")
                    print()
                    print("1. New Booking")
                    print("2. Modify Booking Date")
                    print("3. Cancel Booking")
                    print("4. Exit")
                    ch_res = int(input("Enter Choice from above"))
                    if (ch_res < 1 or ch_res >= 4):
                        break
                    elif (ch_res == 4):
                        break
                    elif (ch_res == 1):
                        new_booking()
                    elif (ch_res == 2):
                        cancel_booking()
                        new_booking()
                    elif (ch_res == 3):
                        cancel_booking()

        elif (ch == 5):
            guest_arrived()

        elif (ch == 6):
            guest_checkout()

        elif (ch == 7):
            billing()
            billpay()

        elif (ch == 8):
            generate_bill()
