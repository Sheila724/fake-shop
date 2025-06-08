# Use uma imagem base Python
FROM python:3.11.0

# Define o diretório de trabalho dentro do contêiner para /app
# Tudo que for copiado ou executado a partir daqui será relativo a /app
WORKDIR /app

# Copia o arquivo requirements.txt da pasta 'src' do host
# para o diretório de trabalho atual do contêiner (/app)
# Caminho no host (relativo ao contexto '.'): src/requirements.txt
# Caminho no contêiner: /app/requirements.txt
COPY src/requirements.txt . 

# Instala as dependências Python listadas no requirements.txt
# Como WORKDIR é /app, ele vai procurar por /app/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt 

# Copia o restante do seu código fonte da pasta 'src' do host
# para o diretório de trabalho atual do contêiner (/app)
# Caminho no host (relativo ao contexto '.'): src/
# Caminho no contêiner: /app/
COPY src . # <<<<<<<<<< CORREÇÃO AQUI!

# Expõe a porta que sua aplicação usa
EXPOSE 8213

# Comando para tornar o entrypoint.sh executável e usá-lo como ENTRYPOINT
# Assumindo que entrypoint.sh está dentro de sua pasta 'src'
COPY src/entrypoint.sh /app/entrypoint.sh # <<<<<<<<<< Adiciona esta linha se o entrypoint.sh estiver em src
RUN chmod +x /app/entrypoint.sh # <<<<<<<<<< Adiciona esta linha para tornar executável
ENTRYPOINT ["/app/entrypoint.sh"] # <<<<<<<<<< Define o entrypoint do contêiner

# CMD padrão (será substituído pelo ENTRYPOINT se ambos estiverem presentes)
# CMD ["flask", "run", "--host=0.0.0.0", "--port=8213"] # Removido ou ajustado conforme sua necessidade
