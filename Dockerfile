# 1) Pick up the Azure Functions Python 3.12 App Service image
FROM mcr.microsoft.com/azure-functions/python:4-python3.12-appservice

# Place the API key in key vault later
ENV AzureWebJobsScriptRoot=/home/site/wwwroot \
    FUNCTIONS_WORKER_RUNTIME=python \
    GOOGLE_API_KEY="AIzaSyCrQcAiL9IJA5GQQ4R6WEzcUr6G77E_h7Y" \
    ROOT=/home/site/wwwroot \
    ROOT_RESULT=/home/site/wwwroot/GeneratedOnBoardings \
    CACHING_DOCUMENTATION=False \
    CACHING_REPO=False \
    CONNECTION_STRING="InstrumentationKey=be00f19d-32bf-4a4b-9d93-36137673825a;IngestionEndpoint=https://westeurope-5.in.applicationinsights.azure.com/;LiveEndpoint=https://westeurope.livediagnostics.monitor.azure.com/;ApplicationId=b658e80f-985c-4648-b56b-8c9c2974602f"

WORKDIR /home/site/wwwroot
COPY . .

USER root
RUN apt-get update \
 && apt-get install -y --no-install-recommends \
      git curl ca-certificates \
 && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir -r requirements.txt


EXPOSE 80

