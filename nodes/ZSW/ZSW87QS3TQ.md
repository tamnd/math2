---
tag: ZSW87QS3TQ
kind: definition
name: Lie derivative
msc: [53A45, 58A10]
defines: PJWK0PKN6Q
uses: [F45VQ47GPV, WX302T93TW, 06738GGWWK, 68FGQEBD6J]
sources:
  - url: https://en.wikipedia.org/wiki/Lie_derivative
---

## Definition

Let $M$ be a smooth manifold, let $X$ be a smooth vector field on $M$, and let $\varphi_t$ be the local [[flow|06738GGWWK]] of $X$.
Let $T$ be a smooth [[tensor field|WX302T93TW]] on $M$, and let $\varphi_t^* T$ be its pullback by the local diffeomorphism $\varphi_t$.
The *Lie derivative* of $T$ along $X$ is the tensor field $\mathcal{L}_X T$ given at each $p \in M$ by
$$(\mathcal{L}_X T)_p = \frac{d}{dt}\Big|_{t = 0} (\varphi_t^* T)_p.$$

## Remarks

For a smooth function $f$, $\mathcal{L}_X f = X f$, the derivative of $f$ in the direction of $X$.
For a vector field $Y$, $\mathcal{L}_X Y = [X, Y]$, the [[Lie bracket|68FGQEBD6J]].
For a differential form $\omega$, Cartan's formula gives $\mathcal{L}_X \omega = d(\iota_X \omega) + \iota_X d\omega$.
Example: on $\R^2$ let $X = -y \, \partial_x + x \, \partial_y$ and $f = x^2 + y^2$; then $\mathcal{L}_X f = -y \cdot 2x + x \cdot 2y = 0$, as $f$ is invariant under the rotations $\varphi_t$.
Non-example of tensoriality: $\mathcal{L}_X Y$ is not $C^\infty(M)$-linear in $X$, since $\mathcal{L}_{fX} Y = f [X, Y] - (Y f) X$.
So $(\mathcal{L}_X T)_p$ depends on $X$ near $p$, not only on $X_p$; this is the difference with a covariant derivative.
The Lie derivative is a derivation: $\mathcal{L}_X (S \otimes T) = \mathcal{L}_X S \otimes T + S \otimes \mathcal{L}_X T$, and it commutes with contractions.
