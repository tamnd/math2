---
tag: AW9FV2ARXF
kind: definition
name: Principle of material frame-indifference
msc: [74A20]
defines: EZQ0E262QV
uses: [Q4C55V47A8, KG2XWEMJ30, HTYRR2WDQ6, X0SSN8AM7G, 0TKYAEJ8N7, 0CGYNDCWRR]
sources:
  - url: https://en.wikipedia.org/wiki/Objective_stress_rate
---

## Definition

A *change of observer* is a map $x \mapsto x^* = c(t) + Q(t)\, x$ of $\R^3$, where $c(t) \in \R^3$.
Here $Q(t)$ is a rotation, that is, an element of the [[special orthogonal group|0CGYNDCWRR]] $SO(3)$.
Under a change of observer the [[deformation gradient|HTYRR2WDQ6]] becomes $F^* = Q F$, and a frame-indifferent (objective) tensor field $T$, such as the [[Cauchy stress tensor|KG2XWEMJ30]], becomes $T^* = Q T Q^T$.
The *principle of material frame-indifference* states that a [[constitutive equation|Q4C55V47A8]] must keep the same form under every change of observer.
For an elastic material with $\sigma = \hat\sigma(F)$ it reads
$$\hat\sigma(Q F) = Q\, \hat\sigma(F)\, Q^T \quad \text{for all } Q \in SO(3) \text{ and all } F \text{ with } \det F > 0.$$

## Remarks

The function $\hat\sigma(F) = \mu (F F^T - I)$, with $\mu \in \R$, satisfies the principle: $\hat\sigma(QF) = \mu (Q F F^T Q^T - I) = Q \hat\sigma(F) Q^T$, using $Q Q^T = I$.
The function $\hat\sigma(F) = \mu (F + F^T - 2I)$ with $\mu \neq 0$ does not: for $F = I$ it gives $\hat\sigma(Q) = \mu(Q + Q^T - 2I)$, which is nonzero for a rotation $Q \neq I$, while $Q \hat\sigma(I) Q^T = 0$.
By the [[polar decomposition|X0SSN8AM7G]] $F = R U$, the principle holds exactly when $\hat\sigma(F) = R\, \hat\sigma(U)\, R^T$ for all $F$, so the response is fixed by its values on the stretch tensors $U$.
Some authors allow $Q$ in the full [[orthogonal group|0TKYAEJ8N7]], including reflections.

## Explanations

### L1 human

The principle says that a material does not care who is watching.
A rigid rotation of the whole body should rotate the stress and nothing more.
