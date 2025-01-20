import requests
import base64

# Download the image
# # image_url = "https://example.com/image.jpg"
# image_url = "https://s3-us-west-1.amazonaws.com/exr-dev-static/upload/masonry/mobile/1.jpg"
# image_response = requests.get(image_url)
# image_data = image_response.content

# # Encode the image to base64
# encoded_image = base64.b64encode(image_data).decode('utf-8')

# # Prepare the request payload
# payload = {
#     "model": "llava",
#     "prompt": "Describe the content of the image in detail.",
#     "images": [encoded_image],
#     "stream": False
# }

# # Send the request to the Ollama server
# response = requests.post("http://localhost:11434/api/generate", json=payload)
# result = response.json()

# # Print the response
# print(result["response"])

import base64
import requests
import json

# Step 1: Download the image from the URL
image_url = "https://s3-us-west-1.amazonaws.com/exr-dev-static/upload/masonry/mobile/1.jpg"
response = requests.get(image_url)
image_data = response.content

# Step 2: Encode the image to base64
encoded_image = base64.b64encode(image_data).decode('utf-8')

# Step 3: Prepare the payload
payload = {
    "model": "llava",
    "prompt": "analyze and provide an detailed information on what's on this picture??",
    "images": [encoded_image]
}

url = "http://localhost:11434/api/generate"
# Step 4: Send the request to the Ollama server
# response = requests.post(url, json=payload)
# print(response.text)

# Send the POST request
response = requests.post(url, json=payload)#, headers=headers, stream=True)

# Initialize a variable to store the complete response
full_response = ""

# Process the streaming response
for line in response.iter_lines():
    if line:
        try:
            # Decode the JSON line
            data = json.loads(line.decode('utf-8'))
            # Concatenate the 'response' field to build the full response
            full_response += data.get("response", "")
        except json.JSONDecodeError:
            print("Invalid JSON:", line.decode('utf-8'))

# Print the complete response
print("Full Response:")
print(full_response)

# raw_response = response.text
# json_objects = raw_response.splitlines()  # Split response into lines
# for obj in json_objects:
#     try:
#         data = json.loads(obj)
#         print(data)
#     except json.JSONDecodeError:
#         print("Invalid JSON:", obj)
# print(response.json())