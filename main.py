import requests
import json
# URL (make sure to add a value for tree_root_ghca_id if needed)
world_tree_url = "https://api.dev3.partly.pro/api/v1/world-tree.search"
vrm_url = "https://api.dev3.partly.pro/api/v1/vrm.search"
vrm_params = {
    "identifier": 
    {
        "plate": "JAJ858",
        "region": "UREG32",
        "state": None
    }
}

vehicle_url = "https://api.dev3.partly.pro/api/v1/vehicles.search"
assembly_url = "https://api.dev3.partly.pro/api/v1/assemblies.v3.search"
# Your Bearer token here
bearer_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJFUzI1NiJ9.eyJpc3MiOiJodHRwczovL2FwaS5kZXYzLnBhcnRseS5wcm8vIiwic3ViIjoiMzhhMDY5OWYtY2E3Zi00ZDU4LTgzYWUtNDg0YmUzZmViNTM2IiwiaWF0IjoxNzUzNTYwNjI2LCJleHAiOjE3NTM2NjA4MDAsImp0aSI6ImFwaWtleTo1OGNjYzcxMy00MjgzLTQwMDEtYjAyNS0yMzYzMGFjYmJiNjAiLCJhdXRob3JpemF0aW9uX2RldGFpbHMiOlt7Imlzc3VlciI6Ii9hcGkvdjEvcmVwYWlyZXJzLnZlcmlmeSIsInBhcmFtZXRlcnMiOnsicmVwYWlyZXJfaWQiOiI5NmEwOGQ2OC05ZjM0LTQ2YmYtYjEwNS1iYzg0M2VkNmJhZjgifSwiZGV0YWlscyI6eyJvcmdhbml6YXRpb25faWQiOiJjOGIzOWUwNS05ODA1LTQ0NTEtOWI1Zi0yOTFmZGZiOTI4NmEiLCJyZXBhaXJlcl9pZCI6Ijk2YTA4ZDY4LTlmMzQtNDZiZi1iMTA1LWJjODQzZWQ2YmFmOCIsInNpdGVfaWRzIjpbXX19LHsiaXNzdWVyIjoiL2FwaS92MS9vcmdhbml6YXRpb25zLnZlcmlmeSIsInBhcmFtZXRlcnMiOnsib3JnYW5pemF0aW9uX2lkIjoiYzhiMzllMDUtOTgwNS00NDUxLTliNWYtMjkxZmRmYjkyODZhIn0sImRldGFpbHMiOnsiaWQiOiJjOGIzOWUwNS05ODA1LTQ0NTEtOWI1Zi0yOTFmZGZiOTI4NmEiLCJwZXJtaXNzaW9ucyI6W3sic2NvcGUiOiJvcmdhbml6YXRpb25fYWRtaW5zIiwiZW50aXR5IjoiYzhiMzllMDUtOTgwNS00NDUxLTliNWYtMjkxZmRmYjkyODZhIn0seyJzY29wZSI6ImJ1c2luZXNzX2FkbWlucyJ9XX19XX0.0v1pBLE1OwN1--8onkvirT_zA1_I15LwChF_Kmq5Qp5xuZATekC31sxbVOHwfQvAbstj-a85j-qUK7N0TOdtww"

# Headers with Authorization
headers = {
    "Authorization": f"Bearer {bearer_token}"
}

vrm_response = requests.post(vrm_url, headers=headers, json={
    "plate": "JAJ858", "region": "UREG32", "state": None})
print("Status Code:", vrm_response.status_code)
print(vrm_response.json())
vrm_chassis = vrm_response.json()["chassis"]
print(vrm_chassis)
vehicle_params = {
    "identifier": {
        "chassis_number": vrm_chassis # Your VIN 
    },
}

# Make the vehicle.search GET request
vehicle_response = requests.post(vehicle_url, headers=headers, json=vehicle_params)



# Print the response (JSON, status code, etc.)
print("Status Code:", vehicle_response.status_code)

id = vehicle_response.json()["variants"][0]["id"]
assembly_response = requests.post(assembly_url, headers=headers, json={"oem_vehicle_id": id})
print("Status Code:", assembly_response.status_code)
print(assembly_response.json()['gapc_human_centric_assemblies']['GHCA9452']['gapc_position_id'])

def find_part_children(part_id):
    world_tree = requests.post(world_tree_url, headers=headers, json={'tree_root_ghca_id': part_id})
    if world_tree.status_code == 200:
        return list(world_tree.json()['nodes'].keys())[1:]
    return []

print(find_part_children('GHCA6437'))

def populate_children(part_ids):
    queue = part_ids
    all_children = list(part_ids)
    i = 0
    while queue:
        i += 1
        print(i)
        parent = queue.pop()
        print(parent)
        children = find_part_children(parent)
        all_children.extend(children)
        queue.extend(children)
        if i > 1000:
            break
    return all_children

print(populate_children())
