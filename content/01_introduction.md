# 💭 Breve Introdução

O Model Context Protocol (MCP) tem ganhado bastante popularidade no ecossistema de Inteligência Artificial (IA). Em muitos casos, seu uso é aplicado de forma incorreta ou limitada, o que impede que algumas soluções explorem seu potencial.

O ecossistema de IA está evoluindo rapidamente, com os Modelos de Linguagem de Grande Escala (LLMs) se tornando cada vez mais avançados. No entanto, esses modelos ainda são limitados por seus dados de treinamento e pela falta de acesso a informações em tempo real ou ferramentas especializadas, o que reduz sua eficácia.

O Model Context Protocol (MCP) surge como solução, permitindo que modelos de IA se conectem a fontes externas de dados, ferramentas e ambientes. Isso viabiliza a troca fluida de informações e amplia a capacidade dos sistemas de IA, promovendo aplicações mais úteis e relevantes.

# 🧐 Mas o que é MCP?

Gostei muito de uma definição que vi em um curso que descreve o MCP como "USB-C para aplicações de IA". De modo geral, o USB-C provê uma interface padronizada para conectar diferentes dispositivos, permitindo a troca de dados, energia e funcionalidades de forma eficiente e universal.

De forma análoga, o MCP estabelece um protocolo consistente para conectar modelos de IA a fontes externas de dados, ferramentas e ambientes operacionais, facilitando intregrações e implementações.

# 🤨 Eu preciso disso em minha aplicação?

Bom, o principal problema que o MCP vem solucionar é o problema de integração. Imagine que temos **M** diferentes aplicações de IA e precisamos conectar a **N** diferentes ferramentas ou fontes de dados. Nesse caso, teríamos **M x N** diferentes integrações, como mostrado na Figura abaixo:

<div style="text-align: center; font-family: 'Arial', sans-serif;">
  <img src="https://huggingface.co/datasets/mcp-course/images/resolve/main/unit1/1a.png" alt="Descrição da imagem" style="max-width: 100%; height: auto;" />
  <p style="margin-top: 10px; font-size: 16px;">
    Fonte: <a href="https://huggingface.co/learn/mcp-course/unit1/key-concepts">Hugging Face</a>
  </p>
</div>


Com uso do MCP conseguimos reduzir nosso problema para **M + N** integrações graças a uma interafce padronizada, como mostrado na Figura abaixo:

<div style="text-align: center; font-family: 'Arial', sans-serif;">
  <img src="https://huggingface.co/datasets/mcp-course/images/resolve/main/unit1/2.png" alt="Descrição da imagem" style="max-width: 100%; height: auto;" />
  <p style="margin-top: 10px; font-size: 16px;">
    Fonte: <a href="https://huggingface.co/learn/mcp-course/unit1/key-concepts">Hugging Face</a>
  </p>
</div>

Cada aplicação implementa o cliente uma vez e cada fonte ou ferramenta também uma vez.

# 🏛️ Arquitetura

O MCP é contruído pensando em uma arquitetura cliente-servidor. O cliente gerencia a comunicação com o servidor MCP, enquanto o servidor se responsabiliza por expor as funcionalidade para as aplicações de IA.

A principal vantagem está na modularidade. Um host pode se conectar aos múltiplos servidores simultaneamente por meio de diferentes clientes. Outra vantagem é que novos servidores podem ser adicionados ao host sem mudanças.

Como sua base, o MCP utiliza JSON-RPC 2.0 como formato das mensagens entre clientes e servidores. Esse protocolo define 3 tipos diferentes de mensagens, como pode ser visto na Figura abaixo:

<div style="text-align: center; font-family: 'Arial', sans-serif;">
  <img src="https://huggingface.co/datasets/mcp-course/images/resolve/main/unit1/5.png" alt="Descrição da imagem" style="max-width: 100%; height: auto;" />
  <p style="margin-top: 10px; font-size: 16px;">
    Fonte: <a href="https://huggingface.co/learn/mcp-course/unit1/key-concepts">Hugging Face</a>
  </p>
</div>

### Request

Enviado do cliente para o servidor para iniciar a operação. Exemplo:

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "method": "tools/call",
  "params": {
    "name": "weather",
    "arguments": {
      "location": "San Francisco"
    }
  }
}
```

### Response

Enviado do servidor para o cliente em resposta a requisição. Exemplo:

```json
{
  "jsonrpc": "2.0",
  "id": 1,
  "result": {
    "temperature": 62,
    "conditions": "Partly cloudy"
  }
}
```

### Notification

Tipicamente enviado do servidor para o cliente para prover atualizações ou informações sobre eventos. Exemplo:

```json
{
  "jsonrpc": "2.0",
  "method": "progress",
  "params": {
    "message": "Processing data...",
    "percent": 50
  }
}
```

### Mecanismos de Transporte

MCP também especifica como as mensagens devem ser transportadas entre clientes e servidores. Existem dois principais:

- **stdio**: Usado no caso em que cliente e servidor estão na mesma máquina

- **HTTP + SSE**: Quando clientes e servidores estão em máquinas diferentes

# ✅ Capacidades

As capacidades expostas pelo protocolo podem ser resumidas em 4:

### Tools

Tools são funções ou ações que os modelos podem chamar por meio do MCP. Exemplo:

```python
def get_weather(location: str) -> dict:
    """Get the current weather for a specified location."""
    
    # Othes steps

    return {
        "temperature": 72,
        "conditions": "Sunny",
        "humidity": 45
    }
```

### Resources

Resources provêm acesso à fontes de dados read-only, possibilitando do modelo recuperar contexto sem executar lógicas complexas. Exemplo:

```python
def read_file(file_path: str) -> str:
    """Read the contents of a file at the specified path."""
    with open(file_path, 'r') as f:
        return f.read()
```

### Prompts

Prompts são templates predefinidos que guiam a interação usuário-modelo. Exemplo:

```python
def code_review(code: str, language: str) -> list:
    """Generate a code review for the provided code snippet."""
    return [
        {
            "role": "system",
            "content": f"You are a code reviewer examining {language} code. Provide a detailed review highlighting best practices, potential issues, and suggestions for improvement."
        },
        {
            "role": "user",
            "content": f"Please review this {language} code:\n\n```{language}\n{code}\n```"
        }
    ]
```

### Sampling

Sampling permite que o servidor requisite ao cliente para performar interações com os LLMs. Exemplo:

```python
def request_sampling(messages, system_prompt=None, include_context="none"):
    """Request LLM sampling from the client."""
    # In a real implementation, this would send a request to the client
    return {
        "role": "assistant",
        "content": "Analysis of the provided data..."
    }
```

# 🔎 Discovery

Uma das principais características é de dynamic discovery. Quando um cliente se conecta aos servidores, ele pode requisitar por Tools, Resources e Prompts por meio de métodos:

- `tools/list`
- `resources/list`
- `prompts/list`