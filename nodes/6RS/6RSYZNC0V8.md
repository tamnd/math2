---
tag: 6RSYZNC0V8
kind: proof
name: Proof that the orthogonal projection is the closest point
msc: [46C05, 65F20]
proves: 0MCDDSCB9Z
uses: [0VGSYBWHV2, 0KG4D8AP6G, 0Q8HZTJC7G, 079D68S3AW, 0TS7VZJBWD, 0BVTDM872V]
sources:
  - url: https://linear.axler.net/LADR4e.pdf
    locator: Theorem 6.61
---

## Proof

We write $v - w$ as a sum of two orthogonal vectors and apply the Pythagorean theorem.

1. Let $V$ be an inner product space over $\R$ or $\C$, with [[inner product|0VGSYBWHV2]] $\ip{\cdot}{\cdot}$ and [[induced norm|0KG4D8AP6G]] $\norm{\cdot}$. Let $W$ be a finite-dimensional subspace, let $v \in V$ and let $w \in W$.
2. By the definition of the [[orthogonal projection|0Q8HZTJC7G]], $v = P_W(v) + w'$ with $P_W(v) \in W$ and $w' = v - P_W(v) \in W^\perp$. Here $W^\perp$ is the [[orthogonal complement|079D68S3AW]].
3. Set $a = v - P_W(v)$ and $b = P_W(v) - w$. Then $v - w = a + b$.
4. Since $W$ is a subspace and $P_W(v), w \in W$, we have $b \in W$. Since $a \in W^\perp$, we get $\ip{a}{b} = 0$. So $a$ and $b$ are [[orthogonal|0TS7VZJBWD]].
5. By the [[Pythagorean theorem|0BVTDM872V]], $\norm{v - w}^2 = \norm{a}^2 + \norm{b}^2$.
6. Since $\norm{b}^2 \ge 0$, this gives $\norm{v - w}^2 \ge \norm{a}^2 = \norm{v - P_W(v)}^2$.
7. Both norms are nonnegative, and the square root is increasing on $[0, \infty)$. So $\norm{v - P_W(v)} \le \norm{v - w}$.
8. Suppose equality holds. Then the squares are equal, and step 5 gives $\norm{b}^2 = 0$.
9. So $\ip{b}{b} = 0$, and positivity of the inner product gives $b = 0$. That is, $w = P_W(v)$.
10. Conversely, if $w = P_W(v)$, then both sides equal $\norm{v - P_W(v)}$. So equality holds only for $w = P_W(v)$.

## Idea

Going from $v$ to a point $w$ of $W$ can be done in two legs: first from $v$ to $P_W(v)$, then inside $W$ to $w$. The first leg is orthogonal to $W$, so the two legs are at a right angle. By Pythagoras, the detour through $P_W(v)$ is longer unless the second leg is zero.
