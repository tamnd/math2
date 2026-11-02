---
tag: C1T9VYKNV1
kind: definition
name: Bredon cohomology
msc: [55N91, 55P91]
defines: YN280Q5G49
uses: [0WCY42EV9V, 5W95QFHXPR, W4DG4WCQ5W, 082GHNPJ53]
sources:
  - url: https://en.wikipedia.org/wiki/Bredon_cohomology
---

## Definition

Let $G$ be a discrete group.
The *orbit category* $\mathcal{O}_G$ has as objects the left $G$-sets $G/H$ for subgroups $H \le G$, and as morphisms the $G$-equivariant maps.
A *coefficient system* is a contravariant [[functor|28NQ0KRHD3]] $M \colon \mathcal{O}_G \to \mathrm{Ab}$ to [[abelian groups|082GHNPJ53]].

Let $X$ be a $G$-CW complex, that is, a [[CW complex|5W95QFHXPR]] with a cellular [[action|0WCY42EV9V]] of $G$.
It is required that each element of $G$ that maps a cell to itself fixes that cell pointwise.
For each subgroup $H$, the fixed set $X^H$ is a subcomplex.
For $n \ge 0$, let $\underline{C}_n(X)$ be the contravariant functor $\mathcal{O}_G \to \mathrm{Ab}$ given by $G/H \mapsto C_n(X^H)$, the [[cellular chains|W4DG4WCQ5W]] of $X^H$.
A $G$-map $G/H \to G/K$ with $H \mapsto gK$ acts by $C_n(X^K) \to C_n(X^H)$, $c \mapsto g c$.
The cellular boundary maps make $\underline{C}_\bullet(X)$ a chain complex of functors.
The *Bredon cochain complex* is
$$C^n_G(X; M) = \operatorname{Nat}(\underline{C}_n(X), M),$$
the group of [[natural transformations|KYCPCC57FT]], with coboundary induced by the boundary of $\underline{C}_\bullet(X)$.
The *Bredon cohomology* $H^n_G(X; M)$ is the $n$-th cohomology of $C^\bullet_G(X; M)$.

## Remarks

Example: let $X$ be a point with the trivial action.
Then $X^H$ is a point for every $H$, so $\underline{C}_0(X)$ is the constant functor $\Z$ and $\underline{C}_n(X) = 0$ for $n > 0$.
A natural transformation from the constant functor $\Z$ to $M$ is fixed by its value at $G/G$, the terminal object of $\mathcal{O}_G$.
So $H^0_G(\mathrm{pt}; M) \cong M(G/G)$ and $H^n_G(\mathrm{pt}; M) = 0$ for $n > 0$.

If $G$ acts freely on $X$ and $M$ is the constant functor with value $A$, then $X^H$ is empty for $H \neq 1$ and $H^n_G(X; M) \cong H^n(X/G; A)$.

Non-example: a family of groups $M(G/H)$ with maps going in the covariant direction is not a coefficient system for this cohomology.
Covariant functors on $\mathcal{O}_G$ are the coefficients of Bredon homology instead.
