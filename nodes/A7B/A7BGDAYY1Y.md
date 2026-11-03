---
tag: A7BGDAYY1Y
kind: statement
role: theorem
name: Fourier inversion on abelian groups
msc: [43A25, 43A50]
uses: [ZR09S9R3AW, VY0HXD3GC4, FMW57WNPDB, VHN5VW5Q92, T4Z8YQZKZV]
about: [VHN5VW5Q92]
sources:
  - url: https://en.wikipedia.org/wiki/Pontryagin_duality
---

## Statement

Let $G$ be a [[locally compact abelian group|ZR09S9R3AW]] with a [[Haar measure|VY0HXD3GC4]] $\mu$, and let $\widehat{G}$ be its [[Pontryagin dual|FMW57WNPDB]].
For $f \in L^1(G)$ let $\widehat{f}(\chi) = \int_G f(x) \overline{\chi(x)} \, d\mu(x)$ be its [[Fourier transform|VHN5VW5Q92]].
Then there is a unique Haar measure $\nu$ on $\widehat{G}$, the dual measure of $\mu$, with the following property.
If $f \in L^1(G)$ and $\widehat{f} \in L^1(\widehat{G}, \nu)$, then
$$f(x) = \int_{\widehat{G}} \widehat{f}(\chi) \, \chi(x) \, d\nu(\chi)$$
for $\mu$-almost every $x \in G$.
If moreover $f$ is continuous, the equality holds for every $x \in G$.

## Remarks

Proof idea: one first treats the functions $f$ that are continuous and positive-definite, or finite combinations of them.
Bochner's theorem writes such an $f$ as $\int \chi(x)\, d\sigma_f(\chi)$ for a measure $\sigma_f$ on $\widehat{G}$.
One shows that $\sigma_f = \widehat{f}\, \nu$ for one Haar measure $\nu$ independent of $f$.
The general case follows by approximation with an approximate identity.

Examples with the usual normalisations follow.
For $G = \R$ with Lebesgue measure and $\chi_\xi(x) = e^{2\pi i \xi x}$, $\nu$ is Lebesgue measure, which gives the classical [[Fourier inversion theorem|T4Z8YQZKZV]].
For $G = \mathbb{T}$ with arc length divided by $2\pi$, $\nu$ is counting measure on $\Z$, and the formula is the Fourier series of $f$.
For $G = \Z/n\Z$ with counting measure, $\nu$ is counting measure divided by $n$.
This gives $f(a) = \frac{1}{n} \sum_{k} \widehat{f}(k) e^{2\pi i k a / n}$.

The hypothesis $\widehat{f} \in L^1$ is needed for the integral to make sense.
For $f = \mathbf{1}_{[-1/2, 1/2]}$ on $\R$, $\widehat{f}(\xi) = \sin(\pi\xi)/(\pi\xi)$ is not integrable.

## Explanations

### L1 human

A function on an abelian group can be rebuilt from its Fourier transform by adding up all the waves, each weighted by its Fourier coefficient.
The weights for the waves have to be measured in the right units, and the theorem says there is exactly one right choice of units on the dual group.

### L2 human

The dual measure ties together the normalisations on $G$ and $\widehat{G}$: if $\mu$ is multiplied by $c > 0$, then $\nu$ is divided by $c$.
With this choice the Fourier transform extends to a unitary map $L^2(G) \to L^2(\widehat{G})$, the Plancherel theorem.
A first consequence is uniqueness: if $f \in L^1(G)$ and $\widehat{f} = 0$, then $f = 0$ almost everywhere.
Inversion and the Plancherel theorem are the main steps in the usual proof of the Pontryagin duality theorem.
