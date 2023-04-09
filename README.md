rec's Port Scanner
This is a simple port scanner application developed using Python and PyQt5. The application allows the user to enter an IP address and a range of ports to scan, and then scans the specified range of ports to check if they are open or closed.

The user interface is designed using PyQt5 and consists of several input fields and a "Scan" button. The application uses Python's socket module and a ThreadPoolExecutor to scan the specified range of ports in parallel.

Usage
To use the application, simply run the portscanner.py script. The following input fields are provided:

IP: The IP address to scan.
Start Port: The starting port number of the range to scan.
End Port: The ending port number of the range to scan.
After entering the input values, click on the "Scan" button to start the scan. The application will display the result in the text area below the input fields. The result will show which ports are open on the specified IP address.

Installation
To install the application, follow these steps:

Clone the repository or download the source code.
Install the required dependencies using pip install -r requirements.txt.
Run the portscanner.py script.
Dependencies
Python 3.10.11
PyQt5
concurrent.futures
License
This application is licensed under the MIT License. See the LICENSE file for more information.
