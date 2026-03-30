git log --all --name-only --pretty=format: \
| grep '^comp130-schedule-' \
| sort -u \
| while read file; do
    commit=$(git log --all --pretty=format:%H -- "$file" | tail -n 1)
    git show "$commit:$file" > "recovered_$file"
done
