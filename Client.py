import socket

def send_data_to_server(data):
    # Server IP and port
    SERVER_IP = '192.168.127.125'
    SERVER_PORT = 5000 # You need to specify the port the server is listening on

    # Create a socket object
    client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to the server
        client_socket.connect((SERVER_IP, SERVER_PORT))

        # Send data to the server
        client_socket.sendall(data.encode())

        print("Data sent successfully to the server.")
    except Exception as e:
        print("Error:", e)
    finally:
        # Close the socket
        client_socket.close()

# Example data in string format
data_to_send = "{01,B,-0200,+0200,1000,1921681010220,0250}"

# Call the function to send data to the server
send_data_to_server(data_to_send)
