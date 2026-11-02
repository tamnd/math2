---
tag: TZYSW0975T
kind: concept
name: Fourier monomial on the circle
msc: [42A16, 43A40]
sources:
  - url: https://en.wikipedia.org/wiki/Fourier_series
---

## Summary

The Fourier monomials are the functions $e_n(x) = e^{inx}$, $n \in \Z$, viewed as functions on the circle $\mathbb{T} = \R / 2\pi\Z$.
They are the continuous homomorphisms from the [[circle group|04EAFVFTF7]] to the unit circle of $\C$, that is, the characters of the circle.
They form an [[orthonormal basis|0S9GGTR0EX]] of $L^2(\mathbb{T})$, and the coefficients of a function in this basis are its [[Fourier coefficients|5NN2YZZR3V]].

## Explanations

### L1 human

The monomial $e_n$ runs around the unit circle of the complex plane $n$ times while $x$ runs once from $0$ to $2\pi$.
For $n$ negative it runs in the opposite direction, and $e_0$ is the constant $1$.
Its real and imaginary parts are the pure waves $\cos nx$ and $\sin nx$.
Every [[trigonometric polynomial|J3NJQ5FZJ5]] is a finite combination of these monomials, as an ordinary polynomial is a combination of powers.
For example, $e_2 \cdot e_{-3} = e_{-1}$, because exponents add.
