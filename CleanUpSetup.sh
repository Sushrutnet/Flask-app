echo -e "${GREEN}Stopping and Deleting Minikube Cluster...${NC}"
if command -v minikube &>/dev/null; then
  minikube stop || echo "Minikube already stopped"
  minikube delete || echo "Minikube cluster already deleted"
else
  echo -e "${RED}Minikube not found.${NC}"
fi

echo -e "${GREEN}Uninstalling Minikube...${NC}"
sudo rm -f /usr/local/bin/minikube

echo -e "${GREEN}Uninstalling kubectl...${NC}"
sudo rm -f /usr/local/bin/kubectl

echo -e "${GREEN}Stopping Docker and Removing Docker Components...${NC}"
if command -v docker &>/dev/null; then
  sudo systemctl stop docker
  sudo apt-get purge -y docker-ce docker-ce-cli containerd.io
  sudo rm -rf /var/lib/docker
  sudo rm -rf /etc/docker
  sudo rm -rf /var/lib/containerd
  sudo rm -rf /etc/apt/keyrings/docker.asc
else
  echo -e "${RED}Docker not found.${NC}"
fi

echo -e "${GREEN}Cleaning up Kubernetes configuration...${NC}"
rm -rf ~/.kube
rm -rf ~/.minikube

echo -e "${GREEN}Cleaning apt caches...${NC}"
sudo apt-get autoremove -y
sudo apt-get clean

echo -e "${GREEN}Cleanup complete!${NC}"

"CleanupK8s.sh" 44L, 1126B                                    44,0-1        Bot
