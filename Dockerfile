FROM svercoutere/mu-python-ml:0.1.0
LABEL maintainer="user_name@mail_provider.com"

ENV THEME_CLASSIFIER_URI="http://theme-classifier/predict"
ENV TYPE_CLASSIFIER_URI="http://type-classifier/predict"
ENV OLLAMA_URI="ollama:11434"