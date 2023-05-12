// Função para cadastrar um cliente
function cadastrarCliente() {
  var nome = document.getElementById('nome').value;
  var email = document.getElementById('email').value;
  var telefone = document.getElementById('telefone').value;

  // Cria um objeto para armazenar os dados do cliente
  var cliente = {
    nome: nome,
    email: email,
    telefone: telefone
  };

  // Recupera os clientes cadastrados do armazenamento local
  var clientesCadastrados = JSON.parse(localStorage.getItem('clientes')) || [];

  // Adiciona o novo cliente à lista
  clientesCadastrados.push(cliente);

  // Armazena a lista atualizada no armazenamento local
  localStorage.setItem('clientes', JSON.stringify(clientesCadastrados));

  // Exibe a mensagem de sucesso
  alert('Cliente cadastrado com sucesso!');

  // Limpa os campos do formulário
  document.getElementById('nome').value = '';
  document.getElementById('email').value = '';
  document.getElementById('telefone').value = '';
}

// Função para exibir os clientes cadastrados
function exibirClientesCadastrados() {
  var tabela = document.getElementById('corpoTabelaClientes');

  // Recupera os clientes cadastrados do armazenamento local
  var clientesCadastrados = JSON.parse(localStorage.getItem('clientes')) || [];

  // Preenche a tabela com os dados dos clientes
  for (var i = 0; i < clientesCadastrados.length; i++) {
    var cliente = clientesCadastrados[i];

    var linha = document.createElement('tr');

    var colunaNome = document.createElement('td');
    colunaNome.textContent = cliente.nome;
    linha.appendChild(colunaNome);

    var colunaEmail = document.createElement('td');
    colunaEmail.textContent = cliente.email;
    linha.appendChild(colunaEmail);

    var colunaTelefone = document.createElement('td');
    colunaTelefone.textContent = cliente.telefone;
    linha.appendChild(colunaTelefone);

    tabela.appendChild(linha);
  }
}
