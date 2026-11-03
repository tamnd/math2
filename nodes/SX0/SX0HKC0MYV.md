---
tag: SX0HKC0MYV
kind: definition
name: Rapidity
msc: [83A05]
defines: T639889CSD
uses: [2E9AJVZS6E, WEVGN4C7PQ, 01PPDSDP2N, 0WFZX06698]
sources:
  - url: https://en.wikipedia.org/wiki/Rapidity
---

## Definition

Let $c > 0$ be the speed of light and let $v$ be a real number with $\abs{v} < c$, a velocity along a fixed line.
The *rapidity* of $v$ is
$$\varphi = \operatorname{artanh}\left( \frac{v}{c} \right),$$
where $\operatorname{artanh}$ is the [[inverse hyperbolic tangent|0WFZX06698]].
Equivalently, $\varphi$ is the unique real number with $\tanh \varphi = v / c$.

## Remarks

Example: for $v = 0.6 c$, $\varphi = \tfrac{1}{2} \ln \frac{1 + 0.6}{1 - 0.6} = \tfrac{1}{2} \ln 4 = \ln 2$.
Check: $\tanh(\ln 2) = (2 - \tfrac{1}{2}) / (2 + \tfrac{1}{2}) = 0.6$.
Non-example: $v = c$ has no rapidity, since $\tanh \varphi < 1$ for every real $\varphi$.
With $\beta = v / c$ and the [[Lorentz factor|2E9AJVZS6E]] $\gamma$, one has $\gamma = \cosh \varphi$ and $\gamma \beta = \sinh \varphi$.
So the boost along $x^1$ of the [[Lorentz transformation|WEVGN4C7PQ]] reads
$$x'^0 = x^0 \cosh \varphi - x^1 \sinh \varphi, \quad x'^1 = -x^0 \sinh \varphi + x^1 \cosh \varphi,$$
using the [[hyperbolic functions|01PPDSDP2N]].
Boosts along the same axis with rapidities $\varphi_1$ and $\varphi_2$ compose to the boost with rapidity $\varphi_1 + \varphi_2$, by the addition formulas for $\cosh$ and $\sinh$.
