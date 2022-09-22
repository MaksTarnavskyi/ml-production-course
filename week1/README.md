## Task 1 - Create simple app

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


## Task 2 - Deploy on K8s

```
    brew install kind
```

Create cluster

```
    kind create cluster --name week-1
```
Check current context
```
    kubectl config get-contexts
```
