#!/bin/bash

file_path="./speech.txt"
word_count=$(wc -w < "$file_path")

echo "The file '$file_path' contains $word_count words."