import socket
import serial

def send_data_to_uart(data):
    # Open the serial port with baud rate 9600
    ser = serial.Serial('/dev/ttyUSB0', 9600, timeout=1)

    # Send data to the serial port
    ser.write(data.encode())
    
    # Close the serial port
    ser.close()

def handle_client_connection(client_socket):
    try:
        # Receive data from the client
        received_data = b''
        while len(received_data) < 37:
            chunk = client_socket.recv(37 - len(received_data))
            if not chunk:
                raise ValueError("Incomplete message received")
            received_data += chunk
        
        # Validate the received message
        if received_data.startswith(b'{') and received_data.endswith(b'}'):
            print("Received valid message from client:", received_data.decode())
            
            # Send data to the UART without decoding it again
            send_data_to_uart(received_data)
            
            print("Data sent to UART successfully.")
        else:
            raise ValueError("Invalid message format")
    except Exception as e:
        print("Error:", e)
    finally:
        # Close the client socket
        client_socket.close()

def start_server():
    # Server IP and port
    SERVER_IP = '192.168.127.125'
    SERVER_PORT = 12345

    # Create a socket object
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Bind the socket to the server IP and port
        server_socket.bind((SERVER_IP, SERVER_PORT))

        # Listen for incoming connections
        server_socket.listen(5)
        print("Server listening on", SERVER_IP, "port", SERVER_PORT)

        while True:
            # Accept incoming connections
            client_socket, client_address = server_socket.accept()
            print("Accepted connection from", client_address)

            # Handle client connection
            handle_client_connection(client_socket)
    except Exception as e:
        print("Error:", e)
    finally:
        # Close the server socket
        server_socket.close()

# Start the server
start_server()
