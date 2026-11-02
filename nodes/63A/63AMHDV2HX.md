---
tag: 63AMHDV2HX
kind: definition
name: Principal series representation
msc: ["22E46", 22D30]
defines: CWDF4KGHS3
uses: [42ZCE14AD2, Z2FEBW5MQM, BM3TWJ0D4P, T2EB8R9HEV, 6Q7AHAZ6Q4, FX3NEFYFFN]
sources:
  - url: https://en.wikipedia.org/wiki/Principal_series_representation
---

## Definition

Let $G$ be a [[real reductive Lie group|42ZCE14AD2]] with [[maximal compact subgroup|T2EB8R9HEV]] $K$.
Let $P$ be a minimal [[parabolic subgroup|Z2FEBW5MQM]] of $G$ with [[Langlands decomposition|BM3TWJ0D4P]] $P = MAN$, and let $\mathfrak a$ be the Lie algebra of $A$.
Let $\rho \in \mathfrak a^*$ be half the sum of the roots of $\mathfrak a$ in the Lie algebra of $N$, counted with multiplicity.
For $a \in A$ and $\lambda \in \mathfrak a^*_\C$, write $a^\lambda = e^{\lambda(\log a)}$.
Let $\sigma$ be an [[irreducible|FX3NEFYFFN]] unitary representation of $M$ on $V_\sigma$, and let $\nu \in \mathfrak a^*_\C$.
The *principal series representation* $I(\sigma, \nu) = \mathrm{Ind}_P^G(\sigma \otimes e^\nu \otimes 1)$ acts on the space of measurable functions $f \colon G \to V_\sigma$ such that
$$f(x m a n) = a^{-(\nu + \rho)} \sigma(m)^{-1} f(x) \qquad (x \in G, \ m \in M, \ a \in A, \ n \in N)$$
and $\int_K \norm{f(k)}^2 \, dk < \infty$, by left translation $(I(\sigma, \nu)(g) f)(x) = f(g^{-1} x)$.

## Remarks

The shift by $\rho$ makes $I(\sigma, \nu)$ unitary when $\nu \in i \mathfrak a^*$; these are the unitary principal series.
Every function in the space is determined by its restriction to $K$, because $G = KP$ by the Iwasawa decomposition.

Example: for $G = \mathrm{SL}_2(\R)$, let $P$ be the upper triangular matrices, so $M = \set{\pm 1}$, $A$ is the positive diagonal matrices and $N$ the unipotent upper triangular ones.
Here $\rho(\log \operatorname{diag}(t, t^{-1})) = \log t$, so $\operatorname{diag}(t, t^{-1})^\rho = t$.
The restriction to $K = \mathrm{SO}(2)$ identifies the space with the functions on the circle that are even or odd according to $\sigma(-1) = \pm 1$.
So each character $e^{in\theta}$ of $K$ with $(-1)^n = \sigma(-1)$ occurs once, and $I(\sigma, \nu)$ is admissible.

Non-example: inducing the trivial representation from the compact subgroup $K$ instead of from $P$ gives the representation of $G$ on $L^2(G/K)$.
It is not a principal series representation: $K$ is not parabolic, and the representation is not even admissible.

Some authors call representations induced from any parabolic subgroup, with discrete series or tempered data on $M$, generalised principal series.
