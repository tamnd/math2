---
tag: ZGH5RYJTQC
kind: definition
name: Orlicz space
msc: ["46E30"]
defines: WBCN9A847H
uses: [P15VQS5DJ9, YYNCJSR0PJ, 07Q7CNM5WF, RARTMA0ZEC, DWJF7ABPR1]
sources:
  - url: https://en.wikipedia.org/wiki/Orlicz_space
---

## Definition

A *Young function* is a [[convex function|07Q7CNM5WF]] $\Phi \colon [0, \infty) \to [0, \infty)$ with $\Phi(0) = 0$ and $\Phi(t) \to \infty$ as $t \to \infty$.
Let $(X, \Sigma, \mu)$ be a [[measure space|P15VQS5DJ9]] and let $\Phi$ be a Young function.
For a real or complex [[measurable function|YYNCJSR0PJ]] $f$ on $X$, the *Luxemburg norm* is
$$\norm{f}_\Phi = \inf \set{\lambda > 0 : \int_X \Phi\!\left( \frac{\abs{f}}{\lambda} \right) d\mu \le 1},$$
with $\inf \emptyset = \infty$.
The *Orlicz space* $L^\Phi(\mu)$ is the set of measurable $f$ with $\norm{f}_\Phi < \infty$, modulo equality [[almost everywhere|RARTMA0ZEC]].

## Remarks

Example: for $1 \le p < \infty$, $\Phi(t) = t^p$ is a Young function.
The condition $\int (\abs{f}/\lambda)^p \, d\mu \le 1$ means $\lambda \ge \norm{f}_p$.
So $L^\Phi = L^p$ with $\norm{f}_\Phi = \norm{f}_p$.

Non-example: $\Phi(t) = \sqrt{t}$ is not a Young function, because it is not convex.
On $[0, 1]$ with Lebesgue measure the Luxemburg functional is then $\left( \int \abs{f}^{1/2} \, d\mu \right)^2$.
It fails the triangle inequality: the indicator functions of $[0, \tfrac12]$ and $(\tfrac12, 1]$ each get the value $\tfrac14$, but their sum gets the value $1$.

A function $f$ lies in $L^\Phi$ exactly when $\int_X \Phi(\abs{f}/\lambda) \, d\mu < \infty$ for some $\lambda > 0$.
With the Luxemburg norm, $L^\Phi(\mu)$ is a Banach space.
Some authors allow Young functions with values in $[0, \infty]$; this includes $L^\infty$ as an Orlicz space.
