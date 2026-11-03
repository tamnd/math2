---
tag: V089PVA6SV
kind: definition
name: Renormalization group
msc: [82B28, 81T17, 82B27]
defines: 5XTSCZCF7Z
uses: [ENWMTRJRND, R0KGM32QN6, 0XMEM406JM]
sources:
  - url: https://en.wikipedia.org/wiki/Renormalization_group
---

## Definition

Let $\mathcal{K} \subset \R^n$ be a set of coupling constants, each $K \in \mathcal{K}$ defining a Hamiltonian $H_K$ of a lattice system on $\Z^d$.
For $K \in \mathcal{K}$, let $Z_N(K)$ be the partition function on a box of $N$ sites.
Let $f(K) = \lim_{N \to \infty} N^{-1} \log Z_N(K)$ be the free energy per site, up to the factor $-\beta^{-1}$, and $\xi(K)$ the correlation length in lattice units.
Let $B$ be a multiplicative [[semigroup|0XMEM406JM]] of real numbers $b \ge 1$ that contains $1$.
A *renormalization group* is a family of maps $R_b \colon \mathcal{K} \to \mathcal{K}$, for $b \in B$, such that:

1. $R_1$ is the identity and $R_b \circ R_{b'} = R_{b b'}$;
2. there is a function $G_b$ on $\mathcal{K}$ with $Z_N(K) = e^{N G_b(K)} Z_{N / b^d}(R_b K)$, so that $f(K) = G_b(K) + b^{-d} f(R_b K)$;
3. $\xi(R_b K) = \xi(K) / b$, where $\xi$ is the [[correlation length|ENWMTRJRND]].

Each $R_b$ is a *renormalization group transformation*.

## Remarks

A point $K^*$ with $R_b K^* = K^*$ is a fixed point, and clause 3 forces $\xi(K^*) = 0$ or $\xi(K^*) = \infty$.
Critical points flow to fixed points with $\xi = \infty$.

Example: decimation of the [[Ising chain|R0KGM32QN6]] with coupling $K = \beta J$ at zero field, for $b = 2^k$.
Summing over a spin $s$ between $s_1$ and $s_2$ gives $\sum_{s = \pm 1} e^{K s (s_1 + s_2)} = A \, e^{K' s_1 s_2}$ with $\tanh K' = \tanh^2 K$ and $A^2 = 4 \cosh 2K$.
So $Z_N(K) = A^{N/2} Z_{N/2}(K')$, which is clause 2.
Since $\xi(K) = -1/\log \tanh K$, the new coupling has $\xi(K') = \xi(K)/2$, which is clause 3.
The fixed points are $K = 0$ and $K = \infty$, and every $0 < K < \infty$ flows to $0$.

Non-example: the identity map taken as $R_2$ fails clause 3 at every $K$ with $0 < \xi(K) < \infty$, since $\xi(K) \ne \xi(K)/2$.

In practice $R_b$ is constructed by [[block spins|H5PQFQS6CE]] or by integrating out momentum shells, and it is usually only approximate, because new couplings appear at each step.
