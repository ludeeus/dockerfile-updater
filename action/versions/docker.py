import requests

def get_docker_tags(image):
    print(f"[docker] {image}")
    try:
        if image != "debian":
            url = f"https://registry.hub.docker.com/v2/repositories/library/{image}/tags"
            response = requests.get(url).json()
            return response["results"]

        url = f"https://registry.hub.docker.com/v1/repositories/library/debian/tags"
        response = requests.get(url).json()
        tags = [x["name"] for x in response if x["name"][0].isdigit()]
        return tags
    except Exception as e:
        print(f"Could not get version for {image} - {e}")
        return []