#### Instructions for basic setup

## create new env 
conda create -n demo_for_chatbot_ds python=3.8.0

## activate env
activate demo_for_chatbot_ds

## install requirements.txt
pip install -r requirements.txt

## check installed version of rasa
pip freeze | grep rasa

## Install spacy 
pip install rasa[spacy]== {version of rasa installed} 

## download the pre-trained models
python -m spacy download en_core_web_md

## create shortcut or Symbolic Link Creation
python -m spacy link en_core_web_md en    


## Train the RASA NLU (this creates NLU model in the models folder)
rasa train nlu
rasa shell nlu

## Train the RASA Core (this creates training model in the models folder)
rasa train
rasa shell

## Actions Defined for bots (Has to be started before running rasa shell/ rasa interactive)
rasa run actions

## Create New Interactive Stories (Creates a new trained model after the export)
rasa interactive
