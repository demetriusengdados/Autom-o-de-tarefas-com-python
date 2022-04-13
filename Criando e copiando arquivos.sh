#Vanos criar um diretorio chamado workspace

mkdir workspace
cd workspace

#Criando uma mensagem dentro do diretorio workspace
echo "Bem-vindo" > mensagem.txt

#Vamos copiar o texto do arquivo que acabamos de criar para um outro de nome "bemvindo.txt" com o comando cp:
cp mensagem.txt bemvindo.txt

#o texto agora está nos 2 arquivos
cat bemvindo.txt
#A saida sera a o texto: bemvindo
cat mensagem.txt
#A saida será a mensagem: bemvindo

#Podemos também mover o arquivo "mensagem.txt" para outro com o comando mv:
mv mensagem.txt bemvindo2.txt

ls
#A saida do código será:
#bemvindo2.txt benvindo.txt

#Perceba que o arquivo mudou de nome.

#Criemos agora mais dois diretórios:

mkdir projetos-java
mkdir projetos-php

#Queremos mover o arquivo "bemvindo.txt" para dentro do diretório "projetos-java":

mv bemvindo.txt projetos-java

#Se quiséssemos além de movê-lo, mudar seu nome, faríamos, por exemplo:

mv bemvindo.txt projetos-java/bemvindo-novo-nome.txt

#Vamos verificar se ele foi realmente movido para o diretório que queríamos:

ls workspace/
#A saida será a seguinte:
#bemvindo2.txt   projetos-java   projetos-php

ls projetos-java/
#bemvindo.txt

#De fato, o arquivo "bemvindo.txt" saiu do workspace e foi para o projetos-java. Vamos copiar "bemvindo2.txt" com o nome "bemvindo.txt" para manter este nos dois diretórios:

cp bemvindo2.txt bemvindo.txt

ls workspace/
#saida do código: bemvindo2.txt   bemvindo.txt   projetos-java   projetos-php

#Se quisermos buscar os dois arquivos "bemvindos" dentro do diretório workspace, fazemos:
ls bemvindo*
#Saida do código: bemvindo2.txt   bemvindo.txt

#erceba que quando usamos o comando ls para arquivos, o terminal retorna tais arquivos. 
#Se fizermos o mesmo para diretórios, ele retorna o que estiver dentro deles. E, ainda, se fizermos ls *, o terminal retorna:

bemvindo2.txt   bemvindo.txt

projetos-java:
bemvindo.txt

projetos-php:

#Ou seja, mostra tanto os diretórios dentro daquele em que estamos trabalhando e seus respectivos arquivos.
#Assim como utilizamos o -r para conseguirmos apagar diretórios, do mesmo jeito fazemos para copiá-los, como por exemplo:

cp -r projetos-java projetos-c#