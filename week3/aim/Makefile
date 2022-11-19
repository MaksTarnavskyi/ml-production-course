build_aim:
	docker build -f Dockerfile -t aim:latest .

run_aim: build_aim
	docker run -it -v ${PWD}:/main aim:latest /bin/bash