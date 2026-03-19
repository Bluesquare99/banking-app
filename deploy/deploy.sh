kubectl delete -f stock-ex-resources.yaml
docker build -t stock-ex --no-cache .
kubectl apply -f stock-ex-resources.yaml
# curl --header "Content-Type: application/json" --request POST --data '{"order_type":"buy","amount":"15"}' http://127.0.0.1:8000/order/
# minikube ssh