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

Create pod for flask-app
```
kubectl create -f k8s-resources/pod-flask-app.yaml
```

Create deployment for flask-app
```
kubectl create -f k8s-resources/deployment-flask-app.yaml
```

Create service for flask-app
```
kubectl create -f k8s-resources/service-flask-app.yaml
```

Run port forwarding
```
    kubectl port-forward svc/deployment-flask-app 5000:5000
```

And then one more time paste in browser: http://0.0.0.0:5000/ and enjoy :)

Try autoscaling
```
    kubectl autoscale deployment deployment-flask-app  --min=2 --max=3
```

See status
```
    kubectl get pods
    kubectl get deployment
    kubectl get service
```

Delete one pod and look that another pod replace it
```
    kubectl delete pod deployment-flask-app-8694ff94bc-682hp
```

Delete everything
```
    kubectl delete service deployment-flask-app
    kubectl delete deployment deployment-flask-app
    kubectl delete pod pod-flask-app
```

Delete cluster
```
    kind delete cluster --name week-1
```
