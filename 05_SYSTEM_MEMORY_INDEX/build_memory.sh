#!/bin/bash

INDEX_FILE="$HOME/Desktop/my-hub/05_SYSTEM_MEMORY_INDEX/master_file_index.csv"

echo "FILE_NAME|CATEGORY_TYPE|FULL_PATH" > "$INDEX_FILE"

echo "Indexing Music & Logic Pro Files..."
find $HOME -type f \( -name "*.logicx" -o -name "*.mp3" -o -name "*.wav" -o -name "*.flac" -o -name "*.aac" \) 2>/dev/null | while read -r file; do
    echo "$(basename "$file")|AUDIO_AND_LOGIC|$file" >> "$INDEX_FILE"
done

echo "Indexing Books, Journals & Academic PDFs..."
find $HOME -type f \( -name "*.pdf" -o -name "*.epub" -o -name "*.mobi" -o -name "*.docx" \) 2>/dev/null | while read -r file; do
    echo "$(basename "$file")|DOCUMENTS_AND_BOOKS|$file" >> "$INDEX_FILE"
done

echo "Indexing Research & Data Scripts..."
find $HOME -type f \( -name "*.sav" -o -name "*.R" -o -name "*.csv" -o -name "*.txt" \) 2>/dev/null | while read -r file; do
    echo "$(basename "$file")|RESEARCH_AND_DATA|$file" >> "$INDEX_FILE"
done

echo "=================================================="
echo "      MAC SYSTEM MEMORY INDEXING COMPLETE!        "
echo "  Total Items Indexed: $(wc -l < "$INDEX_FILE")   "
echo "=================================================="
