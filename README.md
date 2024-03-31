# End-to-End-ML-Approach-to-Wine-Quality-Prediction-with-MLflow

## Workflows 

1. Update config.yaml
2. Update schema.yaml
3. Update params.yaml
4. Update the entity
5. Update the configuration manager in src config
6. Update the components
7. Update the pipeline
8. Update the main.py
9. Update the app.py  


# How to run?

### STEPS: 

Clone the repository 

```bash
https://github.com/Pritamn11/End-to-End-ML-Approach-to-Wine-Quality-Prediction-with-MLflow
```

#### STEPS 01 - Create a virtual environment after opening the repository

```bash
python -m venv newenv
```

```bash
.\newenv\Scripts\activate
```
 
#### STEPS 02 - Install the requirements

```bash
pip install -r requirements.txt
```

```bash
# Finally run the command
python app.py
```

Now,

```bash
open up you local host and port
```

## MLflow


[Documentation](https://mlflow.org/docs/latest/index.html)


##### cmd 
- mlflow ui

## dagshub 
[dagshub](https://dagshub.com/)

MLFLOW_TRACKING_URI=https://dagshub.com/pritamnarwade11/End-to-End-ML-Approach-to-Wine-Quality-Prediction-with-MLflow.mlflow \
MLFLOW_TRACKING_USERNAME=pritamnarwade11 \
MLFLOW_TRACKING_PASSWORD=871b76c6a3213893886036cf5681b2454522ec97 \
python script.py

Run this to export as env variables:

```bash

export MLFLOW_TRACKING_URI=https://dagshub.com/pritamnarwade11/End-to-End-ML-Approach-to-Wine-Quality-Prediction-with-MLflow.mlflow 

export MLFLOW_TRACKING_USERNAME=pritamnarwade11 

export MLFLOW_TRACKING_PASSWORD=871b76c6a3213893886036cf5681b2454522ec97 

```

# AWS-CICD-Deployment-with-Github-Actions

## 1. Login to AWS console.

## 2. Create IAM user for deployment 
  #with specific access 
  1. EC2 access : It is virtual machine. 

  2. ECR : Elastic Container registry to save your docker image in aws.

  #Description: About the deployment 

  1. Build docker image of the source code 

  2. Push your docker image to the ECR 

  3. Launch your EC2 

  4. Pull your image from ECR in EC2 

  5. Launch your docker image in EC2 

  #Policy 

  1. AmazonEC2ContainerRegistryFullAccess

  2. AmazonEC2FullAccess

## 3. Create ECR repo to store/save docker image
   - Save the URI: 180270381290.dkr.ecr.us-west-2.amazonaws.com/wineproj

## 4. Create EC2 machine (Ubuntu)

## 5. Open EC2 and Install docker in EC2 Machine:
    
    #optinal

    sudo apt-get update -y

    sudo apt-get upgrade

    #required

    curl -fsSL https://get.docker.com -o get-docker.sh

    sudo sh get-docker.sh

    sudo usermod -aG docker ubuntu

    newgrp docker

## 6. Configure EC2 as self-hosted runner:

   setting>actions>runner>new self hosted runner> choose os> then run command one by one

## 7. Setup github secrets: 

    AWS_ACCESS_KEY_ID=

    AWS_SECRET_ACCESS_KEY=

    AWS_REGION = us-east-1

    AWS_ECR_LOGIN_URI = demo>>   180270381290.dkr.ecr.us-west-2.amazonaws.com

    ECR_REPOSITORY_NAME = wineproj   

### About MLflow 

  MLflow

   * Its Production Grade
   * Trace all of your expriements
   * Logging & tagging your model    
