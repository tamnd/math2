---
tag: AW16MYJV5Q
kind: example
name: Menshov's set of multiplicity of measure zero
msc: [42A63]
illustrates: [K7CNWXF9SN]
uses: [K7CNWXF9SN, FZK2M8KGXQ, VQQM4Y550T, DYR1QFNGNJ]
sources:
  - url: https://en.wikipedia.org/wiki/Set_of_uniqueness
---

## Example

Let $\mathbb{T} = \R / 2\pi\Z$.
In 1916 Menshov constructed a closed set $E \subset \mathbb{T}$ of Lebesgue measure zero that is a set of multiplicity.
So there is a [[trigonometric series|FZK2M8KGXQ]] $\sum_{n \in \Z} c_n e^{inx}$, with coefficients not all $0$, whose symmetric partial sums converge to $0$ at every point outside $E$.

The construction gives a nonzero positive [[Borel measure|DYR1QFNGNJ]] $\mu$ supported on a perfect [[null set|VQQM4Y550T]] $E$ whose Fourier–Stieltjes coefficients $\hat\mu(n) = \frac{1}{2\pi} \int e^{-inx} \, d\mu(x)$ tend to $0$ as $\abs{n} \to \infty$.
The series $\sum_n \hat\mu(n) e^{inx}$ then converges to $0$ at every point outside the support of $\mu$.
This follows from Riemann's principle of localization for series with coefficients tending to $0$.
Its coefficients are not all $0$, since $\hat\mu(0) = \mu(\mathbb{T}) / 2\pi > 0$.
Hence $E$ is not a [[set of uniqueness|K7CNWXF9SN]].

## Remarks

The example shows that measure zero is necessary but not sufficient for a closed set to be a set of uniqueness.
A measure whose Fourier coefficients tend to $0$ is called a Rajchman measure, and its closed support is always a set of multiplicity by the same argument.
Whether a set of measure zero is a set of uniqueness can depend on fine arithmetic properties of the set.

## Explanations

### L1 human

Cantor showed that a trigonometric series that is $0$ everywhere must be the zero series, and later this was extended to series that are $0$ outside a countable set.
One might guess that any exceptional set of total length zero is harmless.
Menshov showed that this guess is wrong: he built a set of length zero and a nonzero series that is $0$ everywhere outside it.
The series hides all of its non-zero behaviour on a tiny, dust-like set.
