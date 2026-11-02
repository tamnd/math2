---
tag: KDRZKC9T1V
kind: statement
role: theorem
name: Density of trigonometric polynomials in continuous functions
msc: [42A10, 41A50]
uses: [J3NJQ5FZJ5, 0X3WGX95FE, 0ATF6Q0633, 08VZ57PT26, 1P8D3MK79H, TPJZCSXSVN]
about: [J3NJQ5FZJ5]
sources:
  - url: https://en.wikipedia.org/wiki/Fourier_series
---

## Statement

Let $f \colon \R \to \C$ be a [[continuous function|0X3WGX95FE]] that is [[periodic|0ATF6Q0633]] with period $2\pi$, and let $\varepsilon > 0$.
Then there is a [[trigonometric polynomial|J3NJQ5FZJ5]] $T$ such that
$$\sup_{x \in \R} \abs{f(x) - T(x)} < \varepsilon.$$
Equivalently, the trigonometric polynomials are dense in the space $C(\mathbb{T})$ of continuous functions on $\mathbb{T} = \R / 2\pi\Z$ with the supremum norm.

## Remarks

One proof uses the [[Stone–Weierstrass theorem|1P8D3MK79H]] on the compact space $\mathbb{T}$.
The trigonometric polynomials form a subalgebra of $C(\mathbb{T})$ that contains the constants, is closed under complex conjugation, and separates points, since $e^{ix}$ is injective on $\mathbb{T}$.
Another proof is [[Fejér's theorem|TPJZCSXSVN]]: the Cesàro means of the Fourier series of $f$ are trigonometric polynomials that converge to $f$ [[uniformly|08VZ57PT26]].
The partial sums of the Fourier series of $f$ itself need not converge uniformly, and need not converge at all.
So the approximating polynomial is in general not a Fourier partial sum.
The periodicity hypothesis is necessary: every trigonometric polynomial $T$ satisfies $T(-\pi) = T(\pi)$, so the function $x$ on $[-\pi, \pi]$ cannot be approximated uniformly on that interval.
A consequence is that a continuous $2\pi$-periodic function whose Fourier coefficients all vanish is identically zero.

## Explanations

### L1 human

Every continuous periodic function can be imitated, as closely as one likes and at every point at once, by a finite sum of waves.
The number of waves needed grows as the required precision grows.
This is the periodic version of the Weierstrass theorem that continuous functions on an interval are uniform limits of polynomials.

### L2 human

The result is the basic density fact of Fourier analysis on the circle.
Since $C(\mathbb{T})$ is dense in $L^p(\mathbb{T})$ for $1 \le p < \infty$, the trigonometric polynomials are also dense in these spaces.
For $p = 2$ this gives the completeness of the Fourier monomials, so that they form an orthonormal basis of $L^2(\mathbb{T})$.
It also gives uniqueness: two continuous periodic functions with the same Fourier coefficients are equal.
The rate of approximation in terms of the modulus of continuity of $f$ is the subject of Jackson's theorems.
