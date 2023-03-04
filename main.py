#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys

from threading import Thread, Event
from PyQt5.QtWidgets import QApplication, QMainWindow


from database.database import DataBase
from timer.timer import timer

from ui.main_form import Ui_MainWindow

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

def thread_timer():
    """Запуск таймера в отдельном потоке"""

    timer_event = Thread(target=event_timer)
    timer_event.start()

def event_stop_timer():
     stop_event_timer.set()

def event_timer():
    timer(ui.labelTimer, stop_event_timer)


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window)

    data_base = DataBase()
    players = data_base.select_all_players()
    loaded_data_database(players)

    stop_event_timer = Event()

    ui.btnAddUser.clicked.connect(event_add_player_database)
    ui.btnDelUser.clicked.connect(event_delete_player_database)

    ui.btnStartTur.clicked.connect(thread_timer)
    ui.btnStopTur.clicked.connect(event_stop_timer)

    window.show()
    sys.exit(app.exec())
