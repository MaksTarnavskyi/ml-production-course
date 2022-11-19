build_feast:
	docker build -t fs:latest .

run_feast: build_feast
	docker run -it -v $PWD:/app -p 8080:8080 fs:latest /bin/bash
