# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
from ais import plc


def entrypoint():
    # Use a breakpoint in the code line below to debug your script.
    host = '192.168.1.100'
    port = 8080
    conn = plc.Conn(host, port)
    data = ["000A", "0000", "0000", "0000", "0000", "0000", "0000", "0000", "0000", "0000"]
    dreg = plc.DRegister(60, 10, data)
    plc.send_data(conn, dreg)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    entrypoint()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
