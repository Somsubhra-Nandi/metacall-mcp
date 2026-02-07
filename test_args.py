from metacall import metacall_load_from_file, metacall

#Load the JS file that contains the function that needs to be tested
metacall_load_from_file("node", ["args_test.js"])

#Define Python data(Dict containing a List)
my_python_data = {
    "user": "Somsubhra",
    "role": "Contributor",
    "skills": ["Python", "MCP", "MetaCall"],
    "stats": { "commits": 100 }
}

print(f"Python sending: {my_python_data}")

#Send it to JS
#MetaCall converts Python Dict to JS Object
result = metacall("verify_data", my_python_data)

print(f"Python received back: {result}")