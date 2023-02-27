#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

from PyQt5.QtWidgets import QApplication, QMainWindow

from ui.main_form import Ui_MainWindow
from database.database import DataBase


def event_add_player_database():
    """Добавление игрока в базу данных"""

    data_base = DataBase()
    data_base.add_player(ui.editUser.text())

def select_list_users_database():
    """Удаление игрока из списка"""

    players = ui.listUsersDatabase.selectedItems()
    if not players:
        return

    for player in players:
        p = ui.listUsersDatabase.row(player)
        ui.listUsersDatabase.takeItem(p)
        return player.text()

def event_delete_player_database():
    """Удаление игрока из базы данных"""

    fio = select_list_users_database()
    data_base = DataBase()
    data_base.delete_player(fio)

def loaded_data_database(players):
    """Загрузка данных в лист"""

    for player_name in players:
        ui.listUsersDatabase.addItem(player_name[0])

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window)

    data_base = DataBase()
    players = data_base.select_all_players()
    loaded_data_database(players)

    ui.btnAddUser.clicked.connect(event_add_player_database)
    ui.btnDelUser.clicked.connect(event_delete_player_database)

    window.show()
    sys.exit(app.exec())
