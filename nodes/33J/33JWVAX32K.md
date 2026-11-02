---
tag: 33JWVAX32K
kind: definition
name: Quermassintegral
msc: [52A39, 52A38]
defines: H1K36H9ZWB
uses: [QB3Q5FBJ08, 437FSG3419, 0Q0H13G8ZB]
sources:
  - url: https://en.wikipedia.org/wiki/Mixed_volume
---

## Definition

Let $n \ge 1$, let $K$ be a nonempty compact convex subset of $\R^n$ (a [[convex body|437FSG3419]]), and let $B$ be the [[closed unit ball|0Q0H13G8ZB]] of $\R^n$.
For $j = 0, 1, \dots, n$, the $j$-th *quermassintegral* of $K$ is
$$W_j(K) = V(\underbrace{K, \dots, K}_{n - j}, \underbrace{B, \dots, B}_{j}),$$
where $V$ is the [[mixed volume|QB3Q5FBJ08]].

## Remarks

By the [[Steiner formula|F02XA3MYX8]], $\operatorname{vol}(K + tB) = \sum_{j=0}^n \binom{n}{j} W_j(K)\, t^j$ for $t \ge 0$.
Special values: $W_0(K) = \operatorname{vol}(K)$, $n W_1(K)$ is the surface area of $K$, and $W_n(K) = \kappa_n$, the volume of $B$.
Also $W_{n-1}(K) = \frac{\kappa_n}{2} w(K)$, where $w(K)$ is the mean width of $K$.
For $1 \le k \le n$, $W_{n-k}(K)$ equals $\kappa_n / \kappa_k$ times the average, over all $k$-dimensional linear subspaces $E$, of the $k$-dimensional volume of the orthogonal projection of $K$ onto $E$; this is Kubota's formula.

Example: $K = rB$, a ball of radius $r \ge 0$.
By multilinearity, $W_j(rB) = r^{n-j} V(B, \dots, B) = \kappa_n r^{n-j}$.
For $n = 2$ and $r = 1$ this gives $W_1 = \pi$, half the perimeter $2\pi$, as expected.

Non-example: the set $K = \set{0, 1} \subseteq \R$ is not convex, so its mixed volumes are not defined.
Indeed the length of $K + tB$ is $4t$ for $t \le \frac12$ and $1 + 2t$ for $t \ge \frac12$, not one polynomial in $t$.
