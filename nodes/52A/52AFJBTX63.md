---
tag: 52AFJBTX63
kind: definition
name: Simulated annealing
msc: [90C59, 90C26, 65C05]
defines: 578AX75H88
uses: [0G48PYM96Q, MKHF449E22, GYNMZ9201M, ZCFQEZ0A0V]
sources:
  - url: https://en.wikipedia.org/wiki/Simulated_annealing
---

## Definition

Let $S$ be a finite set and let $E \colon S \to \R$ be a cost function, called the energy.
Give each $s \in S$ a nonempty set $N(s) \subseteq S \setminus \set{s}$ of neighbours.
Let $(T_k)_{k \ge 0}$ be positive numbers with $T_k \to 0$, the *cooling schedule*.
*Simulated annealing* is the random sequence $(s_k)$ in $S$ defined from a starting state $s_0$ as follows.
At step $k$, choose $s'$ uniformly at random in $N(s_k)$, and set $s_{k+1} = s'$ with probability
$$\min\left(1, \exp\left(-\frac{E(s') - E(s_k)}{T_k}\right)\right),$$
and $s_{k+1} = s_k$ otherwise.

## Remarks

The sequence is a time-inhomogeneous [[Markov chain|0G48PYM96Q]].
Assume $s' \in N(s)$ exactly when $s \in N(s')$, all sets $N(s)$ have the same size, and the neighbour graph is connected.
Then for a fixed temperature $T$ the chain has the [[Boltzmann distribution|GYNMZ9201M]] $\pi_T(s) \propto e^{-E(s)/T}$ as a stationary distribution, by detailed balance.
As $T \to 0$, $\pi_T$ concentrates on the set of global minimizers of $E$.
Under the same assumptions, let $d^*$ be the largest depth of a local minimum of $E$ that is not global.
Hajek showed in 1988 that for $T_k = c / \log(k + 2)$, one has $P(s_k \text{ is a global minimizer}) \to 1$ if and only if $c \ge d^*$.

Example: $S = \set{0, 1, 2}$ with $N(0) = \set{1}$, $N(1) = \set{0, 2}$, $N(2) = \set{1}$, and $E(0) = 1$, $E(1) = 2$, $E(2) = 0$.
From $s_k = 0$, the only proposal is $1$, accepted with probability $e^{-1/T_k}$.
So the walk can leave the local minimum $0$ and reach the global minimizer $2$, but such uphill moves become rare as $T_k \to 0$.

Non-example: the rule that accepts $s'$ only when $E(s') \le E(s_k)$ is a randomized local search, not simulated annealing.
It corresponds to temperature $0$, and in the example it never leaves the state $0$.
