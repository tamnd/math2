---
tag: 462AEY7MWF
kind: statement
role: theorem
name: Regula falsi
msc: [65H05]
uses: [TR4CNS5PMJ, 0X3WGX95FE, 00KAFBR32E, 0VW90BBSJ4, 0Q4QJWEHW3, YWZQC5E54B]
about: [TR4CNS5PMJ]
sources:
  - url: https://en.wikipedia.org/wiki/Regula_falsi
same_as:
  wikidata: Q1476057
  wikipedia: Regula falsi
---

## Statement

Let $a < b$ be real numbers and let $f \colon [a, b] \to \R$ be a [[continuous function|0X3WGX95FE]] with $f(a) f(b) < 0$.
The *regula falsi* (method of false position) sets $a_0 = a$, $b_0 = b$, and for $k \ge 0$ lets
$$c_k = \frac{a_k f(b_k) - b_k f(a_k)}{f(b_k) - f(a_k)},$$
the zero of the chord through $(a_k, f(a_k))$ and $(b_k, f(b_k))$.
If $f(c_k) = 0$ it stops; if $f(a_k) f(c_k) < 0$ it sets $(a_{k+1}, b_{k+1}) = (a_k, c_k)$; otherwise it sets $(a_{k+1}, b_{k+1}) = (c_k, b_k)$.

1. As long as the method runs, $a_k < c_k < b_k$ and $f(a_k) f(b_k) < 0$, so each $[a_k, b_k]$ contains a zero of $f$.
2. Assume moreover that $f$ is [[twice continuously differentiable|0VW90BBSJ4]] on $[a, b]$ with [[second derivative|0Q4QJWEHW3]] $f'' > 0$, and $f(a) < 0 < f(b)$. Then $f$ has exactly one zero $r$ in $(a, b)$, $b_k = b$ for all $k$, the sequence $(c_k)$ increases strictly to $r$, and
$$\lim_{k \to \infty} \frac{r - c_{k+1}}{r - c_k} = 1 - \frac{f'(r)(b - r)}{f(b)} \in (0, 1).$$

## Remarks

Clause 1: the chord has values of opposite signs at $a_k$ and $b_k$, so its zero $c_k$ lies strictly between them.
The update keeps a sign change, and the [[intermediate value theorem|00KAFBR32E]] gives a zero in each bracket.
Clause 2: by convexity the chord lies above the graph, so $f(c_k) < 0$ and $c_k$ always replaces the left endpoint.
Then $c_{k+1} = g(c_k)$ with $g(x) = x - f(x)(b - x)/(f(b) - f(x))$.
The increasing bounded sequence $(c_k)$ has a limit, which is a fixed point of $g$, hence $r$, and the error ratio tends to $g'(r)$.
So under the hypotheses of clause 2 the method converges only linearly, see [[rate of convergence|YWZQC5E54B]], and the bracket width $b - c_k$ does not tend to $0$.
Example: for $f(x) = x^2 - 2$ on $[1, 2]$, $c_0 = 4/3$, $c_1 = 7/5$, $c_2 = 24/17 \approx 1.41176$, increasing to $\sqrt{2}$ with $b = 2$ fixed, and the limit ratio is $1 - 2\sqrt{2}(2 - \sqrt{2})/2 = 3 - 2\sqrt{2} \approx 0.17$.
The other cases of fixed sign of $f''$ and of $f(a)$ follow by replacing $f(x)$ by $-f(x)$ or by $f(-x)$; then the other endpoint stays fixed.

## Explanations

### L1 human

Like bisection, regula falsi keeps an interval on which the function changes sign.
Instead of cutting the interval in the middle, it draws the straight line between the two end values and cuts where that line crosses zero.
This is often a much better guess than the midpoint.
But when the graph bends the same way throughout, one endpoint never moves and progress can become slow.

### L2 human

Regula falsi is a bracketing [[root-finding algorithm|TR4CNS5PMJ]] like the bisection method, and it uses the same chord formula as the secant method.
The secant method uses the two most recent points instead of the two bracketing ones; it loses the guarantee of a bracket but converges superlinearly near a simple zero.
The fixed-endpoint problem of clause 2 led to modified versions such as the Illinois algorithm.
It halves the stored function value at an endpoint that stays fixed twice in a row.
