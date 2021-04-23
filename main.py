# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from ais import plc


def entrypoint():
    # Use a breakpoint in the code line below to debug your script.
    print(format(2346, '04x').upper())
    host = '192.168.1.100'
    port = 8080
    conn = plc.Conn(host, port)

    data = [6000, 0, 0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0, 0, 0, 1, 1, 1]
    w_data_obj = plc.WDataObj(700, 20, data)
    print(plc.write_data(conn, w_data_obj, plc.DREG))
    # r_data_obj = plc.RDataObj(0, 20)
    # print(plc.read_data(conn, r_data_obj, plc.MBIT))


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    entrypoint()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
