## Descrição do Projeto

Este projeto consiste num programa de gestão de imóveis para arrendamento, desenvolvido em Python. O programa permite a gestão de clientes e imóveis, incluindo operações como adicionar, editar e visualizar imóveis disponíveis para arrendamento. O programa interage com uma base de dados SQLite para armazenar e recuperar informações.

## Estrutura do Projeto

O projeto é composto por três ficheiros principais:

1. **app.py**: O programa principal que contém a lógica de gestão de imóveis e clientes. Inclui funcionalidades como:
   - Adicionar clientes e imóveis.
   - Editar informações de clientes e imóveis.
   - Visualizar imóveis com filtros por tipo, área e cidade.
   - Validação de entradas do utilizador.
   - Registro de erros em `log.txt`.

2. **log.txt**: Ficheiro de registo de erros. Sempre que o utilizador comete um erro (por exemplo, inserir dados inválidos), o programa regista o erro neste ficheiro com detalhes como a data, hora e descrição do erro.

3. **primeiros_dados.sql**: Ficheiro SQL que contém os dados iniciais para popular a base de dados. Inclui:
   - Dados de clientes (nome, email, número de telefone e senha).
   - Dados de imóveis (tipo, número de quartos, endereço, área, número de casas de banho, cidade e valor da mensalidade).

## Funcionalidades Principais

- **Gestão de Clientes**:
  - Adicionar novos clientes com validação de nome, email e número de telefone.
  - Editar informações de clientes existentes.

- **Gestão de Imóveis**:
  - Adicionar novos imóveis com detalhes como tipo, número de quartos, endereço, área, número de casas de banho, cidade e valor da mensalidade.
  - Editar informações de imóveis existentes.
  - Visualizar imóveis com filtros por tipo, área e cidade.

- **Validação de Entradas**:
  - O programa valida todas as entradas do utilizador, garantindo que os dados inseridos são corretos (por exemplo, nome não pode conter números, email deve conter "@", número de telefone deve ter 9 dígitos, etc.).

- **Registo de Erros**:
  - Todos os erros cometidos pelo utilizador são registados no ficheiro `log.txt` com detalhes como a data, hora e descrição do erro.

## Como Utilizar

1. **Base de Dados**:
   - Execute o ficheiro `primeiros_dados.sql` para popular a base de dados com dados iniciais de clientes e imóveis.

2. **Executar o Programa**:
   - Execute o ficheiro `app.py` para iniciar o programa.
   - O programa apresenta um menu onde o utilizador pode escolher entre adicionar clientes, adicionar imóveis, editar clientes, editar imóveis ou visualizar imóveis.

3. **Ficheiro de Log**:
   - O ficheiro `log.txt` é atualizado automaticamente sempre que ocorre um erro no programa.

## Requisitos

- Python 3.x
- SQLite3 (incluído na biblioteca padrão do Python)

## Exemplo de Utilização

1. **Adicionar Cliente**:
   - O utilizador insere o nome, email e número de telefone. O programa valida os dados e, se estiverem corretos, adiciona o cliente à base de dados.

2. **Adicionar Imóvel**:
   - O utilizador insere detalhes como tipo de imóvel, número de quartos, endereço, área, número de casas de banho, cidade e valor da mensalidade. O programa valida os dados e adiciona o imóvel à base de dados.

3. **Visualizar Imóveis**:
   - O utilizador pode visualizar todos os imóveis ou aplicar filtros por tipo, área ou cidade.

## Conclusão

Este projeto é uma solução eficiente para a gestão de imóveis e clientes num contexto de arrendamento. Com funcionalidades de validação de dados e registo de erros, o programa garante a integridade dos dados e facilita a gestão de informações.
