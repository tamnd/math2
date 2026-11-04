---
tag: ZJZ2Q4Z3C1
kind: proof
name: Proof that continuous functions are Riemann integrable
msc: [26A42]
proves: 06SESV7GQY
uses: [0ATVXC3NCC, 0W0TZDRF9C, 0A3CK6DVVB, 0A3GWZ86AY, 0WS1A8E2P9, 0QRQVH0CRW, 017DH8WXTE]
sources:
  - url: https://www.math.ucdavis.edu/~hunter/m125b/ch1.pdf
    locator: Theorem 1.19
---

## Proof

We use uniform continuity and Riemann's criterion.

1. Let $a < b$ and let $f \colon [a, b] \to \mathbb{R}$ be continuous. By the [[boundedness theorem|0ATVXC3NCC]], $f$ is bounded. So its [[Darboux sums|0QRQVH0CRW]] are defined.
2. Let $\varepsilon > 0$. By the [[uniform continuity theorem|0W0TZDRF9C]], $f$ is [[uniformly continuous|0A3CK6DVVB]] on $[a, b]$. So there is $\delta > 0$ with $|f(x) - f(y)| < \frac{\varepsilon}{2(b - a)}$ for all $x, y \in [a, b]$ with $|x - y| < \delta$.
3. By the [[Archimedean property|0A3GWZ86AY]], take $n$ with $n \delta > b - a$. Let $P$ have the points $x_i = a + i (b - a)/n$ for $i = 0, \dots, n$. Each subinterval has length $(b - a)/n < \delta$.
4. Fix $i$. The restriction of $f$ to $[x_{i-1}, x_i]$ is continuous. By the [[extreme value theorem|0WS1A8E2P9]], there are $c_i, d_i \in [x_{i-1}, x_i]$ with $f(c_i) \le f(x) \le f(d_i)$ for all $x$ there.
5. So $M_i = f(d_i)$ and $m_i = f(c_i)$. Since $|d_i - c_i| \le (b - a)/n < \delta$, step 2 gives $M_i - m_i < \frac{\varepsilon}{2(b - a)}$.
6. Hence
   $$U(f, P) - L(f, P) = \sum_{i=1}^{n} (M_i - m_i)(x_i - x_{i-1}) < \frac{\varepsilon}{2(b - a)} \sum_{i=1}^{n} (x_i - x_{i-1}) = \frac{\varepsilon}{2} < \varepsilon.$$
7. Such a partition exists for each $\varepsilon > 0$. By [[Riemann's criterion|017DH8WXTE]], $f$ is Riemann integrable on $[a, b]$.

## Idea

Uniform continuity gives one $\delta$ that works on the whole interval. On every subinterval shorter than $\delta$, the largest and smallest values of $f$ differ by a tiny amount. So the upper and lower sums differ by that amount times $b - a$.
