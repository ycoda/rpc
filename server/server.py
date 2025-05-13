from server_socket_handler import ServerSocketHandler
from request_handler import RequestHandler

def main():
    socket_handler = ServerSocketHandler()
    request_handler = RequestHandler()

    try:
        # ソケットを作成してpathにバインドしてリスニング状態に設定する
        socket_handler.create_and_bind_socket()

        while True:
            # クライアントからの接続を受け入れ、クライアントソケットを取得する
            client_socket = socket_handler.accept_connection()
            # クライアントからのリクエストを処理する
            request_handler.handle_request(client_socket)
    except KeyboardInterrupt:
        print("Server stopped user.")
    finally:
        # サーバーソケットを閉じてリソースを解放する
        socket_handler.close_socket()

# server.pyスクリプトが直接実行された場合にmain()を呼び出す
if __name__ == "__main__":
    main()