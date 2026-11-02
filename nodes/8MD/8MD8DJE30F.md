---
tag: 8MD8DJE30F
kind: statement
role: theorem
name: Uniform convergence of Bernstein approximations
msc: [41A10, 41A36, 41A25]
uses: [0C4VWBFY73, 08FPABDQ4C, 0Q4DR37DVE, AXCJBSQZWF]
about: [0JT92VK307, XAARVNKXF1]
sources:
  - url: https://en.wikipedia.org/wiki/Bernstein_polynomial
---

## Statement

Let $f \colon [0, 1] \to \R$ be continuous, and for $n \ge 1$ let $B_n(f)$ be its $n$-th [[Bernstein polynomial|0C4VWBFY73]],
$$B_n(f)(x) = \sum_{k=0}^{n} f\Big( \frac{k}{n} \Big) \binom{n}{k} x^k (1 - x)^{n-k}.$$
Then $B_n(f) \to f$ [[uniformly|08FPABDQ4C]] on $[0, 1]$ as $n \to \infty$.

## Remarks

The idea of the proof: the weights $\binom{n}{k} x^k (1 - x)^{n-k}$ are nonnegative and sum to $1$, so $B_n(f)(x) - f(x)$ is an average of $f(k/n) - f(x)$.
By [[uniform continuity|0Q4DR37DVE]], the terms with $\abs{k/n - x} < \delta$ contribute less than $\varepsilon$.
The weights are binomial probabilities with mean $x$ and variance $x(1 - x)/n \le 1/(4n)$, so by Chebyshev's inequality the remaining terms carry total weight at most $1/(4 n \delta^2)$, and they contribute at most $2 \norm{f}_\infty / (4 n \delta^2)$.

Example: $B_n$ reproduces $1$ and $x$, and $B_n(x^2) = x^2 + x(1 - x)/n$, so $\norm{B_n(x^2) - x^2}_\infty = 1/(4n)$.
This shows that the convergence is slow: of order $1/n$ even for a polynomial.
More generally $\norm{B_n(f) - f}_\infty$ is bounded by a constant multiple of the [[modulus of continuity|AXCJBSQZWF]] $\omega(f, n^{-1/2})$.

Continuity is needed: for the step function $f = 0$ on $[0, 1/2]$ and $f = 1$ on $(1/2, 1]$, each $B_n(f)$ is continuous, so the convergence cannot be uniform.
The result gives a constructive proof of the [[Weierstrass approximation theorem|0JQE130DHW]].

## Explanations

### L1 human

The Bernstein polynomial of $f$ samples $f$ at the points $0, 1/n, 2/n, \dots, 1$ and blends these values with smooth weights.
The theorem says that as you take more sample points, the blended curve hugs the graph of $f$ everywhere on $[0, 1]$.
This gives an explicit polynomial close to any continuous function.

### L2 human

The proof is the model for the theory of positive linear operators.
The operator $B_n$ is linear and maps nonnegative functions to nonnegative functions.
It is exact on $1$ and $x$, with a small error on $x^2$.
Korovkin's theorem shows that these three facts alone force uniform convergence.
Bernstein polynomials also preserve shape: if $f$ is monotone or convex, so is $B_n(f)$, which is why they appear in computer graphics as Bézier curves.
The price is the slow rate, which cannot beat order $1/n$ for nonlinear smooth $f$.
