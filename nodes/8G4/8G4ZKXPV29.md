---
tag: 8G4ZKXPV29
kind: definition
name: Doubling measure
msc: [28A12, 30L99]
defines: W1JXH6NCKX
uses: [0VKD1TP7F3, DYR1QFNGNJ, 0YE5868HZB]
sources:
  - url: https://en.wikipedia.org/wiki/Doubling_space
---

## Definition

Let $(X, d)$ be a [[metric space|0VKD1TP7F3]] and let $\mu$ be a [[Borel measure|DYR1QFNGNJ]] on $X$.
For $x \in X$ and $r > 0$, let $B(x, r)$ be the [[open ball|0YE5868HZB]] of centre $x$ and radius $r$.
The measure $\mu$ is *doubling* if:

1. $0 < \mu(B(x, r)) < \infty$ for all $x \in X$ and $r > 0$.
2. There is a constant $C \ge 1$ with $\mu(B(x, 2r)) \le C \, \mu(B(x, r))$ for all $x \in X$ and $r > 0$.

## Remarks

Example: Lebesgue measure $\lambda$ on $\R^n$ is doubling with $C = 2^n$.
Indeed $\lambda(B(x, r)) = \omega_n r^n$ with $\omega_n$ the volume of the unit ball, so the ratio is exactly $2^n$.

Non-example: the standard Gaussian measure $\gamma$ on $\R$ satisfies clause 1 but not clause 2.
Let $\varphi(t) = e^{-t^2/2}/\sqrt{2\pi}$ be its density, which decreases on $[0, \infty)$, and let $x > 2$.
Then $\gamma(B(x, 1)) \le 2 \varphi(x - 1)$ and $\gamma(B(x, 2)) \ge \frac12 \varphi(x - \frac32)$.
So $\gamma(B(x,2)) / \gamma(B(x,1)) \ge \frac14 e^{(x - 5/4)/2}$, which is unbounded as $x \to \infty$.

Some authors drop clause 1 and only ask for clause 2 for balls of positive finite measure.
A metric space with a doubling measure is a doubling metric space: each ball is covered by a bounded number of balls of half the radius.
