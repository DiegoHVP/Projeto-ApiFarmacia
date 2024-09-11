# API de Farmácia

Este projeto consiste na produção de uma API para gerenciar operações de uma farmácia, fornecendo endpoints para manipulação de medicamentos, funcionários, clientes, fornecedores e compras. Para isso, foi utilizado o framework FastAPI.

## Diagrama Entidade e Relacionamento
A estrutura de dados do projeto é definida por meio de diagrama de entidade e relacionamento. Abaixo está uma representação do modelo:
[![](https://mermaid.ink/img/pako:eNqlVc1u1DAQfpXI5_YF9lbRXYSAgkoOHCJZgz3JWtie1HEQsN0H4jl4MZz_jZOlkepTMv_z-ZvxiQmSyHYM3b2CwoHJbBLOAZwBoSA5df_NefeQ7t_uHxMlk8_vJ3G6_5omlgxGIk0CdCc7Z7b7-IhSCTBoPW2IfH-X7pMfaIVqPSbF4cOnuzQpHQpaBnmqwXolQcYFgUZXKKgicQ7qJ3D04BREKlNwoyNZbddiz_sfSsl7FLmSS2WljNLgsFqqCrTolKAVlUP4BpVHgS7C9lAHoMiGNlaxNeBDyFrD8vJKvnJ99ZpQlHkkqdAeYR0i7l2oVR9X7kiQ9Y408gGhuBdyNrQoKcDzCgo2acCv5DcTD8e7GZO_0Soo8DV5N8HkUWNONnZGA0q_SN0RSZCBDo4iJCd2UxDzEgq4mKGpVTKl2zLkY7oOmxmh2zGV4IGLNty2kbyYYe7JL1ZFVxp_YWN0GfmVaufXvGoSlzZRcNiAz8-3t3Sara5dkrGSqqpWGVu3vhzGxronPAz2l9GuJJj2w3afaXFc95nNVuOUtwIlKSnJXWtoGIq2mY5zEDzQDA6DwWDfMasxDytLq99j671mZsfjRhq8_v4x_2njimN4LqQaC2M3zGBoRMnwxLX0yZg_YhhY1hhLcN8bs3Owg9rTl19WsJ13Nd4wR3VxZLscdBX-6jIQHPsnspee_wEH7C4H?type=png)](https://mermaid.live/edit#pako:eNqlVc1u1DAQfpXI5_YF9lbRXYSAgkoOHCJZgz3JWtie1HEQsN0H4jl4MZz_jZOlkepTMv_z-ZvxiQmSyHYM3b2CwoHJbBLOAZwBoSA5df_NefeQ7t_uHxMlk8_vJ3G6_5omlgxGIk0CdCc7Z7b7-IhSCTBoPW2IfH-X7pMfaIVqPSbF4cOnuzQpHQpaBnmqwXolQcYFgUZXKKgicQ7qJ3D04BREKlNwoyNZbddiz_sfSsl7FLmSS2WljNLgsFqqCrTolKAVlUP4BpVHgS7C9lAHoMiGNlaxNeBDyFrD8vJKvnJ99ZpQlHkkqdAeYR0i7l2oVR9X7kiQ9Y408gGhuBdyNrQoKcDzCgo2acCv5DcTD8e7GZO_0Soo8DV5N8HkUWNONnZGA0q_SN0RSZCBDo4iJCd2UxDzEgq4mKGpVTKl2zLkY7oOmxmh2zGV4IGLNty2kbyYYe7JL1ZFVxp_YWN0GfmVaufXvGoSlzZRcNiAz8-3t3Sara5dkrGSqqpWGVu3vhzGxronPAz2l9GuJJj2w3afaXFc95nNVuOUtwIlKSnJXWtoGIq2mY5zEDzQDA6DwWDfMasxDytLq99j671mZsfjRhq8_v4x_2njimN4LqQaC2M3zGBoRMnwxLX0yZg_YhhY1hhLcN8bs3Owg9rTl19WsJ13Nd4wR3VxZLscdBX-6jIQHPsnspee_wEH7C4H)

#### Fornecedor

Representa informações dos fornecedores que fornecem produtos para a farmácia.

| Atributo        | Tipo      | Descrição                                                                          |
| --------------- | --------- | ---------------------------------------------------------------------------------- |
| `id`            | `int`     | Identificador único do fornecedor                                                  |
| `nome`          | `str`     | Nome do fornecedor                                                                |
| `contato`       | `str`     | Informações de contato do fornecedor                                               |
| `medicamento_id`| `int`     | ID do medicamento relacionado ao fornecedor (opcional, chave estrangeira)           |

#### Farmácia

Representa informações da farmácia.

| Atributo   | Tipo     | Descrição                          |
| ---------- | -------- | ---------------------------------- |
| `id`       | `int`    | Identificador único da farmácia    |
| `nome`     | `str`    | Nome da farmácia                   |
| `local`    | `str`    | Localização da farmácia (opcional) |

#### Farmacêutico

Representa informações dos farmacêuticos que trabalham na farmácia.

| Atributo           | Tipo     | Descrição                                                              |
| ------------------ | -------- | ---------------------------------------------------------------------- |
| `matricula`        | `int`    | Número de matrícula do farmacêutico                                     |
| `p_nome`           | `str`    | Primeiro nome do farmacêutico                                           |
| `u_nome`           | `str`    | Último nome do farmacêutico (opcional)                                  |
| `cpf`              | `str`    | Número de CPF do farmacêutico                                           |
| `unidade_trabalho` | `str`    | Unidade de trabalho do farmacêutico (opcional)                          |
| `controle_farmacia`| `int`    | ID da farmácia que o farmacêutico gerencia (opcional, chave estrangeira)|
| `senha`            | `str`    | Senha de acesso do farmacêutico                                         |

#### Cliente

Representa informações dos clientes que utilizam a farmácia para realizar compras de medicamentos e produtos.

| Atributo            | Tipo     | Descrição                                                    |
| ------------------- | -------- | ------------------------------------------------------------ |
| `id`                | `int`    | Identificador único do cliente                                |
| `nome`              | `str`    | Nome completo do cliente                                      |
| `sobrenome`         | `str`    | Sobrenome do cliente (opcional)                               |
| `cpf`               | `str`    | Número de CPF do cliente                                      |
| `telefone`          | `str`    | Número de telefone do cliente                                 |
| `email`             | `str`    | Endereço de e-mail do cliente (opcional)                      |
| `alergias`          | `str`    | Informações sobre alergias do cliente (opcional)              |
| `cadastro_farmacia` | `int`    | ID da farmácia associada ao cliente (opcional, chave estrangeira)|
| `forma_pagamento`   | `str`    | Método preferido de pagamento do cliente (opcional)           |
| `senha`             | `str`    | Senha de acesso do cliente                                    |

#### Medicamento

Representa informações sobre os medicamentos disponíveis na farmácia.

| Atributo          | Tipo     | Descrição                                                      |
| ----------------- | -------- | -------------------------------------------------------------- |
| `id`              | `int`    | Identificador único do medicamento                              |
| `vencimento`      | `date`   | Data de vencimento do medicamento (opcional)                    |
| `preco`           | `float`  | Preço do medicamento                                            |
| `quantidade`      | `int`    | Quantidade disponível do medicamento (opcional)                 |
| `alergias`        | `list`   | Alergias relacionadas ao medicamento (opcional)                 |
| `faixa_etaria`    | `str`    | Faixa etária recomendada para o medicamento (opcional)          |
| `mg_ml`           | `str`    | Miligramas por mililitro do medicamento (opcional)              |
| `unidade`         | `str`    | Unidade de medida do medicamento (opcional)                     |
| `nome`            | `str`    | Nome do medicamento                                             |
| `farmacia_id`     | `int`    | ID da farmácia associada ao medicamento (opcional, chave estrangeira)|
| `similares`       | `list`   | IDs de medicamentos similares (opcional, chave estrangeira)     |
| `genericos`       | `list`   | IDs de medicamentos genéricos (opcional, chave estrangeira)     |
| `reabastecer`     | `int`    | ID do fornecedor do medicamento (opcional, chave estrangeira)   |

#### Compra

Representa informações sobre as compras realizadas na farmácia.

| Atributo         | Tipo      | Descrição                                               |
| ---------------- | --------- | ------------------------------------------------------- |
| `id`             | `int`     | Identificador único da compra                            |
| `cliente_id`     | `int`     | ID do cliente que realizou a compra (chave estrangeira)  |
| `medicamento_ids`| `list`    | Lista de IDs dos medicamentos comprados (chave estrangeira) |
| `quantidade`     | `list`    | Lista de quantidades de medicamentos comprados          |
| `data_compra`    | `date`    | Data em que a compra foi realizada                       |
| `preco_total`    | `float`   | Preço total da compra                                    |

### Relacionamentos

- **Medicamento** está associado a uma **Farmácia** e pode ter relações com **Fornecedores**, **Clientes** e **Farmácia**.
- **Farmacêutico** tem relação com uma **Farmácia**.
- **Cliente** está vinculado a uma **Farmácia**.
- **Compra** está relacionada a **Cliente** e **Medicamento**.

### Tabela de Endpoints

| Método | Endpoint                        | Descrição                                         | Requisição                                        | Resposta                                    |
|--------|---------------------------------|---------------------------------------------------|--------------------------------------------------|---------------------------------------------|
| POST   | /compra/                        | Adiciona uma nova compra                          | `{ "cliente_id": 1, "medicamento_ids": [1], "quantidade": [1] }` | `{ "message": "Compra registrada com sucesso" }` |
| GET    | /compra/{id}                    | Obtém detalhes de uma compra específica           | -                                                | `{ "Compra": { "id": 1, "cliente_id": 1, "data_compra": "2024-09-11", "quantidade": 1, "preco_total": 100, "medicamentos": [ { "medicamento_id": 1, "quantidade": 1 } ] } }` |
| GET    | /compra/                        | Obtém todas as compras                            | -                                                | `{ "Compras": [ { "id": 1, "cliente_id": 1, "data_compra": "2024-09-11", "quantidade": 1, "preco_total": 100, "medicamentos": [ { "medicamento_id": 1, "quantidade": 1 } ] } ] }` |
| PUT    | /compra/{id}                    | Atualiza uma compra existente                     | `{ "cliente_id": 1, "medicamento_ids": [1], "quantidade": [1] }` | `{ "message": "Compra com ID 1 foi atualizada" }` |
| DELETE | /compra/{id}                    | Deleta uma compra específica                      | -                                                | `{ "message": "Compra com ID 1 foi deletada" }` |
| GET    | /compra/me/{id}                 | Obtém todas as compras de um cliente              | -                                                | `{ "Compras": [ { "id": 1, "cliente_id": 1, "data_compra": "2024-09-11", "quantidade": 1, "preco_total": 100, "medicamentos": [ { "medicamento_id": 1, "quantidade": 1 } ] } ] }` |
| POST   | /farmacia                       | Adiciona uma nova farmácia                        | `{ "nome": "Farmacia ABC", "local": "Rua X" }`  | `{ "message": "Farmacia Farmacia ABC foi cadastrada" }` |
| GET    | /farmacia/{id}                  | Obtém detalhes de uma farmácia específica         | -                                                | `{ "farmacia": { "id": 1, "nome": "Farmacia ABC", "local": "Rua X" } }` |
| GET    | /farmacia                       | Obtém todas as farmácias                          | -                                                | `{ "farmacias": [ { "id": 1, "nome": "Farmacia ABC", "local": "Rua X" } ] }` |
| PUT    | /farmacia/{id}                  | Atualiza uma farmácia existente                   | `{ "nome": "Farmacia XYZ", "local": "Rua Y" }`  | `{ "message": "Farmacia Farmacia XYZ foi atualizada com sucesso" }` |
| DELETE | /farmacia/{id}                  | Deleta uma farmácia específica                    | -                                                | `{ "message": "Farmacia Farmacia XYZ foi deletada do sistema" }` |
| POST   | /farmaceutico                   | Adiciona um novo farmacêutico                     | `{ "nome": "Dr. João", "registro": "12345" }`   | `{ "message": "Farmacêutico Dr. João foi cadastrado" }` |
| GET    | /farmaceutico/{id}              | Obtém detalhes de um farmacêutico específico      | -                                                | `{ "farmaceutico": { "id": 1, "nome": "Dr. João", "registro": "12345" } }` |
| GET    | /farmaceutico                   | Obtém todos os farmacêuticos                      | -                                                | `{ "farmaceuticos": [ { "id": 1, "nome": "Dr. João", "registro": "12345" } ] }` |
| PUT    | /farmaceutico/{id}              | Atualiza um farmacêutico existente                | `{ "nome": "Dr. Pedro", "registro": "67890" }`  | `{ "message": "Farmacêutico Dr. Pedro foi atualizado com sucesso" }` |
| DELETE | /farmaceutico/{id}              | Deleta um farmacêutico específico                 | -                                                | `{ "message": "Farmacêutico Dr. Pedro foi deletado do sistema" }` |
| POST   | /cliente                       | Adiciona um novo cliente                          | `{ "nome": "Carlos Silva", "cpf": "12345678900" }` | `{ "message": "Cliente Carlos Silva foi cadastrado" }` |
| GET    | /cliente/{id}                  | Obtém detalhes de um cliente específico           | -                                                | `{ "cliente": { "id": 1, "nome": "Carlos Silva", "cpf": "12345678900" } }` |
| GET    | /cliente                       | Obtém todos os clientes                          | -                                                | `{ "clientes": [ { "id": 1, "nome": "Carlos Silva", "cpf": "12345678900" } ] }` |
| PUT    | /cliente/{id}                  | Atualiza um cliente existente                    | `{ "nome": "Carlos Souza", "cpf": "12345678900" }` | `{ "message": "Cliente Carlos Souza foi atualizado com sucesso" }` |
| DELETE | /cliente/{id}                  | Deleta um cliente específico                     | -                                                | `{ "message": "Cliente Carlos Souza foi deletado do sistema" }` |
| POST   | /medicamento                   | Adiciona um novo medicamento                     | `{ "nome": "Paracetamol", "preco": 10.0, "quantidade": 100 }` | `{ "message": "Medicamento Paracetamol foi cadastrado" }` |
| GET    | /medicamento/{id}              | Obtém detalhes de um medicamento específico      | -                                                | `{ "medicamento": { "id": 1, "nome": "Paracetamol", "preco": 10.0, "quantidade": 100 } }` |
| GET    | /medicamento                   | Obtém todos os medicamentos                     | -                                                | `{ "medicamentos": [ { "id": 1, "nome": "Paracetamol", "preco": 10.0, "quantidade": 100 } ] }` |
| PUT    | /medicamento/{id}              | Atualiza um medicamento existente               | `{ "nome": "Dipirona", "preco": 12.0, "quantidade": 80 }` | `{ "message": "Medicamento Dipirona foi atualizado com sucesso" }` |
| DELETE | /medicamento/{id}              | Deleta um medicamento específico                | -                                                | `{ "message": "Medicamento Dipirona foi deletado do sistema" }` |
| POST   | /fornecedor                   | Adiciona um novo fornecedor                     | `{ "nome": "Fornecedor X", "contato": "123456789" }` | `{ "message": "Fornecedor Fornecedor X foi cadastrado" }` |
| GET    | /fornecedor/{id}              | Obtém detalhes de um fornecedor específico       | -                                                | `{ "fornecedor": { "id": 1, "nome": "Fornecedor X", "contato": "123456789" } }` |
| GET    | /fornecedor                   | Obtém todos os fornecedores                    | -                                                | `{ "fornecedores": [ { "id": 1, "nome": "Fornecedor X", "contato": "123456789" } ] }` |
| PUT    | /fornecedor/{id}              | Atualiza um fornecedor existente                | `{ "nome": "Fornecedor Y", "contato": "987654321" }` | `{ "message": "Fornecedor Fornecedor Y foi atualizado com sucesso" }` |
| DELETE | /fornecedor/{id}              | Deleta um fornecedor específico                 | -                                                | `{ "message": "Fornecedor Fornecedor Y foi deletado do sistema" }` |


## Instalação

Para utilizar esta API, siga estes passos:

1. Clone este repositório.
2. Instale as dependências com `pip install -r requirements.txt`.
3. Execute o projeto com o comando:

   ```bash
   python main.py
   ```