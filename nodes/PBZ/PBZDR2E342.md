---
tag: PBZDR2E342
kind: definition
name: Choquet theory
msc: [46A55, 52A07]
defines: ABPK3RW5MW
uses: [B6GY2KJMWW, 02AS45T3H9, 0R6EWFKRCF, 3MSGFJM2NX, 059TJN0NZ1, 03TM135G0N, RSRAY0Q68S, 0ACRGYNHSR]
sources:
  - url: https://en.wikipedia.org/wiki/Choquet_theory
---

## Definition

Let $E$ be a real Hausdorff [[locally convex space|B6GY2KJMWW]], and let $K \subseteq E$ be a nonempty [[compact|0R6EWFKRCF]] [[convex set|02AS45T3H9]].
Let $\mu$ be a Borel [[probability measure|059TJN0NZ1]] on $K$, and let $x \in K$.
The measure $\mu$ *represents* $x$, and $x$ is the *barycenter* of $\mu$, if
$$\ell(x) = \int_K \ell \, d\mu$$
for every [[continuous linear form|03TM135G0N]] $\ell \colon E \to \R$.
*Choquet theory* is the study of representing measures of points of $K$ that are concentrated on the set $\operatorname{ext} K$ of [[extreme points|3MSGFJM2NX]] of $K$.

## Remarks

Every point of $K$ is represented by the [[Dirac measure|0ACRGYNHSR]] at that point; the theory asks for measures on the extreme points.
Choquet's theorem: if $K$ is metrizable, then $\operatorname{ext} K$ is a $G_\delta$ set, and every $x \in K$ is represented by a probability measure $\mu$ with $\mu(\operatorname{ext} K) = 1$.
The Bishop–de Leeuw theorem extends this to non-metrizable $K$ in a weaker form.
For metrizable $K$, the measure on $\operatorname{ext} K$ is unique for every $x$ exactly when $K$ is a Choquet simplex.

Example: let $K = [0, 1] \subseteq \R$, with $\operatorname{ext} K = \set{0, 1}$.
The measure $\mu = (1 - x) \delta_0 + x \delta_1$ represents $x$.
The check: for $\ell(t) = c t$, one gets $\int \ell \, d\mu = c x = \ell(x)$.

Non-example: for $x = 1/2$, the measure $\delta_0$ is concentrated on $\operatorname{ext} K$ but does not represent $x$, since its barycenter is $0$.

For the square $K = [0, 1]^2$, the centre is represented by $\frac12(\delta_{(0,0)} + \delta_{(1,1)})$ and by $\frac12(\delta_{(1,0)} + \delta_{(0,1)})$, so uniqueness fails.

## Explanations

### L1 human

A representing measure writes a point as an average of other points of the set.
Choquet theory asks for averages of extreme points only, the corners of the set.
It is the infinite-dimensional version of barycentric coordinates.
