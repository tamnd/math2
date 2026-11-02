---
tag: ZP4AWD45CE
kind: conjecture
name: Volume conjecture
msc: [57K16, 57K32, 57K14]
uses: [QYEAZTYGPT, K47G2Q24DT, 4SPC17FPXE, GHVW1Z35BS]
about: [4SPC17FPXE, K47G2Q24DT]
sources:
  - url: https://en.wikipedia.org/wiki/Volume_conjecture
same_as:
  wikidata: Q7940887
  wikipedia: Volume conjecture
history:
  posed_by: "Rinat Kashaev"
  first_stated: "1997"
---

## Statement

Let $K$ be a [[hyperbolic knot|K47G2Q24DT]] in $S^3$, so that its complement $S^3 \setminus K$ is a [[hyperbolic 3-manifold|GHVW1Z35BS]] of finite volume $\mathrm{Vol}(S^3 \setminus K)$.
For $N \ge 2$, let $J_N(K; q)$ be the $N$-th colored [[Jones polynomial|4SPC17FPXE]] of $K$, normalised so that its value on the unknot is $1$.
The conjecture states that
$$\lim_{N \to \infty} \frac{2\pi}{N} \log \abs{J_N\left(K; e^{2\pi i / N}\right)} = \mathrm{Vol}(S^3 \setminus K).$$

## Remarks

Kashaev formulated the conjecture in 1997 for invariants he had built from the quantum dilogarithm.
H. Murakami and J. Murakami showed that Kashaev's invariant equals $J_N(K; e^{2\pi i / N})$.
They extended the conjecture to all knots, with the simplicial volume of the complement in place of the hyperbolic volume.
The conjecture is open in general.
It has been verified for the figure-eight knot and for a few other hyperbolic knots.
It would imply that a knot whose colored Jones polynomials all agree with those of the unknot has a complement of simplicial volume zero.

## Explanations

### L1 human

The colored Jones polynomials of a knot come from algebra and quantum physics.
The volume of the knot complement comes from hyperbolic geometry.
The conjecture says that the growth rate of the first, evaluated at special roots of unity, is exactly the second.
It would be a deep bridge between quantum invariants and geometry.
