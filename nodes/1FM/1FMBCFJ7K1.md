---
tag: 1FMBCFJ7K1
kind: definition
name: Simpson's rule
msc: [65D32, 41A55, 65D30]
defines: MNXC26G3BQ
uses: [ADSVMCY77A, BQPQAY1FDJ, ZYT1JNT1Y0]
sources:
  - url: https://en.wikipedia.org/wiki/Simpson%27s_rule
---

## Definition

Let $a < b$, let $f \colon [a, b] \to \R$ be continuous, and let $m = (a + b)/2$.
*Simpson's rule* is the [[quadrature rule|ADSVMCY77A]]
$$S(f) = \frac{b - a}{6} \big( f(a) + 4 f(m) + f(b) \big).$$
For an even integer $N \ge 2$, let $h = (b - a)/N$ and $x_i = a + i h$.
The *composite Simpson's rule* is
$$S_N(f) = \frac{h}{3} \Big( f(x_0) + 4 f(x_1) + 2 f(x_2) + 4 f(x_3) + \cdots + 2 f(x_{N-2}) + 4 f(x_{N-1}) + f(x_N) \Big),$$
the sum of $S$ over the subintervals $[x_{2j}, x_{2j+2}]$.

## Remarks

$S$ is the closed [[Newton–Cotes formula|BQPQAY1FDJ]] with $n = 2$, and its [[degree of exactness|ZYT1JNT1Y0]] is $3$, one more than the degree of the interpolating parabola, by symmetry.
Example: for $f(x) = x^3$ on $[0, 1]$, $S(f) = \frac{1}{6}\big(0 + \frac{1}{2} + 1\big) = \frac{1}{4} = \int_0^1 x^3\, dx$.
Non-example of exactness: for $f(x) = x^4$ on $[0, 1]$, $S(f) = \frac{1}{6}\big(0 + \frac{1}{4} + 1\big) = \frac{5}{24}$, while the integral is $\frac{1}{5}$; so the degree is not $4$.
If $f$ has a continuous fourth derivative, then $\int_a^b f - S_N(f) = -\frac{(b - a) h^4}{180} f^{(4)}(\xi)$ for some $\xi \in [a, b]$.
For $x^4$ on $[0, 1]$ with $N = 2$ this gives $-\frac{1}{16 \cdot 180} \cdot 24 = -\frac{1}{120}$, matching $\frac{1}{5} - \frac{5}{24}$.
