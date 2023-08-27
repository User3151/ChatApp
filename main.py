from server import ChatServer
import threading
import os
import datetime 
from utils import find_longest_message, find_most_active_client, read_messages_in_time_frame
from dotenv import load_dotenv
load_dotenv()

def main():
    HOST = os.environ.get('CHAT_SERVER_HOST', '127.0.0.1')
    PORT = int(os.environ.get('CHAT_SERVER_PORT', 5050))

    server = ChatServer(HOST, PORT)
    
    # thread to handle incoming client connections
    accept_thread = threading.Thread(target=server.client_acceptance_thread)
    accept_thread.start()

    try:
        while True:
            pass
    except KeyboardInterrupt:
        server.shutdown_server()

if __name__ == "__main__":
    main()

longest_message, longest_client_name = find_longest_message()
print("\nLongest Message:")
print(f"From {longest_client_name}: {longest_message}")

most_active_client = find_most_active_client()
print("\nMost Active Client:" + most_active_client)

start_time_str = input("Enter start time (YYYY-MM-DD HH:MM:SS): ")
end_time_str = input("Enter end time (YYYY-MM-DD HH:MM:SS): ")

start_time = datetime.datetime.strptime(start_time_str, '%Y-%m-%d %H:%M:%S')
end_time = datetime.datetime.strptime(end_time_str, '%Y-%m-%d %H:%M:%S')

messages_in_time_frame = read_messages_in_time_frame(start_time, end_time)

print("\nMessages in Time Frame:")
for message in messages_in_time_frame:
    print(message)

