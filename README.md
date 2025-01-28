# ![veld code](https://raw.githubusercontent.com/veldhub/.github/refs/heads/main/images/symbol_V_letter.png) veld_code__flair

\***work in progress!\***

This repo contains [code velds](https://zenodo.org/records/13322913) encapsulating 
[flair](https://github.com/flairnlp/flair) workflows.

## requirements

- git
- docker compose (note: older docker compose versions require running `docker-compose` instead of 
  `docker compose`)

## how to use

A code veld may be integrated into a chain veld, or used directly by adapting the configuration 
within its yaml file and using the template folders provided in this repo. Open the respective veld 
yaml file for more information.

Run a veld with:
```
docker compose -f <VELD_NAME>.yaml up
```

## contained code velds

**[./veld_jupyter_notebook.yaml](./veld_jupyter_notebook.yaml)** 

For interactive experiments.

```
docker compose -f veld_jupyter_notebook.yaml up
```

**[./veld_infer.yaml](./veld_infer.yaml)** 

To infer on data with given models

```
docker compose -f veld_infer.yaml up
```

