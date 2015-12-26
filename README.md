docker build -t tensor .

docker run -t -P -i tensor

docker ps -l
CONTAINER ID        IMAGE               COMMAND             CREATED             STATUS              PORTS                     NAMES
11ada4d7f98e        tensor              "/bin/bash"         2 minutes ago       Up 2 minutes        0.0.0.0:32770->5000/tcp   reverent_brahmagupta

docker-machine ls
NAME      ACTIVE   DRIVER       STATE     URL                         SWARM   DOCKER   ERRORS
default   *        virtualbox   Running   tcp://192.168.99.100:2376           v1.9.1

curl -X GET -H "Content-Type: application/json" -H "Cache-Control: no-cache" 'http://192.168.99.100:32770/health'

curl -X POST -H "Content-Type: application/json" -H "Cache-Control: no-cache" -F "filedata=@15976.jpg" 'http://192.168.99.100:32770/tensor/classify'