import socket as plc


class Conn:
    def __init__(self, ipaddress, port):
        self.ip = ipaddress
        self.port = port


class DRegister:
    def __init__(self, startdreg, datalength, data):
        self.startdreg = startdreg
        self.datalength = datalength
        self.data = data


def send_data(conn, dregister):
    with plc.socket(plc.AF_INET, plc.SOCK_STREAM) as s:
        s.connect((conn.ip, conn.port))
        # First command
        sh = "5000"
        nn = "00"
        pcn = "FF"
        rdmio = "03FF"
        rdms = "00"
        # Second command
        dl = "0040"
        mt = "0028"
        rwcmd = "1401"
        scmd = "0000"
        reg = "D*"
        rno = format(dregister.startdreg, '06').upper()
        ndp = format(dregister.datalength, '04x').upper()
        data = ""
        for x in range(dregister.datalength):
            data = data + dregister.data[x]
        cmd = sh+nn+pcn+rdmio+rdms+dl+mt+rwcmd+scmd+reg+rno+ndp+data
        s.sendall(cmd.encode())
        data = s.recv(1024)
    print('Received', repr(data))
