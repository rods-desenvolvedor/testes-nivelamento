<template>
  <div class="container">
    <h2>Buscar Operadora</h2>

    <div class="busca-box">
      <label>Busca por nome (texto livre):</label>
      <input
        v-model="termo"
        @keyup.enter="buscarPorTexto"
        placeholder="Ex: UNIMED, BRADESCO, AMIL..."
      />
      <button @click="buscarPorTexto">Buscar por texto</button>
    </div>

    <div class="busca-box">
      <label>Busca por código da operadora (registro ANS):</label>
      <select v-model="registroSelecionado" @change="buscarPorRegistro">
        <option disabled value="">Selecione uma operadora</option>
        <option
          v-for="(op, index) in operadoras"
          :key="index"
          :value="op.REGISTRO_ANS"
        >
          {{ op.NOME_FANTASIA }} - {{ op.REGISTRO_ANS }}
        </option>
      </select>
    </div>

    <div v-if="carregando" class="status"> Buscando...</div>
    <div v-if="erro" class="erro"> {{ erro }}</div>

    <div v-if="resultados.length">
      <h3>Resultados encontrados: {{ resultados.length }}</h3>
      <table>
        <thead>
          <tr>
            <th>Registro ANS</th>
            <th>Nome Fantasia</th>
            <th>Razão Social</th>
            <th>CNPJ</th>
            <th>Cidade</th>
            <th>UF</th>
          </tr>
        </thead>
        <tbody>
          <tr v-for="(op, index) in resultados" :key="index">
            <td>{{ op.REGISTRO_ANS }}</td>
            <td>{{ op.NOME_FANTASIA }}</td>
            <td>{{ op.RAZAO_SOCIAL }}</td>
            <td>{{ op.CNPJ }}</td>
            <td>{{ op.CIDADE }}</td>
            <td>{{ op.UF }}</td>
          </tr>
        </tbody>
      </table>
    </div>
  </div>
</template>

<script lang="ts" setup>
import { ref, onMounted } from 'vue'
import axios from 'axios'

interface Operadora {
  REGISTRO_ANS: string
  CNPJ: string
  RAZAO_SOCIAL: string
  NOME_FANTASIA: string
  CIDADE: string
  UF: string
}

const termo = ref('')
const registroSelecionado = ref('')
const resultados = ref<Operadora[]>([])
const operadoras = ref<Operadora[]>([])
const erro = ref('')
const carregando = ref(false)

const buscarPorTexto = async () => {
  if (!termo.value) return
  erro.value = ''
  carregando.value = true
  resultados.value = []

  try {
    const response = await axios.get('http://localhost:5000/buscar', {
      params: { query: termo.value }
    })
    resultados.value = response.data
  } catch (err) {
    erro.value = 'Erro ao buscar por texto.'
  } finally {
    carregando.value = false
  }
}

const buscarPorRegistro = async () => {
  if (!registroSelecionado.value) return
  erro.value = ''
  carregando.value = true
  resultados.value = []

  try {
    const response = await axios.get('http://localhost:5000/buscar', {
      params: { query: registroSelecionado.value }
    })
    resultados.value = response.data
  } catch (err) {
    erro.value = 'Erro ao buscar por registro.'
  } finally {
    carregando.value = false
  }
}

onMounted(async () => {
  try {
    const response = await axios.get('http://localhost:5000/buscar')
    operadoras.value = response.data
  } catch (err) {
    erro.value = 'Erro ao carregar lista de operadoras.'
  }
})
</script>

<style scoped>
body {
  background-color: #121212;
  color: #f5f5f5;
  font-family: 'Segoe UI', sans-serif;
}

.container {
  max-width: 1000px;
  margin: 2rem auto;
  padding: 2rem;
  background-color: #1e1e1e;
  border-radius: 12px;
  box-shadow: 0 0 12px rgba(255, 255, 255, 0.05);
}

h2, h3 {
  text-align: center;
  color: #ffffff;
  margin-bottom: 1.5rem;
}

.busca-box {
  margin-bottom: 1.5rem;
}

label {
  display: block;
  margin-bottom: 0.3rem;
  color: #ccc;
}

input,
select {
  width: 100%;
  padding: 10px;
  margin-top: 4px;
  margin-bottom: 8px;
  background-color: #2b2b2b;
  color: #fff;
  border: 1px solid #444;
  border-radius: 4px;
}

button {
  padding: 8px 16px;
  background-color: #007bff;
  border: none;
  border-radius: 4px;
  color: #fff;
  cursor: pointer;
}
button:hover {
  background-color: #0056b3;
}

table {
  width: 100%;
  border-collapse: collapse;
  margin-top: 1.5rem;
  background-color: #2b2b2b;
  color: #f5f5f5;
  border-radius: 6px;
  overflow: hidden;
}

th, td {
  padding: 10px 12px;
  border: 1px solid #444;
  text-align: left;
}
th {
  background-color: #333;
  color: #ddd;
}

.erro {
  color: #ff6b6b;
  margin-top: 10px;
  text-align: center;
}
.status {
  text-align: center;
  color: #aaa;
}
</style>
