# Desafio Final Luiza Code - Equipe BestPy :heart::heart:

## Descrição do desafio

O Magazine está com um projeto de expansão, onde deseja conectar vendedores que infelizmente devido a pandemia não conseguem vender seus produtos da forma como antes 
e oferecer uma diversidade maior de produtos para nossos clientes.
Isso traria um impacto enorme para toda a cadeia: 

1. Os vendedores conseguiriam melhorar seu faturamento e ter a continuidade de seu negócio utilizando nossa plataforma para realizar a venda de seus produtos;
2. Os clientes ficariam felizes com a diversidade de produtos oferecidas;
3. O Magazine Luiza melhorará muito seu faturamento conectando vendedores e clientes dos mais diversos nichos.

Para isso, o time de negócios pensou em criar uma solução aberta para outros vendedores colocarem seus produtos a venda
em nossa plataforma.

Discutindo os requisitos para o MVP, o pessoal de produto considerou:

### Requisitos Obrigatórios:

* O desenvolvimento deve ser via API REST (sugestão de frameworks: Django, Flask, aiohttp);
* A representação dos dados (cadastrar/visualizar produto) o formato de dados é preferencialmente JSON
* Na solução, deve ser possível:
   * Cadastrar um produto;
   * Atualizar um produto;
   * Consultar um produto;
   * Inativar um produto (observação: não é necessário apagar produto e sim inativar);
   
* Um produto deve ter os seguintes campos:
   * Título;
   * Preço;
   * Código do produto;
   * Identificador do vendedor (seller);
   * Quantidade em estoque;
   
### Requisitos não obrigatórios:

 * Criação de testes unitários para a solução;
 * Implementação de Continuous Integration (Sugestão se for fazer, utilizem o github =) );
 * Versionamento do código (git);
 * Autenticação na API por seller (cada seller teria uma "chave" de acesso)
