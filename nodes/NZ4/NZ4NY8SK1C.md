---
tag: NZ4NY8SK1C
kind: object
name: Hyperfinite type II1 factor
msc: [46L36, 46L10]
instance_of: [PSFWQVZ0FS]
uses: [PSFWQVZ0FS, 4XM1VN1C1N, HM2HHE3J51]
sources:
  - url: https://en.wikipedia.org/wiki/Hyperfinite_type_II_factor
---

## Description

The hyperfinite type $\mathrm{II}_1$ factor $R$ is the [[von Neumann algebra|PSFWQVZ0FS]] obtained as the closure of an increasing union of matrix algebras.
Embed $M_{2^n}(\C)$ into $M_{2^{n+1}}(\C)$ by $x \mapsto I_2 \otimes x = \begin{pmatrix} x & 0 \\ 0 & x \end{pmatrix}$.
These embeddings preserve the normalized trace $\tau(x) = 2^{-n} \operatorname{tr}(x)$, so $\tau$ is well defined on the union $A_\infty = \bigcup_n M_{2^n}(\C)$.
Let $H$ be the [[Hilbert space|HM2HHE3J51]] completion of $A_\infty$ for the inner product $\langle x, y \rangle = \tau(y^* x)$, and let $A_\infty$ act on $H$ by left multiplication.
Then $R$ is the closure of $A_\infty$ in the [[weak operator topology|4XM1VN1C1N]] on $H$.

## Remarks

The algebra $R$ is a factor: its center consists of scalars.
The trace $\tau$ extends to a faithful normal tracial state on $R$, and the values of $\tau$ on projections fill $[0, 1]$, so $R$ has type $\mathrm{II}_1$.
It is hyperfinite: it contains an increasing sequence of finite-dimensional subalgebras whose union is weakly dense.
Murray and von Neumann proved that a hyperfinite $\mathrm{II}_1$ factor with separable predual is unique up to isomorphism.
Connes proved that, among $\mathrm{II}_1$ factors with separable predual, $R$ is also the unique injective one.
Other constructions give the same factor, for example the group von Neumann algebra of the group of finitely supported permutations of $\N$.
Every type $\mathrm{II}_1$ factor contains a von Neumann subalgebra isomorphic to $R$.

## Explanations

### L1 human

Matrices of size $2 \times 2$, $4 \times 4$, $8 \times 8$, and so on, sit inside each other by repeating a matrix twice along the diagonal.
Measured with the normalized trace, which gives the identity size $1$, the projections in these algebras have sizes $k / 2^n$.
Taking a suitable limit of all of them gives the factor $R$, where projections can have any size between $0$ and $1$.
It is the simplest and most important example of an operator algebra with this "continuous dimension".
