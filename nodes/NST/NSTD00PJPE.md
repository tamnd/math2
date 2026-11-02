---
tag: NSTD00PJPE
kind: statement
role: theorem
name: Fenchel–Young inequality
msc: [52A41, 26B25, 26D15]
uses: [T7V2VPY61S, 9C5WXYYQEK, 03J5RAKB30, 4A82S5FVRT, 0GSZ7B0CGR]
about: [T7V2VPY61S]
sources:
  - url: https://en.wikipedia.org/wiki/Convex_conjugate
    locator: Fenchel's inequality
---

## Statement

Let $X$ be a real [[normed space|03J5RAKB30]] with [[continuous dual space|4A82S5FVRT]] $X^*$.
Let $f \colon X \to (-\infty, +\infty]$ be a function that is not identically $+\infty$, and let $f^*$ be its [[Fenchel conjugate|T7V2VPY61S]].
Then for all $x \in X$ and $y \in X^*$,
$$f(x) + f^*(y) \ge y(x).$$
Moreover, let $x$ be a point with $f(x)$ finite.
Then equality holds if and only if $y$ is a subgradient of $f$ at $x$, that is, $f(z) \ge f(x) + y(z - x)$ for all $z \in X$.

## Remarks

Since $f$ is finite somewhere, $f^*$ never takes the value $-\infty$, so the left side is a well-defined element of $(-\infty, +\infty]$.
The proof is one line: $f^*(y) \ge y(x) - f(x)$ by the definition of $f^*$ as a supremum over $x$.
Equality means that $x$ attains this supremum, which is the subgradient inequality rearranged.
The set of subgradients is the [[subdifferential|9C5WXYYQEK]] $\partial f(x)$.

Example: for $p > 1$ and $q = p/(p - 1)$, the function $f(x) = \abs{x}^p / p$ on $\R$ has $f^*(y) = \abs{y}^q / q$.
The inequality becomes Young's inequality $xy \le \abs{x}^p/p + \abs{y}^q/q$, with equality exactly when $y = \sgn(x) \abs{x}^{p-1}$.
For $p = 2$ it is $xy \le \tfrac12 x^2 + \tfrac12 y^2$, which is $(x - y)^2 \ge 0$.

## Explanations

### L1 human

The conjugate $f^*$ is built so that this inequality holds: it is the smallest function with $f(x) + f^*(y) \ge xy$ for all $x$.
It generalizes the inequality $xy \le \tfrac12 x^2 + \tfrac12 y^2$ and Young's inequality for products.
Equality picks out the pairs where $y$ is a slope of $f$ at $x$.

### L2 human

The inequality gives weak duality in convex optimization: the value of a dual problem never exceeds the value of the primal problem.
Its equality case links the conjugate with the subdifferential: $y \in \partial f(x)$ if and only if $f(x) + f^*(y) = y(x)$.
For proper convex lower semicontinuous $f$, the Fenchel–Moreau theorem then gives the symmetric statement $x \in \partial f^*(y)$, so $\partial f^*$ is the inverse of $\partial f$.
It is the source of many classical inequalities obtained by choosing $f$.
