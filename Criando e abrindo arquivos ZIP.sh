#Agora que já sabemos como trabalhar com arquivos e diretórios, copiá-los, movê-los, etc, 
#vamos ver como compactá-los. Queremos, por exemplo, compactar o workspace, cujo conteúdo podemos conferir utilizando o comando ls:

ls bemvindo2.txt  bemvindo.txt  projetos-c#  projetos-java  projetos-php

#Primeiramente precisamos estar no diretório ao qual ele pertence com o comando cd .. 
#para subir um diretório acima e depois usamos o comando zip informando o nome do arquivo que será gerado e o que o comando deve compactar:

cd..
zip work.zip workspace/

#A mensagem adding: workspace/ (stored 0%) será exibida. 
#Lembre-se que work.zip é o nome que demos para o arquivo de compactação. 
#Podemos verificar rapidamente o conteúdo do arquivo compactado utilizando o comando unzip -l work.zip (o comando após unzip é a letra L minúscula, e não o número 1) 
#dessa forma conseguimos observar quais arquivos e diretórios foram compactados.
#É importante observar que, da mesma forma que os comandos para apagar e copiar, o comando zip não é suficiente para compactar
#todos os arquivos e diretórios dentro de workspace. Se você conferiu o onteúdo do zip, percebeu que apenas o diretório workspace foi
#compactado, mas nenhum dos seus arquivos e subdiretórios estava presente no zip final. Para isso precisamos usar a ferramenta de
#recursividade aqui também, ou seja, o -r em conjunto com o comando zip:

zip -r work.zip workspace/

#Esse comando apresentará uma saída diferente, informando os arquivos encontrados e adicionados ao zip final. A saida do código deverá ser algo tipo abaixo:

#updating: workspace/ (stored 0%)
  #adding: workspace/bemvindo2.txt (stored 0%)
  #adding: workspace/projetos-php/ (stored 0%)
  #adding: workspace/projetos-java/ (stored 0%)
  #adding: workspace/projetos-java/bemvindo.txt (stored 0%)
  #adding: workspace/bemvindo.txt (stored 0%)
  #adding: workspace/projetos-c#/ (stored 0%)
  #adding: workspace/projetos-c#/bemvindo.txt (stored 0%)

#Para descompactar o arquivo zip utilizamos o comando unzip, informando o nome do arquivo work.zip.

Archive: work.zip
creating: workspace/
extracting: workspace/bemvindo2.txt
creating: workspace/projetos-php/
creating: workspace/projetos-java/
extracting: workspace/projetos-java/bemvindo.txt
extracting: workspace/bemvindo.txt
creating: workspace/projetos-c#/
extracting: workspace/projetos-c#/bemvindo.txt

#Descompactar os arquivos do zip no mesmo diretório irá sobrescrever os arquivos já existentes. Experimente remover o
#diretório workspace com o comando rm antes de descompactar o arquivo work.zip. Utilize também o comando ls para verificar o
#resultado de cada comando.

#Perceba que tanto o zip quanto o unzip são comandos muito verborrágicos, ou seja, imprimem muita informação. O modificador 
#-q permite que o retorno seja vazio (apesar de o resto funcionar perfeitamente):

unzip -q work.zip

#e para zip: 
zip -rq work.zip workspace

#Podemos deixar juntos o -q e o comando de recursividade -r formando o -rq.
