---
tag: PBZ9B2X4QT
kind: definition
name: Congestion game
msc: [91A14]
defines: VEZX21F7WW
uses: [5MZTZRC3CZ, G5FRB9E3J1, 745WYP9YJ0]
sources:
  - url: https://en.wikipedia.org/wiki/Congestion_game
---

## Definition

A *congestion game* consists of the following data.

1. A finite set $N = \set{1, \dots, n}$ of players and a finite set $E$ of *resources*.
2. For each player $i$, a nonempty set $S_i$ of nonempty subsets of $E$, the strategies of $i$.
3. For each resource $e \in E$, a *cost function* $c_e \colon \set{1, \dots, n} \to \R$.

For a profile $s = (s_1, \dots, s_n)$, let $n_e(s)$ be the number of players $i$ with $e \in s_i$.
The cost of player $i$ is $C_i(s) = \sum_{e \in s_i} c_e(n_e(s))$.
This is the [[normal-form game|5MZTZRC3CZ]] with strategy sets $S_i$ and payoffs $u_i = -C_i$.

## Remarks

Rosenthal's function $\Phi(s) = \sum_{e \in E} \sum_{k=1}^{n_e(s)} c_e(k)$ satisfies $C_i(t_i, s_{-i}) - C_i(s_i, s_{-i}) = \Phi(t_i, s_{-i}) - \Phi(s)$.
So $-\Phi$ is an exact potential, and every congestion game is a [[potential game|G5FRB9E3J1]].
In particular it has a pure [[Nash equilibrium|745WYP9YJ0]]: any minimiser of $\Phi$.
Monderer and Shapley showed the converse: every finite exact potential game is isomorphic to a congestion game.
Example: two players each choose one of two parallel roads $a$ and $b$, with $c_a(k) = k$ and $c_b(k) = 2$.
Then $S_1 = S_2 = \set{\set{a}, \set{b}}$; all clauses hold, and one player on each road is a pure equilibrium.
Non-example: if the cost of a road depends on which players use it, and not only on how many, clause 3 fails.
