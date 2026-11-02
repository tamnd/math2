---
tag: J2XK2WAHBG
kind: definition
name: Sparse approximation
msc: [41A46, 94A12, 65F50]
defines: WC8P971XGW
uses: [0VD9ZSWWJG, 0GT4WWGWH2]
sources:
  - url: https://en.wikipedia.org/wiki/Sparse_approximation
---

## Definition

Let $A$ be an $m \times N$ real or complex [[matrix|0VD9ZSWWJG]], usually with $m < N$, let $b \in \mathbb{K}^m$ with $\mathbb{K} = \R$ or $\C$, and let $\norm{\cdot}_2$ be the Euclidean norm.
For $x \in \mathbb{K}^N$, let $\norm{x}_0$ be the number of nonzero entries of $x$; the vector $x$ is *$s$-sparse* if $\norm{x}_0 \le s$.
*Sparse approximation* is either of the two following problems.

1. Given an integer $s \ge 1$, find an $s$-sparse $x$ that minimizes $\norm{Ax - b}_2$.
2. Given a tolerance $\varepsilon \ge 0$, find $x$ with $\norm{Ax - b}_2 \le \varepsilon$ that minimizes $\norm{x}_0$.

For $\varepsilon = 0$, the second problem asks for the sparsest solution of the [[system of linear equations|0GT4WWGWH2]] $Ax = b$.

## Remarks

The count $\norm{x}_0$ is not a norm, since $\norm{2x}_0 = \norm{x}_0$; the notation is standard anyway.
Example: let $A = \begin{pmatrix} 1 & 0 & 1 \\ 0 & 1 & 1 \end{pmatrix}$, $b = (1, 1)$ and $\varepsilon = 0$.
The vector $x = (0, 0, 1)$ solves $Ax = b$ with $\norm{x}_0 = 1$, and no $x$ with $\norm{x}_0 = 0$ works since $b \ne 0$, so it solves problem 2.
Non-example: $x = (1, 1, 0)$ also solves $Ax = b$, but $\norm{x}_0 = 2$ is not minimal, so it is not a solution of problem 2.
Replacing $\norm{x}_0$ by the convex norm $\norm{x}_1 = \sum_j \abs{x_j}$ gives basis pursuit, a linear program; a penalized form of it is the [[Lasso|KZ226116HW]].
