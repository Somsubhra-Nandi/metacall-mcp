from metacall import metacall_load_from_file, metacall

metacall_load_from_file("ts", ["../protocol/src/protocol_mcp.ts"])

# 1. Init: Use "http://localhost:8080" and ANY random string for token
metacall("init", "some_random_token", "http://localhost:8081")

# 2. Inspect: It should return [] (Empty list) because it's a fresh server
print("Inspecting Local Docker...")
print(metacall("inspect"))