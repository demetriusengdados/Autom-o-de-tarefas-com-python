#Aprendemos a compactar arquivos e diretórios utilizando a extensão zip, com o comando zip, que é uma extensão muito famosa no
#sistema operacional Windows. No Linux, uma outra extensão é mais convencional de se utilizar, a extensão tar. Vamos, então, fazer o
#mesmo trabalho da aula passada mas utilizando o comando tar. Para compactar o diretório workspace fazemos:

tar -cz workspace > work.tar.gz

#O tar sozinho não serve para compactar arquivos. Na verdade o tar serve para empacotar vários diretórios e arquivos em um único
#arquivo, facilitando a transferência. Para compactar usaremos o tar combinado com o zip, o primeiro empacota e o segundo compacta.
#O modificador -cz indica que o arquivo tar será criado (-c) e será compactado pelo zip(-z) usando o redirecionamento >. Uma
#observação interessante é que comando tar já é automaticamente recursivo.
#Lembre-se de utilizar o comando ls para verificar o arquivo criado e de remover o diretório workspace antes de descompactar os arquivos com o comando rm.
#Para descompactar o arquivo .tar.gz que criamos, fazemos:

tar -xz < work.tar.gz

#Perceba que houveram apenas duas diferenças em relação ao comando de compactação, a presença -x de "extract", para extrair os
#arquivos e a direção do redirecionamento < que agora em vez de indicar saída de dados, indica entrada de dados.

#Mas não é muito bom ficarmos o tempo todo trabalhando com redirecionamento, é meio chato. Para isso o comando tar possui o
#modificador -f para podermos passar o nome do arquivo que queremos criar:

tar -czf work.tar.gz workspace/


#Note que inversão no nome do arquivo e diretório a ser compactado, com redirecionamento, o nome do arquivo final vem depois, agora ele
#está vindo antes. Agora para descompactar fazemos:

tar -xzf work.tar.gz

#Uma outra característica que faz o comando tar diferente do zip é que ele não é verborrágico por padrão. Consequentemente não
#precisamos dar comandos para que as informações de compactação não apareçam. Pelo contrário, para que as informações apareçam,
#usamos o modificador -v (de "verbose"):

tar -vxzf work.tar.gz

#A saída será semelhante a mostrada abaixo:
#workspace/
#workspace/bemvindo2.txt
#workspace/projetos-php/
#workspace/projetos-java/
#workspace/projetos-java/bemvindo.txt
#workspace/bemvindo.txt
#workspace/projetos-c#/
#workspace/projetos-c#/bemvindo.txt

#Existem muitos modificadores para compactar e descompactar diretórios, tanto em zip quanto em tar. Por isso podemos recorrer
#sempre que necessário à documentação usando o comando man. Como por exemplo: man tar para sabermos sobre outras opções de
#modificadores disponíveis para o comando tar.
