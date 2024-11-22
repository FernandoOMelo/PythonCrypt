
# PythonCrypt

PythonCrypt é um programa simples de criptografia e descriptografia de texto, desenvolvido em Python. Ele utiliza uma lógica básica para substituir caracteres do texto de entrada por seus índices no alfabeto, ajustados por uma constante (-5), enquanto preserva os espaços.

## ⚙️ Funcionalidades

1. **Criptografia de texto**:
   - Converte cada letra do texto em um índice numérico (baseado no alfabeto e outros caracteres suportados), subtraindo 5 do índice.
   - Mantém os espaços intactos.
   - Retorna o texto criptografado como uma sequência de números separados por espaços.

2. **Descriptografia de texto**:
   - Reverte a criptografia, convertendo os números de volta para os caracteres originais.
   - Garante a recuperação exata do texto original, incluindo os espaços.

## 🛠️ Requisitos

- Python 3.6 ou superior.

## 🚀 Como usar

1. Clone este repositório:
   ```bash
   git clone https://github.com/FernandoOMelo/PythonCrypt.git
   ```
2. Navegue até o diretório do projeto:
   ```bash
   cd PythonCrypt
   ```
3. Execute o script:
   ```bash
   python3 PythonCrypt.py
   ```

4. Escolha uma das opções no menu:
   - **(1) Criptografar texto**: Digite um texto com até 100 caracteres para criptografia.
   - **(2) Descriptografar texto**: Digite um texto criptografado (sequência de números) para recuperação.

## 📌 Limitações

- O texto de entrada para criptografia deve ter no máximo **100 caracteres**.
- Suporta apenas os caracteres definidos na lista `Caracteres`.

## 🔍 Exemplos de Uso

### Criptografia
Entrada:
```
Digite um texto para ser criptografado: hello world
```
Saída:
```
3 0 6 6 9 87 72 9 12 6 
```

### Descriptografia
Entrada:
```
Digite um texto para ser descriptografado: 3 0 6 6 9 87 72 9 12 6 
```
Saída:
```
hello world
```

## 🧩 Estrutura do Código

- `criptografaTexto()`: Realiza a criptografia com base nos índices de `Caracteres`.
- `descriptografaTexto()`: Reverte a criptografia com base nos índices de `Caracteres`.
- `Caracteres`: Uma lista de caracteres suportados pelo sistema.
- Menu interativo para escolher entre criptografia e descriptografia.

## 📂 Estrutura do Repositório
```
PythonCrypt/
├── PythonCrypt.py  # Código principal
├── README.md        # Documentação do projeto
```

## 🛡️ Licença

Este projeto está licenciado sob a licença MIT. Consulte o arquivo [LICENSE](LICENSE) para mais detalhes.
