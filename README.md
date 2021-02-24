![Alt text](https://github.com/diegoMasin/maximumtech/blob/master/assets/img/logo-colorida.png)

# Split Pdf and Move/Rename

###### To split general Pdf of Rendimentos by CPF of the exported in program of Dirf. (Dividir Pdf geral de Rendimentos pelo CPF dos exportados no programa da Dirf)

**Importants dependencies (Windows or Linux):**

```
- pipenv
- python == 3.6
- VsCode
```

**Installing and configuration:**

```
- git clone https://github.com/diegoMasin/split-pdf-rendimentos-dirf-by-cpf.git
- Entre no diretório do projeto e execute:
  - pipenv --python 3.6
  - pipenv shell
  - pip install -r requirements.txt
  - code .
- Acho já no VsCode, Ctrl+Shift+P, digite interpreter e escolha o interpretador python criado pelo pipenv.
- Copie para dentro da raiz do projeto(lado a lado com o main.py) o arquivo geral de todos os rendimentos das pessoas da empresa extraído no programa da DIRF
- Crie uma pasta rendimentos, e dentro dela crie mais duas pastas, extract e rename. (Pode mudar os nomes desde que inclua na configuração)
- Edite o arquivo main.py:
  - configure os caminhos absolutos de: extract_to e rename_to
  - mude o prefixo_file se assim desejar
  - coloque em filename_all_rendimentos o nome do arquivo pdf com todos os rendimentos

```

**Running:**

```
- No VsCode, feito todos os passos acima, apenas pressione F5.
```

#### Listen the story that problem and the why this solution

- ***
