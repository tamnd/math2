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

1. Let $V$ be an inner product space over $\R$ or $\C$, with [[inner product|0VGSYBWHV2]] $\ip{\cdot}{\cdot}$ and [[induced norm|0KG4D8AP6G]] $\norm{\cdot}$. Let $U$ be a finite-dimensional subspace, let $v \in V$ and let $u \in U$.
2. By the definition of the [[orthogonal projection|0Q8HZTJC7G]], $v = P_U v + a$ with $P_U v \in U$ and $a = v - P_U v$ in the [[orthogonal complement|079D68S3AW]] $U^\perp$.
3. Set $b = P_U v - u$. Then $v - u = a + b$.
4. Since $U$ is a subspace and $P_U v, u \in U$, we have $b \in U$. Since $a \in U^\perp$, we get $\ip{a}{b} = 0$. So $a$ and $b$ are [[orthogonal|0TS7VZJBWD]].
5. By the [[Pythagorean theorem|0BVTDM872V]], $\norm{v - u}^2 = \norm{a}^2 + \norm{b}^2$.
6. Since $\norm{b}^2 \ge 0$, this gives $\norm{v - u}^2 \ge \norm{a}^2 = \norm{v - P_U v}^2$. Both norms are nonnegative, so $\norm{v - P_U v} \le \norm{v - u}$. This proves part 1.
7. Suppose equality holds. Then step 5 gives $\norm{b}^2 = 0$, and positivity gives $b = 0$, that is, $u = P_U v$. Conversely, $u = P_U v$ gives equality. This proves part 2.
8. Part 3, forward direction: if $u_0$ is a closest point, then $u_0 = P_U v$ by part 2, and $v - u_0 = a \in U^\perp$ by step 2.
9. Part 3, backward direction: if $u_0 \in U$ and $v - u_0 \in U^\perp$, then $v = u_0 + (v - u_0)$ is a splitting with parts in $U$ and $U^\perp$. By the uniqueness in the [[orthogonal decomposition|0SP7P0G7KQ]], $u_0 = P_U v$, which is the closest point by part 1.
10. Part 4: by parts 1 and 2 the minimum exists and equals $\norm{v - P_U v}$.
11. $P_U v \in U$ and $v - P_U v \in U^\perp$ are orthogonal, so the Pythagorean theorem gives $\norm{v}^2 = \norm{P_U v}^2 + \norm{v - P_U v}^2$. Hence $d(v, U)^2 = \norm{v}^2 - \norm{P_U v}^2$.
12. By the [[projection formulas|AK3JJ5HHG2]], $P_U v = \sum_i \ip{v}{e_i} e_i$. The $e_i$ are orthonormal, so the Pythagorean theorem for $k$ orthogonal terms gives $\norm{P_U v}^2 = \sum_i \abs{\ip{v}{e_i}}^2$. This proves part 4.

## Idea

Going from $v$ to a point $u$ of $U$ can be done in two legs: first from $v$ to $P_U v$, then inside $U$ to $u$.
The first leg is orthogonal to $U$, so the two legs are at a right angle.
By Pythagoras, the detour through $P_U v$ is longer unless the second leg is zero.

## Variants

A calculus proof: for $u \in U$ and $h \in U$, the function $t \mapsto \norm{v - u - t h}^2$ is a quadratic polynomial in real $t$.
At a minimum its derivative at $t = 0$ is $0$, which gives $\operatorname{Re} \ip{v - u}{h} = 0$ for all $h \in U$.
Over $\C$, replacing $h$ by $ih$ also gives $\operatorname{Im} \ip{v - u}{h} = 0$, and so $v - u \in U^\perp$.
