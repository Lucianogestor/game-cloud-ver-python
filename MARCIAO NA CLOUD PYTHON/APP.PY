# app.py
from flask import Flask, render_template, request, session
import random

app = Flask(__name__)
app.secret_key = 'sua_chave_secreta_aqui'

perguntas = [
    {"pergunta": "Qual protocolo é comumente usado para interações na API RESTful?", "respostas": ["SOAP", "HTTP", "FTP"], "correta": "HTTP"},
    {"pergunta": "O que é escalabilidade na computação em nuvem?", "respostas": ["Capacidade de aumentar a quantidade de armazenamento", "Capacidade de aumentar ou diminuir recursos de acordo com a demanda", "Capacidade de mover dados de um local para outro"], "correta": "Capacidade de aumentar ou diminuir recursos de acordo com a demanda"},
    {"pergunta": "O que é um ataque DDoS?", "respostas": ["Um ataque que tenta tornar um serviço indisponível ao sobrecarregar com tráfego", "Um ataque que tenta roubar informações confidenciais", "Um ataque que tenta alterar dados em um banco de dados"], "correta": "Um ataque que tenta tornar um serviço indisponível ao sobrecarregar com tráfego"},
    {"pergunta": "O que é virtualização na computação em nuvem?", "respostas": ["Processo de execução de múltiplas instâncias de um sistema operacional em um único hardware", "Processo de criação de uma versão virtual de um dispositivo de hardware", "Ambos"], "correta": "Ambos"},
    {"pergunta": "O que é o Kubernetes?", "respostas": ["Uma plataforma de código aberto para automação de implantação, dimensionamento e gerenciamento de aplicativos em contêiner", "Uma ferramenta para gerenciamento de banco de dados", "Uma linguagem de programação"], "correta": "Uma plataforma de código aberto para automação de implantação, dimensionamento e gerenciamento de aplicativos em contêiner"},
    {"pergunta": "O que é o Docker na computação em nuvem?", "respostas": ["Uma plataforma de código aberto que automatiza a implantação de aplicativos dentro de contêineres de software", "Uma ferramenta para gerenciamento de banco de dados", "Uma linguagem de programação"], "correta": "Uma plataforma de código aberto que automatiza a implantação de aplicativos dentro de contêineres de software"},
    {"pergunta": "O que é SaaS na computação em nuvem?", "respostas": ["Software como serviço", "Armazenamento como serviço", "Segurança como serviço"], "correta": "Software como serviço"},
    {"pergunta": "O que é PaaS na computação em nuvem?", "respostas": ["Plataforma como serviço", "Produto como serviço", "Programa como serviço"], "correta": "Plataforma como serviço"},
    {"pergunta": "O que é IaaS na computação em nuvem?", "respostas": ["Infraestrutura como serviço", "Internet como serviço", "Interface como serviço"], "correta": "Infraestrutura como serviço"},
    {"pergunta": "Qual é a principal vantagem da computação em nuvem?", "respostas": ["Redução de custos", "Maior segurança", "Maior controle sobre os dados"], "correta": "Redução de custos"},
    {"pergunta": "O que é um data center virtual na computação em nuvem?", "respostas": ["Uma coleção de servidores virtuais", "Um local físico onde os dados são armazenados", "Um tipo de software de gerenciamento de dados"], "correta": "Uma coleção de servidores virtuais"},
    {"pergunta": "O que é multi-tenancy na computação em nuvem?", "respostas": ["A capacidade de um sistema de suportar usuários ou clientes diferentes", "A capacidade de um sistema de suportar vários tipos de dados", "A capacidade de um sistema de suportar várias conexões de rede"], "correta": "A capacidade de um sistema de suportar usuários ou clientes diferentes"},
    {"pergunta": "O que é orquestração na computação em nuvem?", "respostas": ["O processo de gerenciamento e coordenação de tarefas complexas", "O processo de distribuição de recursos de computação", "O processo de otimização de consultas de banco de dados"], "correta": "O processo de gerenciamento e coordenação de tarefas complexas"},
    {"pergunta": "O que é computação sem servidor?", "respostas": ["Um modelo de computação em nuvem onde o provedor de nuvem gerencia a infraestrutura", "Um tipo de computação distribuída", "Um tipo de sistema operacional"], "correta": "Um modelo de computação em nuvem onde o provedor de nuvem gerencia a infraestrutura"},
    {"pergunta": "O que é um hipervisor na computação em nuvem?", "respostas": ["Software que cria e gerencia máquinas virtuais", "Hardware que suporta a virtualização", "Um tipo de sistema de arquivos"], "correta": "Software que cria e gerencia máquinas virtuais"}
]

if __name__ == '__main__':
    app.run(debug=True)