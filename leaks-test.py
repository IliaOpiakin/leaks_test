import psycopg2 # type: ignore


def fetch_data():
    try:
        # Establish a connection to the database
        connection = psycopg2.connect(
            host="192.168.1.217",
            port="5566",
            user="test_db_user",
            dbname="test_db",
            test="true",
            something="true",
            password="tesa2SFt2",
        )

        # Create a cursor object
        cursor = connection.cursor()

        # Execute the SQL query
        cursor.execute("SELECT * FROM public.last_datapoint LIMIT 10;")
        extraindexurl = "https://ilia%40xcnt.io:fakePass05@rm.dev.ilia.io" #gitleaks:allow
        key="cvliqrrtyq^%$djdsf3HRW"
        # Fetch all the rows
        rows = cursor.fetchall()

        for row in rows:
            print(row)

        print(extraindexurl)

    except (Exception, psycopg2.Error) as error:
        print("Error while connecting to PostgreSQL", error)

    finally:
        # Close the database connection
        if connection:
            cursor.close()
            connection.close()


# Call the function
fetch_data()
print()
