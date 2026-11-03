---
tag: 3E09CKTVWF
kind: definition
name: Lorentz transformation
msc: [83A05, "22E43"]
defines: WEVGN4C7PQ
uses: [G49G4R1K04, 2E9AJVZS6E, QWK3BYVJ9W, 8CTX67V404]
sources:
  - url: https://en.wikipedia.org/wiki/Lorentz_transformation
---

## Definition

Let $(V, \eta)$ be [[Minkowski space|G49G4R1K04]].
A *Lorentz transformation* is a linear map $\Lambda \colon V \to V$ such that
$$\eta(\Lambda x, \Lambda y) = \eta(x, y) \quad \text{for all } x, y \in V.$$
In a basis where $\eta$ has the matrix $\eta = \operatorname{diag}(-1, 1, 1, 1)$, this means $\Lambda^T \eta \Lambda = \eta$.

## Remarks

Example: the *boost* with velocity $v$ along the $x^1$ axis, where $\abs{v} < c$, $\beta = v / c$ and $\gamma = 1/\sqrt{1 - \beta^2}$ is the [[Lorentz factor|2E9AJVZS6E]]:
$$x'^0 = \gamma (x^0 - \beta x^1), \quad x'^1 = \gamma (x^1 - \beta x^0), \quad x'^2 = x^2, \quad x'^3 = x^3.$$
Check: $-(x'^0)^2 + (x'^1)^2 = \gamma^2 (1 - \beta^2) \big( -(x^0)^2 + (x^1)^2 \big) = -(x^0)^2 + (x^1)^2$, because the cross terms $\pm 2 \gamma^2 \beta x^0 x^1$ cancel.
With $x^0 = ct$ these are the familiar formulas $t' = \gamma (t - v x / c^2)$ and $x' = \gamma (x - v t)$.
Non-example: the [[Galilean transformation|8CTX67V404]] $t' = t$, $x' = x - vt$ with $v \ne 0$ is linear but does not preserve $\eta$.
It sends $(ct, x) = (c, 0)$ to $(c, -v)$, and $-c^2 + v^2 \ne -c^2$.
The Lorentz transformations form the [[Lorentz group|QWK3BYVJ9W]] $O(1, 3)$.
Every Lorentz transformation with $\det \Lambda = 1$ that preserves the direction of time is a rotation followed by a boost.
A Lorentz transformation followed by a translation is a Poincaré transformation; some authors call these inhomogeneous Lorentz transformations.
