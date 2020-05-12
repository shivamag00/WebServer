# Web Server & Client
Make sure to turn your firewall OFF in case you want to set up a server on one host and client on the other host. 

# Basic
## TEST 1
Suppose the above server program is running. It takes 10 secs for the server to completely process the request.
Suppose Client A requests the server at t = 0s.
At t=5s Client B requests the server. The Client A and Client B are now waiting to receive a response. 
Then at t=10s server will send its response to Client A and at t=11s it will start processing request of Client B.
The Client B will keep on waiting until it receives the response from server which it will receive at t=20s 
