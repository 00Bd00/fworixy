# fwproxy

## Functionality:
The script acts as a TCP proxy server, forwarding traffic between client connections and a specified target host and port.

## Usage: 
1. Run the script (python your_script_name.py).
2. When prompted, enter the desired proxy port number.
3. Enter the target host address (e.g., "www.example.com").
4. Enter the target port number (e.g., 80 for HTTP).
5. The proxy server starts listening on the specified port.

## How it works:
1.Clients connect to the proxy server on the defined port.
2.For each client connection, a new thread is created.
3.The thread handles the client connection:
 -Receives data from the client up to a maximum of 4096 bytes.
 -Establishes a connection to the target host and port.
 -Forwards the received data to the target host.
 -Receives the response from the target host.
 -Sends the response back to the client.
5.Both client and target connections are closed after data transfer is complete.

## Dependencies:
Python 3.x
socket module
threading module

## Limitations:

- This is a simple implementation for educational purposes and might not be suitable for production use.
- It only supports TCP connections and doesn't handle advanced features like HTTP proxies.

## Additional notes:
- The current implementation reads target host and port information from user input during runtime. You can modify the code to store this information in a configuration file or accept it as command-line arguments.
- Consider adding error handling and logging for a more robust implementation.
