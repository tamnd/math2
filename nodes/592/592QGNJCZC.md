---
tag: 592QGNJCZC
kind: definition
name: Woodin cardinal
msc: ["03E55", "03E60"]
defines: CMC2C1D53W
uses: [0EBACQFAZW, CGH8C8EA9N, 3SZADQXVZJ]
sources:
  - url: https://en.wikipedia.org/wiki/Woodin_cardinal
---

## Definition

Let $\kappa$ be a [[cardinal|0EBACQFAZW]].
For an ordinal $\gamma$, let $V_\gamma$ be the set of sets of rank less than $\gamma$ in the [[von Neumann universe|3SZADQXVZJ]].
The cardinal $\kappa$ is a *Woodin cardinal* if for every function $f \colon \kappa \to \kappa$ there is an ordinal $\alpha < \kappa$ such that:

1. $f(\beta) < \alpha$ for every $\beta < \alpha$.
2. There is an [[elementary embedding|CGH8C8EA9N]] $j \colon V \to M$, with $M$ a transitive class, whose critical point is $\alpha$.
3. $V_{j(f)(\alpha)} \subseteq M$.

## Remarks

If $\kappa$ is a Woodin cardinal, then $\kappa$ is Mahlo, and there are $\kappa$ measurable cardinals below $\kappa$.
Every supercompact cardinal is a Woodin cardinal.
A non-example: a measurable cardinal $\kappa$ that is the least measurable cardinal is not Woodin, since a Woodin cardinal has measurable cardinals below it.
Martin and Steel proved that if there are $n$ Woodin cardinals with a measurable cardinal above them all, then every $\Pi^1_{n+1}$ set of reals is determined.
