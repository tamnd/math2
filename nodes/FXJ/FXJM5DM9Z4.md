---
tag: FXJM5DM9Z4
kind: definition
name: Block spin transformation
msc: [82B28, 82B20]
defines: H5PQFQS6CE
uses: [PAEME5EQRM, R0KGM32QN6]
sources:
  - url: https://en.wikipedia.org/wiki/Renormalization_group
---

## Definition

Let $d \ge 1$, $L \ge 1$, and let $b \ge 3$ be an odd integer.
Let $\Lambda = \set{0, 1, \dots, bL - 1}^d$ and $\Lambda' = \set{0, 1, \dots, L - 1}^d$.
For $y \in \Lambda'$, the *block* of $y$ is $B_y = by + \set{0, 1, \dots, b - 1}^d \subset \Lambda$.
The blocks $B_y$, $y \in \Lambda'$, partition $\Lambda$, and each has $b^d$ sites, an odd number.
The *majority-rule block spin transformation* is the map $T \colon \set{-1, 1}^\Lambda \to \set{-1, 1}^{\Lambda'}$ given by
$$(T\sigma)(y) = \sgn\Big(\sum_{x \in B_y} \sigma(x)\Big), \qquad y \in \Lambda'.$$
Let $H \colon \set{-1, 1}^\Lambda \to \R$ be a Hamiltonian, which includes the inverse temperature.
The *renormalized Hamiltonian* $H' \colon \set{-1, 1}^{\Lambda'} \to \R$ is defined by
$$e^{-H'(\sigma')} = \sum_{\sigma \in \set{-1, 1}^\Lambda : \, T\sigma = \sigma'} e^{-H(\sigma)}.$$

## Remarks

The map $H \mapsto H'$ is one step of a real-space renormalization group with scale factor $b$.
It keeps the partition function: $\sum_{\sigma'} e^{-H'(\sigma')} = \sum_{\sigma} e^{-H(\sigma)}$, since every $\sigma$ has exactly one image $T\sigma$.
So the image under $T$ of the Gibbs measure of $H$ is the Gibbs measure of $H'$.

Example: for $d = 1$, $b = 3$ and $L = 2$, the configuration $\sigma = (+1, -1, +1, -1, -1, +1)$ has block sums $1$ and $-1$.
So $T\sigma = (+1, -1)$.

Non-example: for $b = 2$ and $d = 1$, a block can have sum $0$, so the majority rule does not define a spin $\pm 1$.
Then one needs a tie-breaking rule, or one uses the block average $b^{-d} \sum_{x \in B_y} \sigma(x)$ as a real-valued block variable.

Even for a nearest-neighbour Ising Hamiltonian $H$, the renormalized $H'$ in general contains interactions of all ranges and of many spins.
