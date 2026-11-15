# Sistema — Aventura de exemplo

> Regras do jogo em linguagem natural, escritas para o mestre (IA) ler. A parte que o
> código precisa ler fica no `sistema.json`; os nomes usados aqui devem bater com os de lá.

## Visão geral
Fantasia medieval sombria. Letalidade média: o combate é perigoso, mas raramente mata
sem aviso. Estilo heroico com tons sombrios; investigação e intriga pesam tanto quanto
as lutas.

## Atributos
| Sigla | Nome | Representa |
|---|---|---|
| `for` | Força | Potência física, carregar peso, golpes corpo a corpo. |
| `des` | Destreza | Agilidade, reflexos, furtividade, ataques à distância. |
| `con` | Constituição | Resistência, vigor, tolerância a venenos e cansaço. |
| `int` | Inteligência | Raciocínio, memória, conhecimento. |
| `sab` | Sabedoria | Percepção, intuição, força de vontade. |
| `car` | Carisma | Presença, persuasão, intimidação. |

Os valores vão de 1 a 20.

## Modificadores
Modificador = `(valor − 10) ÷ 2`, arredondado para baixo. Ex.: 16 → +3, 8 → −1.

## Perícias
| Perícia | Atributo |
|---|---|
| Atletismo | `for` |
| Furtividade | `des` |
| Percepção | `sab` |

Se o personagem é proficiente na perícia, soma o bônus de proficiência ao teste.

## Testes
Rolagem: `d20 + modificador (+ proficiência, se houver)` contra uma CD.

| Dificuldade | CD |
|---|---|
| Fácil | 10 |
| Média | 15 |
| Difícil | 20 |
| Quase impossível | 25 |

Peça teste apenas quando houver chance real de falha **e** a falha tiver consequência
interessante. Ações triviais simplesmente acontecem.

## Vantagem e desvantagem
Com vantagem, rolam-se dois d20 e usa-se o maior; com desvantagem, o menor. Vantagem:
posição favorável, ajuda de aliado, preparação. Desvantagem: ferimento, escuridão,
pressa, condição negativa. Elas se anulam.

## Crítico e falha crítica
- **20 natural:** sucesso automático; em ataques, o dano é rolado em dobro.
- **1 natural:** falha automática, com uma complicação narrativa.

## Combate
- **Iniciativa:** `d20 + modificador de des`, em ordem decrescente.
- **Turno:** um movimento e uma ação (atacar, usar item, ajudar, fugir…).
- **Ataque:** `d20 + modificador + proficiência` contra a CA do alvo.
- **Dano:** dado da arma + modificador do atributo do ataque.
- **0 PV:** o personagem cai inconsciente e faz testes de morte (3 sucessos estabiliza,
  3 falhas morre).
- **Teatro da mente:** distâncias são "perto" (corpo a corpo) ou "longe" (à distância).

## Condições
- **Envenenado:** desvantagem em ataques e testes.
- **Caído:** desvantagem em ataques; ataques corpo a corpo contra ele têm vantagem.
- **Atordoado:** não pode agir no próximo turno.
- **Cego:** falha em testes que dependem de visão; desvantagem em ataques.

## Descanso e cura
- **Descanso curto (1 hora):** recupera metade dos PV máximos uma vez por dia.
- **Descanso longo (8 horas):** recupera todos os PV e recursos.

## Progressão
XP necessário: nível 2 com 300, nível 3 com 900, nível 4 com 2700. Ao subir de nível:
+1d10 + mod. de `con` em PV máximos e um novo talento narrativo.

## Regras da casa
- Tochas duram 1 hora de jogo.
- Moedas e itens comuns não precisam de controle de peso.

## Limites do mestre
- Não matar o protagonista sem teste ou sem aviso prévio de perigo.
- Não criar itens mágicos sem motivo na história.
- Não revelar segredos do `mundo.md` sem que o jogador os descubra.
- Não decidir ações, falas ou sentimentos do protagonista.
