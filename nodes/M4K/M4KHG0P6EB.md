---
tag: M4KHG0P6EB
kind: proof
name: Proof of Fermat's theorem on stationary points
msc: [26A24]
proves: 0PCVBRV9VJ
uses: [00999TYPXB, 0NS8BP96QX, 0F1WR9C83K, 000MXHEY22, 0N32V0E3XJ, 0WH916TJNY, 09G6KHS6GY, 0Z9JB71BS0]
sources:
  - url: https://en.wikipedia.org/wiki/Interior_extremum_theorem
    locator: Proof
---

## Proof

We treat a local maximum first, using one-sided sequences of difference quotients.

1. Suppose $f$ has a [[local maximum|00999TYPXB]] at $a$. Then there is $\delta > 0$ with $f(x) \le f(a)$ for all $x \in I$ with $\abs{x - a} < \delta$.
2. Since $I$ is an open interval containing $a$, we may shrink $\delta$ so that $(a - \delta, a + \delta) \subseteq I$.
3. For $h \ne 0$ with $a + h \in I$, write $q(h) = \frac{f(a + h) - f(a)}{h}$. By the definition of the [[derivative|0F1WR9C83K]], $q(h) \to f'(a)$ as $h \to 0$.
4. For $0 < h < \delta$, the numerator of $q(h)$ is $\le 0$ and $h > 0$. So $q(h) \le 0$.
5. For $-\delta < h < 0$, the numerator is $\le 0$ and $h < 0$. So $q(h) \ge 0$.
6. Put $h_n = \frac{\delta}{n + 2}$ for $n \in \N$. Then $0 < h_n < \delta$. Also $h_n \to 0$, by [[this lemma|0WH916TJNY]] and the [[epsilon-N form|09G6KHS6GY]].
7. By the [[sequential characterization of limits|000MXHEY22]], $q(h_n) \to f'(a)$. By step 4 and [[limits preserve non-strict inequalities|0N32V0E3XJ]], compared with the constant sequence $0$, $f'(a) \le 0$.
8. The sequence $-h_n$ also tends to $0$, with $-\delta < -h_n < 0$. In the same way, step 5 gives $f'(a) \ge 0$.
9. So $f'(a) = 0$ at a local maximum.
10. Now suppose $f$ has a [[local minimum|0NS8BP96QX]] at $a$. Then $-f$ has a local maximum at $a$, since $f(x) \ge f(a)$ means $-f(x) \le -f(a)$.
11. By the [[constant multiple rule|0Z9JB71BS0]] with $c = -1$, $-f$ is differentiable at $a$ with derivative $-f'(a)$.
12. Steps 1 to 9 for $-f$ give $-f'(a) = 0$. So $f'(a) = 0$.

## Idea

At a local maximum, moving right does not increase $f$, so the difference quotients on the right are at most $0$. Moving left also does not increase $f$, but now we divide by a negative $h$, so those quotients are at least $0$. The derivative is the limit from both sides, so it is $0$.
