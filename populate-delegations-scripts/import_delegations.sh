#!/bin/bash
TABLE_NAME="Delegations"

jq -c '.[]' delegations.json | while read -r delegation; do
    aws dynamodb put-item \
        --table-name "$TABLE_NAME" \
        --item "$(echo "$delegation" | jq '{
            "delegationId": {"S": .delegationId},
            "operation": {"S": .operation},
            "name": {"S": .name},
            "address": {"S": .address},
            "city": {"S": .city},
            "carQuantity": {"N": (.carQuantity|tostring)},
            "managerName": {"S": .managerName},
            "contactInfo": {"M": {
                "phone": {"S": .contactInfo.phone},
                "email": {"S": .contactInfo.email}
            }}
        }')"
done

echo "5 items inserted to $TABLE_NAME"

