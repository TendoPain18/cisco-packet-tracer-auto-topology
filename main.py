import pygetwindow as gw
import pyautogui as pg


def is_window_open(window_name):
    is_open = any(window_name in window.title for window in gw.getAllWindows())
    if open:
        print(window_name + " is open.")
    else:
        print(window_name + " is not open.")
    return is_open


def get_window(window_name):
    window = gw.getWindowsWithTitle(window_name)[0]
    return window


def get_window_details(window):
    x, y, width, height = window.left, window.top, window.width, window.height
    print(f"Window coordinates: x={x}, y={y}, width={width}, height={height}")
    return [x, y, width, height]


def resize_window(window, new_x=-1, new_y=-1, new_width=-1, new_height=-1):
    data = get_window_details(window)
    if new_x != -1:
        data[0] = new_x
    if new_y != -1:
        data[1] = new_y
    if new_width != -1:
        data[2] = new_width
    if new_height != -1:
        data[3] = new_height
    window.moveTo(data[0], data[1])
    window.resizeTo(data[2], data[3])


def bring_on_top(window):
    window.activate()


def send_mouse_to(window, x, y):
    absolute_x = window.left + x
    absolute_y = window.top + y
    pg.moveTo(absolute_x, absolute_y)


def mouse_click():
    pg.click()


def default_zoom():
    pg.hotkey('ctrl', '0')


def zoom_in():
    pg.hotkey('ctrl', '=')


def zoom_out():
    pg.hotkey('ctrl', '-')


def add_pt_router(window, grid_, used_, row, col):
    if used_[row][col] == 0:
        send_mouse_to(window, 30, win_data[3] - 115)
        mouse_click()
        send_mouse_to(window, 30, win_data[3] - 50)
        mouse_click()
        send_mouse_to(window, 600, win_data[3] - 120)
        mouse_click()
        send_mouse_to(window, grid_[row][col][0], grid_[row][col][1])
        mouse_click()
        used_[row][col] = 1
    else:
        print("Error! Position at row " + str(row) + " and col " + str(col) + " used")


def add_pt_switch(window, grid_, used_, row, col):
    if used_[row][col] == 0:
        send_mouse_to(window, 30, win_data[3] - 115)
        mouse_click()
        send_mouse_to(window, 65, win_data[3] - 50)
        mouse_click()
        send_mouse_to(window, 280, win_data[3] - 120)
        mouse_click()
        send_mouse_to(window, grid_[row][col][0], grid_[row][col][1])
        mouse_click()
        used_[row][col] = 1
    else:
        print("Error! Position at row " + str(row) + " and col " + str(col) + " used")


def add_pc(window, grid_, used_, row, col):
    if used_[row][col] == 0:
        send_mouse_to(window, 65, win_data[3] - 115)
        mouse_click()
        send_mouse_to(window, 30, win_data[3] - 50)
        mouse_click()
        send_mouse_to(window, 240, win_data[3] - 120)
        mouse_click()
        send_mouse_to(window, grid_[row][col][0], grid_[row][col][1])
        mouse_click()
        used_[row][col] = 1
    else:
        print("Error! Position at row " + str(row) + " and col " + str(col) + " used")


def connect(window, grid_, used_, device_one, device_two):
    # if used_[device_one[0]][device_one[1]] == 1 and used_[device_two[0]][device_two[1]] == 1:
    send_mouse_to(window, 130, win_data[3] - 115)
    mouse_click()
    send_mouse_to(window, 30, win_data[3] - 50)
    mouse_click()
    send_mouse_to(window, 240, win_data[3] - 120)
    mouse_click()
    send_mouse_to(window, grid_[device_one[0]][device_one[1]][0] - 15, grid_[device_one[0]][device_one[1]][1] - 5)
    mouse_click()
    send_mouse_to(window, grid_[device_two[0]][device_two[1]][0] - 15, grid_[device_two[0]][device_two[1]][1] - 5)
    mouse_click()
    # else:
    #     print("Error! Can't connect to Air O_o")


def create_grid():
    used_ = []
    grid_ = []
    y_index = 198
    x_index = 61
    for ii in range(0, 14, 1):
        u = []
        row = []
        for jj in range(0, 37, 1):
            u.append(0)
            row.append([x_index, y_index])
            x_index = x_index + 50
        used_.append(u)
        grid_.append(row)
        x_index = 61
        y_index = y_index + 50
    print("grid size: " + str(len(grid_) * len(grid_[0])))
    return used_, grid_


def start():
    window = get_window("Cisco Packet Tracer")
    bring_on_top(window)
    resize_window(window, -1, -1, 1920, 1080)  # 1600 => 1549  , 1600 => 1226
    temp = get_window_details(window)
    bounds = [[11, 173], [temp[2] - 39, 173], [temp[2] - 39, temp[3] - 200], [11, temp[3] - 200]]
    default_zoom()
    zoom_out()
    zoom_out()
    zoom_out()
    used_, grid_ = create_grid()
    # print(1549 / 25)
    # print((1920 - 51) / 50)
    # print((1080 - 374) / 50)
    return window, temp, grid_, used_


if is_window_open("Cisco Packet Tracer"):
    win, win_data, grid, used = start()

    add_pc(win, grid, used, 5, 5)
    add_pt_switch(win, grid, used, 10, 10)
    connect(win, grid, used, [5, 5], [10, 10])
    # add_pt_router(win, grid, used, 0, 0)



