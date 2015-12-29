# mesos-demo-app

Just a small web application for demonstrating Mantl / Mesos scale out feature. 

## Usage

The docker container runs at port 1234.
Once the Docker container is up and running, you should be able to access it using curl. 

$ curl http://IPADDRESS:1234

By default the timeout is 20 seconds and maximum connection limit is 5. 
So for every five requests in 20 seconds you will get "Hello world" as output and other requests will output "Too much load".
To modify the variables .. you know what to do. 

