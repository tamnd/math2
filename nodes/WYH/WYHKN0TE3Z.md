---
tag: WYHKN0TE3Z
kind: definition
name: Majorization
msc: [26D15, 15B51]
defines: 5K7VT2VKZT
uses: [JJA90EB2PS]
sources:
  - url: https://en.wikipedia.org/wiki/Majorization
---

## Definition

Let $n \ge 1$ and let $x, y \in \R^n$.
Write $x^{\downarrow}$ for the vector with the entries of $x$ in decreasing order, so $x^{\downarrow}_1 \ge x^{\downarrow}_2 \ge \cdots \ge x^{\downarrow}_n$.
The vector $x$ *majorizes* $y$, written $y \prec x$, if:

1. $\sum_{i=1}^{k} y^{\downarrow}_i \le \sum_{i=1}^{k} x^{\downarrow}_i$ for each $k = 1, \ldots, n - 1$.
2. $\sum_{i=1}^{n} y_i = \sum_{i=1}^{n} x_i$.

## Remarks

Example: $y = (\frac{1}{2}, \frac{1}{2}, 0) \prec x = (1, 0, 0)$.
Check: $\frac{1}{2} \le 1$ for $k = 1$, $1 \le 1$ for $k = 2$, and both sums equal $1$.
Non-example: $(1, 0) \not\prec (2, 0)$, because clause 1 holds but the sums $1$ and $2$ differ, so clause 2 fails.
The relation is a preorder: $y \prec x$ and $x \prec y$ hold together exactly when $y$ is a permutation of $x$.
By a theorem of Hardy, Littlewood and Pólya, $y \prec x$ if and only if $y = Dx$ for some $n \times n$ [[doubly stochastic matrix|JJA90EB2PS]] $D$.
