---
tag: PAXJGJYDE3
kind: definition
name: Intrinsic volume
msc: [52A39, 52A22]
defines: C2CK6KSSTV
uses: [H1K36H9ZWB, 437FSG3419]
sources:
  - url: https://en.wikipedia.org/wiki/Hadwiger's_theorem
---

## Definition

Let $n \ge 1$ and let $K$ be a nonempty compact convex subset of $\R^n$ (a [[convex body|437FSG3419]]).
For $m \ge 0$ let $\kappa_m$ be the volume of the closed unit ball of $\R^m$, so $\kappa_0 = 1$, $\kappa_1 = 2$, $\kappa_2 = \pi$.
For $j = 0, 1, \dots, n$, the $j$-th *intrinsic volume* of $K$ is
$$V_j(K) = \binom{n}{j} \frac{W_{n-j}(K)}{\kappa_{n-j}},$$
where $W_{n-j}$ is the $(n-j)$-th [[quermassintegral|H1K36H9ZWB]].

## Remarks

Equivalently, with $B$ the closed unit ball, the Steiner formula reads
$$\operatorname{vol}(K + tB) = \sum_{j=0}^n \kappa_{n-j} V_j(K)\, t^{n-j} \quad (t \ge 0).$$
Special values: $V_n(K) = \operatorname{vol}(K)$, $V_{n-1}(K)$ is half the surface area, and $V_0(K) = 1$.
If $K$ lies in a $k$-dimensional affine subspace, then $V_j(K)$ is the same whether computed in $\R^n$ or in that subspace, and $V_j(K) = 0$ for $j > k$.

Example: the unit square $K = [0,1]^2$ in $\R^2$.
Its parallel body has area $1 + 4t + \pi t^2$, and the formula above gives $V_2(K) + 2 V_1(K)\, t + \pi V_0(K)\, t^2$.
So $V_2(K) = 1$, $V_1(K) = 2$ (half the perimeter) and $V_0(K) = 1$.

Non-example: $K = \set{0, 1} \subseteq \R$ is compact but not convex.
The length of $K + tB$ is $4t$ for $t \le \frac12$ and $1 + 2t$ for $t \ge \frac12$, which is not one polynomial, so there are no intrinsic volumes of $K$ in this sense.
