import sqlite3

class DataBase:
    """Попытка подключения к БД"""

    try:
        __database_connection = sqlite3.connect('database/tournaments.db')
        __cursor = __database_connection.cursor()
    except sqlite3.Error as e:
        print('Ошибка при подключении к базе данных:', e)

    @staticmethod
    def add_player(fio):
        """Добавление игрока в БД"""

        try:
            DataBase.__cursor.execute("""
                INSERT INTO gamers (FIO)
                VALUES (?)
            """, [fio])
            DataBase.__database_connection.commit()
        except sqlite3.Error as e:
            print("Ошибка добавления игрока в базу данных:", e)

    @staticmethod
    def delete_player(self, fio):
        """Удаления игрока из БД"""

        try:
            self.__cursor.execute(f"""
                DELETE FROM gamers
                WHERE fio = "{fio}"
            """)
            DataBase.__database_connection.commit()
        except sqlite3.Error as e:
            print('Ошибка удаления игрока:', e)

    @staticmethod
    def select_all_players():
        """Все игроки из БД"""

        try:
            res = DataBase.__cursor.execute("""
                SELECT FIO 
                FROM gamers
            """)
            return res.fetchall()
        except sqlite3.Error as e:
            print('Ошибка при извлечении данных:', e)

    @staticmethod
    def close_database():
        """Закрытие соединения с БД"""

        try:
            if (DataBase.__database_connection):
                DataBase.__cursor.close()
                DataBase.__database_connection.close()

        except sqlite3.Error as e:
            print('Ошибка при закрытии базы данных:', e)