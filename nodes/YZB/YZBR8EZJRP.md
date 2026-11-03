---
tag: YZBR8EZJRP
kind: definition
name: Deceleration parameter
msc: ["83F05"]
defines: QF1K65J7HD
uses: [J70F32P86W, ECJMS4VDTF]
sources:
  - url: https://en.wikipedia.org/wiki/Deceleration_parameter
---

## Definition

Let $a \colon I \to (0, \infty)$ be the [[scale factor|J70F32P86W]] of a [[Friedmann–Lemaître–Robertson–Walker metric|ECJMS4VDTF]], twice differentiable, and let $t \in I$ with $\dot a(t) \neq 0$.
The *deceleration parameter* at time $t$ is
$$q(t) = -\frac{a(t)\, \ddot a(t)}{\dot a(t)^2}.$$

## Remarks

With the Hubble parameter $H = \dot a / a$, one has $q = -1 - \dot H / H^2$.
Example: for $a(t) = t^{2/3}$, $\dot a = \tfrac{2}{3} t^{-1/3}$ and $\ddot a = -\tfrac{2}{9} t^{-4/3}$, so $q = \tfrac{2}{9} / \tfrac{4}{9} = \tfrac{1}{2}$.
For $a(t) = e^{Ht}$ with $H$ constant, $q = -1$.
Non-example: for a static model, $\dot a = 0$, so $q$ is not defined.
The sign of $q$ is opposite to the sign of $\ddot a$: $q < 0$ exactly when the expansion accelerates.
For a mixture of perfect fluids with constant equation of state parameters $w_i$ and density parameters $\Omega_i$, the second Friedmann equation gives $q = \tfrac{1}{2} \sum_i \Omega_i (1 + 3 w_i)$.
