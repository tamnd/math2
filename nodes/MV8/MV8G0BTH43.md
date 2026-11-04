---
tag: MV8G0BTH43
kind: proof
name: Proof that 1 + x is at most exp x
msc: [33B10, 26D15]
proves: 012C7GFF20
uses: [0RMVS7RXZX, 0EX9GFJ0B3, 0MH1WK89PP, 0M0TKFRX2A, 07ZMX4ANJS, 0KN2V7840E, 07J5X2T1ZX]
sources:
  - url: https://www.vaia.com/en-us/textbooks/math/a-first-course-in-real-analysis-2-edition/chapter-5/problem-8-prove-that-ex-geqslant-1x-for-all-x/
---

## Proof

We study the sign of the derivative of $g(x) = e^x - 1 - x$ on each side of $0$.

1. Let $g(x) = e^x - 1 - x$ for real $x$, where $e^x = \exp(x)$ is the [[exponential function|0RMVS7RXZX]]. The claim is that $g(x) \ge 0$, with equality only at $x = 0$.
2. From the series, $e^0 = 1$, so $g(0) = 0$.
3. By [[the derivative of exp|0EX9GFJ0B3]], the [[derivative of a polynomial|0MH1WK89PP]] and the [[linearity of differentiation|0M0TKFRX2A]], $g$ is differentiable on $\R$ and $g'(x) = e^x - 1$.
4. So $g$ is [[continuous|07ZMX4ANJS]] on $\R$.
5. Since $\exp$ is [[strictly increasing|0KN2V7840E]] and $e^0 = 1$, we have $g'(x) > 0$ for $x > 0$ and $g'(x) < 0$ for $x < 0$.
6. On $I = [0, \infty)$, the interior points are the $x > 0$, where $g'(x) > 0$. By the theorem on a [[positive derivative|07J5X2T1ZX]], $g$ is strictly increasing on $[0, \infty)$.
7. So for $x > 0$, $g(x) > g(0) = 0$.
8. Let $h = -g$. By linearity of differentiation, $h'(x) = 1 - e^x$, which is positive for $x < 0$ by step 5. Also $h$ is continuous by step 4.
9. On $I = (-\infty, 0]$, the interior points are the $x < 0$. By the theorem on a positive derivative, $h$ is strictly increasing on $(-\infty, 0]$.
10. So for $x < 0$, $h(x) < h(0) = 0$, that is, $g(x) > 0$.
11. By steps 2, 7 and 10, $g(x) \ge 0$ for all real $x$, with $g(x) = 0$ only for $x = 0$. So $1 + x \le e^x$, with equality if and only if $x = 0$.

## Idea

The function $e^x - 1 - x$ vanishes at $0$. Its derivative $e^x - 1$ is negative to the left of $0$ and positive to the right. So the function falls until $0$ and rises after it, and its only zero is at $0$.
