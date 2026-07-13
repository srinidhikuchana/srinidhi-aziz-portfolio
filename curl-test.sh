#!/usr/bin/env bash

set -euo pipefail

BASE_URL="http://localhost:5000"
UNIQUE_ID="$(date +%s)-${RANDOM}"

NAME="Aziz-${UNIQUE_ID}"
EMAIL="aziz-${UNIQUE_ID}@example.com"
CONTENT="Random timeline test post ${UNIQUE_ID}"

echo "Creating a timeline post..."

curl --fail --silent --show-error \
  --request POST \
  "${BASE_URL}/api/timeline_post" \
  --data-urlencode "name=${NAME}" \
  --data-urlencode "email=${EMAIL}" \
  --data-urlencode "content=${CONTENT}"

echo
echo "Retrieving timeline posts..."

GET_RESPONSE="$(curl --fail --silent --show-error "${BASE_URL}/api/timeline_post")"

echo "${GET_RESPONSE}"
echo

if echo "${GET_RESPONSE}" | grep --fixed-strings --quiet "${CONTENT}"; then
  echo "PASS: The timeline post was created and retrieved successfully."
else
  echo "FAIL: The created timeline post was not found."
  exit 1
fi
