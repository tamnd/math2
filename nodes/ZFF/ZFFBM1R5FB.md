---
tag: ZFFBM1R5FB
kind: definition
name: Stochastic game
msc: [91A15, 91A50]
defines: RT0NQMS7WA
uses: [5MZTZRC3CZ, XHE1BSE7BF, 0DVDCMA2DK, 0G48PYM96Q, 0WQNRCNY3M, GJ8VTBFNP2]
sources:
  - url: https://en.wikipedia.org/wiki/Stochastic_game
---

## Definition

A finite *stochastic game* with discount factor $\delta \in (0, 1)$ consists of:

1. a finite set $N = \set{1, \dots, n}$ of players;
2. a finite set $S$ of states and an initial state $s_0 \in S$;
3. for each player $i$, a finite set $A_i$ of actions; write $A = A_1 \times \cdots \times A_n$;
4. for each player $i$, a stage payoff function $r_i \colon S \times A \to \R$;
5. a transition function $p$ that assigns to each $(s, a) \in S \times A$ a [[probability distribution|0DVDCMA2DK]] $p(\cdot \mid s, a)$ on $S$.

Play proceeds in periods $t = 0, 1, 2, \dots$.
In period $t$ all players observe the current state $s_t$ and the past states and actions, and choose actions $a^t_i \in A_i$ simultaneously.
Player $i$ receives $r_i(s_t, a^t)$, and the next state $s_{t+1}$ is drawn from $p(\cdot \mid s_t, a^t)$.
Player $i$ evaluates the play by the [[expected value|0WQNRCNY3M]] of $\sum_{t=0}^{\infty} \delta^t r_i(s_t, a^t)$.

## Remarks

A strategy is *stationary* if the action distribution in period $t$ depends only on the current state $s_t$.
For fixed stationary strategies, the sequence of states is a [[Markov chain|0G48PYM96Q]].
Shapley proved that every finite two-player zero-sum stochastic game with discounting has a value and that both players have stationary optimal strategies.
His proof applies the [[minimax theorem|GJ8VTBFNP2]] state by state inside a contraction mapping argument.

Example: if $S$ has a single state, the stochastic game is the infinitely [[repeated game|XHE1BSE7BF]] of the [[normal-form game|5MZTZRC3CZ]] with payoffs $r_i(s_0, \cdot)$, up to the normalizing factor $1 - \delta$.
If $N$ has a single player, the stochastic game is a Markov decision process.

Non-example: a dynamic game in which the distribution of the next state depends on the whole past and not only on the current state and actions fails clause 5.
Such a game can often be turned into a stochastic game by enlarging the set of states to record the relevant history.
