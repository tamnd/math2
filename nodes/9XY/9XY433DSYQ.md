---
tag: 9XY433DSYQ
kind: proof
name: Proof that monotone functions are Riemann integrable
msc: [26A42]
proves: 04YKAYDQPW
uses: [0WFF6AZPBP, 0QRQVH0CRW, 0A3GWZ86AY, 017DH8WXTE]
sources:
  - url: https://www.math.ucdavis.edu/~hunter/m125b/ch1.pdf
    locator: Theorem 1.21
---

## Proof

We compute the Darboux sums for a partition into equal pieces and use Riemann's criterion.

1. Let $a < b$ and let $f \colon [a, b] \to \mathbb{R}$ be [[monotone|0WFF6AZPBP]]. First assume that $f$ is increasing, that is, $x \le y$ implies $f(x) \le f(y)$.
2. Then $f(a) \le f(x) \le f(b)$ for all $x \in [a, b]$. So $f$ is bounded, and its [[Darboux sums|0QRQVH0CRW]] are defined.
3. Let $\varepsilon > 0$. By the [[Archimedean property|0A3GWZ86AY]], take $n \ge 1$ with $n \varepsilon > (b - a)(f(b) - f(a))$. Let $P$ have the points $x_i = a + i (b - a)/n$ for $i = 0, \dots, n$.
4. On $[x_{i-1}, x_i]$ we have $f(x_{i-1}) \le f(x) \le f(x_i)$, and both bounds are values of $f$ there. So $M_i = f(x_i)$ and $m_i = f(x_{i-1})$.
5. Each subinterval has length $(b - a)/n$. So the sum telescopes:
   $$U(f, P) - L(f, P) = \frac{b - a}{n} \sum_{i=1}^{n} \big(f(x_i) - f(x_{i-1})\big) = \frac{b - a}{n} \big(f(b) - f(a)\big) < \varepsilon.$$
6. Such a partition exists for each $\varepsilon > 0$. By [[Riemann's criterion|017DH8WXTE]], $f$ is Riemann integrable.
7. Now assume that $f$ is decreasing. Then $f(b) \le f(x) \le f(a)$, so $f$ is bounded. Let $\varepsilon > 0$.
   Take $n \ge 1$ with $n \varepsilon > (b - a)(f(a) - f(b))$, and let $P$ be the partition into $n$ equal pieces as in step 3.
8. Now $M_i = f(x_{i-1})$ and $m_i = f(x_i)$. As in step 5, $U(f, P) - L(f, P) = \frac{b - a}{n} (f(a) - f(b)) < \varepsilon$. As in step 6, $f$ is Riemann integrable.

## Idea

For an increasing function, the supremum on a piece is the value at the right end and the infimum is the value at the left end. So the gaps between upper and lower sums telescope to $(f(b) - f(a))(b - a)/n$, which is small for large $n$.
