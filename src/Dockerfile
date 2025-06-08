# Use uma imagem base Python
FROM python:3.11.0

# Define o diretório de trabalho dentro do contêiner para /app
WORKDIR /app

# Copia o arquivo requirements.txt da RAIZ do host
COPY requirements.txt .

# Instala as dependências Python
RUN pip install --no-cache-dir -r requirements.txt

# Copia o restante do seu código fonte da RAIZ do host
COPY . . 

# ---- LINHA DE DEBUG TEMPORÁRIA ----
RUN ls -la / # Lista o conteúdo da raiz do contêiner
RUN ls -la /app # Lista o conteúdo de /app (onde o código é copiado)
RUN ls -la /app/entrypoint.sh # Tenta listar o arquivo específico
# ----------------------------------

# Expõe a porta que sua aplicação usa
EXPOSE 8217

# Comando para tornar o entrypoint.sh executável e usá-lo como ENTRYPOINT
RUN chmod +x /app/entrypoint.sh

ENTRYPOINT ["/app/entrypoint.sh"]
