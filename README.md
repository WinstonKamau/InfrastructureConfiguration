# InfrastructureConfiguration

This repository is a learning project. I used it to learn how to create a Google Cloud Kubernetes Engine using [Google Cloud Deployment Manager](https://cloud.google.com/deployment-manager/docs).
By using the templates above, you create a Kubernetes cluster called `gke-cluster`. It contains a node pool that contains three `f1-micro` compute engines located in the `us-central1-a` region.

### Upgrades
- The cluster by default will be upgraded automatically by Google Cloud to the newest stable and secure version.
- Being a zonal cluster, it contains only one control plane or one master node. During upgrades:
    - Workloads run.
    - You can't deploy new workloads.
    - You can't modify existing workloads.
    - You can't make any changes to the existing cluster's configuration.
- With regards to node pools, they are upgraded one at a time with no defined order.

### Creating, Listing, Updating, Previewing and Deleting Deployments.

#### Setup
- Ensure you have the [gcloud package](https://cloud.google.com/sdk/install) installed on your machine.
- Ensure you have a Google Cloud project.
- Configure your gcloud package to point to the project where you would like to deploy the cluster.
```
gcloud config set core/project {project id}
```
- Your gcloud package should be authenticated to access your Google Cloud project.
```
gcloud auth login
gcloud application-default login
``` 
- Assuming your have cloned this repository and changed directory into the root of the repository, change directory to the `gke_cluster` directory.
```
cd gke_cluster
```
- export the deployment name
```
export DEPLOYMENT_NAME={deployment name}
```
#### Create a Deployment

```
gcloud deployment-manager deployments create ${DEPLOYMENT_NAME} --config gke_cluster.yaml
```

#### Update a Deployment

```
gcloud deployment-manager deployments update ${DEPLOYMENT_NAME} --config gke_cluster.yaml
```

#### Delete a Deployment

```
gcloud deployment-manager deployments delete ${DEPLOYMENT_NAME}
```

#### List Deployments

```
gcloud deployment-manager deployments list
```

#### Preview an update, and finally Update after preview
- Preview an update
```
gcloud deployment-manager deployments update ${DEPLOYMENT_NAME} --config gke_cluster.yaml --preview
```
- Go forth and update with the preview
```
gcloud deployment-manager deployments update ${DEPLOYMENT_NAME}
```
- Cancel a preview
```
gcloud deployment-manager deployments cancel-preview ${DEPLOYMENT_NAME}
```
