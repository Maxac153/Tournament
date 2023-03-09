#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys
import random

from threading import Thread, Event
from PyQt5.QtWidgets import QApplication, QMainWindow

from database.database import DataBase
from timer.timer import timer

from ui.main_form import Ui_MainWindow

def event_add_player_database():
    """Добавление игрока в базу данных"""

    fio = ui.editUser.text()
    DataBase.add_player(fio)
    players_db.append(fio)
    ui.listUsersDatabase.addItem(fio)


def select_list_users_database(ui_list):
    """Удаление игрока из списка"""

    players = ui_list.selectedItems()
    if not players:
        return

    for player in players:
        p = ui_list.row(player)
        ui_list.takeItem(p)
        return player.text()


def event_del_player_database():
    """Удаление игрока из базы данных"""

    fio = select_list_users_database(ui.listUsersDatabase)
    DataBase.delete_player(fio)
    players_db.remove(fio)

def loaded_data_database(players):
    """Загрузка данных в лист"""

    for player_name in players:
        ui.listUsersDatabase.addItem(player_name)


def event_add_player_list():
    """Добавление игрока в турнир"""

    fio = select_list_users_database(ui.listUsersDatabase)
    ui.listUsersTournament.addItem(fio)

def event_del_player_list():
    """Удаление игрока из турнира"""

    fio = select_list_users_database(ui.listUsersTournament)
    ui.listUsersDatabase.addItem(fio)

def thread_timer():
    """Запуск таймера в отдельном потоке"""

    timer_event = Thread(target=event_timer)
    timer_event.start()

def event_stop_timer():
     stop_event_timer.set()

def event_timer():
    players = []
    players_scrole = {}

    for i in range(len(ui.listUsersTournament)):
        fio = ui.listUsersTournament.item(i).text()
        players.append(fio)
        players_scrole[fio] = 0

    if len(players) % 2 != 0:
        players.append('by')

    print(players)
    tournament_parings = []

    for _ in range(len(players) // 2):
        player_one, player_two = random.sample(players, 2)
        players.remove(player_one)
        players.remove(player_two)
        tournament_parings.append((player_one, player_two))

    print(tournament_parings)

    timer(ui.labelTimer, stop_event_timer) 

def event_search_player():
    """Поиск игрока в листе"""

    fio = ui.editSearchUser.text()
    result_search = []

    for player in players_db:
        if player.find(fio) != -1:
            result_search.append(player)

    ui.listUsersDatabase.clear()
    ui.listUsersDatabase.addItems(result_search)



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(window)

    players_db = [player[0] for player in DataBase.select_all_players()]

    loaded_data_database(players_db)

    stop_event_timer = Event()

    ui.btnAddUser.clicked.connect(event_add_player_database)
    ui.btnDelUser.clicked.connect(event_del_player_database)

    ui.btnStartTur.clicked.connect(thread_timer)
    ui.btnStopTur.clicked.connect(event_stop_timer)

    ui.btnAddList.clicked.connect(event_add_player_list)
    ui.btnDelList.clicked.connect(event_del_player_list)

    ui.editSearchUser.textChanged.connect(event_search_player)

    window.show()
    sys.exit(app.exec())
