#!/bin/bash
TABLE_NAME="Delegations"

for calendar in $(jq -c '.[]' calendar.json); do
    aws dynamodb put-item \
        --table-name $TABLE_NAME \
        --item "$(echo "$calendar" | jq '{
            "delegationId": {"S": .delegationId},
            "operation": {"S": .operation},
            "dates": {"M": (.dates | to_entries | map({(.key): {"BOOL": .value}}) | add)}
        }')"
done

echo "Calendar data inserted into $TABLE_NAME"