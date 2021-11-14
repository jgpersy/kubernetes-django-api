# A Kubernetes/Flask API #

## Objectives ## 

Set up a scalable Kubernetes API on a local machine.
The API can display multiple different versions of the same endpoint for A/B testing.
The theme is types of recipes, a meat recipes list and a vegetarian recipes list.

For unix machines.


## Technical description ##

A Kubernetes cluster with REST API microservices written in Python/Flask.

Each rest API endpoint is a separate microservice.

This increases stability as endpoints can be modified and deployed independently of eachother.

Istio acts as a "service mesh", layering on top of a standard Kubernetes Service, to direct traffic for A/B testing.

Each pod has 3 containers:
- A Flask web app served by Gunicorn
- An NGINX reverse proxy container.
- An Istio container which is injected automatically.

An additional NGINX ingress is used. This is to display the app on the local machine.
On a production deploy this could be e.g. an AWS Application Load Balancer instead.


## Setup ##

### Kubernetes ###

- Install Kubernetes' [kubectl](https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/)

### Minikube ###

- Install [minikube](https://minikube.sigs.k8s.io/docs/start/).

- Run `minikube start`

- Allow Minikube to access local Docker images 
`eval $(minikube docker-env)`

- Install istioctl and enable Istio in the cluster by following steps for ['Download Istio' and 'Install Istio'](https://istio.io/latest/docs/setup/getting-started/)

- Enable the NGINX ingess [(docs)](https://kubernetes.io/docs/tasks/access-application-cluster/ingress-minikube/)
`minikube addons enable ingress`

- Verify that the NGINX Ingress controller is running
`kubectl get pods -n ingress-nginx`

### Build Docker images ###

- Navigate into this repo at the top level, and run the commands to build each Docker container.

- Make sure whatever you tag the images as, they are referenced in the minikube.yaml file.

`docker build -t nginx-meat:0.3 -f dockerfiles/Dockerfile.meat.nginx .`

`docker build -t meat-api-v1:0.3 -f dockerfiles/Dockerfile.meat.v1 .`

`docker build -t meat-api-v2:0.4 -f dockerfiles/Dockerfile.meat.v2 .`

`docker build -t veg-api:0.1 -f dockerfiles/Dockerfile.vegetarian.v1 .`

`docker build -t nginx-veggie:0.2 -f dockerfiles/Dockerfile.vegetarian.nginx .`

### Deploy to Kubernetes cluster ###

- Run your kubectl applys

`kubectl apply -f kube-yaml-files/minikube.yaml`

`kubectl apply -f kube-yaml-files/istio.yaml`

`kubectl apply -f kube-yaml-files/nginx-ingress.yaml`

### View the webpage ###

- Run `kubectl get ingress`

- Use the "Address" column's IP from the output and add the following line to the bottom of the /etc/hosts file on your computer (you will need administrator access)
e.g.
`172.17.0.15 recipes.info`

- You can now navigate to recipes.info in your browser, go to /meat/ or /vegetarian/ to see the API's response.

- Try opening /meat/ in an Incognito/Private Browser window a few times to see the different API versions.
