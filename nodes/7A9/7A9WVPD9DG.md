---
tag: 7A9WVPD9DG
kind: definition
name: Restricted isometry property
msc: [94A12, 41A46, 15B52]
defines: B0K18PWN2A
uses: [0VD9ZSWWJG, 54T6Y6DSY4]
sources:
  - url: https://en.wikipedia.org/wiki/Restricted_isometry_property
---

## Definition

Let $A$ be a real or complex $m \times N$ [[matrix|0VD9ZSWWJG]] and let $1 \le s \le N$ be an integer.
A vector $x$ is *$s$-sparse* if it has at most $s$ nonzero entries; $\norm{\cdot}_2$ is the Euclidean norm.
The *restricted isometry constant* $\delta_s = \delta_s(A)$ is the smallest $\delta \ge 0$ such that
$$(1 - \delta) \norm{x}_2^2 \le \norm{Ax}_2^2 \le (1 + \delta) \norm{x}_2^2 \quad \text{for every $s$-sparse } x \in \mathbb{K}^N ,$$
where $\mathbb{K}$ is $\R$ or $\C$.
The matrix $A$ has the *restricted isometry property* of order $s$ with constant $\delta \in (0, 1)$ if $\delta_s(A) \le \delta$.

## Remarks

Equivalently, $\delta_s = \max_S \norm{A_S^* A_S - I}_{2 \to 2}$, where $S$ runs over the sets of at most $s$ column indices, $A_S$ keeps the columns in $S$, and the norm is the spectral [[matrix norm|54T6Y6DSY4]].
So $\delta_s$ bounds how far the eigenvalues of all the Gram matrices $A_S^* A_S$ are from $1$.
Example: if the columns of $A$ are orthonormal, then $\norm{Ax}_2 = \norm{x}_2$ for all $x$, so $\delta_s = 0$ for every $s$.
Non-example: suppose the first two columns of $A$ are equal.
Then $x = e_1 - e_2$ is $2$-sparse with $Ax = 0$, so the left inequality needs $\delta \ge 1$, and $A$ has no restricted isometry property of order $2$.
The constants increase with the order: $\delta_1 \le \delta_2 \le \cdots \le \delta_N$.
If $\delta_{2s} < 1$, then distinct $s$-sparse vectors have distinct images, since their difference is $2s$-sparse.
