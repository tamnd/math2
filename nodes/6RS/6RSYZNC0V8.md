---
tag: 6RSYZNC0V8
kind: proof
name: Proof of the best approximation theorem
msc: [46C05, 65F20]
topics: [8GQVME4SZZ]
audience: ug1
proves: 0MCDDSCB9Z
uses: [0VGSYBWHV2, 0KG4D8AP6G, 0Q8HZTJC7G, 079D68S3AW, 0TS7VZJBWD, 0BVTDM872V, AK3JJ5HHG2, 0SP7P0G7KQ]
methods: [0NTF6DMVAP, TFQ1845T84]
sources:
  - url: https://linear.axler.net/LADR4e.pdf
    locator: Theorem 6.61
  - book: isbn:9783031410253
    locator: Section 6C
---

## Proof

We write $v - u$ as a sum of two orthogonal vectors and apply the Pythagorean theorem.
Let $V$ be an inner product space over $\R$ or $\C$, with [[inner product|0VGSYBWHV2]] $\ip{\cdot}{\cdot}$ and [[induced norm|0KG4D8AP6G]] $\norm{\cdot}$, let $U$ be a finite-dimensional subspace, and let $v \in V$.

1. By the definition of the [[orthogonal projection|0Q8HZTJC7G]], $v = P_U v + a$ with $P_U v \in U$ and $a = v - P_U v$ in the [[orthogonal complement|079D68S3AW]] $U^\perp$.
2. Let $u \in U$ and set $b = P_U v - u$, so that $v - u = a + b$.
3. Both $P_U v$ and $u$ lie in the subspace $U$, so $b \in U$, and since $a \in U^\perp$ we get $\ip{a}{b} = 0$, so $a$ and $b$ are [[orthogonal|0TS7VZJBWD]].
4. The [[Pythagorean theorem|0BVTDM872V]] gives
$$\norm{v - u}^2 = \norm{a}^2 + \norm{b}^2.$$
5. Since $\norm{b}^2 \ge 0$, this gives $\norm{v - u}^2 \ge \norm{a}^2 = \norm{v - P_U v}^2$, and since both norms are nonnegative, $\norm{v - P_U v} \le \norm{v - u}$, which is part 1.
6. If equality holds, step 4 gives $\norm{b}^2 = 0$, and positivity of the inner product gives $b = 0$, that is, $u = P_U v$; since $u = P_U v$ gives equality, this is part 2.
7. For the forward direction of part 3, if $u_0$ is a closest point, then $u_0 = P_U v$ by part 2, and $v - u_0 = a \in U^\perp$ by step 1.
8. For the backward direction, if $u_0 \in U$ and $v - u_0 \in U^\perp$, then $v = u_0 + (v - u_0)$ is a splitting with parts in $U$ and $U^\perp$, so the uniqueness in the [[orthogonal decomposition|0SP7P0G7KQ]] gives $u_0 = P_U v$, the closest point by part 1.
9. For part 4, parts 1 and 2 show that the minimum exists and equals $\norm{v - P_U v}$.
10. The vectors $P_U v \in U$ and $v - P_U v \in U^\perp$ are orthogonal, so the Pythagorean theorem gives $\norm{v}^2 = \norm{P_U v}^2 + \norm{v - P_U v}^2$, and hence $d(v, U)^2 = \norm{v}^2 - \norm{P_U v}^2$.
11. By the [[projection formulas|AK3JJ5HHG2]], $P_U v = \sum_i \ip{v}{e_i} e_i$, and since the $e_i$ are orthonormal, the Pythagorean theorem for $k$ orthogonal terms gives $\norm{P_U v}^2 = \sum_i \abs{\ip{v}{e_i}}^2$, which completes part 4.

## Idea

To go from $v$ to a point $u$ of $U$, we can travel in two legs: first from $v$ to $P_U v$, and then inside $U$ from $P_U v$ to $u$.
The first leg is orthogonal to $U$ and the second lies in $U$, so the two legs meet at a right angle.
By Pythagoras, the straight path from $v$ to $u$ is the hypotenuse, and it is longer than the first leg unless the second leg has length zero.

## Variants

A calculus proof finds the same condition.
For $u, h \in U$, the function $f(t) = \norm{v - u - t h}^2$ of a real variable $t$ is a quadratic polynomial,
$$f(t) = \norm{v - u}^2 - 2t \operatorname{Re} \ip{v - u}{h} + t^2 \norm{h}^2.$$
If $u$ is a closest point, $f$ has a minimum at $t = 0$, so $f'(0) = -2 \operatorname{Re} \ip{v - u}{h} = 0$ for all $h \in U$.
Over $\C$, replacing $h$ by $ih$ also gives $\operatorname{Im} \ip{v - u}{h} = 0$, and so $v - u \in U^\perp$.
This proves the forward direction of part 3 without knowing in advance that a closest point is $P_U v$, but existence still needs the projection.
