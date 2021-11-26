docker build -t nginx-meat:0.5 -f dockerfiles/Dockerfile.meat.nginx .

docker build -t meat-api-v1:0.5 -f dockerfiles/Dockerfile.meat.v1 .

docker build -t meat-api-v2:0.5 -f dockerfiles/Dockerfile.meat.v2 .

docker build -t veg-api:0.5 -f dockerfiles/Dockerfile.vegetarian.v1 .

docker build -t nginx-veggie:0.5 -f dockerfiles/Dockerfile.vegetarian.nginx .
