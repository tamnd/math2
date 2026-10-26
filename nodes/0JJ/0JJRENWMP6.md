---
tag: 0JJRENWMP6
kind: statement
role: corollary
name: Cauchy's estimates
aliases: [cauchy-inequalities, cauchy-estimate]
msc: [30A10]
uses: [0DG0Z72CQD, 0F0H5P5DED, 0DJMGPN8K9]
sources:
  - url: https://en.wikipedia.org/wiki/Cauchy%27s_integral_formula
    locator: Consequences
---

## Statement

Let $U \subseteq \mathbb{C}$ be an open set and let $f : U \to \mathbb{C}$ be [[holomorphic|0DG0Z72CQD]] on $U$.
Let $c \in \mathbb{C}$ and $r > 0$ be such that the closed disc $\{z : |z - c| \le r\}$ is contained in $U$.
Let $M \ge 0$ be a real number with $|f(z)| \le M$ for each $z$ with $|z - c| = r$.
Then for each integer $n \ge 0$,
$$|f^{(n)}(c)| \le \frac{n! \, M}{r^n}.$$

## Remarks

Proof: apply the [[estimation lemma|0DJMGPN8K9]] to the [[formula for the derivatives|0F0H5P5DED]] with $a = c$. The circle has length $2 \pi r$, and $|f(z) / (z - c)^{n+1}| \le M / r^{n+1}$ on it.
For $n = 1$, the estimate is $|f'(c)| \le M / r$.
If $f(z) = \sum a_n (z - c)^n$ is the Taylor series, the estimate is $|a_n| \le M / r^n$.

## Explanations

### L1 human

If a holomorphic function is small on a circle, then its derivatives at the center cannot be large.
A larger circle with the same bound $M$ gives a better bound for the derivatives. This is the idea of [[Liouville's theorem|0EHKVRF4J6]].
