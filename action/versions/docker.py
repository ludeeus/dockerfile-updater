import requests


def get_docker_tags(image):
    print(f"[docker] {image}")
    skip = ["3.9", "3.9.6", "edge", "latest"]
    try:
        if image != "debian":
            url = (
                f"https://registry.hub.docker.com/v2/repositories/library/{image}/tags"
            )
            response = requests.get(url).json()
            return [x["name"] for x in response["results"] if x["name"][0].isdigit() and x["name"] not in skip]

        url = f"https://registry.hub.docker.com/v1/repositories/library/debian/tags"
        response = requests.get(url).json()
        tags = [x["name"] for x in response if x["name"][0].isdigit() and x["name"] not in skip]
        return tags
    except Exception as e:
        print(f"Could not get version for {image} - {e}")
        return []
