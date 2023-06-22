import sqlite3

with sqlite3.connect('products.db') as connection:
    cursor = connection.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS product(
            id INTEGER PRIMARY KEY AUTOINCREMENT NOT NULL,
            name TEXT NOT NULL,
            price INTEGER NOT NULL,
            description STRING 
        );
    """)

    # values = [
    #     ('Tea', 12, 'hot drink'),
    #     ('Milk', 12, 'BEST DRINK IN THE ENTIRE WORLD'),
    #     ('Cola Soda', 28, 'Cheap Cola alternative'),
    #     ('Orange Fresh', 150, 'Homemade orange juice'),
    #     ('Dry Wine', 123, 'Alcohol sugar less drink'),
    #     ('VODKA', 134, 'Hard alcohol drink'),
    # ]

    # cursor.executemany(
    #     """
    #     INSERT INTO product (name, price, description)
    #     VALUES (?, ?, ?)
    #     """,
    #     values,
    #  )

    # data = cursor.execute("""
    #     SELECT *
    #     FROM product
    # """)
    #
    # print(data.fetchmany(5))

    # data = cursor.execute("""
    #     SELECT *
    #     FROM product
    #     WHERE
    #         price > 100 AND description like '%sugar%'
    #     ;
    # """)
    # print(data.fetchall())

    # cursor.execute("""
    #     UPDATE product
    #     SET
    #         price = price + 12
    #     WHERE
    #         price < 10;
    # """)

    cursor.execute("""
        DELETE FROM product
        WHERE name LIKE '%Cola%';
     """)
