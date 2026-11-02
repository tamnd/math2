---
tag: 4KXHGXZQY8
kind: counterexample
name: Weierstrass's counterexample to the Dirichlet principle
msc: [49J05, 35A15]
uses: [PQ25NHV0KS, JRQZ803Q5Y, TE379HBTY0]
sources:
  - url: https://en.wikipedia.org/wiki/Dirichlet%27s_principle
---

## Counterexample

Consider the [[integral functional|JRQZ803Q5Y]]
$$J(u) = \int_{-1}^{1} x^2 \, u'(x)^2 \, dx$$
on the set $\mathcal{A}$ of functions $u \in C^1([-1, 1])$ with $u(-1) = -1$ and $u(1) = 1$.
Then $\inf_{\mathcal{A}} J = 0$, but no $u \in \mathcal{A}$ has $J(u) = 0$, so $J$ has no minimiser on $\mathcal{A}$.

Check that the infimum is $0$.
For $\varepsilon > 0$, put $u_\varepsilon(x) = \arctan(x / \varepsilon) / \arctan(1 / \varepsilon)$, which lies in $\mathcal{A}$.
With $c_\varepsilon = \arctan(1 / \varepsilon)$, one has $u_\varepsilon'(x) = \varepsilon / \big(c_\varepsilon (\varepsilon^2 + x^2)\big)$.
Since $x^2 \le \varepsilon^2 + x^2$,
$$J(u_\varepsilon) \le \frac{1}{c_\varepsilon^2} \int_{-1}^{1} \frac{\varepsilon^2}{\varepsilon^2 + x^2} \, dx = \frac{2 \varepsilon}{c_\varepsilon},$$
which tends to $0$ as $\varepsilon \to 0$, because $c_\varepsilon \to \pi / 2$.

Check that $0$ is not attained.
If $J(u) = 0$, then $x u'(x) = 0$ for all $x$, by continuity of the integrand.
So $u' = 0$ for $x \ne 0$, hence also at $0$, and $u$ is constant.
This contradicts $u(-1) = -1 \ne 1 = u(1)$.

## Remarks

Riemann had used the Dirichlet principle, the claim that a nonnegative energy with given boundary values attains its infimum.
Weierstrass's example shows that this claim can fail, even for a nonnegative functional with a smooth integrand.
The minimising functions $u_\varepsilon$ tend to the sign function, which jumps at $0$ and does not belong to the admissible class.
The integrand $x^2 \xi^2$ is convex in $\xi$, but its coefficient vanishes at $x = 0$.
So $J$ gives no bound on $u'$ near $0$, and minimising sequences can develop a jump there.
This is the failure of the compactness step of the [[direct method|TE379HBTY0]].
Hilbert later justified the Dirichlet principle for the Dirichlet energy by the direct method.

## Explanations

### L1 human

The problem asks for a curve from height $-1$ to height $1$ that makes a weighted energy as small as possible.
The weight $x^2$ is zero at the middle, so steep slopes there are almost free.
Curves that jump more and more steeply at $0$ get energies closer and closer to $0$.
But a curve with energy exactly $0$ would have to be flat everywhere, and then it could not climb from $-1$ to $1$.
So the infimum is never reached: the best candidates converge to a jump, which is not an allowed curve.
