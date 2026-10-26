---
tag: 0F0H5P5DED
kind: statement
role: theorem
name: Cauchy's integral formula for derivatives
aliases: [cauchy-differentiation-formula]
msc: ["30E20"]
uses: [0DG0Z72CQD, 0DG10TVYPN, 0QEBN8DGVE, 0T7ABX4CWE]
sources:
  - url: https://en.wikipedia.org/wiki/Cauchy%27s_integral_formula
    locator: Theorem
---

## Statement

Let $U \subseteq \mathbb{C}$ be an open set and let $f : U \to \mathbb{C}$ be [[holomorphic|0DG0Z72CQD]] on $U$.
Let $c \in \mathbb{C}$ and $r > 0$ be such that the closed disc $\{z : |z - c| \le r\}$ is contained in $U$.
Then for each integer $n \ge 0$ and each $a \in \mathbb{C}$ with $|a - c| < r$,
$$f^{(n)}(a) = \frac{n!}{2 \pi i} \oint_{|z - c| = r} \frac{f(z)}{(z - a)^{n+1}} \, dz,$$
where $f^{(n)}$ is the $n$-th complex derivative of $f$, which exists by [[holomorphic functions are infinitely differentiable|0QEBN8DGVE]].

## Remarks

For $n = 0$, this is [[Cauchy's integral formula|0DG10TVYPN]].
Formally, the formula comes from differentiating $\frac{1}{z - a}$ $n$ times under the integral sign with respect to $a$.
For example, with $f(z) = e^z$, $c = a = 0$ and $r = 1$: $\oint_{|z| = 1} \frac{e^z}{z^{n+1}} \, dz = \frac{2 \pi i}{n!}$.
It gives [[Cauchy's estimates|0JJRENWMP6]] for the derivatives.

## Explanations

### L1 human

The values of a holomorphic function on a circle determine not only its values inside, but also all its derivatives inside.
To get the $n$-th derivative, you put a higher power of $z - a$ in the denominator and multiply by $n!$.
