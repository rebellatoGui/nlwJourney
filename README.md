# Especificações

✪ Plann.er

O projeto Journey tem como objetivo ajudar o usuário a **organizar viagens à trabalho ou lazer**.

O usuário pode criar uma viagem com nome, data de início e fim.

Dentro da viagem o usuário pode planejar sua viagem adicionando atividades para realizar em cada dia.

## Requisitos

### Requisitos Funcionais

1. O usuário cadastra uma viagem informando o local de destino, data de início, data de término, e-mails dos convidados e também seu nome completo e endereço de e-mail;
2. O criador da viagem recebe um e-mail para confirmar a nova viagem através de um link. Ao clicar no link, a viagem é confirmada, os convidados recebem e-mails de confirmação de presença e o criador é redirecionado para a página da viagem;
3. Os convidados, ao clicarem no link de confirmação de presença, são redirecionados para a aplicação onde devem inserir seu nome (além do e-mail que já estará preenchido) e então estarão confirmados na viagem;
4. Na página do evento, os participantes da viagem podem adicionar links importantes da viagem como reserva do AirBnB, locais para serem visitados, etc...
5. Ainda na página do evento, o criador e os convidados podem adicionar atividades que irão ocorrer durante a viagem com título, data e horário;
6. Novos participantes podem ser convidados dentro da página do evento através do e-mail e assim devem passar pelo fluxo de confirmação como qualquer outro convidado;

# Banco de dados

## Nessa aplicação vamos utilizar banco de dados relacional (SQL). Para ambiente de desenvolvimento seguiremos com o SQLite pela facilidade do ambiente.

![plann.er](nlw_Journey_api_docs/plann.er.png)

## Especificações da API para o back-end da aplicação plann.er construída durante o NLW Journey da Rocketseat.

![trips](nlw_Journey_api_docs/endpoints_trips.png)
![participants](nlw_Journey_api_docs/endpoints_participants.png)
![activities](nlw_Journey_api_docs/endpoints_activities.png)
![links](nlw_Journey_api_docs/endpoints_links.png)