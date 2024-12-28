from db import sessions_collection
# Insert a test document
test_doc = {"test": "Hello, MongoDB!"}
result = sessions_collection.insert_one(test_doc)
print(f"Inserted document with ID: {result.inserted_id}")
