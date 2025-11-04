// Conteúdo para: frontend_react/src/pages/ParceirosPage.js
// (Este é o código do react_django/src/pages/ParceirosPage.js)

import React, { useState, useEffect } from 'react';
import { getParceiros, createParceiro } from '../services/api';

function ParceirosPage() {
  // 1. "Estado" do React. Substitui as variáveis do template.
  const [parceiros, setParceiros] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  
  // 2. Busca os dados quando o componente é montado
  useEffect(() => {
    fetchParceiros();
  }, []);

  const fetchParceiros = async () => {
    try {
      setLoading(true);
      const response = await getParceiros();
      setParceiros(response.data); // Coloca os dados da API no "estado"
      setError(null);
    } catch (err) {
      setError('Falha ao buscar parceiros.');
    } finally {
      setLoading(false);
    }
  };
  
  // 3. Função para lidar com a criação (você pode expandir isso)
  const handleCreate = async (formData) => {
    // Esta função é um exemplo, você precisará de um formulário
    // para coletar o 'formData'
    try {
        // await createParceiro(formData);
        // fetchParceiros(); // Atualiza a lista!
        alert('Funcionalidade de Criar Parceiro ainda não implementada no form de React.');
    } catch (err) {
        alert('Erro ao criar parceiro: ' + err.response?.data?.detail);
    }
  };
  
  // (Aqui teriam funções handleEdit, handleDelete, etc.)

  // 4. Renderiza o "HTML" (JSX)
  return (
    <div className="container">
      <h1>Gerenciar Parceiros (React)</h1>
      
      {/* Aqui você teria seu <ParceiroForm onSubmit={handleCreate} /> */}
      <button onClick={() => alert('Formulário de criação não implementado')}>Adicionar Novo Parceiro (Exemplo)</button>
      
      <h2>Parceiros Cadastrados</h2>
      
      {loading && <p>Carregando...</p>}
      {error && <div className="alert alert-danger">{error}</div>}
      
      <table style={{ color: '#000', backgroundColor: '#fff', width: '100%' }}>
        <thead>
          <tr>
            <th>Nome Fantasia</th>
            <th>Email Gestor</th>
            <th>Tipo</th>
            <th>Senha Definida?</th>
            <th>Ações</th>
          </tr>
        </thead>
        <tbody>
          {parceiros.map((p) => (
            <tr key={p.id}>
              <td>{p.nome_fantasia}</td>
              <td>{p.email_gestor}</td>
              <td>{p.tipo}</td>
              <td style={{ textAlign: 'center' }}>
                {p.senha_definida ? '✓' : '✗'}
              </td>
              <td>
                <div className="action-buttons-container">
                  <button className="button-filter">Editar</button>
                  <button className="button-danger">Excluir</button>
                </div>
              </td>
            </tr>
          ))}
        </tbody>
      </table>
    </div>
  );
}

export default ParceirosPage;