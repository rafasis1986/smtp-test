# smtp_test

A sendmail library with sockets.

[![Circle CI](https://circleci.com/gh/rafasis1986/smtp-test/tree/develop.svg?style=svg)](https://circleci.com/gh/rafasis1986/smtp-test/tree/develop)

To use the library you will need import the `Custom_SMTP``from the smtp file and set the args to send the emails

```
from smtp_test.smtp import Custom_SMTP

username = "your@email.com"
password = "password"
email_server = "smtp_server"
email_port = 25
crypto = None   # you can use TLS or SSL string

```

We create thw socket client

```
client_socket = Custom_SMTP(
        host=email_server,
        port=email_port,
        crypto_method=crypto)
```

Later we create the conection and login with our credentials
```
client_socket.connect()
client_socket.ehlo()
client_socket.login(username, password)
   
```

And finally send the email with a custom message or subject
```
client_socket.send_mail(
    from_=username,
    to_=another@email.com,
    msg="Content message",
    subject="title")
    
``` 
