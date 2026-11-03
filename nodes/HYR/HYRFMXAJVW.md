---
tag: HYRFMXAJVW
kind: concept
name: Laguerre series expansion of the Laplace transform
msc: [44A10, 33C45, 65R10]
sources:
  - url: https://en.wikipedia.org/wiki/Laguerre_polynomials
---

## Summary

The Laguerre series expansion writes the [[Laplace transform|0V49JEZW06]] $F(s)$ of a function, times $s + 1/2$, as a power series in $w = (s - 1/2)/(s + 1/2)$.
Here $w$ is a Möbius transformation of the transform variable $s$.
Its coefficients are the coefficients of the function in the orthonormal basis of Laguerre functions $e^{-t/2} L_n(t)$ of $L^2(0, \infty)$.
Here $L_n$ are the [[Laguerre polynomials|WAMRHWW82R]].
The expansion converts Laplace inversion into the computation of Taylor coefficients of an analytic function on the unit disk.
It is the basis of Weeks' method for the [[numerical inversion of the Laplace transform|41QNF4CGNY]].

## Explanations

### L1 human

The Laplace transform of each Laguerre function is very simple: a power of $(s - 1/2)$ divided by a power of $(s + 1/2)$.
So if a function is a sum of Laguerre functions, its Laplace transform is a sum of these simple terms.
The change of variable $w = (s - 1/2)/(s + 1/2)$ makes this sum an ordinary power series in $w$.
For example, $f(t) = e^{-t/2}$ is the first Laguerre function, and its transform $1/(s + 1/2)$ is the first term of the series.
To recover $f$ from its transform, one reads off the power series coefficients in $w$.
