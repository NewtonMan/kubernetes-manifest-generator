#!/usr/bin/env python3
import sys
from os.path import exists
import requests

APPNAME = sys.argv[1]
CONTAINER_IMAGE = sys.argv[2]
NAMESPACE = sys.argv[3]
if NAMESPACE != "main":
    APPNAME = "-".join([APPNAME, NAMESPACE])

APPURL="{}.obvious.net.br".format(APPNAME)

CUSTOM_MANIFEST="./manifests/{}.yml".format(APPNAME)
if exists(CUSTOM_MANIFEST):
    MANIFEST=CUSTOM_MANIFEST
if NAMESPACE != "main" and NAMESPACE != "hml":
    MANIFEST='./k8s/deployments/dev.yml'
else:
    MANIFEST="./k8s/deployments/{}.yml".format(NAMESPACE)

try:
    REGISTRY = sys.argv[4]
except:
    REGISTRY = "obvious"
with open(MANIFEST, 'r') as file:
    DEPLOYMENT = file.read()

DEPLOYMENT = DEPLOYMENT.replace('__APPNAME', APPNAME)
DEPLOYMENT = DEPLOYMENT.replace('__NAMESPACE', NAMESPACE)
DEPLOYMENT = DEPLOYMENT.replace('__APPURL', APPURL)
DEPLOYMENT = DEPLOYMENT.replace('__CONTAINER_IMAGE', CONTAINER_IMAGE)
DEPLOYMENT = DEPLOYMENT.replace('__REGISTRY', REGISTRY)

print(DEPLOYMENT)

# INTEGRANDO PORTAL devops-status.obvious.com.br
DEVOPS_WORKER_URL = "devops-status.obvious.net.br"
DEVOPS_WORKER_TOKEN = "teste"
try:
    response = requests.post("https://{}/newEvent.php?token={}&appslug={}".format(DEVOPS_WORKER_URL, DEVOPS_WORKER_TOKEN, APPNAME), data = {'message':"BUILD do Projeto na URL: https://{}".format(APPURL)})
except:
    print("# Erro ao enviar notificação para {}".format(DEVOPS_WORKER_URL))
    pass
