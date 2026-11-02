---
tag: MHJETA01P6
kind: definition
name: Loop space
msc: [55P35]
defines: 2JFF5F3EGF
uses: [T9DG8DDE75, 0WS9P12FQR, RG15F0TWPW]
sources:
  - url: https://en.wikipedia.org/wiki/Loop_space
---

## Definition

Let $(X, x_0)$ be a [[pointed space|T9DG8DDE75]] and let $I = [0, 1]$.
The *loop space* of $(X, x_0)$ is the set
$$\Omega X = \set{\gamma \colon I \to X \text{ continuous} : \gamma(0) = \gamma(1) = x_0},$$
with the [[subspace topology|0WS9P12FQR]] of the [[compact-open topology|RG15F0TWPW]] on the set of continuous maps $I \to X$.
Its base point is the constant loop at $x_0$.

## Remarks

Concatenation $(\alpha \cdot \beta)(s) = \alpha(2s)$ for $s \le 1/2$ and $\beta(2s - 1)$ for $s \ge 1/2$ is a continuous product on $\Omega X$ that is associative and unital up to homotopy.
The set of path components $\pi_0(\Omega X)$ is in bijection with $\pi_1(X, x_0)$, and $\pi_n(\Omega X) \cong \pi_{n+1}(X, x_0)$ for $n \ge 1$.
For pointed spaces $A$ and $X$, pointed homotopy classes of maps $\Sigma A \to X$ from the reduced [[suspension|Q7RFNJH76Q]] correspond bijectively to pointed homotopy classes of maps $A \to \Omega X$.
Example: if $X$ is the one-point space, then $\Omega X$ is a single point, the constant loop.
Non-example: the free loop space of all continuous maps $S^1 \to X$ with no condition at a base point is a different space; it contains loops that miss $x_0$.
