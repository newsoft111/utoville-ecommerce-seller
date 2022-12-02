run:
	docker pull mcfly17/utoville-homecare-seller:dev
	docker stop seller
	docker run -d --name seller -p 8002:8002 docker/utoville-homecare-seller