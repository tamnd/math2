---
tag: WF7KQAQTS2
kind: statement
role: theorem
name: Reflection formula for the gamma function
msc: [33B15, 30D30]
uses: [0V3FZMVB4K, 0A7YDKRNR6, 0NSD1TPHR0, 0WPQYW8MTE]
about: [0H5SYBSED9]
sources:
  - url: https://en.wikipedia.org/wiki/Reflection_formula
---

## Statement

Let $\Gamma$ be the [[gamma function|0V3FZMVB4K]], extended to a [[meromorphic function|0NSD1TPHR0]] on $\C$.
For every $z \in \C \setminus \Z$,
$$\Gamma(z)\,\Gamma(1 - z) = \frac{\pi}{\sin(\pi z)},$$
where $\sin$ is the [[complex sine|0A7YDKRNR6]].

## Remarks

For $0 < \operatorname{Re} z < 1$, the product $\Gamma(z)\Gamma(1-z)$ equals the beta integral $\int_0^\infty \frac{t^{z-1}}{1+t}\,dt$.
This integral is computed by the residue theorem, or for real $z$ by a substitution, and equals $\pi / \sin(\pi z)$.
Both sides are meromorphic on $\C$, so the identity extends from the strip to all of $\C \setminus \Z$ by the identity theorem.
Another proof multiplies the Weierstrass products of $1/\Gamma(z)$ and $1/\Gamma(1-z)$ and compares with [[Euler's sine product|DQEHD56649]].
At $z = 1/2$ the formula gives $\Gamma(1/2)^2 = \pi$, so $\Gamma(1/2) = \sqrt{\pi}$, because $\Gamma(1/2) > 0$.
The integers are excluded: at each $n \in \Z$ one factor on the left has a [[pole|0WPQYW8MTE]] and $\sin(\pi n) = 0$.
In Mathlib it is `Complex.Gamma_mul_Gamma_one_sub`.

## Explanations

### L1 human

The gamma function at $z$ times the gamma function at $1 - z$ is a simple expression in the sine function.
The two points $z$ and $1 - z$ are symmetric about the point $1/2$, so the formula relates the values of $\Gamma$ on the two sides of $1/2$, hence the name.
The formula explains why $\Gamma(1/2) = \sqrt{\pi}$.

### L2 human

The right side $\pi/\sin(\pi z)$ is never $0$, so the formula shows that $\Gamma$ has no zeros off the integers.
Since also $\Gamma(n) = (n-1)! \ne 0$ for $n \ge 1$, the function $1/\Gamma$ is entire with zeros exactly at $0, -1, -2, \ldots$.
Together with the functional equation $\Gamma(z+1) = z\Gamma(z)$ and the duplication formula, it is one of the basic identities of the gamma function.
It is used, for example, in the functional equation of the Riemann zeta function, where values of $\Gamma$ at $s/2$ and $(1-s)/2$ appear.
