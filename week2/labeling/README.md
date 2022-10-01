## Install label studio

```
    mkdir mydata
    docker pull heartexlabs/label-studio:latest
    docker run -it -p 8080:8080 -v mydata:/label-studio/data heartexlabs/label-studio:latest
```

## Instruction how to setup up labeling process

![0](./screenshots/0.png)
![1](./screenshots/1.png)
![2](./screenshots/2.png)
![3](./screenshots/3.png)
![4](./screenshots/4.png)
![5](./screenshots/5.png)
![6](./screenshots/6.png)
![7](./screenshots/7.png)
![8](./screenshots/8.png)
![9](./screenshots/9.png)

## Data

I decied to use data from [UA-GEC](https://github.com/grammarly/ua-gec#python-library) - Ukrainian Grammatical Error Correction dataset
