build_app_streamlit:
	docker build -f Dockerfile -t app-streamlit:latest --target app-streamlit .  

run_app_streamlit: build_app_streamlit
	docker run -it -p 8080:8080 -e WANDB_API_KEY=${WANDB_API_KEY} app-streamlit:latest
