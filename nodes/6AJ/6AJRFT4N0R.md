---
tag: 6AJRFT4N0R
kind: definition
name: Repeated game
msc: [91A20, 91A10]
defines: XHE1BSE7BF
uses: [5MZTZRC3CZ, 0DVDCMA2DK, 01X5CVV1Q5]
sources:
  - url: https://en.wikipedia.org/wiki/Repeated_game
---

## Definition

Let $G$ be a finite [[normal-form game|5MZTZRC3CZ]], the *stage game*, with players $i = 1, \dots, n$, finite action sets $A_i$, and payoff functions $u_i \colon A \to \R$, where $A = A_1 \times \cdots \times A_n$.
Let $0 < \delta < 1$ be a discount factor.
The *infinitely repeated game* $G^\infty(\delta)$ is played as follows.

1. In each period $t = 0, 1, 2, \dots$ the players choose actions $a^t_i \in A_i$ simultaneously.
2. At the end of each period, every player observes the action profile $a^t = (a^t_1, \dots, a^t_n)$.
3. A strategy of player $i$ is a map that assigns to each history $(a^0, \dots, a^{t-1}) \in A^t$, for every $t \ge 0$, a [[probability distribution|0DVDCMA2DK]] on $A_i$.
4. A sequence of action profiles $(a^t)_{t \ge 0}$ gives player $i$ the payoff $(1 - \delta) \sum_{t=0}^{\infty} \delta^t u_i(a^t)$.

For mixed strategies, the payoff is the expected value of this sum.
The *finitely repeated game* $G^T$ with $T \ge 1$ periods is defined in the same way with periods $t = 0, \dots, T - 1$ and payoff $\sum_{t=0}^{T-1} u_i(a^t)$.

## Remarks

The factor $1 - \delta$ normalizes payoffs: by the [[geometric series|01X5CVV1Q5]], the constant sequence $a^t = a$ gives $u_i(a)$.

Example: let $G$ be the prisoner's dilemma with $u(C, C) = (2, 2)$, $u(D, D) = (1, 1)$, $u(D, C) = (3, 0)$ and $u(C, D) = (0, 3)$.
"Grim trigger" plays $C$ in period $0$ and after every history in which everyone played $C$, and plays $D$ otherwise.
If both use grim trigger, each gets $2$.
A player who first defects at some period gains at most $(1 - \delta) \cdot 3 + \delta \cdot 1$ in normalized value from that period on, compared with $2$.
So grim trigger is a Nash equilibrium of $G^\infty(\delta)$ exactly when $\delta \ge 1/2$.

Non-example: a dynamic game in which the payoff functions change from period to period according to a state that the players' actions influence is not a repeated game.
It fails the requirement that the same stage game is played in every period; such games are called stochastic games.
