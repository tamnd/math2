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

We prove the entry rule by induction on the exponent $k$, and then take $k = n$.
Let $N = (n_{ij})$ be a strictly upper triangular $n \times n$ matrix over a ring $R$, so $n_{ij} = 0$ whenever $j - i < 1$.
The claim for each $k \ge 1$ is that $(N^k)_{ij} = 0$ whenever $j - i < k$.

1. Base case $k = 1$: the claim says $n_{ij} = 0$ whenever $j - i < 1$, that is, whenever $i \ge j$. This is the [[definition|0MKABWDRNC]] of strictly upper triangular.
2. Induction step: assume the claim for some $k \ge 1$. By the [[product rule|076JGP6R3T]],
$$(N^{k+1})_{ij} = (N^k N)_{ij} = \sum_{l=1}^{n} (N^k)_{il}\, n_{lj}.$$
3. A term of this sum can be nonzero only if $(N^k)_{il} \neq 0$ and $n_{lj} \neq 0$. By the induction hypothesis and by step 1, this needs $l - i \ge k$ and $j - l \ge 1$.
4. Adding the two inequalities gives $j - i \ge k + 1$. So when $j - i < k + 1$, every term is $0$, and $(N^{k+1})_{ij} = 0$. This is the claim for $k + 1$.
5. By [[induction|0ASJVEFA9J]], the claim holds for every $k \ge 1$.
6. Take $k = n$. For all indices $1 \le i, j \le n$ we have $j - i \le n - 1 < n$. So every entry of $N^n$ is $0$ by step 5, and $N^n = 0$.

## Idea

Number the diagonals by $j - i$.
A nonzero entry of $N^k$ at $(i, j)$ needs a chain $i = l_0 < l_1 < \dots < l_k = j$ of indices, because each factor $N$ moves the index up by at least one.
Such a chain climbs at least $k$ steps, so $j - i \ge k$.
An $n \times n$ matrix has no positions with $j - i \ge n$, so $N^n$ has no room for a nonzero entry.

## Variants

The same proof can be told with maps.
Let $V_j$ be the span of $e_1, \dots, e_j$, with $V_0 = 0$.
Column $j$ of $N$ has zeros from row $j$ down, so $N V_j \subseteq V_{j-1}$, and by induction $N^k V_n \subseteq V_{n-k}$.
For $k = n$ this gives $N^n V_n \subseteq V_0 = 0$, so $N^n = 0$.

The [[product theorem|45RET2Y995]] shows only that each power of $N$ stays strictly upper triangular.
It does not show that the powers reach zero, so the finer entry rule, or the flag argument, is needed.
