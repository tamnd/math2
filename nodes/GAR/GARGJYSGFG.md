---
tag: GARGJYSGFG
kind: statement
role: theorem
name: Poisson summation formula
msc: [42A38, 43A25]
uses: [CG9JEATW3Q, DPVM34ADZV, G12KXDHPPS]
about: [DPVM34ADZV]
sources:
  - url: https://en.wikipedia.org/wiki/Poisson_summation_formula
same_as:
  wikidata: Q387743
  wikipedia: Poisson summation formula
---

## Statement

Let $f \colon \R \to \C$ be a function in the [[Schwartz space|CG9JEATW3Q]].
Let $\widehat{f}(\xi) = \int_\R f(x) e^{-2\pi i x \xi} \, dx$ be its [[Fourier transform|DPVM34ADZV]].
Then
$$\sum_{n \in \Z} f(n) = \sum_{k \in \Z} \widehat{f}(k),$$
and both series converge absolutely.

## Remarks

The proof periodises $f$: the function $F(x) = \sum_{n \in \Z} f(x + n)$ is smooth and has period $1$.
Its [[Fourier coefficients|G12KXDHPPS]] are $\int_0^1 F(x) e^{-2\pi i k x} \, dx = \widehat{f}(k)$, so its Fourier series $\sum_k \widehat{f}(k) e^{2\pi i k x}$ converges to $F(x)$, and $x = 0$ gives the formula.
Example: for $t > 0$ and $f(x) = e^{-\pi t x^2}$ one has $\widehat{f}(\xi) = t^{-1/2} e^{-\pi \xi^2 / t}$, and the formula gives $\sum_{n} e^{-\pi t n^2} = t^{-1/2} \sum_{k} e^{-\pi k^2/t}$, the transformation law of the Jacobi theta function.
The Schwartz hypothesis can be weakened, but some decay and regularity of $f$ and $\widehat{f}$ is needed for both sides to converge to the same value.
Let $G$ be a locally compact abelian group and $H$ a discrete subgroup with $G/H$ compact.
A similar formula then holds, with the sum on the right over the characters of $G$ trivial on $H$.
It needs suitable conditions on $f$ and a suitable normalisation of the Haar measures.

## Explanations

### L1 human

Sample a function at the integers and add up the values.
The formula says that one gets the same total by sampling the Fourier transform at the integers and adding those values.
A function that is spread out has a transform that is concentrated, so one side can be hard to compute while the other side is easy.

### L2 human

The formula is the basic link between a lattice and its dual lattice; in $\R^n$ it reads $\sum_{v \in L} f(v) = \frac{1}{\operatorname{vol}(\R^n/L)} \sum_{w \in L^*} \widehat{f}(w)$ for a lattice $L$ with dual lattice $L^*$.
Applied to Gaussians it gives the functional equation of theta functions, which leads to the functional equation of the Riemann zeta function.
In signal processing it underlies the sampling theorem, and in analytic number theory it is used to count lattice points.
