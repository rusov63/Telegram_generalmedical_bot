import psycopg2

if True:
    with psycopg2.connect(user='', password="", host="localhost", port="5432",
                          database="") as conn:

        with conn.cursor() as cur:
            cur.execute("CREATE TABLE donor (id serial primary key, "
                        "recipient char(10) not null,"
                        "compatible char(35) not null,"
                        "indications char(26) not null)")
            print(f"Таблица donor успешно создана")

            cur.executemany("INSERT INTO donor values (%s, %s, %s, %s)",
                            [(1, 'CcDee', 'CcDee CCDee ccddee ccDee Ccddee', 'отсутствуют'),
                             (2, 'CCDee', 'CCDee CCddee', 'отсутствуют'),
                             (3, 'CcDEe', 'Любой фенотип, кроме Cw +', 'Любой фенотип, кроме Cw +'),
                             (4, 'ccddee', 'ccddee', 'Ccddee'),
                             (5, 'ccDEe', 'ccDEe ccddee ccDee ccDEE ccddEe', 'CcDee CcDEe Ccddee CcddEe'),
                             (6, 'CwCDee', 'CwCDee', 'CCDee'),
                             (7, 'ccDEE', 'ccDEE ccddEE', 'ccDEe CcDEE'),
                             (8, 'CwcDee', 'CwcDee', 'CcDee CCDee CwCdee'),
                             (9, 'ccDee', 'ccDee ccddee', 'CcDee Ccddee'),
                             (10, 'Ccddee', 'Ccddee ccddee CCddee', 'ccddEe'),
                             (11, 'CwcDEe', 'CwcDEe ccDEe ccddee', 'CcDee CcDEe'),
                             (12, 'ccDweakee', 'ccDweakee ccddee', 'Ccddee'),
                             (13, 'CcddEe', 'ccddee Ccddee CcddEe ccddEe CCddee', 'отсутствуют'),
                             (14, 'CCDEe', 'CCDEe CCDee CCddee', 'отсутствуют'),
                             (15, 'ccddEe', 'ccddEe ccddEE ccddee', 'Ccddee CcddEe'),
                             (16, 'CcDEE', 'CcDEE ccDEE ccddEE', 'CcDEe CcddEe ccddEe'),
                             (17, 'Cwcddee', 'Cwcddee ccddee', 'Ccddee'),
                             (18, 'CCddee', 'CCddee', 'Ccddee ccddee'),
                             (19, 'CCDEE', 'CCDEE', 'CCDEe CCDee'),
                             (20, 'CCddEe', 'CCddEe CCddee', 'Ccddee ccddee'),
                             (21, 'CcddEE', 'CcddEE ccddEE', 'CcddEe ccddEe ccddee'),
                             (22, 'ccddEE', 'ccddEE', 'ccddEe'),
                             (23, 'CCDweakee', 'CCDweakee CCddee', 'CCDee'),
                             (24, 'CcDweakee', 'CcDweakee CCDweakee ccDweakee', 'Ccddee ccddee'),
                             (25, 'ccDweakEe', 'ccddee ccddEe ccDweakEe', 'Ccddee CcddEe'),
                             (26, 'ccDweakEE', 'ccDweakEE ccddEe ccddEE', 'CcddEe ccddee'),
                             (27, 'CwcddEe', 'ccddee ccddEe CwcddEe', 'Ccddee CcddEe'),
                             (28, 'CwcDEE', 'CwcDEE ccDEE ccddEE', 'CcDEe'),
                             (29, 'kk', 'kk', 'отсутствуют'),
                             (30, 'Kk', 'Kk kk KK', 'отсутствуют'),
                             (31, 'KK', 'KK', 'Kk kk')])
            conn.commit()
            print(f"Данные успешно добавлены")

            cur.execute("SELECT * FROM donor")

            total = cur.fetchall()
            print('\n'.join([str(i) for i in total]))
else:
    print(f'С базой данных соединение не произошло')

#insert into donor (recipient, compatible, indications) values ('CcDee', 'CcDee CCDee ccddee ccDee Ccddee', 'отсутствуют');