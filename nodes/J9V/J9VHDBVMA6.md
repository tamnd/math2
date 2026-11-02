---
tag: J9VHDBVMA6
kind: definition
name: Weak-type estimate
msc: [42B25, 47B38, "46E30"]
defines: 9534R6VMY0
uses: [P15VQS5DJ9, YYNCJSR0PJ, SASP14MA1Z, H4C888M5AZ]
sources:
  - url: https://en.wikipedia.org/wiki/Lp_space
---

## Definition

Let $(X, \mu)$ and $(Y, \nu)$ be [[measure spaces|P15VQS5DJ9]] and let $1 \le p \le \infty$ and $1 \le q < \infty$.
Let $T$ be an operator that maps each $f$ in the [[Lp space|SASP14MA1Z]] $L^p(X, \mu)$ to a [[measurable function|YYNCJSR0PJ]] $Tf$ on $Y$.
The operator $T$ is of *weak type $(p, q)$* if there is a constant $C$ such that
$$\nu(\set{y \in Y : \abs{Tf(y)} > \lambda}) \le \left( \frac{C \norm{f}_{L^p}}{\lambda} \right)^q$$
for every $f \in L^p(X, \mu)$ and every $\lambda > 0$.
One also says that $T$ satisfies a weak-type $(p, q)$ estimate.

## Remarks

Equivalently, $\norm{Tf}_{q, \infty} \le C \norm{f}_p$, where $\norm{\cdot}_{q,\infty}$ is the quasinorm of the [[weak Lp space|H4C888M5AZ]] $L^{q,\infty}(\nu)$.
The operator is of *strong type $(p, q)$* if $\norm{Tf}_q \le C \norm{f}_p$.
By Chebyshev's inequality $\nu(\set{\abs{g} > \lambda}) \le \lambda^{-q} \norm{g}_q^q$, strong type $(p, q)$ implies weak type $(p, q)$ with the same constant.
By convention, weak type $(p, \infty)$ means strong type $(p, \infty)$.

Example: let $X = (0, 1)$ and $Y = (0, \infty)$ with Lebesgue measure, and let $Tf(y) = c_f / y$ with $c_f = \int_0^1 f$.
Then $\set{y : \abs{Tf(y)} > \lambda} = (0, \abs{c_f}/\lambda)$, of measure $\abs{c_f}/\lambda \le \norm{f}_1/\lambda$.
So $T$ is of weak type $(1, 1)$ with $C = 1$, but not of strong type $(1, 1)$, because $\int_0^\infty dy/y = \infty$ when $c_f \neq 0$.

Non-example: on the same spaces, with $Y = (0, 1)$, let $Tf(y) = c_f / y^2$.
For $f = 1$ one has $c_f = 1$ and $\set{Tf > \lambda} = (0, \lambda^{-1/2})$ for $\lambda > 1$.
The ratio $\lambda^{-1/2} / (C/\lambda) = \lambda^{1/2}/C$ is unbounded as $\lambda \to \infty$, so $T$ is not of weak type $(1, 1)$.
