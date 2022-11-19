build_aim:
	docker build -f Dockerfile -t aim:latest .

run_aim: build_aim
	docker run -p 43800:43800 -v ${PWD}:/main aim:latest 
