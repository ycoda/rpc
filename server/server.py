from server_socket_handler import ServerSocketHandler
from request_handler import RequestHandler
import threading

def main():
    socket_handler = ServerSocketHandler()
    request_handler = RequestHandler()

    try:
        # ソケットを作成してpathにバインドしてリスニング状態に設定する
        socket_handler.create_and_bind_socket()

        while True:
            # クライアントからの接続を受け入れ、クライアントソケットを取得する
            client_socket = socket_handler.accept_connection()
            # スレッドを作成し、同時接続を可能にする
            client_thread = threading.Thread(target=request_handler.handle_request, args=(client_socket,))
            client_thread.start()
    except KeyboardInterrupt:
        print("Server stopped user.")
    finally:
        # サーバーソケットを閉じてリソースを解放する
        socket_handler.close_socket()

# server.pyスクリプトが直接実行された場合にmain()を呼び出す
if __name__ == "__main__":
    main()