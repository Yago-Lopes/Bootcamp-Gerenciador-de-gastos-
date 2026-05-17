from django.test import TestCase
from django.urls import reverse

class CotacaoMoedasIntegrationTest(TestCase):
    """Testes de integração para a nova funcionalidade de cotação de moedas."""

    def test_pagina_inicial_carrega_com_sucesso_e_contem_cotacoes(self):
        """Valida se a página principal renderiza e exibe os dados do Dólar e Euro."""
        # Acessa a URL correspondente à página index do gerenciador de gastos
        url = reverse('gastos:index')
        resposta = self.client.get(url)

        # 1. Verifica se a página carregou corretamente (Status HTTP 200 OK)
        self.assertEqual(resposta.status_code, 200)

        # 2. Verifica se as chaves 'dolar' e 'euro' foram enviadas no contexto para o HTML
        self.assertIn('dolar', resposta.context)
        self.assertIn('euro', resposta.context)

        # 3. Garante que os valores não vieram vazios ou zerados padrão se a API falhar
        self.assertNotEqual(resposta.context['dolar'], "0.00")
        self.assertNotEqual(resposta.context['euro'], "0.00")