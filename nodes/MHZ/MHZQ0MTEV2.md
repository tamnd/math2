---
tag: MHZQ0MTEV2
kind: definition
name: Normal-form game
msc: [91A10, 91A06]
defines: 5MZTZRC3CZ
uses: [070R982G4B, 09CEDJYBKP]
sources:
  - url: https://en.wikipedia.org/wiki/Normal-form_game
---

## Definition

A *normal-form game* $G = (N, (S_i)_{i \in N}, (u_i)_{i \in N})$ consists of the following.

1. A [[finite set|070R982G4B]] $N = \set{1, \dots, n}$ of *players*.
2. For each player $i \in N$, a nonempty set $S_i$ of *pure strategies*.
3. For each player $i \in N$, a *payoff function* $u_i \colon S \to \R$, where $S = S_1 \times \cdots \times S_n$ is the [[Cartesian product|09CEDJYBKP]] of the strategy sets.

An element $s = (s_1, \dots, s_n)$ of $S$ is a *strategy profile*.
The game is *finite* if every $S_i$ is finite.

## Remarks

For $s \in S$ one writes $s_{-i}$ for the strategies of all players except $i$, and $(t_i, s_{-i})$ for the profile obtained from $s$ by replacing $s_i$ with $t_i$.
A finite two-player game is given by two $m \times n$ matrices $A$ and $B$ with $A_{jk} = u_1(j, k)$ and $B_{jk} = u_2(j, k)$; it is then called a *bimatrix game*.
Example: the prisoner's dilemma has $N = \set{1, 2}$, $S_1 = S_2 = \set{C, D}$ and $u_1(C, C) = 3$, $u_1(C, D) = 0$, $u_1(D, C) = 5$, $u_1(D, D) = 1$, with $u_2(s_1, s_2) = u_1(s_2, s_1)$; all three clauses hold.
Non-example: suppose a description gives the strategy sets but says only that "player 1 prefers to win".
It gives no payoff function on all of $S$, so clause 3 fails.
