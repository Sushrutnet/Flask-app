from kubernetes import client, config
from kubernetes.client.exceptions import ApiException

def get_k8s_client():
    try:
        # Load the kube config
        config.load_kube_config()
        return client.CoreV1Api()
    except Exception as e:
        print(f"Error loading Kubernetes config: {e}")
        return None

def get_running_pods(api_client, namespace):
    try:
        pods = api_client.list_namespaced_pod(namespace)
        return [pod for pod in pods.items if pod.status.phase == "Running"]
    except ApiException as e:
        print(f"Error fetching pods: {e}")
        return []

def check_pods_status(pods):
    for pod in pods:
        print(f"Pod Name: {pod.metadata.name}, Status: {pod.status.phase}")

def fetch_and_save_logs(api_client, pod_name, namespace="default"):
    try:
        # Fetch logs of the pod
        logs = api_client.read_namespaced_pod_log(pod_name, namespace=namespace)

        # Save the logs to a file
        log_filename = f"{pod_name}-logs.txt"
        with open(log_filename, 'w') as log_file:
            log_file.write(logs)

        print(f"Logs for pod {pod_name} saved to {log_filename}")

    except ApiException as e:
        print(f"Error fetching logs for pod {pod_name}: {e}")

def main():
    namespace = "default"  # Specify the namespace where your pods are located
    api_client = get_k8s_client()

    if api_client is None:
        return

    # Get all the pods in the specified namespace
    pods = get_running_pods(api_client, namespace)

    if pods:
        # Check the status of each pod
        check_pods_status(pods)

        # Fetch logs for each running pod
        for pod in pods:
            fetch_and_save_logs(api_client, pod.metadata.name, namespace)
    else:
        print("No pods found in the specified namespace.")

if __name__ == "__main__":
    main()

