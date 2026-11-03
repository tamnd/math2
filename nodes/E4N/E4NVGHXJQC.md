---
tag: E4NVGHXJQC
kind: counterexample
name: Allais paradox
msc: [91B06, 91B16]
uses: [8C2N37XPJ8, H67ET07G6W]
sources:
  - url: https://en.wikipedia.org/wiki/Allais_paradox
same_as:
  wikidata: Q1890213
  wikipedia: Allais paradox
---

## Counterexample

Consider four lotteries over the prizes $0$, $1$ and $5$ (in millions of euros).

1. $A_1$: $1$ for sure.
2. $B_1$: $1$ with probability $0.89$, $0$ with probability $0.01$, $5$ with probability $0.10$.
3. $A_2$: $1$ with probability $0.11$, $0$ with probability $0.89$.
4. $B_2$: $5$ with probability $0.10$, $0$ with probability $0.90$.

Many people choose $A_1$ over $B_1$ and $B_2$ over $A_2$.
No [[expected utility|8C2N37XPJ8]] representation fits these two choices.
Write $u_0, u_1, u_5$ for the utilities of the prizes.
The first choice means $u_1 > 0.89 u_1 + 0.01 u_0 + 0.10 u_5$, that is, $0.11 u_1 > 0.01 u_0 + 0.10 u_5$.
The second choice means $0.10 u_5 + 0.90 u_0 > 0.11 u_1 + 0.89 u_0$, that is, $0.01 u_0 + 0.10 u_5 > 0.11 u_1$.
The two inequalities contradict each other.

## Remarks

The choices violate the independence axiom of the [[von Neumann–Morgenstern utility theorem|H67ET07G6W]].
Each pair differs only by a common part: with probability $0.89$, $A_1$ and $B_1$ both pay $1$, and $A_2$ and $B_2$ both pay $0$.
On the remaining probability $0.11$, both pairs compare the same thing, $1$ for sure against $5$ with probability $10/11$ and $0$ with probability $1/11$.
Independence says that the common part should not matter, so the preferred option should be the same in both pairs.
The usual explanation is a certainty effect: a sure gain is valued more than the probabilities alone suggest.

## Explanations

### L1 human

Most people prefer a sure million to a gamble that adds a small chance of losing everything for a chance at five million.
But when both options are already unlikely to pay, most people go for the five million.
These two choices seem natural, yet no single assignment of values to the prizes can explain both by expected utility.
The paradox, posed by Maurice Allais, was a main motivation for theories such as prospect theory.
