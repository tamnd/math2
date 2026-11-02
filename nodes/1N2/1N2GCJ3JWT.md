---
tag: 1N2GCJ3JWT
kind: definition
name: Bernstein–Bézier form
msc: [41A10, 65D17, 41A15]
defines: Z5Y0VH10YR
uses: [0C4VWBFY73, 1G0B73WPX8, 0KCQ9Y3QKA]
sources:
  - url: https://en.wikipedia.org/wiki/Bernstein_polynomial
---

## Definition

Let $a < b$ be real numbers and let $n \ge 0$ be an integer.
For $k = 0, \dots, n$ let
$$b_{k,n}^{[a,b]}(x) = \binom{n}{k} \left(\frac{x - a}{b - a}\right)^{k} \left(\frac{b - x}{b - a}\right)^{n-k}.$$
These $n + 1$ polynomials form a [[basis|0KCQ9Y3QKA]] of the space of real [[polynomials|1G0B73WPX8]] of degree at most $n$.
Let $p$ be a polynomial of degree at most $n$.
Its *Bernstein–Bézier form* on $[a, b]$ is its expansion
$$p(x) = \sum_{k=0}^{n} c_k\, b_{k,n}^{[a,b]}(x).$$
The uniquely determined numbers $c_0, \dots, c_n$ are its *Bézier coefficients* of degree $n$ on $[a, b]$.

## Remarks

On $[0, 1]$ the basis consists of the [[Bernstein basis polynomials|0C4VWBFY73]] $\binom{n}{k} x^k (1-x)^{n-k}$.
Since the basis functions are nonnegative on $[a, b]$ and sum to $1$, the values of $p$ on $[a, b]$ lie between $\min_k c_k$ and $\max_k c_k$, and $p(a) = c_0$, $p(b) = c_n$.
Example: on $[0, 1]$ with $n = 2$, $x = \tfrac{1}{2} \cdot 2x(1-x) + 1 \cdot x^2$, so $x$ has Bézier coefficients $0, 1/2, 1$.
Non-example: $p(x) = x^3$ has no Bernstein–Bézier form of degree $2$, since it is not a polynomial of degree at most $2$; one must take $n \ge 3$.
In several variables one uses barycentric coordinates $\lambda_0, \dots, \lambda_d$ of a simplex and the basis $\frac{n!}{\alpha_0! \cdots \alpha_d!} \lambda_0^{\alpha_0} \cdots \lambda_d^{\alpha_d}$ with $\abs{\alpha} = n$.
