---
tag: 1313JFBBAD
kind: definition
name: Betti numbers of a module
msc: [13D02, 13D07]
defines: 3B1743XS7S
uses: [MZ02BKPHJA, NJ3APQ8BHH, 05QY1VEBYD, DDQRERAQCV, HK2AA1YSQ2, 0DZ9DKAKZR, 0670T59HGE]
sources:
  - url: https://en.wikipedia.org/wiki/Betti_number
---

## Definition

Let $(R, \mathfrak{m}, k)$ be a [[Noetherian|0670T59HGE]] [[local ring|MZ02BKPHJA]] with [[residue field|NJ3APQ8BHH]] $k = R/\mathfrak{m}$.
Let $M$ be a [[finitely generated|05QY1VEBYD]] $R$-module.
For each $i \ge 0$, the module $\operatorname{Tor}^R_i(M, k)$ is annihilated by $\mathfrak{m}$, so it is a finite-dimensional $k$-vector space.
The $i$-th *Betti number* of $M$ is
$$\beta_i(M) = \dim_k \operatorname{Tor}^R_i(M, k).$$

In the graded case, $R = k[x_1, \ldots, x_n]$ is graded by degree, $\mathfrak{m} = (x_1, \ldots, x_n)$, and $M$ is a finitely generated graded $R$-module.
Then each $\operatorname{Tor}^R_i(M, k)$ is graded, and the *graded Betti numbers* are $\beta_{i,j}(M) = \dim_k \operatorname{Tor}^R_i(M, k)_j$.

## Remarks

Equivalently, $\beta_i(M)$ is the rank of the [[free module|0DZ9DKAKZR]] $F_i$ in a minimal free [[resolution|HK2AA1YSQ2]] $\cdots \to F_1 \to F_0 \to M \to 0$, that is, one whose differentials have all entries in $\mathfrak{m}$.

For $R = k[x, y]$ and $M = k = R/(x, y)$, the Koszul complex
$$0 \to R(-2) \to R(-1)^2 \to R \to k \to 0$$
is a minimal resolution, so $\beta_0 = 1$, $\beta_1 = 2$, $\beta_2 = 1$, and the nonzero graded Betti numbers are $\beta_{0,0} = 1$, $\beta_{1,1} = 2$, $\beta_{2,2} = 1$.

The ranks in a resolution that is not minimal are not the Betti numbers.
For $M = R/(x)$ over $R = k[x]$, the resolution $0 \to R \oplus R \to R \oplus R \to M \to 0$, with the second summand mapped identically, has ranks $2, 2$, while $\beta_0 = \beta_1 = 1$.

$\beta_0(M)$ is the least number of generators of $M$, and the largest $i$ with $\beta_i(M) \ne 0$ is the [[projective dimension|MR9QCH1PNA]] of $M$ when it is finite.
