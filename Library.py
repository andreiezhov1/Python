import sqlite3

def select_all_author(my_cursor: sqlite3.Cursor) -> None:
    try:
        query: str = "SELECT * from authors;"
        my_cursor.execute(query)
        rows: list[tuple[int, str, int]] = my_cursor.fetchall()
        row: tuple[int, str, int]
        for row in rows:
            print(row)
    except sqlite3.OperationalError as error:
        print(f"Ошибка в запросе: {error}")

def select_all_author(my_cursor: sqlite3.Cursor) -> None:
	try:
		query: str = "SELECT * from authors;"
		my_cursor.execute(query)
		rows: list[tuple[int, str, int]] = my_cursor.fetchall()
		row: tuole[int, str, int]
		for row in rows:
			print(row)
	except sqlite3.OperationalError as error:
		print(f"Ошибка в запросе: {error}")

def select_all_author(my_cursor: sqlite3.Cursor) -> None:
    try:
        query	
	

	
