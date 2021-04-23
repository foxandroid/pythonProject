import socket as plc

DREG = 1
RREG = 2
WREG = 3
MBIT = 4
BBIT = 5


class Conn:
    def __init__(self, ipaddress, port):
        self.ip = ipaddress
        self.port = port


class WDataObj:
    def __init__(self, start_address, data_length, data):
        self.start_address = start_address
        self.data_length = data_length
        self.data = data


class RDataObj:
    def __init__(self, start_address, data_length):
        self.start_address = start_address
        self.data_length = data_length


def write_data(conn, wdataobj, datatype):
    if wdataobj.data_length == len(wdataobj.data):
        # First command
        data = ""
        for x in range(wdataobj.data_length):
            if 0 < datatype < 4:
                data = data + format(wdataobj.data[x], '04x').upper()
            elif 3 < datatype < 6:
                data = data + format(wdataobj.data[x], '0x').upper()
        rd = __get_common_data_2(2, wdataobj.start_address, wdataobj.data_length, datatype) + data
        dl = format(len(rd), '04x').upper()
        cmd = __get_common_data_1() + dl + rd
        print(cmd)
        __socket_send(conn, cmd)
    else:
        print("Data Error")
        return 0


def read_data(conn, read_data_obj, datatype):
    # First command
    rd = __get_common_data_2(1, read_data_obj.start_address, read_data_obj.data_length, datatype)
    dl = format(len(rd), '04x').upper()
    cmd = __get_common_data_1() + dl + rd
    print(cmd)
    __socket_send(conn, cmd)


def __get_common_data_1():
    # Fix Data
    sh = "5000"
    nn = "00"
    pcn = "FF"
    rdmio = "03FF"
    rdms = "00"

    commondata = sh + nn + pcn + rdmio + rdms
    return commondata


def __get_common_data_2(rwinfo, start_address, data_length, datatype):
    # Read Data
    if rwinfo == 1:
        mt = "0000"
        rwcmd = "0401"
        # Write Data
    elif rwinfo == 2:
        mt = "0028"
        rwcmd = "1401"
    else:
        return "0000"

    if 0 < datatype < 4:
        scmd = "0000"
    elif 3 < datatype < 6:
        scmd = "0001"
    else:
        return "0000"
    if datatype == 1:
        reg = "D*"
    elif datatype == 2:
        reg = "R*"
    elif datatype == 3:
        reg = "W*"
    elif datatype == 4:
        reg = "M*"
    elif datatype == 5:
        reg = "B*"
    else:
        return "0000"

    rno = format(start_address, '06').upper()
    ndp = format(data_length, '04x').upper()

    commondata2 = mt + rwcmd + scmd + reg + rno + ndp
    return commondata2


def __socket_send(conn, cmd):
    with plc.socket(plc.AF_INET, plc.SOCK_STREAM) as s:
        s.connect((conn.ip, conn.port))
        s.sendall(cmd.encode())
        data = s.recv(1024)
    print('Received', repr(data))
