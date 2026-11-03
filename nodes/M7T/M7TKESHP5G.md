---
tag: M7TKESHP5G
kind: statement
role: theorem
name: Poisson summation formula for abelian groups
msc: [43A25, 43A70]
uses: [ZR09S9R3AW, VY0HXD3GC4, FMW57WNPDB, VHN5VW5Q92, 0KYX2N69J0, YT42EZ7GQQ, NW3R4Q6WN9, A7BGDAYY1Y, GARGJYSGFG]
about: [VHN5VW5Q92]
sources:
  - url: https://en.wikipedia.org/wiki/Poisson_summation_formula
---

## Statement

Let $G$ be a [[locally compact abelian group|ZR09S9R3AW]], let $H$ be a closed subgroup, and let $H^\perp \subseteq \widehat{G}$ be its [[annihilator|YT42EZ7GQQ]] in the [[Pontryagin dual|FMW57WNPDB]].
Choose [[Haar measures|VY0HXD3GC4]] on $G$, $H$ and the [[quotient group|0KYX2N69J0]] $G/H$ related by [[Weil's quotient integral formula|NW3R4Q6WN9]].
Give $H^\perp \cong \widehat{G/H}$ the Haar measure dual to the one on $G/H$.
Let $f \in L^1(G)$ be continuous, with [[Fourier transform|VHN5VW5Q92]] $\widehat{f}$, and assume:

1. for each $x \in G$, the function $h \mapsto f(x + h)$ is integrable on $H$, and $x + H \mapsto \int_H f(x + h)\, dh$ is continuous on $G/H$;
2. the restriction of $\widehat{f}$ to $H^\perp$ is integrable on $H^\perp$.

Then
$$\int_H f(h) \, dh = \int_{H^\perp} \widehat{f}(\chi) \, d\chi.$$

## Remarks

Proof idea: let $F(x + H) = \int_H f(x + h)\, dh$.
By Weil's formula $F$ is integrable on $G/H$, and its Fourier transform at $\chi \in H^\perp = \widehat{G/H}$ is $\widehat{f}(\chi)$.
Since $F$ is continuous and $\widehat{F}$ is integrable, [[Fourier inversion|A7BGDAYY1Y]] holds at every point, and the point $0 + H$ gives the formula.

Example: $G = \R$ with Lebesgue measure, $H = \Z$ with counting measure, and $\chi_\xi(x) = e^{2\pi i \xi x}$.
Then $G/H$ is the circle of length $1$, $H^\perp = \set{\chi_k : k \in \Z}$ carries counting measure, and the formula is the classical [[Poisson summation formula|GARGJYSGFG]] $\sum_{n} f(n) = \sum_{k} \widehat{f}(k)$.
For $G = \Z/N\Z$ and $H$ the subgroup of multiples of $d$, where $d$ divides $N$, it is an identity between two finite sums.

Some hypotheses of this kind are needed.
For a continuous integrable $f$ on $\R$ alone, the series $\sum_k \widehat{f}(k)$ need not converge, and then the right side has no meaning.

## Explanations

### L1 human

Summing a function over a subgroup gives the same result as summing its Fourier transform over the waves that do not see the subgroup.
On the real line this says that the samples of a function at the integers add up to the samples of its transform at the integers.

### L2 human

The abstract form explains where the classical formula comes from: periodising $f$ over $H$ gives a function on $G/H$, whose Fourier coefficients are the values of $\widehat{f}$ on $H^\perp$.
With $G = \R^n$ and $H$ a lattice, $H^\perp$ is the dual lattice, which gives the theta function identities and the functional equation of the Riemann zeta function.
With $G$ the adeles of a number field and $H$ the field itself, the same formula is the starting point of Tate's thesis.
