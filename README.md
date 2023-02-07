# kubernetes-manifest-generator
This tool generate customized manifests for kubernetes based on models at manifests folder, built for pipeline integration.

Run the generate.py as follows:

`python3 generate.py APPNAME DOMAIN CONTAINER_IMAGE NAMESPACE REGISTRY > customized-manifest.yml`

| ARG NAME | ARG DESCRIPTION |
| - | - |
| APPNAME | Prefix to your service, ex: APPNAME.example.com |
| DOMAIN | Suffix to your service, ex: appname.DOMAIN |
| CONTAINER_IMAGE | Image name of the container |
| NAMESPACE | The kubernetes namespace |
| REGISTRY | Container Registry of the image |

# Conventions do Adopt
Production namespace name "main", staging/homolog "hml", others will be considered as dev!

You may use a manifest for a spacific application or a template manifest for the entire namespace you chose.

At /manifests folder you can use yaml files as models, the priority is to use a manifest for an application if it exists, otherwise will get a manifest based on the NAMESPACE.
