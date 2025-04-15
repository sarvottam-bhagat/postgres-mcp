import psycopg

try:
    # Connect to the PostgreSQL database
    # Connect to Supabase PostgreSQL database
    conn = psycopg.connect(
        host="db.gldmcfjxjnrkjelljxwx.supabase.co",
        port=5432,
        user="postgres",
        password="Khushi5678xyz*",
        dbname="postgres"
    )

    # Create a cursor
    with conn.cursor() as cursor:
        # Execute a simple query
        cursor.execute("SELECT version()")
        result = cursor.fetchone()
        print("Successfully connected to the database!")
        if result:
            print(f"PostgreSQL version: {result[0]}")
        else:
            print("No version information returned")

        # Get schema information
        cursor.execute("""
            SELECT
                n.nspname AS schema_name,
                c.relname AS table_name,
                d.description AS table_description
            FROM pg_catalog.pg_class c
            LEFT JOIN pg_catalog.pg_namespace n ON n.oid = c.relnamespace
            LEFT JOIN pg_catalog.pg_description d ON d.objoid = c.oid AND d.objsubid = 0
            WHERE
                c.relkind = 'r'
                AND n.nspname = 'public'
            ORDER BY schema_name, table_name;
        """)
        tables = cursor.fetchall()
        print("\nSchema information:")
        for table in tables:
            print(f"Table: {table[1]}, Description: {table[2] or 'No description'}")

    # Close the connection
    conn.close()
except Exception as e:
    print(f"Error connecting to the database: {e}")
