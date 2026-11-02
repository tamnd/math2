---
tag: WZC2MN3CX3
kind: definition
name: Fiber of a morphism
msc: [14A15]
defines: 963QWX2E2Z
uses: [JXRKH6P1Z4, 1DZMT4S9FB, G51E8MW7J1]
sources:
  - url: https://en.wikipedia.org/wiki/Fiber_product_of_schemes
---

## Definition

Let $f \colon X \to Y$ be a [[morphism of schemes|JXRKH6P1Z4]] and let $y \in Y$.
Let $\kappa(y)$ be the [[residue field|G51E8MW7J1]] of $Y$ at $y$.
Let $\iota_y \colon \operatorname{Spec} \kappa(y) \to Y$ be the canonical morphism with image $y$.
The *fiber* of $f$ over $y$ is the [[fiber product|1DZMT4S9FB]]
$$X_y = X \times_Y \operatorname{Spec} \kappa(y),$$
taken with respect to $f$ and $\iota_y$.
It is a scheme over $\kappa(y)$.

## Remarks

The projection $X_y \to X$ is a homeomorphism of the underlying space of $X_y$ onto $f^{-1}(y)$.
Example: let $f \colon \operatorname{Spec} \Z[i] \to \operatorname{Spec} \Z$ and $y = (p)$ for a prime $p$.
Then $X_y = \operatorname{Spec}(\Z[i] \otimes_\Z \F_p) = \operatorname{Spec} \F_p[x]/(x^2 + 1)$.
For $p = 5$ this is $\operatorname{Spec} \F_5[x]/((x-2)(x+2))$, two points.
For $y = (0)$ the fiber is $\operatorname{Spec} \Q(i)$, the generic fiber.
Non-example: the fiber is in general not the reduced point structure on $f^{-1}(y)$.
Let $k$ be a field with $2 \ne 0$, let $f \colon \operatorname{Spec} k[t] \to \operatorname{Spec} k[x]$ be given by $x \mapsto t^2$, and let $y = (x)$.
Then $X_y = \operatorname{Spec} k[t]/(t^2)$, which is not reduced, while the single point of $f^{-1}(y)$ with its reduced structure is $\operatorname{Spec} k$.
