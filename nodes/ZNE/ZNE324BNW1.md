---
tag: ZNE324BNW1
kind: proof
name: Proof that the exponential function is strictly convex
msc: [26A51]
proves: 0D7GRZ2ADX
uses: [0RMVS7RXZX, 0EX9GFJ0B3, 07ZMX4ANJS, 0BARQY52N5, 0KN2V7840E, 06BA5JZKTQ]
sources:
  - url: https://proofwiki.org/wiki/Real_Function_is_Strictly_Convex_iff_Derivative_is_Strictly_Increasing
    locator: Sufficient Condition
---

## Proof

We apply the mean value theorem on two adjacent intervals.

1. Let $x \ne y$ be real and let $t \in (0, 1)$. If we swap $x$ with $y$ and $t$ with $1 - t$, both sides of the claimed inequality stay the same. So we may assume $x < y$.
2. Let $z = t x + (1 - t) y$. Then $z - x = (1 - t)(y - x) > 0$ and $y - z = t (y - x) > 0$. So $x < z < y$.
3. The [[exponential function|0RMVS7RXZX]] is differentiable on $\mathbb{R}$ with [[derivative $e^x$|0EX9GFJ0B3]]. So it is also [[continuous|07ZMX4ANJS]].
4. By the [[mean value theorem|0BARQY52N5]] on $[x, z]$, there is $c_1 \in (x, z)$ with $e^z - e^x = e^{c_1} (z - x) = e^{c_1} (1 - t)(y - x)$.
5. By the mean value theorem on $[z, y]$, there is $c_2 \in (z, y)$ with $e^y - e^z = e^{c_2} (y - z) = e^{c_2} \, t (y - x)$.
6. Since $c_1 < z < c_2$ and the [[exponential function is strictly increasing|0KN2V7840E]], we have $e^{c_1} < e^{c_2}$.
7. Since $t + (1 - t) = 1$, we can write
   $$t e^x + (1 - t) e^y - e^z = (1 - t)(e^y - e^z) - t (e^z - e^x).$$
8. By steps 4 and 5, the right side equals $t (1 - t)(y - x)\big(e^{c_2} - e^{c_1}\big)$.
9. Each factor is positive, by step 6 and since $0 < t < 1$ and $x < y$. So $e^{t x + (1 - t) y} < t e^x + (1 - t) e^y$.
10. This holds for all $x \ne y$ and $t \in (0, 1)$. So the exponential function is [[strictly convex|06BA5JZKTQ]] on $\mathbb{R}$.

## Idea

The point $z$ splits $[x, y]$ into two pieces. By the mean value theorem, the slope of the graph over each piece is a value of $e^x$ inside that piece. Since $e^x$ is strictly increasing, the right slope is larger than the left slope, so the graph bends upward and lies strictly below the chord.
