---
tag: B1E1ES1BYD
kind: statement
role: theorem
name: Convergence to equilibrium of ergodic Markov chains
msc: [60J10]
uses: [033TJBZDG0, 0F462493EA, 0KRH5157WP, HTR7J0W66V, PBZTBWZ4GS, 8TV1YW8EXC]
about: [0G48PYM96Q, 0KRH5157WP]
sources:
  - url: https://en.wikipedia.org/wiki/Markov_chain
---

## Statement

Let $(X_n)_{n \ge 0}$ be a time-homogeneous [[Markov chain|033TJBZDG0]] on a countable set $S$ with [[transition matrix|0F462493EA]] $P = (p_{ij})$, and write $p^{(n)}_{ij}$ for the entries of $P^n$.
Assume that:

1. the chain is irreducible: for all $i, j \in S$ there is $n \ge 0$ with $p^{(n)}_{ij} > 0$;
2. the chain is aperiodic: for each $i \in S$, the greatest common divisor of $\set{n \ge 1 : p^{(n)}_{ii} > 0}$ is $1$;
3. the chain has a [[stationary distribution|0KRH5157WP]] $\pi$.

Then, for every law of $X_0$,
$$\lim_{n \to \infty} \sum_{j \in S} \abs{P(X_n = j) - \pi_j} = 0.$$
In particular $P(X_n = j) \to \pi_j$ for each $j \in S$.

## Remarks

The classical proof is by [[coupling|HTR7J0W66V]].
Run a second independent copy $(Y_n)$ started from $\pi$; aperiodicity makes the pair $(X_n, Y_n)$ an irreducible chain with a stationary distribution.
Hence the pair is [[recurrent|PBZTBWZ4GS]] and hits the diagonal at a finite time $\tau$, and $\sum_j \abs{P(X_n = j) - \pi_j} \le 2 P(\tau > n) \to 0$.
Example: on $S = \set{1, 2}$ let $p_{12} = a$ and $p_{21} = b$ with $0 < a, b \le 1$ and $a + b < 2$.
Then $\pi = (b, a)/(a + b)$ and $P(X_n = 1) - \pi_1 = (1 - a - b)^n \left(P(X_0 = 1) - \pi_1\right)$, which tends to $0$.
Aperiodicity is needed: for $a = b = 1$ the chain alternates, and $P(X_n = 1)$ oscillates between $0$ and $1$ when $X_0 = 1$.
Irreducibility is needed: with two absorbing states the limit depends on the starting state.

## Explanations

### L1 human

A chain that can reach every state from every other and does not move in a fixed cycle forgets where it started.
After a long time, the chance of being in each state is close to its value under the stationary distribution, whatever the start.
This is why shuffling a deck long enough makes every order of the cards almost equally likely.

### L2 human

The theorem justifies Markov chain Monte Carlo: running an ergodic chain produces samples whose law approaches $\pi$.
The speed of convergence is measured by the [[mixing time|8TV1YW8EXC]], and for finite chains it is geometric, governed by the second largest eigenvalue modulus of $P$.
Without aperiodicity, the averages $\frac1n \sum_{k=1}^{n} P(X_k = j)$ still converge to $\pi_j$.
For a finite state space, condition 3 follows from condition 1.
