---
tag: AMP0CRE14P
kind: statement
role: theorem
name: Existence of best approximations from finite-dimensional subspaces
msc: [41A65, 41A50, 46B20]
uses: [7N4988HN3P, 03J5RAKB30, 00YC1D652K, 03GSZ8RTZJ]
about: [7N4988HN3P]
sources:
  - url: https://en.wikipedia.org/wiki/Approximation_theory
---

## Statement

Let $X$ be a real or complex [[normed vector space|03J5RAKB30]], and let $V \subseteq X$ be a [[linear subspace|00YC1D652K]] of finite [[dimension|03GSZ8RTZJ]].
Then every $x \in X$ has a [[best approximation|7N4988HN3P]] from $V$: there is $v^* \in V$ with
$$\norm{x - v^*} = \inf_{v \in V} \norm{x - v}.$$

## Remarks

The idea of the proof: the point $0 \in V$ has distance $\norm{x}$ from $x$, so it suffices to minimize over $B = \set{v \in V : \norm{v} \le 2 \norm{x}}$, since every $v \notin B$ has $\norm{x - v} \ge \norm{v} - \norm{x} > \norm{x}$.
In a finite-dimensional normed space closed bounded sets are compact, so $B$ is compact.
The continuous function $v \mapsto \norm{x - v}$ attains its minimum on $B$.

Example: for $f \in C[a, b]$ with the supremum norm and $V$ the polynomials of degree at most $n$, a best uniform approximation by polynomials of degree at most $n$ exists.
The same holds for trigonometric polynomials, for splines with fixed knots, and in every $L^p$ norm.

Finite dimension is needed.
In the space $c_0$ of null sequences with the supremum norm, the functional $\varphi(y) = \sum_{k \ge 1} 2^{-k} y_k$ has norm $1$ but $\abs{\varphi(y)} < \norm{y}_\infty$ for every $y \ne 0$.
Its kernel is a closed subspace, and no point outside the kernel has a best approximation from it.

The best approximation need not be unique: in $\R^2$ with the maximum norm, all points $(t, 0)$ with $\abs{t} \le 1$ are best approximations of $(0, 1)$ from the horizontal axis.

## Explanations

### L1 human

When the approximating family depends on finitely many parameters, such as the coefficients of a polynomial of degree $n$, a best choice always exists.
The reason is compactness: only a bounded region of parameters is worth searching, and in finitely many dimensions a continuous function attains its minimum on a closed bounded region.

### L2 human

This is the basic existence result of linear approximation theory, and every concrete problem with a fixed degree, such as minimax polynomial approximation, starts from it.
The questions that follow are uniqueness, which needs extra structure such as strict convexity or the Haar condition, and characterization, given by the Kolmogorov criterion and the equioscillation theorem.
In a Hilbert space the result holds for every closed subspace, by the projection theorem, but in general Banach spaces infinite-dimensional closed subspaces may fail to have best approximations.
