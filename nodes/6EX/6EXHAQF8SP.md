---
tag: 6EXHAQF8SP
kind: statement
role: theorem
name: Lévy–Steinitz theorem
msc: [40A05]
uses: [0HRJ2Y74T3, 0FBXFBZBH8, 0XPR1E85W0, 0M856Q1AMZ, 0W3K3QPEWT]
about: [0W1K48V5SG]
sources:
  - url: https://en.wikipedia.org/wiki/L%C3%A9vy%E2%80%93Steinitz_theorem
same_as:
  wikidata: Q2341004
  wikipedia: Lévy–Steinitz theorem
---

## Statement

Let $d \ge 1$ and let $(x_n)_{n \ge 0}$ be a sequence in the [[Euclidean space|0XPR1E85W0]] $\R^d$.
Let $S$ be the set of all $s \in \R^d$ such that some [[rearrangement|0HRJ2Y74T3]] $\sum_n x_{\sigma(n)}$ converges to $s$.
Let $\Gamma$ be the set of [[linear functionals|0M856Q1AMZ]] $f \colon \R^d \to \R$ such that $\sum_n \abs{f(x_n)} < \infty$.
If $S$ is not empty, then
$$S = s_0 + \set{v \in \R^d : f(v) = 0 \text{ for all } f \in \Gamma}$$
for any $s_0 \in S$.
In particular, $S$ is either empty or an [[affine subspace|0FBXFBZBH8]] of $\R^d$.

## Remarks

For $d = 1$ this is the [[Riemann rearrangement theorem|0E7VBYGFF7]].
If the series converges [[absolutely|0W3K3QPEWT]], then $\Gamma$ contains all functionals and $S$ is a single point.
If it converges conditionally, then $\Gamma = \set{0}$ and $S = \R$.
Example in $\R^2$: take $x_n = ((-1)^n/(n+1), 1/2^n)$.
The second coordinate converges absolutely, the first only conditionally, so $S$ is a horizontal line $\set{(t, 2) : t \in \R}$.
The proof is harder than in dimension one.
Its core is a lemma of Steinitz on finitely many vectors in $\R^d$ with sum zero.
They can be ordered so that every partial sum has norm at most $C_d$ times the largest norm of the vectors, where $C_d$ depends only on $d$.
In infinite-dimensional Banach spaces the conclusion can fail: the set of sums need not be an affine subspace.

## Explanations

### L1 human

Reordering a convergent series in the plane or in space can change its sum.
The theorem says that the possible sums always form a point, a line, a plane, or a higher flat piece of space.
The directions in which the sum cannot move are the directions in which the series converges absolutely.

### L2 human

The theorem extends Riemann's rearrangement theorem from $\R$ to $\R^d$.
The subspace of possible shifts is cut out by the functionals that make the series absolutely convergent.
It explains why unconditional convergence and absolute convergence coincide in $\R^d$: the set $S$ is a single point exactly when every functional is in $\Gamma$.
