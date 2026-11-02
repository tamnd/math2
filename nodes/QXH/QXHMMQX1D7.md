---
tag: QXHMMQX1D7
kind: statement
role: theorem
name: Castelnuovo's rationality criterion
msc: [14J26, "14E08"]
uses: [55A4A53TRF, KFTECAATKG, W05VYY4HBR, PQ6Q143ARJ, Y30JE2DC6Y]
about: [55A4A53TRF]
sources:
  - url: https://en.wikipedia.org/wiki/Rational_surface
---

## Statement

Let $X$ be a smooth projective [[algebraic surface|KFTECAATKG]] over an algebraically closed field, with [[canonical divisor|W05VYY4HBR]] $K_X$.
Let $q = \dim H^1(X, \mathcal{O}_X)$ be its irregularity, in the sense of [[sheaf cohomology|PQ6Q143ARJ]], and let $P_2 = \dim H^0(X, \mathcal{O}_X(2K_X))$ be its second plurigenus.
If $q = 0$ and $P_2 = 0$, then $X$ is a [[rational surface|55A4A53TRF]].

## Remarks

The converse holds as well, since $q$ and $P_2$ are birational invariants and both vanish for $\mathbb{P}^2$.
Castelnuovo proved it over $\C$, and Zariski extended it to positive characteristic.
The proof passes to a minimal model and uses Riemann–Roch on the surface to show that $K_X$ is not nef.
A minimal surface with this property is $\mathbb{P}^2$ or a ruled surface, and $q = 0$ makes the base curve of the ruling rational.
The plurigenus $P_2$ cannot be replaced by the geometric genus $p_g = h^0(K_X)$: an [[Enriques surface|Y30JE2DC6Y]] has $q = p_g = 0$ but $P_2 = 1$, and it is not rational.
Example: over $\C$ a unirational surface $X$ is dominated by $\mathbb{P}^2$.
Pulling back forms shows that $q$ and $P_2$ of $X$ are at most those of $\mathbb{P}^2$, which vanish.
Hence every complex unirational surface is rational.

## Explanations

### L1 human

Deciding whether a surface can be parametrized by the plane seems hard, since one would have to find the parametrization.
Castelnuovo's criterion replaces this by two numbers that can be computed: the number of independent holomorphic $1$-forms and the number of independent sections of twice the canonical bundle.
If both are zero, the surface is rational.

### L2 human

The criterion is the key step in the classification of surfaces of Kodaira dimension $-\infty$.
It shows that, for surfaces over $\C$, the Lüroth problem has a positive answer: unirational implies rational.
This fails in dimension three, where there are unirational threefolds that are not rational, and it fails for surfaces in positive characteristic.
The Enriques surface shows that the weaker condition $q = p_g = 0$ is not enough.
