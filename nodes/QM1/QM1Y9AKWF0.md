---
tag: QM1Y9AKWF0
kind: definition
name: Ellipsoid method
msc: [90C25, 90C05, 68Q25]
defines: TJR5MQHNYE
uses: [02AS45T3H9, 0KX66CZMBB, 9DMSG5HAQX]
sources:
  - url: https://en.wikipedia.org/wiki/Ellipsoid_method
---

## Definition

Let $n \ge 2$ and let $K \subseteq \R^n$ be a [[convex set|02AS45T3H9]].
Assume that $K$ is given by a *separation oracle*: for each $c \in \R^n$ it either states $c \in K$, or returns $a \in \R^n \setminus \set{0}$ with $a^T x \le a^T c$ for all $x \in K$.
For $c \in \R^n$ and a [[positive definite matrix|0KX66CZMBB]] $P$ of size $n \times n$, let $E(c, P) = \set{x \in \R^n : (x - c)^T P^{-1} (x - c) \le 1}$.
Assume that $K \subseteq E(c_0, P_0)$ for a given ellipsoid.
The *ellipsoid method* is the [[algorithm|9DMSG5HAQX]] that, for $k = 0, 1, 2, \dots$, runs these steps.

1. Query the oracle at $c_k$; if $c_k \in K$, stop and return $c_k$.
2. Otherwise, take the returned vector $a$ and set $b = P_k a / \sqrt{a^T P_k a}$.
3. Set $c_{k+1} = c_k - \frac{1}{n + 1} b$ and $P_{k+1} = \frac{n^2}{n^2 - 1} \bigl(P_k - \frac{2}{n + 1} b b^T\bigr)$.

Then $E(c_{k+1}, P_{k+1})$ is the ellipsoid of least volume containing the half-ellipsoid $E(c_k, P_k) \cap \set{x : a^T x \le a^T c_k}$, and so it contains $K$.

## Remarks

Example: let $n = 2$, $c_0 = 0$, $P_0 = I$, and let $K = \set{x : x_1 \ge 1/2,\ x_1^2 + x_2^2 \le 1}$.
The center $0$ is not in $K$, and $a = (-1, 0)$ separates it, since $-x_1 \le 0$ on $K$.
Then $b = (-1, 0)$, $c_1 = (1/3, 0)$ and $P_1 = \frac{4}{3}\bigl(I - \frac{2}{3} e_1 e_1^T\bigr) = \mathrm{diag}(4/9, 4/3)$.
The new ellipse has semi-axes $2/3$ and $2/\sqrt{3}$, and it passes through $(1, 0)$ and $(0, \pm 1)$.
Its center $(1/3, 0)$ is not in $K$ either, so the method goes on.

Non-example: if $K$ is not convex, a point outside $K$ need not be separated from $K$ by a hyperplane, so no separation oracle exists in general.

The volume satisfies $\mathrm{vol}\, E(c_{k+1}, P_{k+1}) < e^{-1/(2(n+1))}\, \mathrm{vol}\, E(c_k, P_k)$.
So if $K$ contains a ball of radius $r$ and $E(c_0, P_0)$ is a ball of radius $R$, the method finds a point of $K$ within $O(n^2 \log(R/r))$ steps.
