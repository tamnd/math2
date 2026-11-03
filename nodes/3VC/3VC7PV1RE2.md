---
tag: 3VC7PV1RE2
kind: statement
role: theorem
name: Complexity of computing a Nash equilibrium
msc: [91A68, 68Q17]
uses: [5MZTZRC3CZ, 745WYP9YJ0, 85RY1ZGSTC, 1FSR0S8E45, ESPYW94XGR]
about: [745WYP9YJ0]
sources:
  - url: https://en.wikipedia.org/wiki/PPAD_(complexity)
---

## Statement

Let PPAD be the [[complexity class|ESPYW94XGR]] of total search problems that reduce in polynomial time to the problem End-of-the-Line.

1. The problem of finding a [[Nash equilibrium|745WYP9YJ0]] of a finite two-player [[normal-form game|5MZTZRC3CZ]] with rational payoff matrices is PPAD-complete.
2. For every fixed number $n \ge 3$ of players, finding an $\varepsilon$-Nash equilibrium of a finite $n$-player game is PPAD-complete. Here $\varepsilon > 0$ is part of the input, written in binary.

## Remarks

End-of-the-Line gives a directed graph on exponentially many vertices, each with in-degree and out-degree at most $1$, by circuits that compute the neighbours.
Given a source vertex, one must find another vertex of degree $1$.
Membership in PPAD comes from the path-following proofs of [[Nash's theorem|85RY1ZGSTC]], such as the [[Lemke–Howson algorithm|1FSR0S8E45]] for two players.
Hardness was shown by Daskalakis, Goldberg and Papadimitriou for games with four or more players, then for three players, and by Chen and Deng for two players.
The problem always has a solution, so it is unlikely to be NP-hard: NP-hardness would imply NP = coNP.
For three or more players the approximation is needed, because the only equilibria can have irrational probabilities.

## Explanations

### L1 human

Nash proved that every finite game has an equilibrium, but his proof does not tell how to find one quickly.
This theorem says that finding one is as hard as any problem in a class called PPAD.
Most researchers believe that PPAD problems cannot be solved in polynomial time.
So there is likely no fast general method for finding equilibria.

### L2 human

The result questions Nash equilibrium as a prediction: if computers cannot find equilibria quickly, players may not reach them either.
PPAD also contains the search for Brouwer fixed points and for Sperner triangles, which have path-following existence proofs.
Some classes of games are easier.
For example, equilibria of two-player zero-sum games can be computed in polynomial time by linear programming.
