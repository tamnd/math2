---
tag: R1PHMVBJ9J
kind: statement
role: theorem
name: Marcinkiewicz interpolation theorem
msc: [46B70, "46E30", 42B25]
uses: [SASP14MA1Z, H4C888M5AZ, WEBBT18D4X]
about: [SASP14MA1Z, H4C888M5AZ]
sources:
  - url: https://en.wikipedia.org/wiki/Marcinkiewicz_interpolation_theorem
same_as:
  wikidata: Q6757284
  wikipedia: Marcinkiewicz interpolation theorem
---

## Statement

Let $(X, \mu)$ and $(Y, \nu)$ be [[σ-finite|WEBBT18D4X]] measure spaces and let $1 \le p_0 < p_1 \le \infty$.
Let $T$ map $L^{p_0}(\mu) + L^{p_1}(\mu)$ into the measurable functions on $Y$.
Assume that $T$ is sublinear: for all $f, g$ and scalars $c$, almost everywhere,
$$\abs{T(f + g)} \le \abs{T f} + \abs{T g}, \qquad \abs{T(c f)} = \abs{c} \abs{T f}.$$
Assume that $T$ is of weak type $(p_0, p_0)$: there is $A_0$ with
$$\nu(\set{y : \abs{T f(y)} > t}) \le \left( \frac{A_0 \norm{f}_{p_0}}{t} \right)^{p_0} \quad \text{for all } f \in L^{p_0}(\mu) \text{ and } t > 0.$$
Assume that $T$ is of weak type $(p_1, p_1)$ in the same sense with a constant $A_1$, where for $p_1 = \infty$ this means $\norm{T f}_\infty \le A_1 \norm{f}_\infty$.
Then for every $p$ with $p_0 < p < p_1$ there is a constant $A$, depending only on $p$, $p_0$, $p_1$, $A_0$ and $A_1$, with
$$\norm{T f}_p \le A \norm{f}_p \quad \text{for all } f \in L^p(\mu).$$

## Remarks

The weak type condition says that $T$ maps $L^{p_i}$ boundedly into the [[weak Lp space|H4C888M5AZ]] $L^{p_i,\infty}$.
The proof writes $\norm{T f}_p^p = p \int_0^\infty t^{p-1} \nu(\set{\abs{T f} > t}) \, dt$ by the [[layer cake representation|H78RXJC1K1]].
For each $t$, it splits $f$ into the part where $\abs{f} > c t$, which lies in $L^{p_0}$, and the rest, which lies in $L^{p_1}$.
The two weak-type bounds and Fubini's theorem then give the bound.

Example: the [[Hardy–Littlewood maximal function|VX1A56P5KQ]] operator $M$ on $\R^n$ is of weak type $(1, 1)$, and $\norm{M f}_\infty \le \norm{f}_\infty$.
The theorem gives $\norm{M f}_p \le A_p \norm{f}_p$ for $1 < p < \infty$.

The endpoints are not included in the conclusion.
The maximal operator is not bounded on $L^1(\R^n)$: for $f$ the indicator function of the unit ball, $M f(x)$ is of order $\abs{x}^{-n}$ for large $\abs{x}$, which is not integrable.

## Explanations

### L1 human

Some important operators on functions are not bounded on $L^1$, but satisfy a weaker estimate there that controls the measure of the set where the output is large.
The theorem says that two such weak estimates, at two exponents, give a genuine $L^p$ bound for every exponent strictly between them.
It works even for operators that are not linear, such as maximal functions.

### L2 human

In harmonic analysis one usually proves a weak $(1, 1)$ bound by a covering or Calderón–Zygmund argument and an $L^2$ or $L^\infty$ bound by other means.
Marcinkiewicz interpolation then gives all the $L^p$ bounds in between.
Compared with the [[Riesz–Thorin theorem|AGRKRG1TMJ]], it needs less (weak type, sublinearity) and gives less (an unspecified constant).
There is also an off-diagonal version, from weak type $(p_i, q_i)$ to strong type $(p, q)$, which requires $p_0 \le q_0$, $p_1 \le q_1$, $q_0 \ne q_1$, and gives the conclusion for $p \le q$.
