#!/bin/bash

TARGET_DIR="$HOME/Desktop/my-hub/01_ACADEMIC_AND_RESEARCH_CORE/Thesis_Greater_Palestine"
OUTPUT_FILE="$TARGET_DIR/Clean_Archive/master_clean_notes.txt"

echo "Processing and cleaning text files safely..."

# 1. Find text files, convert to plain ASCII (strip non-printable/code junk)
# 2. Filter out lines that look like code or formatting garbage
# 3. Sort and remove exact duplicate lines (deduplication)
find "$TARGET_DIR" -maxdepth 2 -type f \( -name "*.txt" -o -name "*.md" \) ! -name "master_clean_notes.txt" -exec cat {} + 2>/dev/null | \
tr -cd '\11\12\15\40-\176' | \
grep -vE '^[[:space:]]*$' | \
grep -vE '({|}|<|>|==|--|\/|\\|#|\$|var |function|import|class)' | \
sort -u > "$OUTPUT_FILE"

echo "=================================================="
echo "  CLEANUP COMPLETE!                              "
echo "  Merged & Deduplicated File Saved To:           "
echo "  $OUTPUT_FILE"
echo "=================================================="
