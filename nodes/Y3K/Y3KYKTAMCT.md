---
tag: Y3KYKTAMCT
kind: definition
name: Henstock–Kurzweil integral
msc: [26A39]
defines: FCGHXDGVV9
uses: [069P20KYQT, 0HBY48G8G1]
sources:
  - url: https://en.wikipedia.org/wiki/Henstock%E2%80%93Kurzweil_integral
---

## Definition

Let $a < b$ be real numbers and let $f \colon [a, b] \to \R$ be a function.
A *gauge* on $[a, b]$ is a function $\delta \colon [a, b] \to (0, \infty)$.
A tagged [[partition|069P20KYQT]] $a = x_0 < x_1 < \cdots < x_n = b$ with tags $t_i \in [x_{i-1}, x_i]$ is *$\delta$-fine* if $[x_{i-1}, x_i] \subseteq (t_i - \delta(t_i), t_i + \delta(t_i))$ for every $i$.
The function $f$ is *Henstock–Kurzweil integrable* on $[a, b]$, with integral $A \in \R$, if the following holds.
For every $\varepsilon > 0$ there is a gauge $\delta$ such that
$$\Bigl\lvert \sum_{i=1}^{n} f(t_i)(x_i - x_{i-1}) - A \Bigr\rvert < \varepsilon$$
for every $\delta$-fine tagged partition of $[a, b]$.

## Remarks

Cousin's lemma says that for every gauge a $\delta$-fine tagged partition exists, so the integral, when it exists, is unique.
If the gauges can always be taken constant, the definition is that of the [[Riemann integral|0QM4TXT3DR]].

Example: let $F(x) = x^2 \sin(1/x^2)$ for $x \ne 0$ and $F(0) = 0$, and $f = F'$ on $[0, 1]$.
The function $F$ is differentiable everywhere, so $f$ is Henstock–Kurzweil integrable with integral $F(1) - F(0) = \sin 1$.
Here $f(x) = 2x \sin(1/x^2) - (2/x)\cos(1/x^2)$ for $x \ne 0$, and $\abs{f}$ is not Lebesgue integrable.

Non-example: $f(x) = 1/x$ for $0 < x \le 1$ and $f(0) = 0$.
A nonnegative Henstock–Kurzweil integrable function is Lebesgue integrable, and $\int_0^1 dx/x = \infty$, so $f$ is not integrable.
