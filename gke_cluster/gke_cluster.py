def get_node_pool_oauth_scopes(oauth_scopes):
    oauth_scopes_list = []
    for scope in oauth_scopes:
        oauth_scopes_list.append("https://www.googleapis.com/auth/" + scope)
    return oauth_scopes_list


def generate_node_pools(cluster_properties):
    node_pools_properties = cluster_properties.get("nodePools")
    final_node_pools_config = []
    for node_pool in node_pools_properties:
        node_pool_config = node_pool.get("config")
        oauth_scopes = get_node_pool_oauth_scopes(node_pool_config.get("oauthScopes"))
        node_pool_object = {
            "name": node_pool.get("name"),
            "config": {
                "machineType": node_pool_config.get("machineType") or "f1-micro",
                "oauthScopes": oauth_scopes,
                "imageType": node_pool_config.get("imageType") or "COS",
                },
            "initialNodeCount": node_pool.get("initialNodeCount"),
            "locations": node_pool.get("locations")
        }
        final_node_pools_config.append(node_pool_object)
    return final_node_pools_config


def GenerateConfig(context):

    cluster_properties =  context.properties['cluster'] or context.env["name"]
    node_pools = generate_node_pools(cluster_properties)
    resources = [
        {
            "name": "k8s-cluster",
            "type": "container.v1.cluster",
            "properties": {
                "zone": context.properties["zone"],
                "cluster": {
                    "name": cluster_properties.get("name"),
                    "nodePools": node_pools
                }
            }
        }
    ]
    return {"resources": resources}
