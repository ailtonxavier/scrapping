# baixa a imagem do python, versão 3.12 com debian slim (tamanho reduzido)
FROM python:3.12-slim
# seta a variável do python para dar outputs no container
ENV PYTHONUNBUFFERED 1
# define a pasta do projeto
WORKDIR /app
# copia a pasta do seu projeto local para a pasta definida no WORKDIR
COPY . .
# executa as dependências
RUN set -x && \
    pip install --upgrade pip && \
    pip install -r requirements.txt && \
    rm -r requirements.txt
# executa o app com o python
CMD ["python", "app.py"]