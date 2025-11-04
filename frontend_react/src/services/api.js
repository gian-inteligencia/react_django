// Conteúdo para: frontend_react/src/services/api.js
// (Este é o código do react_django/src/services/api.js)

// Usamos 'axios' por conveniência, mas 'fetch' puro funciona
import axios from 'axios';

// Configura o 'fetch' para sempre falar com nosso backend Django
const api = axios.create({
  baseURL: 'http://localhost:8000/api/v1/' // URL da API Django
  // Aqui também iriam os headers de autenticação (Tokens JWT, etc)
});

// Funções que nosso app React irá chamar
export const getParceiros = () => api.get('/parceiros/');
export const createParceiro = (parceiroData) => api.post('/parceiros/', parceiroData);
export const deleteParceiro = (id) => api.delete(`/parceiros/${id}/`);
// etc.