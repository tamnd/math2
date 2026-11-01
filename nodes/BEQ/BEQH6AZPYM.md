---
tag: BEQH6AZPYM
kind: statement
role: theorem
name: Pólya's recurrence theorem
msc: [60G50, 60J10]
uses: [04VZE3FZXF, PBZTBWZ4GS, 0G48PYM96Q]
about: [04VZE3FZXF, PBZTBWZ4GS]
sources:
  - url: https://en.wikipedia.org/wiki/Random_walk
---

## Statement

Let $d \ge 1$ and let $(S_n)_{n \ge 0}$ be the simple [[random walk|04VZE3FZXF]] on $\Z^d$ with $S_0 = 0$: its steps are independent and uniform on the $2d$ vectors $\pm e_1, \ldots, \pm e_d$.

1. If $d = 1$ or $d = 2$, then $P(S_n = 0 \text{ for some } n \ge 1) = 1$.
2. If $d \ge 3$, then $P(S_n = 0 \text{ for some } n \ge 1) < 1$.

## Remarks

The walk is a [[Markov chain|0G48PYM96Q]], and the origin is [[recurrent|PBZTBWZ4GS]] if and only if $\sum_{n} P(S_{2n} = 0) = \infty$.
For $d = 1$, $P(S_{2n} = 0) = \binom{2n}{n} 4^{-n}$, which behaves like $(\pi n)^{-1/2}$.
For $d = 2$, $P(S_{2n} = 0) = \left(\binom{2n}{n} 4^{-n}\right)^2$, which behaves like $(\pi n)^{-1}$, so the sum still diverges.
For general $d$, $P(S_{2n} = 0)$ is of order $n^{-d/2}$, and the sum converges for $d \ge 3$.
In dimension $3$, the probability of return is about $0.34$.
In dimensions $1$ and $2$ the walk returns infinitely often, and in dimension $d \ge 3$ it satisfies $\abs{S_n} \to \infty$ almost surely.

## Explanations

### L1 human

A walker on a grid takes unit steps in random directions.
On a line or in the plane, she is sure to come back home eventually.
In space of three or more dimensions, there is a fair chance that she wanders off and never returns.

### L2 human

The proof reduces recurrence to the divergence of the expected number of returns, which local limit estimates for $P(S_{2n} = 0)$ settle.
Another proof views the lattice as an electrical network: the walk is recurrent if and only if the effective resistance from the origin to infinity is infinite.
The same dichotomy between $d \le 2$ and $d \ge 3$ appears for Brownian motion, which is neighbourhood recurrent in the plane and transient in $\R^3$.
