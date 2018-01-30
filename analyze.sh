#!/bin/bash

inputFile=$1
outputFile=$2

# Error checking
if [ "$#" -ne 2 ]; then
    echo "Incorrect number of arguments. You must specify exactly 2 arguments"
    exit 1
fi
if [ ! -f "$inputFile" ]; then
    echo "$inputFile is not found"
    exit 1
fi
if [ ! -f "$outputFile" ]; then
    echo "$outputFile is not found"
    exit 1
fi
if [ ! -r "$inputFile" ]; then
    echo "$inputFile cannot be read"
    exit 1
fi
if [ ! -w "$outputFile" ]; then
    echo "$outputFile cannot be written"
    exit 1
fi
# Create a temporary modified json that can be read using json.load in the 
# python script
touch "formatted-$inputFile.json"
echo "[" >> "formatted-$inputFile.json"
cat "$inputFile" >> "formatted-$inputFile.json"
echo "]" >> "formatted-$inputFile.json"

python classDataParser.py "formatted-$inputFile.json" "$outputFile"

rm "formatted-$inputFile.json"
