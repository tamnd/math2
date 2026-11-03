---
tag: ACH2SKQB7D
kind: definition
name: Kaluza–Klein theory
msc: ["83E15", 81T33]
defines: E55CCQ3K4S
uses: [BY4QYYS788, 3MCZ97SW6V, WRZJRJS44W, 060W5CBZP6]
sources:
  - url: https://en.wikipedia.org/wiki/Kaluza–Klein_theory
---

## Definition

Let $M$ be a four-dimensional manifold and let $S^1$ be a [[circle|060W5CBZP6]] of circumference $2 \pi r$ with coordinate $y$.
Let $g_{\mu\nu}$ be a Lorentzian metric on $M$, $A_\mu$ a one-form on $M$, $\phi > 0$ a function on $M$ and $k$ a constant.
*Kaluza–Klein theory* is five-dimensional general relativity on $M \times S^1$ for the [[Lorentzian|BY4QYYS788]] metric
$$d\hat s^2 = g_{\mu\nu}(x) \, dx^\mu dx^\nu + \phi(x)^2 \left( dy + k A_\mu(x) \, dx^\mu \right)^2.$$
The fields must not depend on $y$ (the cylinder condition).
The dynamics is given by the five-dimensional vacuum [[Einstein field equations|3MCZ97SW6V]] for $\hat g$.

## Remarks

Under a change of coordinate $y \mapsto y + k \lambda(x)$, the one-form changes as $A_\mu \mapsto A_\mu - \partial_\mu \lambda$, which is a gauge transformation of electromagnetism.
So $A_\mu$ behaves as an electromagnetic potential, with field strength $F_{\mu\nu} = \partial_\mu A_\nu - \partial_\nu A_\mu$, the [[electromagnetic tensor|WRZJRJS44W]].
Example: with $\phi \equiv 1$ and $A = 0$, the metric $g_{\mu\nu} dx^\mu dx^\nu + dy^2$ with $g$ the Minkowski metric is flat, so it solves the five-dimensional vacuum equations.
Reducing the five-dimensional Einstein–Hilbert action over $S^1$ gives the four-dimensional Einstein–Hilbert action, the Maxwell action $-\frac14 \phi^3 F_{\mu\nu} F^{\mu\nu}$ (with $k$ chosen suitably) and terms for the scalar $\phi$.
Non-example: a metric whose components depend on $y$ fails the cylinder condition; such fields describe the massive Kaluza–Klein modes, whose masses are multiples of $1/r$.
