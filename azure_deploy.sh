#!/usr/bin/env bash
set -e

RG="codeboarding"
LOC="switzerlandnorth"

# delete existing resource group if it exists
ez_group=$(az group exists --name "$RG")
if [ "$ez_group" = "true" ]; then
  echo "Deleting existing resource group: $RG"
  az group delete \
    --name "$RG" \
    --yes \
    --no-wait
  echo "Waiting for deletion to complete..."
  az group wait --name "$RG" --deleted
fi

# create resource group
echo "Creating resource group $RG in $LOC"
az group create \
  --name "$RG" \
  --location "$LOC"

# storage account (no suffix, must be unique manually)
STORAGE_ACCOUNT_NAME="codeboarding"
echo "Creating storage account: $STORAGE_ACCOUNT_NAME"
az storage account create \
  --name "$STORAGE_ACCOUNT_NAME" \
  --resource-group "$RG" \
  --location "$LOC" \
  --sku Standard_LRS

# function app
FUNCTIONAPP_NAME="codeboarding-demo"
echo "Creating Function App: $FUNCTIONAPP_NAME"
az functionapp create \
  --resource-group "$RG" \
  --consumption-plan-location "$LOC" \
  --os-type Linux \
  --runtime python \
  --functions-version 4 \
  --name "$FUNCTIONAPP_NAME" \
  --storage-account "$STORAGE_ACCOUNT_NAME"

echo "Function App $FUNCTIONAPP_NAME created successfully."
