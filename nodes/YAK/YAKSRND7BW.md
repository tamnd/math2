---
tag: YAKSRND7BW
kind: proof
name: Proof that a strictly upper triangular matrix is nilpotent
msc: ["15A99"]
topics: [Y1ESNQ2V52]
audience: ug1
proves: AW5RBMW7RK
methods: [0ASJVEFA9J]
uses: [0MKABWDRNC, 076JGP6R3T]
sources:
  - url: https://en.wikipedia.org/wiki/Nilpotent_matrix
    locator: Examples
---

## Proof

Let $N$ be strictly upper triangular, so $n_{ij} = 0$ when $j - i < 1$.
We prove by induction on $k \ge 1$: $(N^k)_{ij} = 0$ whenever $j - i < k$.

1. Base case $k = 1$: this is the [[definition|0MKABWDRNC]] of strictly upper triangular.
2. Induction step: assume the claim for $k$. By the [[product rule|076JGP6R3T]], $(N^{k+1})_{ij} = \sum_{l=1}^{n} (N^k)_{il}\, n_{lj}$.
3. A term can be nonzero only if $(N^k)_{il} \neq 0$ and $n_{lj} \neq 0$. By the hypothesis and step 1, this needs $l - i \ge k$ and $j - l \ge 1$.
4. Adding the two inequalities gives $j - i \ge k + 1$. So if $j - i < k + 1$, every term is $0$, and $(N^{k+1})_{ij} = 0$.
5. This proves the claim for all $k \ge 1$ by [[induction|0ASJVEFA9J]].
6. Take $k = n$. For all indices, $j - i \le n - 1 < n$. So every entry of $N^n$ is $0$, and $N^n = 0$.

## Idea

The entries of $N^k$ live on and above the $k$-th diagonal above the main one.
An $n \times n$ matrix has only $n - 1$ diagonals above the main one, so $N^n$ has no room left.

## Variants

- By maps: $N V_j \subseteq V_{j-1}$ for $V_j = \langle e_1, \dots, e_j \rangle$ and $V_0 = 0$. So $N^k V_n \subseteq V_{n-k}$, and $N^n V_n = 0$.
- The [[product theorem|45RET2Y995]] shows that products of strictly upper triangular matrices stay strictly upper triangular, but not the faster decay; the induction above gives the decay.
