---
tag: RM4GB5V1ZH
kind: definition
name: Pure and mixed strategy
msc: [91A10]
defines: P01KKHB155
uses: [5MZTZRC3CZ, 4Y8AF9H9HA, 0DVDCMA2DK, 0WQNRCNY3M]
sources:
  - url: https://en.wikipedia.org/wiki/Strategy_(game_theory)
---

## Definition

Let $G = (N, (S_i), (u_i))$ be a finite [[normal-form game|5MZTZRC3CZ]].
A *pure strategy* of player $i$ is an element of $S_i$.
A *mixed strategy* of player $i$ is a [[probability distribution|0DVDCMA2DK]] $\sigma_i$ on $S_i$.
The set of mixed strategies of $i$ is written $\Delta(S_i)$.
A *mixed strategy profile* is a tuple $\sigma = (\sigma_1, \dots, \sigma_n)$ with $\sigma_i \in \Delta(S_i)$ for each $i$.
The payoff of player $i$ at $\sigma$ is the [[expected value|0WQNRCNY3M]]
$$u_i(\sigma) = \sum_{s \in S} \Big( \prod_{j \in N} \sigma_j(s_j) \Big) u_i(s),$$
where the players randomise independently.

## Remarks

A pure strategy $s_i$ is identified with the mixed strategy that puts probability $1$ on $s_i$.
The *support* of $\sigma_i$ is the set of pure strategies $s_i$ with $\sigma_i(s_i) > 0$.
The set $\Delta(S_i)$ is a simplex of dimension $\abs{S_i} - 1$, and $u_i(\sigma)$ is linear in each $\sigma_j$ separately.
Example: in matching pennies, with $S_1 = S_2 = \set{H, T}$, take $\sigma_1(H) = \sigma_1(T) = 1/2$.
These numbers are nonnegative and sum to $1$, so $\sigma_1$ is a mixed strategy.
Against any $\sigma_2$, player 1 then gets payoff $0$.
Non-example: the assignment $\sigma_1(H) = 0.7$, $\sigma_1(T) = 0.7$ is not a mixed strategy, since the weights sum to $1.4$.
In an [[extensive-form game|4Y8AF9H9HA]] one also uses *behavior strategies*, which randomise separately at each information set.
