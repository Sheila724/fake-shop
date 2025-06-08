# Use uma imagem base Python
FROM python:3.11.0

# Define o diretório de trabalho dentro do contêiner para /app
WORKDIR /app

# Copia o arquivo requirements.txt da pasta 'src' do host
# para o diretório de trabalho atual do contêiner (/app)
COPY src/requirements.txt .

# Instala as dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do seu código fonte da pasta 'src' do host
# para o diretório de trabalho atual do contêiner (/app)
COPY src .

# Expõe a porta que sua aplicação usa
EXPOSE 8213

# Comando para tornar o entrypoint.sh executável e usá-lo como ENTRYPOINT
# CORREÇÃO AQUI: Copia o entrypoint.sh da RAIZ do contexto (fake-shop/)
COPY entrypoint.sh /app/entrypoint.sh

RUN chmod +x /app/entrypoint.sh
ENTRYPOINT ["/app/entrypoint.sh"]
