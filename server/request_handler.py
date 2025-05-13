import json #JSON形式のデータを扱うためのライブラリ
from rpc_functions import functions
from display_json import custom_format_display

class RequestHandler:
    # クライアントからのリクエストを処理するメソッド
    def handle_request(self, client_socket):
        try:
            # クライアントからのリクエストを受信する
            request = client_socket.recv(1024).decode('utf-8')
            # JSON文字列をPythonの辞書形式に変換する
            request_data = json.loads(request)

            # リクエストデータから値を取得して表示
            method = request_data.get("method")
            params = request_data.get("params")
            param_types = request_data.get("param_types")
            request_id = request_data.get("id")
            custom_format_display(method, params, param_types, request_id)

            # クライアントへのレスポンスを作成する
            response = {}
            try:
                result = functions[method](*params)
                response["results"] = result
                response["result_type"] = type(result).__name__
                response["id"] = request_id
            except Exception as e:
                print(f"Received request: {request_data}")
                response["error"] = f"Error executing method '{method}': {str(e)}"
                print(response["error"])
            
            # レスポンスをクライアントに送信する
            client_socket.sendall(json.dumps(response, separators=(", ", ": ")).encode('utf-8'))
        except Exception as e:
            print(f"An error occurred while handling the request: {e}")
        finally:
            # クライアントソケットを閉じてリソースを解放する
            client_socket.close()
            print("Client socket closed.")
