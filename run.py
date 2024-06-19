from lenar import app as flask_app


HOST = "0.0.0.0"
PORT = 8080


def main():
    flask_app.run(host=HOST, port=PORT)


if __name__ == '__main__':
    main()
