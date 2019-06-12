import mock

from hamcrest import assert_that
from smtp_test.smtp import Custom_SMTP


def test_login():
    with mock.patch('socket.socket') as mock_socket:
        mock_socket.return_value.recv.return_value = b'220 debugmail ESMTP ready\r\n'

        username = "rdtr.sis@gmail.com"
        password = "9f011aa0-8c9b-11e9-b444-f1b5425fec20"
        email_server = "debugmail.io"
        email_port = 25
        t = Custom_SMTP(
            host=email_server,
            port=email_port)
        t.connect()
        mock_socket.return_value.recv.return_value = b'250-debugmail\r\n250-AUTH PLAIN LOGIN\r\n250 STARTTLS\r\n'
        t.ehlo()
        resp = t.login(username=username, password=password)
        assert_that(resp, 89)
