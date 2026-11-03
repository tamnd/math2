---
tag: DXWZATJB75
kind: definition
name: Evolutionarily stable strategy
msc: [91A22, 92D15]
defines: 9ECGX1RGGT
uses: [5MZTZRC3CZ, P01KKHB155, 745WYP9YJ0]
sources:
  - url: https://en.wikipedia.org/wiki/Evolutionarily_stable_strategy
---

## Definition

Let $A$ be a real $n \times n$ matrix, the payoff matrix of a symmetric two-player [[normal-form game|5MZTZRC3CZ]] with pure strategies $1, \dots, n$.
A [[mixed strategy|P01KKHB155]] is a vector $x \in \R^n$ with $x_i \ge 0$ and $x_1 + \cdots + x_n = 1$.
Write $u(x, y) = x^T A y$ for the expected payoff of a player using $x$ against an opponent using $y$.
A mixed strategy $x^*$ is an *evolutionarily stable strategy* (ESS) if for every mixed strategy $y \ne x^*$:

1. $u(y, x^*) \le u(x^*, x^*)$, and
2. if $u(y, x^*) = u(x^*, x^*)$, then $u(y, y) < u(x^*, y)$.

## Remarks

Clause 1 says that $(x^*, x^*)$ is a symmetric [[Nash equilibrium|745WYP9YJ0]].
An equivalent form: for every $y \ne x^*$ there is $\bar\varepsilon > 0$ such that $u(x^*, w) > u(y, w)$ for all $\varepsilon \in (0, \bar\varepsilon)$, where $w = \varepsilon y + (1 - \varepsilon) x^*$.
So in a population where a small share $\varepsilon$ of mutants plays $y$, the residents do strictly better.
A strict symmetric Nash equilibrium, with $u(y, x^*) < u(x^*, x^*)$ for all $y \ne x^*$, is always an ESS.

Example: the Hawk–Dove game with prize $2$ and fight cost $4$ has
$$A = \begin{pmatrix} -1 & 2 \\ 0 & 1 \end{pmatrix},$$
with strategy $1$ = Hawk and $2$ = Dove.
Let $x^* = (1/2, 1/2)$; then $A x^* = (1/2, 1/2)^T$, so every $y$ earns $1/2$ against $x^*$, and clause 1 holds with equality.
For $y = (q, 1 - q)$ with $q \ne 1/2$, one computes $u(x^*, y) - u(y, y) = (x^* - y)^T A y = (1/2 - q)(1 - 2q) = 2 (1/2 - q)^2 > 0$, so clause 2 holds.

Non-example: in rock–paper–scissors with payoffs $1$ for a win, $-1$ for a loss and $0$ for a tie, let $x^* = (1/3, 1/3, 1/3)$.
Every $y$ earns $0$ against $x^*$, so clause 2 applies.
For $y$ = pure rock, $u(y, y) = 0 = u(x^*, y)$, so clause 2 fails and $x^*$ is not an ESS, although it is the unique Nash equilibrium.
