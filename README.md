##INSTALAÇÃO DOCKER

$ sudo apt-get install docker 
$ sudo apt-get install docker-compose
$ sudo groupadd docker-compose
$ sudo usermod -aG docker-compose $USER
$ sudo groupadd docker
$ sudo usermod -aG docker $USER
$ newgrp docker



##REFERÊNCIAS

https://docs.docker.com/compose/gettingstarted/
https://www.w3schools.com/python/pandas/default.asp
https://www.youtube.com/watch?v=VtTd_kArC74
https://stackoverflow.com/questions/16476924/how-to-iterate-over-rows-in-a-dataframe-in-pandas


##EXECUTAR PROJETO
$ docker-compose up --build
Acessar: http://localhost:8000/