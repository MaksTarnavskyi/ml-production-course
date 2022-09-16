## Task 1

To build image:
```
    docker build -t maksymtarnavskyi/simple-app .
```

To pull image:
```
    docker pull maksymtarnavskyi/simple-app:week1-simple-app
```

To build and push - run bash script:
```
    chmod +x task-1.sh
    ./task-1.sh
```

To run application:
```
    docker run -p 8888:5000 maksymtarnavskyi/simple-app
```
Then paste in browser: http://0.0.0.0:8888/ and enjoy :)
