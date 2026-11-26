# 🌐 Exercícios de Programação em Várias Linguagens

![Python](https://img.shields.io/badge/Python-3776AB?logo=python&logoColor=white)
![C](https://img.shields.io/badge/C-00599C?logo=c&logoColor=white)
![C++](https://img.shields.io/badge/C%2B%2B-00599C?logo=cplusplus&logoColor=white)
![C#](https://img.shields.io/badge/C%23-239120)
![Status](https://img.shields.io/badge/status-em%20progresso-yellow)

> **+170 exercícios, várias resoluções.** A mesma lista de desafios, do "Hello World" a projetos com manipulação de dados, resolvida em diferentes linguagens de programação.

---

## 📖 Sobre o projeto

Este repositório reúne as minhas soluções para a lista de exercícios do site **[exercicios.dunossauro.com](https://exercicios.dunossauro.com/)**, resolvida em **mais de uma linguagem**. Cada exercício tem uma solução por linguagem, o que permite comparar abordagens, sintaxes e filosofias lado a lado.

Ele nasceu da expansão de um outro repositório, focado em resoluções em Python, e foi pensado para crescer: novas linguagens podem ser adicionadas ao longo do tempo, seguindo a mesma organização.

## 🚧 Status

**Em progresso.** Conforme eu for finalizando os exercícios em cada linguagem, o repositório será atualizado. A seção [Progresso](#-progresso) mostra o andamento de cada uma.

## 🤔 Por que resolver os mesmos exercícios em várias linguagens?

- **Lógica é separada de sintaxe.** Quando o problema já está resolvido, o desafio passa a ser expressar a mesma ideia em outra linguagem. Isso deixa claro o que é raciocínio e o que é detalhe da linguagem.
- **Cada linguagem ensina algo diferente.** O Python mostra como ser produtivo e expressivo, o C expõe memória e ponteiros, o C++ une controle de baixo nível a abstrações, e o C# mostra a orientação a objetos em ambientes gerenciados, e por aí vai.
- **Comparação revela trade-offs.** Ver mais de uma solução para o mesmo problema mostra o que cada linguagem facilita, o que exige mais código e por quê.
- **Fundamentos que se transferem.** Tipagem, gerenciamento de memória, compilação, coleções e orientação a objetos são conceitos que reaparecem em quase toda linguagem.
- **Código idiomático.** Em vez de traduzir linha a linha, o objetivo é escrever cada solução do jeito que a linguagem pede, com suas coleções, bibliotecas e convenções.

## 🧰 Linguagens

| Linguagem | Paradigma principal | Execução | Tipagem | Memória | Status |
|-----------|---------------------|----------|---------|---------|:------:|
| **Python** | Multiparadigma | Interpretada | Dinâmica | Automática (GC) | 🚧 |
| **C** | Procedural | Compilada (nativa) | Estática | Manual | 🚧 |
| **C++** | Multiparadigma | Compilada (nativa) | Estática | Manual, com RAII e *smart pointers* | ⏳ |
| **C#** | Orientada a objetos | Compilada para IL e executada no .NET | Estática | Automática (GC) | ⏳ |

**Legenda:** ✅ concluída · 🚧 em progresso · ⏳ planejada

## 🔍 O mesmo exercício, VÁRIAS linguagens

Um programa simples que lê um nome e exibe uma saudação mostra bem as diferenças de estilo.

**Python**
```python
nome = input("Qual é o seu nome? ")
print(f"Olá, {nome}!")
```

**C**
```c
#include <stdio.h>

int main(void) {
    char nome[100];
    printf("Qual é o seu nome? ");
    scanf("%99s", nome);
    printf("Olá, %s!\n", nome);
    return 0;
}
```

**C++**
```cpp
#include <iostream>
#include <string>

int main() {
    std::string nome;
    std::cout << "Qual é o seu nome? ";
    std::cin >> nome;
    std::cout << "Olá, " << nome << "!\n";
    return 0;
}
```

**C#**
```csharp
Console.Write("Qual é o seu nome? ");
string? nome = Console.ReadLine();
Console.WriteLine($"Olá, {nome}!");
```

## 📚 Categorias de exercícios

| # | Categoria | Exercícios | O que cobre |
|:-:|-----------|:----------:|-------------|
| 1 | Estrutura sequencial | 18 | Entrada e saída, variáveis, operadores aritméticos e conversões |
| 2 | Estrutura de decisão | 28 | Condicionais, operadores lógicos e de comparação |
| 3 | Estrutura de repetição | 51 | Laços, contadores, acumuladores e controle de fluxo |
| 4 | Listas | 24 | Coleções de dados: percorrer, buscar, filtrar e ordenar |
| 5 | Funções | 14 | Modularização, parâmetros, retorno e escopo |
| 6 | Strings | 14 | Manipulação e processamento de texto |
| 7 | Manipulação de arquivos | 2 | Leitura e escrita de arquivos |
| 8 | Classes | 17 | Orientação a objetos: atributos, métodos e interação entre objetos |
| 9 | Projetos | 3 | Programas maiores, combinando vários conceitos |
| 10 | Dados | 6 | Organização, tratamento e análise de conjuntos de dados |
| | **Total** | **177** | |

### 🔄 Equivalências entre linguagens

Alguns exercícios mudam de forma conforme a linguagem. A tabela mostra como cada conceito costuma aparecer:

| Conceito | Python | C | C++ | C# |
|----------|--------|---|-----|----|
| **Lista** | `list` | Array / `malloc` | `std::vector` | `List<T>` | `ArrayList` |
| **Dicionário** | `dict` | Implementação própria | `std::map` / `std::unordered_map` | `Dictionary<K, V>` | `HashMap` |
| **String** | `str` | `char[]` com `'\0'` | `std::string` | `string` | `String` |
| **Classe** | `class` | `struct` + funções | `class` / `struct` | `class` | `class` |
| **Arquivo** | `open()` com `with` | `fopen()` / `fclose()` | `std::fstream` | `File` / `StreamReader` | `Files` / `BufferedReader` |

Na categoria **Classes**, o C não possui orientação a objetos nativa, então as soluções nessa linguagem são adaptadas com `struct`.

## 📊 Progresso

| # | Categoria | Exercícios | Python | C | C++ | C# | 
|:-:|-----------|:----------:|:------:|:-:|:---:|:--:|
| 1 | Estrutura sequencial | 18 | ✅ | 🚧 | ⏳ | ⏳ | 
| 2 | Estrutura de decisão | 28 | 🚧 | 🚧 | ⏳ | ⏳ | 
| 3 | Estrutura de repetição | 51 | 🚧 | 🚧 | ⏳ | ⏳ | 
| 4 | Listas | 24 | 🚧 | 🚧 | ⏳ | ⏳ | 
| 5 | Funções | 14 | 🚧 | 🚧 | ⏳ | ⏳ | 
| 6 | Strings | 14 | 🚧 | 🚧 | ⏳ | ⏳ | 
| 7 | Manipulação de arquivos | 2 | 🚧 | 🚧 | ⏳ | ⏳ | 
| 8 | Classes | 17 | 🚧 | 🚧 | ⏳ | ⏳ | 
| 9 | Projetos | 3 | 🚧 | 🚧 | ⏳ | ⏳ | 
| 10 | Dados | 6 | 🚧 | 🚧 | ⏳ | ⏳ | 


**Convenções:**
- Cada linguagem tem a sua pasta, com as mesmas dez categorias dentro.
- O número do exercício é o mesmo em todas as linguagens: `ex01` em Python é o mesmo desafio que `ex01` em C ou Java.
- Em Java, o nome do arquivo precisa coincidir com o da classe pública (por exemplo, `Ex01.java` contém `public class Ex01`).

## 🔗 Fonte e créditos

Os enunciados pertencem ao site **[exercicios.dunossauro.com](https://exercicios.dunossauro.com/)**. As soluções deste repositório são de minha autoria, escritas durante meus estudos.

## 💡 Sugestões

Viu uma solução que pode ser melhorada, ou tem uma forma mais idiomática de resolver algum exercício em uma das linguagens? Fique à vontade para abrir uma *issue* ou um *pull request*.
