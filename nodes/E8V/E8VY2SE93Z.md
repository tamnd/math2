---
tag: E8VY2SE93Z
kind: definition
name: Fourier monomial on the circle
msc: [42A16, 43A40]
defines: TZYSW0975T
uses: [04EAFVFTF7, 07GJV36896]
sources:
  - url: https://en.wikipedia.org/wiki/Fourier_series
---

## Definition

Let $\mathbb{T} = \R / 2\pi\Z$ be the circle, and write $[x]$ for the class of $x \in \R$ in $\mathbb{T}$.
For $n \in \Z$, the *Fourier monomial* of index $n$ is the function $e_n \colon \mathbb{T} \to \C$ given by
$$e_n([x]) = e^{inx},$$
where $e^{inx}$ is the [[complex exponential|07GJV36896]].

## Remarks

The function is well defined: if $x' = x + 2\pi k$ with $k \in \Z$, then $e^{inx'} = e^{inx} e^{2\pi i nk} = e^{inx}$.
It is continuous, takes values of absolute value $1$, and satisfies $e_n e_m = e_{n+m}$ and $e_n(s + t) = e_n(s) e_n(t)$.
So each $e_n$ is a continuous homomorphism from $\mathbb{T}$ to the [[circle group|04EAFVFTF7]], and every continuous homomorphism of this kind is one of the $e_n$.
For the inner product $\langle f, g \rangle = \frac{1}{2\pi} \int_{-\pi}^{\pi} f(x) \overline{g(x)} \, dx$, one has $\langle e_n, e_m \rangle = 1$ if $n = m$ and $0$ otherwise.
Example: $e_3([x]) = e^{3ix} = \cos 3x + i \sin 3x$.
Non-example: $x \mapsto e^{ix/2}$ is not a function on $\mathbb{T}$, since $x = 0$ and $x = 2\pi$ give the same point of $\mathbb{T}$ but the values $1$ and $-1$.
On the circle $\R / T\Z$ of length $T > 0$, the Fourier monomials are $x \mapsto e^{2\pi i n x / T}$.
