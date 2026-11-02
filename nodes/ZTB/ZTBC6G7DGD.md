---
tag: ZTBC6G7DGD
kind: statement
role: theorem
name: Faber's theorem on interpolation
msc: [41A05, 41A10]
uses: [7V7KWNK9HN, 237KR6FRCK, 0X3WGX95FE, 08VZ57PT26]
about: [7V7KWNK9HN]
sources:
  - url: https://en.wikipedia.org/wiki/Lebesgue_constant
---

## Statement

Let $a < b$.
For each $n \ge 0$, let $x_{n,0} < x_{n,1} < \cdots < x_{n,n}$ be $n + 1$ points of $[a, b]$.
For a [[continuous function|0X3WGX95FE]] $f$ on $[a, b]$, let $p_n(f)$ be the [[Lagrange interpolation|237KR6FRCK]] polynomial of degree at most $n$ that agrees with $f$ at $x_{n,0}, \dots, x_{n,n}$.
Then there is a continuous function $f$ on $[a, b]$ such that $p_n(f)$ does not [[converge uniformly|08VZ57PT26]] to $f$ on $[a, b]$.

## Remarks

Proof idea: the norm of the interpolation map $f \mapsto p_n(f)$ on $C[a, b]$ is the [[Lebesgue constant|7V7KWNK9HN]] $\Lambda_n$ of the $n$-th row of nodes.
For every choice of nodes, $\Lambda_n \ge c \log n$ for some constant $c > 0$, so $\Lambda_n \to \infty$.
By the uniform boundedness principle, $\sup_n \norm{p_n(f)}_\infty = \infty$ for some continuous $f$, and for this $f$ the sequence $p_n(f)$ cannot converge uniformly.

Example: for Chebyshev nodes $\Lambda_n$ grows only like $\frac{2}{\pi} \log n$, which is slow but still unbounded.
So even interpolation at Chebyshev nodes fails for some continuous function, although it converges for every Lipschitz function.

The theorem concerns one fixed array of nodes for all functions.
For each single continuous $f$ there is an array of nodes for which $p_n(f) \to f$ uniformly, for example nodes where $f$ meets its best approximations.

## Explanations

### L1 human

No fixed recipe for choosing interpolation points works for every continuous function.
Whatever points are chosen, some continuous function makes the interpolating polynomials fail to converge to it.
This contrasts with the Weierstrass approximation theorem, which says that good polynomial approximations always exist.

### L2 human

Faber's theorem separates existence of good approximations from their construction by interpolation.
It is a typical application of the uniform boundedness principle with norms that grow like a logarithm, as for divergent Fourier series of continuous functions.
In practice it is mild: for Chebyshev nodes, Lebesgue's lemma gives convergence as soon as $\omega(f, 1/n) \log n \to 0$.
