---
tag: 4GG7VRW0DY
kind: definition
name: Chern class
msc: [14C17, 57R20, 55R40]
defines: PAD37GKDPD
uses: [EQSHJPE7H8, P4DZM975BV, EBEF6PEK4N, 4HV4WTAX9P, 7JCF2TE3V5, FHV05ZK99F, V93Y0XYPZD]
sources:
  - url: https://en.wikipedia.org/wiki/Chern_class
---

## Definition

Let $X$ be a smooth [[quasi-projective variety|EQSHJPE7H8]] over a field, with [[Chow ring|4HV4WTAX9P]] $CH^\bullet(X)$ built from its [[Chow groups|EBEF6PEK4N]].
For an [[invertible sheaf|7JCF2TE3V5]] $L$ on $X$, let $c_1(L) \in CH^1(X)$ be the class of a [[Cartier divisor|FHV05ZK99F]] $D$ with $L \cong \mathcal{O}_X(D)$.
Let $E$ be a [[vector bundle|P4DZM975BV]] of rank $r$ on $X$.
Let $\pi \colon \mathbb{P}(E) \to X$ be the associated projective bundle, $\mathbb{P}(E) = \operatorname{Proj} \operatorname{Sym} E$, and let $\xi = c_1(\mathcal{O}_{\mathbb{P}(E)}(1)) \in CH^1(\mathbb{P}(E))$, where $\mathcal{O}_{\mathbb{P}(E)}(1)$ is the [[twisting sheaf|V93Y0XYPZD]].
Then $CH^\bullet(\mathbb{P}(E))$ is a free $CH^\bullet(X)$-module, through $\pi^*$, with basis $1, \xi, \ldots, \xi^{r-1}$.
The *Chern classes* $c_i(E) \in CH^i(X)$, for $0 \le i \le r$, are the unique classes with $c_0(E) = 1$ and
$$\sum_{i=0}^{r} (-1)^i \, \pi^* c_i(E) \, \xi^{r-i} = 0.$$
One sets $c_i(E) = 0$ for $i > r$, and the *total Chern class* is $c(E) = \sum_i c_i(E)$.

## Remarks

This is Grothendieck's definition.
The Chern classes satisfy the Whitney formula $c(E) = c(E') \, c(E'')$ for every exact sequence $0 \to E' \to E \to E'' \to 0$, and they are compatible with pullback.
Example: for a line bundle $L$, $\mathbb{P}(L) = X$ and $\mathcal{O}_{\mathbb{P}(L)}(1) = L$, so $\xi = c_1(L)$, and the relation $\xi - c_1(L) = 0$ agrees with the definition of $c_1(L)$ for invertible sheaves.
On $\mathbb{P}^n$ with hyperplane class $h$, the Euler sequence gives $c(T_{\mathbb{P}^n}) = (1 + h)^{n+1}$.
Non-example: the skyscraper sheaf $k(P)$ at a point $P$ of a curve is coherent but not locally free.
So it is not a vector bundle, and the definition does not apply to it directly.
Over $\C$, the cycle class map sends $c_i(E)$ to the topological Chern class $c_i(E) \in H^{2i}(X(\C), \Z)$.
