---
tag: 7WVVST5TTY
kind: definition
name: Cauchy elastic material
msc: [74B20, 74A20]
defines: DV71K7X1JD
uses: [HTYRR2WDQ6, KG2XWEMJ30, Q4C55V47A8, EZQ0E262QV]
sources:
  - url: https://en.wikipedia.org/wiki/Cauchy_elastic_material
---

## Definition

Let a body occupy a reference configuration $\mathcal{B} \subset \R^3$, and let $\mathrm{M}^3_+$ be the set of real $3 \times 3$ matrices with positive determinant.
For a deformation of the body, let $F(X)$ be its [[deformation gradient|HTYRR2WDQ6]] at $X \in \mathcal{B}$.
Let $\sigma$ be the [[Cauchy stress tensor|KG2XWEMJ30]] at the image point of $X$.
The material is *Cauchy elastic* if there is a function $\mathcal{G} \colon \mathrm{M}^3_+ \times \mathcal{B} \to \mathrm{Sym}(3)$, the response function, such that for every deformation and every $X \in \mathcal{B}$,
$$\sigma = \mathcal{G}(F(X), X).$$
The [[principle of material frame-indifference|EZQ0E262QV]] requires in addition $\mathcal{G}(QF, X) = Q \, \mathcal{G}(F, X) \, Q^T$ for every rotation $Q \in SO(3)$.

## Remarks

The relation $\sigma = \mathcal{G}(F)$ is a [[constitutive equation|Q4C55V47A8]].
The material is homogeneous if $\mathcal{G}$ does not depend on $X$.
Example: the compressible material with $\mathcal{G}(F) = \mu (FF^T - I)/\det F$ for a constant $\mu > 0$ is Cauchy elastic, and $\mathcal{G}(QF) = \mu(QFF^TQ^T - QQ^T)/\det F = Q\mathcal{G}(F)Q^T$, so it is frame-indifferent.
Non-example: a viscous fluid, with $\sigma = -pI + 2\eta D$ where $D$ is the rate of deformation, is not Cauchy elastic.
Its stress depends on the rate of deformation and not on $F$ alone.
A Cauchy elastic material need not have a stored energy; the work done by the stress around a closed cycle of deformations can be nonzero.

## Explanations

### L1 human

The stress is a fixed function of the local deformation gradient.
So the same shape always gives the same stress, whatever happened before.
