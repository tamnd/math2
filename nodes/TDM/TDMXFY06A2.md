---
tag: TDMXFY06A2
kind: statement
role: theorem
name: Abel inversion formula
msc: [45D05, "45E10", 26A33]
uses: [H6ZGEDM4VV, QHNWVSC6AQ, 0H5SYBSED9, JTKCZ44NN3]
about: [H6ZGEDM4VV]
sources:
  - url: https://en.wikipedia.org/wiki/Abel_transform
---

## Statement

Let $b > 0$, let $0 < \alpha < 1$, and let $\varphi \colon [0, b] \to \C$ be continuous.
Let
$$f(x) = \int_0^x \frac{\varphi(t)}{(x - t)^{\alpha}} \, dt, \quad x \in [0, b].$$
Then the function $F(x) = \int_0^x \frac{f(t)}{(x - t)^{1 - \alpha}} \, dt$ is continuously differentiable on $[0, b]$, and
$$\varphi(x) = \frac{\sin(\pi \alpha)}{\pi} \, F'(x) = \frac{\sin(\pi \alpha)}{\pi} \, \frac{d}{dx} \int_0^x \frac{f(t)}{(x - t)^{1 - \alpha}} \, dt, \quad x \in [0, b].$$
In particular, the [[Volterra equation of the first kind|H6ZGEDM4VV]] $\int_0^x \varphi(t) (x - t)^{-\alpha} \, dt = f(x)$ has at most one continuous solution $\varphi$.

## Remarks

Proof idea: insert the formula for $f$ into $F$ and exchange the order of integration.
This gives $F(x) = \int_0^x \varphi(s) \left( \int_s^x (x - t)^{\alpha - 1} (t - s)^{-\alpha} \, dt \right) ds$.
The substitution $t = s + u(x - s)$ turns the inner integral into the [[Beta function|QHNWVSC6AQ]] value $B(\alpha, 1 - \alpha) = \Gamma(\alpha) \Gamma(1 - \alpha) = \pi / \sin(\pi \alpha)$, which does not depend on $x$ or $s$.
So $F(x) = \frac{\pi}{\sin(\pi \alpha)} \int_0^x \varphi(s) \, ds$, and the fundamental theorem of calculus gives the formula.

Example: for $\alpha = \tfrac12$ the formula reads $\varphi(x) = \frac{1}{\pi} \frac{d}{dx} \int_0^x \frac{f(t)}{\sqrt{x - t}} \, dt$, the inversion of [[Abel's integral equation|G4GWBYTW7B]].
With $f(x) = 2\sqrt{x}$, the inner integral is $2 x B(\tfrac32, \tfrac12) = \pi x$, so $\varphi = 1$; indeed $\int_0^x (x - t)^{-1/2} \, dt = 2\sqrt{x}$.

The statement starts from a solution $\varphi$; it does not say that every $f$ arises.
A given $f$ is of this form for a continuous $\varphi$ only if $F$ is continuously differentiable; for instance $f$ must vanish at $0$.
If $f$ is continuously differentiable with $f(0) = 0$, then the solution can also be written $\varphi(x) = \frac{\sin(\pi \alpha)}{\pi} \int_0^x \frac{f'(t)}{(x - t)^{1 - \alpha}} \, dt$.

## Explanations

### L1 human

Abel's equation hides the unknown $\varphi$ inside an integral with a kernel that blows up at the endpoint.
The inversion formula recovers $\varphi$ by applying a second integral of the same kind, with the complementary exponent $1 - \alpha$, and then differentiating.
The two integrals together amount to one ordinary integration, which the derivative undoes.

### L2 human

In the language of fractional calculus, the equation says $\Gamma(1 - \alpha) \, I^{1 - \alpha} \varphi = f$, where $I^\beta$ is the [[Riemann–Liouville integral|JTKCZ44NN3]] of order $\beta$.
The formula then reads $\varphi = \frac{1}{\Gamma(1 - \alpha)} \frac{d}{dx} I^{\alpha} f$, using $I^\alpha I^{1 - \alpha} = I^1$; the reflection formula $\Gamma(\alpha) \Gamma(1 - \alpha) = \pi / \sin(\pi \alpha)$ for the [[Gamma function|0H5SYBSED9]] shows that this agrees with the statement.
It solves the [[tautochrone problem|A56P5S5D6Z]], and its variant for the Abel transform is the basis of Abel inversion in tomography of radially symmetric objects.
