---
tag: BCJD3SR975
kind: definition
name: H-space
msc: [55P45]
defines: EASHTX8EG5
uses: [T9DG8DDE75, F2F143KQ2M, JX47MS1R1H]
sources:
  - url: https://en.wikipedia.org/wiki/H-space
---

## Definition

An *H-space* is a [[pointed space|T9DG8DDE75]] $(X, e)$ together with a continuous map $\mu \colon X \times X \to X$ with these properties.

1. $\mu(e, e) = e$.
2. The map $X \to X$, $x \mapsto \mu(e, x)$, is [[homotopic|F2F143KQ2M]] to $\id_X$ through pointed maps.
3. The map $X \to X$, $x \mapsto \mu(x, e)$, is homotopic to $\id_X$ through pointed maps.

## Remarks

Some authors drop the condition that the homotopies fix $e$; for CW complexes the two definitions give the same class of spaces.
An H-space is *homotopy associative* if $\mu \circ (\mu \times \id) \simeq \mu \circ (\id \times \mu)$, and *homotopy commutative* if $\mu \simeq \mu \circ \tau$, where $\tau$ swaps the factors.

Example: every topological group $G$ with $e$ its identity and $\mu$ its multiplication is an H-space, since $\mu(e, x) = \mu(x, e) = x$ on the nose.

Example: the [[loop space|2JFF5F3EGF]] $\Omega Y$ with concatenation of loops is an H-space; the constant loop is a unit up to the standard reparametrization homotopy.

Non-example: $S^2$ admits no such $\mu$.
If it did, let $x \in H^2(S^2; \Z)$ be a generator; the unit condition forces $\mu^*(x) = x \times 1 + 1 \times x$ in $H^2(S^2 \times S^2; \Z)$.
Then $0 = \mu^*(x^2) = (x \times 1 + 1 \times x)^2 = 2 (x \times x)$ for the [[cup product|JX47MS1R1H]], which is false since $x \times x$ generates $H^4(S^2 \times S^2; \Z) \cong \Z$.
