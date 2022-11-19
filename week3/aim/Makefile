build_aim:
	docker build -f Dockerfile -t aim:latest .

run_aim: build_aim
	docker run -v ${PWD}:/main aim:latest