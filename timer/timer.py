import time

def convert_sec(t):
    return f'{t // 60}:{t % 60}'

def timer(ui_label_timer, event):
    time_end_min = 50
    time_end_sec = time_end_min * 60
    for i in range(time_end_sec):
        time.sleep(1)
        t = time_end_sec - i
        ui_label_timer.setText(convert_sec(t))
        if event.is_set():
             event.clear()
             return

    ui_label_timer.setText('5 ходов!')