---
tag: NVMCZWHTZE
kind: definition
name: Brown–Peterson cohomology
msc: [55N22, 55P42]
defines: S8S72AA9C8
uses: [5CZHFNY9F3, BAW0T68GWK, TNHP7XXYZT, H28PSZR7XG, 01826KMG2H]
sources:
  - url: https://en.wikipedia.org/wiki/Brown–Peterson_cohomology
---

## Definition

Let $p$ be a [[prime number|01826KMG2H]], and let $\Z_{(p)}$ be the ring of rational numbers whose denominators are prime to $p$.
Let $MU_{(p)}$ be the $p$-localization of the [[complex cobordism|5CZHFNY9F3]] spectrum.
Quillen's idempotent is a map of [[ring spectra|BAW0T68GWK]] $e \colon MU_{(p)} \to MU_{(p)}$ with $e \circ e = e$.
On coefficients it sends the [[formal group law|TNHP7XXYZT]] of $MU_{(p)}$ to a $p$-typical one.
A formal group law is $p$-typical if its logarithm over $\Q$ has the form $\sum_{i \ge 0} \ell_i x^{p^i}$ with $\ell_0 = 1$.
The *Brown–Peterson spectrum* $BP$ (at $p$) is the image of $e$, that is, the homotopy colimit of $MU_{(p)} \xrightarrow{e} MU_{(p)} \xrightarrow{e} \cdots$.
*Brown–Peterson cohomology* is the [[generalized cohomology theory|H28PSZR7XG]] $BP^*(-)$ represented by $BP$.

## Remarks

The coefficient ring is $\pi_* BP \cong \Z_{(p)}[v_1, v_2, \ldots]$ with $\abs{v_i} = 2(p^i - 1)$.
With Hazewinkel's generators, the logarithm coefficients satisfy $p \ell_n = \sum_{i=0}^{n-1} \ell_i v_{n-i}^{p^i}$.
For example, $p \ell_1 = v_1$, so $\ell_1 = v_1 / p$.
The formal group law of $BP$ is the universal $p$-typical formal group law over a $\Z_{(p)}$-algebra.

Example: $MU_{(p)}$ is equivalent to a wedge $\bigvee_j \Sigma^{2 d_j} BP$, so $BP$ is a retract of $MU_{(p)}$, as an image of an idempotent should be.

Non-example: $MU_{(p)}$ itself is not $BP$, because $\pi_2 MU_{(p)} \cong \Z_{(p)}$ is nonzero for every $p$, while $\pi_2 BP = 0$ for $p$ odd since the first generator $v_1$ has degree $2(p - 1) \ge 4$.

Brown and Peterson first built $BP$ in 1966 by a different construction; Quillen's idempotent gives the description above.
