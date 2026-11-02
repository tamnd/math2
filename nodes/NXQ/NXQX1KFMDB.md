---
tag: NXQX1KFMDB
kind: statement
role: theorem
name: Fourier basis of L2 of the circle
msc: [42A16, 42A65, 46C05]
uses: [TZYSW0975T, SASP14MA1Z, HM2HHE3J51, 0S9GGTR0EX, KDRZKC9T1V]
about: [TZYSW0975T, 0S9GGTR0EX]
sources:
  - url: https://en.wikipedia.org/wiki/Fourier_series
---

## Statement

Let $\mathbb{T} = \R / 2\pi\Z$, and let $L^2(\mathbb{T})$ be the [[Lebesgue space|SASP14MA1Z]] of square integrable functions on $\mathbb{T}$, with the inner product
$$\langle f, g \rangle = \frac{1}{2\pi} \int_{-\pi}^{\pi} f(x) \overline{g(x)} \, dx.$$
For $n \in \Z$ let $e_n(x) = e^{inx}$ be the [[Fourier monomial|TZYSW0975T]] of index $n$.
Then the family $(e_n)_{n \in \Z}$ is an [[orthonormal basis|0S9GGTR0EX]] of the [[Hilbert space|HM2HHE3J51]] $L^2(\mathbb{T})$.

## Remarks

Orthonormality is a direct computation: $\langle e_n, e_m \rangle = \frac{1}{2\pi} \int_{-\pi}^{\pi} e^{i(n-m)x} \, dx$ is $1$ if $n = m$ and $0$ otherwise.
Completeness means that the linear span of the $e_n$ is dense in $L^2(\mathbb{T})$.
This span is the space of trigonometric polynomials; it is dense in $C(\mathbb{T})$ for the supremum norm by the [[density of trigonometric polynomials|KDRZKC9T1V]], and $C(\mathbb{T})$ is dense in $L^2(\mathbb{T})$.
Since $\norm{g}_2 \le \sup \abs{g}$, uniform approximation gives approximation in $L^2$.
The coordinates of $f$ in this basis are its Fourier coefficients $\hat f(n) = \langle f, e_n \rangle$.
Example: $\cos x = \frac{1}{2} e_1 + \frac{1}{2} e_{-1}$, and indeed $\norm{\cos}_2^2 = \frac{1}{2\pi} \int_{-\pi}^{\pi} \cos^2 x \, dx = \frac{1}{2} = \frac{1}{4} + \frac{1}{4}$.
With the normalised measure $dx / 2\pi$ the $e_n$ have norm $1$; with the measure $dx$ one uses $e_n / \sqrt{2\pi}$ instead.

## Explanations

### L1 human

The pure waves $e^{inx}$ act like perpendicular unit axes in an infinite-dimensional space of functions.
Every square integrable periodic function has coordinates along these axes, namely its Fourier coefficients.
Completeness says that no direction is missing: a function perpendicular to every wave is zero.

### L2 human

The theorem puts Fourier series inside Hilbert space theory.
General facts about orthonormal bases then give at once the convergence of Fourier series in $L^2$, Parseval's identity and the Riesz–Fischer theorem.
The map $f \mapsto (\hat f(n))_{n \in \Z}$ is a unitary isomorphism from $L^2(\mathbb{T})$ onto $\ell^2(\Z)$.
The same holds on the torus $\mathbb{T}^d$ with the monomials $e^{i k \cdot x}$, $k \in \Z^d$, and, by the Peter–Weyl theorem, on any compact abelian group with its characters.
