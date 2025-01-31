#!/bin/bash

if [[ "$run_interactively" == "true" ]]; then
  jupyter notebook --allow-root --ip='*' --NotebookApp.token='' --NotebookApp.password=''
elif [[ "$run_interactively" == "false" ]]; then
  if [[ "$1" == "infer" ]]; then
    jupyter nbconvert --to script /veld/code/notebooks/infer.ipynb
    python /veld/code/notebooks/infer.py
    rm /veld/code/notebooks/infer.py
  elif [[ "$1" == "train" ]]; then
    jupyter nbconvert --to script /veld/code/notebooks/train.ipynb
    python /veld/code/notebooks/train.py
    rm /veld/code/notebooks/train.py
  else
    echo "wrong or missing argument. Must be either 'infer' or 'train'"
  fi
else
  echo "wrong or missing argument. Var 'run_interactively' must be either 'true' or 'false'"
fi

