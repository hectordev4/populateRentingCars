#!/bin/bash
TABLE_NAME="Delegations"

for car in $(jq -c '.[]' cars.json); do
    aws dynamodb put-item \
        --table-name $TABLE_NAME \
        --item "$(echo "$car" | jq '{
            "delegationId": {"S": .delegationId},
            "operation": {"S": .operation},
            "manufacturer": {"S": .manufacturer},
            "model": {"S": .model},
            "numberPlate": {"S": .numberPlate},
            "year": {"N": (.year|tostring)},
            "color": {"S": .color},
            "price": {"N": (.price|tostring)},
            "rentedDates": {"S": .rentedDates}
        }')"
done

echo "50 items inserted to $TABLE_NAME"
