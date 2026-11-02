---
tag: MNJ030R4CA
kind: statement
role: theorem
name: Blaschke–Santaló inequality
msc: [52A40, 52A20]
uses: [437FSG3419, 2Z2QVWZ262, 0S52TNNTH9]
about: [437FSG3419]
sources:
  - url: https://en.wikipedia.org/wiki/Mahler_volume
---

## Statement

Let $n \ge 1$ and let $K \subseteq \R^n$ be a compact [[convex body|437FSG3419]] with nonempty interior that is symmetric about the origin, that is, $K = -K$.
Let $K^\circ = \set{y \in \R^n : x \cdot y \le 1 \text{ for all } x \in K}$ be its polar body, where $x \cdot y$ is the [[dot product|0S52TNNTH9]].
Let $\operatorname{vol}$ be [[Lebesgue measure|2Z2QVWZ262]] and $\kappa_n$ the volume of the closed unit ball $B$ of $\R^n$.
Then
$$\operatorname{vol}(K) \operatorname{vol}(K^\circ) \le \kappa_n^2,$$
with equality if and only if $K$ is an ellipsoid centered at the origin.

## Remarks

The product $\operatorname{vol}(K) \operatorname{vol}(K^\circ)$ is the Mahler volume of $K$; it does not change when $K$ is replaced by $AK$ for an invertible linear map $A$, because $(AK)^\circ = (A^T)^{-1} K^\circ$.
A standard proof uses Steiner symmetrization: symmetrizing $K$ in a hyperplane does not decrease the Mahler volume, and suitable sequences of symmetrizations converge to a ball.
The inequality holds without symmetry if the origin is replaced by the Santaló point of $K$, the unique interior point $z$ that minimizes $\operatorname{vol}((K - z)^\circ)$.

Example: $K = [-1, 1]^2$ has $K^\circ = \set{(y_1, y_2) : \abs{y_1} + \abs{y_2} \le 1}$, of area $2$.
So the Mahler volume is $4 \cdot 2 = 8$, which is less than $\pi^2 \approx 9.87$.

Some centering is needed: for $K = [-1, 1]^2 - (1 - \varepsilon, 0)$, the origin is at distance $\varepsilon$ from the boundary, and $\operatorname{vol}(K^\circ) \to \infty$ as $\varepsilon \to 0$.

## Explanations

### L1 human

The polar body $K^\circ$ is a kind of reciprocal of $K$: when $K$ gets bigger, $K^\circ$ gets smaller.
The product of their volumes is unchanged by stretching.
The Blaschke–Santaló inequality says that this product is largest for balls and ellipsoids.

### L2 human

The inequality is a basic tool of asymptotic convex geometry and has functional forms for log-concave functions.
The reverse question, how small $\operatorname{vol}(K) \operatorname{vol}(K^\circ)$ can be, is the [[Mahler conjecture|FFZHNFJCZS]].
For symmetric $K$, the Bourgain–Milman inequality gives a lower bound $c^n \kappa_n^2$ with an absolute constant $c > 0$.
