---
tag: 033TJBZDG0
kind: definition
name: Markov chain
msc: [60J10]
defines: 0G48PYM96Q
uses: [0QH5ENKZM1, 0FJB06AD2P, 0HB8SXHPFA, 0ZG61TFBES]
sources:
  - url: https://en.wikipedia.org/wiki/Markov_chain
    locator: Discrete-time Markov chain
inventory: [GPZTSFYRZT]
---

## Definition

Let $S$ be a nonempty [[countable set|0ZG61TFBES]].
Let $(X_n)_{n \ge 0}$ be a [[stochastic process|0QH5ENKZM1]] with values in $S$. It is a Markov chain with state space $S$ if
$$P(X_{n+1} = j \mid X_0 = i_0, \dots, X_{n-1} = i_{n-1}, X_n = i) = P(X_{n+1} = j \mid X_n = i)$$
for each $n \ge 0$ and all states $i_0, \dots, i_{n-1}, i, j \in S$ with $P(X_0 = i_0, \dots, X_n = i) > 0$.
The chain is time-homogeneous if $p_{ij} = P(X_{n+1} = j \mid X_n = i)$ does not depend on $n$.

## Remarks

The condition is the [[Markov property|0HB8SXHPFA]] in discrete time.
For a time-homogeneous chain, the numbers $p_{ij}$ form the [[transition matrix|0F1KBVY161]] $P = (p_{ij})_{i, j \in S}$.
The initial distribution $\lambda_i = P(X_0 = i)$ and $P$ determine the law of the chain: $P(X_0 = i_0, \dots, X_n = i_n) = \lambda_{i_0} p_{i_0 i_1} \cdots p_{i_{n-1} i_n}$.
Markov chains also exist in continuous time and on general state spaces.

## Explanations

### L1 human

A Markov chain has no memory beyond the present state.
Consider the weather each day: if tomorrow depends only on today, the sequence of weather states is a Markov chain.
