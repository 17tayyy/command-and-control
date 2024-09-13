## Usage

This scripts form a simple client-server remote control setup, where `listener.py` acts as the server (listener) and `backdoor.py` acts as the client (backdoor). The listener receives commands and the backdoor executes them on the remote machine.

### Setup

1. **Ensure both scripts are on separate machines (or different terminals on the same machine for testing).**
   - The listener should be run on the attacker's machine.
   - The backdoor should be run on the target machine (you can make backdoor.py an executable file).

2. **Configure IP and Port**
   - Update the IP address and port in both scripts to match the network setup. By default, they are set to `192.168.1.50` and port `443`.

### Steps to Run

#### 1. Run the Listener (Server)

The listener waits for an incoming connection and then interacts with the connected backdoor.

```bash
./listener.py
````

#### 2. Run the Backdoor (client)
On the target machine, run the backdoor to establish a connection to the listener.

````bash
./backdoor.py
````
Once connected, the backdoor will:

- Receive commands from the listener.
- Execute them on the target system.
- Send back the output of the executed commands.

### Command Usage

In the `listener.py` session, you can run the following commands (i will be adding more in the future):

- **get users**: This command retrieves a list of system users from the target machine and sends it via email to a predefined address.

    ```bash
    >> get users
    ```

- **get firefox**: This command tries to list Firefox profiles stored on the target machine.

    ```bash
    >> get firefox
    ```

- **help**: Displays the available commands.

    ```bash
    >> help
    ```

- **Other Commands**: Any other commands entered will be executed remotely on the target machine using the backdoor.

    Example:

    ```bash
    >> dir
    ```
