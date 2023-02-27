import sqlite3

class DataBase:
    """Попытка подключения к БД"""

    try:
        __database_connection = sqlite3.connect('database/tournaments.db')
        __cursor = __database_connection.cursor()
    except sqlite3.Error as e:
        print('Ошибка при подключении к базе данных:', e)

    def add_player(self, fio):
        """Добавление игрока в БД"""

        try:
            self.__cursor.execute("""
                INSERT INTO gamers (FIO)
                VALUES (?)
            """, [fio])
            self.__database_connection.commit()
        except sqlite3.Error as e:
            print("Ошибка добавления игрока в базу данных:", e)

    def delete_player(self, fio):
        """Удаления игрока из БД"""

        try:
            self.__cursor.execute(f"""
                DELETE FROM gamers
                WHERE fio = "{fio}"
            """)
            self.__database_connection.commit()
        except sqlite3.Error as e:
            print('Ошибка удаления игрока:', e)

    def select_all_players(self):
        """Все игроки из БД"""

        try:
            res = self.__cursor.execute("""
                SELECT FIO 
                FROM gamers
            """)
            return res.fetchall()
        except sqlite3.Error as e:
            print('Ошибка при извлечении данных:', e)


    def close_database(self):
        """Закрытие соединения с БД"""

        try:
            if (self.__database_connection):
                self.__cursor.close()
                self.__database_connection.close()

        except sqlite3.Error as e:
            print('Ошибка при закрытии базы данных:', e)