#!/bin/bash

BASE_URL="http://localhost:5000/api/timeline_post"
RANDOM_ID=$RANDOM

NAME="TestUser_$RANDOM_ID"
EMAIL="testuser_${RANDOM_ID}@example.com"
CONTENT="This is a random test post #$RANDOM_ID"

echo "===================================="
echo "1. Sending POST request to create timeline post"
echo "===================================="

POST_RESPONSE=$(curl -s -X POST "$BASE_URL" \
  -H "Content-Type: application/json" \
  -d "{\"name\": \"$NAME\", \"email\": \"$EMAIL\", \"content\": \"$CONTENT\"}")

echo "Response: $POST_RESPONSE"

# Extract the id of the newly created post (requires jq)
POST_ID=$(echo "$POST_RESPONSE" | jq -r '.id')

if [ "$POST_ID" == "null" ] || [ -z "$POST_ID" ]; then
  echo "Failed to create post or extract ID. Exiting."
  exit 1
fi

echo "Created post with ID: $POST_ID"
echo ""

echo "===================================="
echo "2. Sending GET request to verify post was added"
echo "===================================="

GET_RESPONSE=$(curl -s -X GET "$BASE_URL")
echo "Response: $GET_RESPONSE"

# Check if our content shows up in the GET response
if echo "$GET_RESPONSE" | grep -q "$CONTENT"; then
  echo "SUCCESS: Test post found in GET response."
else
  echo "FAILURE: Test post NOT found in GET response."
  exit 1
fi

echo ""
echo "===================================="
echo "3. (Bonus) Deleting the test post"
echo "===================================="

DELETE_RESPONSE=$(curl -s -X DELETE "$BASE_URL/$POST_ID")
echo "Response: $DELETE_RESPONSE"

echo ""
echo "===================================="
echo "4. Confirming deletion via GET"
echo "===================================="

FINAL_GET=$(curl -s -X GET "$BASE_URL")

if echo "$FINAL_GET" | grep -q "$CONTENT"; then
  echo "FAILURE: Test post still exists after deletion."
  exit 1
else
  echo "SUCCESS: Test post successfully deleted."
fi

echo ""
echo "===================================="
echo "All tests passed!"
echo "===================================="
