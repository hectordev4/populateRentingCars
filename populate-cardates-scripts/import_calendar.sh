#!/bin/bash
TABLE_NAME="Calendar"

for calendar in $(jq -c '.[]' calendar.json); do
    aws dynamodb put-item \
        --table-name $TABLE_NAME \
        --item "$(echo "$calendar" | jq '{
            "operation": {"S": .operation},
            (to_entries | map({(.key): {"BOOL": .value}}) | add)
        }')"
done

echo "Calendar data inserted into $TABLE_NAME"