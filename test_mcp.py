import requests
import json

# Base URL for the FastMCP server
base_url = "http://localhost:3000"

def test_list_resources():
    """Test listing available resources"""
    try:
        response = requests.get(f"{base_url}/resources/list")
        if response.status_code == 200:
            print("Successfully listed resources:")
            print(json.dumps(response.json(), indent=2))
        else:
            print(f"Error listing resources: {response.status_code}")
            print(response.text)
    except Exception as e:
        print(f"Error: {e}")

def test_read_resource(resource_uri):
    """Test reading a specific resource"""
    try:
        # URL encode the resource URI
        encoded_uri = requests.utils.quote(resource_uri)
        response = requests.get(f"{base_url}/resources/read?uri={encoded_uri}")
        if response.status_code == 200:
            print(f"Successfully read resource {resource_uri}:")
            print(json.dumps(response.json(), indent=2))
        else:
            print(f"Error reading resource: {response.status_code}")
            print(response.text)
    except Exception as e:
        print(f"Error: {e}")

def test_list_tools():
    """Test listing available tools"""
    try:
        response = requests.get(f"{base_url}/tools/list")
        if response.status_code == 200:
            print("Successfully listed tools:")
            print(json.dumps(response.json(), indent=2))
        else:
            print(f"Error listing tools: {response.status_code}")
            print(response.text)
    except Exception as e:
        print(f"Error: {e}")

def test_call_tool(tool_name, arguments):
    """Test calling a specific tool"""
    try:
        payload = {
            "name": tool_name,
            "arguments": arguments
        }
        response = requests.post(f"{base_url}/tools/call", json=payload)
        if response.status_code == 200:
            print(f"Successfully called tool {tool_name}:")
            print(json.dumps(response.json(), indent=2))
        else:
            print(f"Error calling tool: {response.status_code}")
            print(response.text)
    except Exception as e:
        print(f"Error: {e}")

if __name__ == "__main__":
    print("Testing FastMCP server...")

    # Test listing resources
    print("\n=== Testing List Resources ===")
    test_list_resources()

    # Test reading a specific resource
    print("\n=== Testing Read Resource ===")
    test_read_resource("database://public")

    # Test listing tools
    print("\n=== Testing List Tools ===")
    test_list_tools()

    # Test calling the query_database tool
    print("\n=== Testing Call Tool ===")
    test_call_tool("query_database", {"query": "SELECT * FROM products LIMIT 5"})
