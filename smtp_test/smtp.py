import base64
import socket as _socket
import time
import ssl


class Custom_SMTP:

    def __init__(self, host='', port=0, crypto_method=None,
                 timeout=_socket._GLOBAL_DEFAULT_TIMEOUT,
                 source_address=None):
        self._host = host
        self._port = port
        self.timeout = timeout
        self.esmtp_features = {}
        self.command_encoding = "ascii"
        self.source_address = source_address
        if crypto_method == "SSL":
            self.socket = ssl.wrap_socket(_socket.socket(_socket.AF_INET, _socket.SOCK_STREAM), ssl_version=ssl.PROTOCOL_SSLv23)   # noqa
        elif crypto_method == "TLS":
            self.socket = ssl.wrap_socket(_socket.socket(_socket.AF_INET, _socket.SOCK_STREAM), ssl_version=ssl.PROTOCOL_TLSv1_2)    # noqa
        else:
            self.socket = _socket.socket(_socket.AF_INET, _socket.SOCK_STREAM)

    def connect(self):
        self.socket.connect((self._host, self._port),)
        if self.socket.recv(1024).decode()[:3] != '220':
            raise Exception('220 reply not received from server.')

    def ehlo(self):
        heloCommand = 'EHLO Alice\r\n'
        self.socket.send(heloCommand.encode())

        if self.socket.recv(1024).decode()[:3] != '250':
            raise Exception('250 reply not received from server.')

    def login(self, username, password):
        base64_str = ("\x00" + username + "\x00" + password).encode()
        base64_str = base64.b64encode(base64_str)
        authMsg = "AUTH PLAIN ".encode() + base64_str + "\r\n".encode()
        return self.socket.send(authMsg)

    def send_mail(self, from_, to_, msg, subject):
        mail_from = "MAIL FROM:<%s>\r\n" % from_
        self.socket.send(mail_from.encode())

        mail_to = "RCPT TO:<%s>\r\n" % to_
        self.socket.send(mail_to.encode())

        data = "DATA\r\n"
        self.socket.send(data.encode())

        subject = "Subject: %s \r\n\r\n" % subject
        self.socket.send(subject.encode())

        date_format = "%a, %d %b %Y %H:%M:%S +0000"
        date = "%s \r\n\r\n" % time.strftime(date_format, time.gmtime())
        self.socket.send(date.encode())

        self.socket.send(msg.encode())

        endmsg = "\r\n.\r\n"
        self.socket.send(endmsg.encode())

        quit_str = "QUIT\r\n"
        self.socket.send(quit_str.encode())

        self.socket.close()
