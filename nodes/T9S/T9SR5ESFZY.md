---
tag: T9SR5ESFZY
kind: definition
name: Fourier transform on finite groups
msc: [43A30, 20C15, 43A25]
defines: G7968MRFNH
uses: [G5S1M9, FX3NEFYFFN, 0AR68JTMDT, 2Z29JN3VES, FPRA2KEHFF, TST0GH66A5]
sources:
  - url: https://en.wikipedia.org/wiki/Fourier_transform_on_finite_groups
---

## Definition

Let $G$ be a finite [[group|G5S1M9]], and let $\widehat{G}$ be a set of representatives of the isomorphism classes of [[irreducible|FX3NEFYFFN]] complex representations of $G$.
Write each $\rho \in \widehat{G}$ as a homomorphism $\rho \colon G \to U(d_\rho)$ into the group of $d_\rho \times d_\rho$ [[unitary matrices|0AR68JTMDT]].
The *Fourier transform* of a function $f \colon G \to \C$ is the family of matrices
$$\widehat{f}(\rho) = \sum_{a \in G} f(a)\, \rho(a), \qquad \rho \in \widehat{G}.$$

## Remarks

The transform is inverted by
$$f(a) = \frac{1}{\abs{G}} \sum_{\rho \in \widehat{G}} d_\rho \, \tr\big(\rho(a^{-1})\, \widehat{f}(\rho)\big).$$
For the [[convolution|2Z29JN3VES]] $(f * g)(a) = \sum_{b \in G} f(b)\, g(b^{-1}a)$ one has $\widehat{f * g}(\rho) = \widehat{f}(\rho)\, \widehat{g}(\rho)$.

Example: let $f = \delta_e$ be $1$ at the identity and $0$ elsewhere.
Then $\widehat{f}(\rho)$ is the identity matrix for each $\rho$.
The inversion formula gives $\frac{1}{\abs{G}}\sum_\rho d_\rho \chi_\rho(a^{-1})$, where $\chi_\rho = \tr \rho$, and this is the character of the regular representation divided by $\abs{G}$, which is $1$ at $a = e$ and $0$ elsewhere.

If $G$ is abelian, every $\rho$ has $d_\rho = 1$, so $\widehat{G}$ is the [[character group|FPRA2KEHFF]] and $\widehat{f}(\chi) = \sum_{a} f(a) \chi(a)$ is a function on it.
For $G = \Z/n\Z$ and $\chi_k(a) = e^{2\pi i k a / n}$, this is the [[discrete Fourier transform|TST0GH66A5]] up to the sign in the exponent.
Many texts use $\rho(a)^*$, or $\overline{\chi(a)}$, in place of $\rho(a)$, and the formulas above change accordingly.

Non-example: the regular representation of $G$ is reducible when $\abs{G} > 1$, so it is not one of the $\rho \in \widehat{G}$.
The sum $\sum_a f(a) \rho(a)$ is still defined for it, but it repeats the information of the irreducible pieces, and the inversion formula above does not use it.
