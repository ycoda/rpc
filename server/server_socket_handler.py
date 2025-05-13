import socket # ソケット通信を行うためのライブラリ
import os # ファイル操作やパス操作を行うためのライブラリ

class ServerSocketHandler:
    def __init__(self, socket_path='/tmp/unix.sock'):
        self.socket_path = socket_path # インスタンス変数に保存
        self.server_socket = None # インスタンス変数を初期化

    # ソケットを作成してバインドするメソッド
    def create_and_bind_socket(self):
        if os.path.exists(self.socket_path): # ソケットファイルが存在するかどうか
            os.remove(self.socket_path) #  存在する場合は削除
        
        # ソケットを作成する
        self.server_socket = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
        # ソケットをpathにバインドする
        self.server_socket.bind(self.socket_path)
        # 同時接続の数を指定する
        self.server_socket.listen(5)
        print(f"Server listening on {self.socket_path}")

    def accept_connection(self):
        # リスニングソケットが接続要求を受け入れる
        client_socket, client_address = self.server_socket.accept()
        print("Client connected:")
        return client_socket

    def close_socket(self):
        # ソケットが存在する場合は削除する   
        if self.server_socket:
            self.server_socket.close()
            print("Server socket closed.")
