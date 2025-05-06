IMAGE_NAME=movie-recommendation
CONTAINER_NAME=movie-container

build:
	@echo "Construindo a imagem Docker..."
	docker build -t $(IMAGE_NAME) .

run:
	@echo "Rodando o container em segundo plano..."
	docker run -d --name $(CONTAINER_NAME) -p 5000:5000 $(IMAGE_NAME)

stop:
	@echo "Parando o container..."
	docker stop $(CONTAINER_NAME)

clean: stop
	@echo "Deletando o container..."
	docker rm $(CONTAINER_NAME)

delete-image:
	@echo "Deletando a imagem Docker..."
	docker rmi $(IMAGE_NAME)