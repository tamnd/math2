---
tag: 9SDN6KYPA0
kind: definition
name: Conformal gravity
msc: [83D05, 53C18]
defines: 2FSTM4PBX0
uses: [BY4QYYS788, SBHY31HESP, GTVQFG2SH9]
sources:
  - url: https://en.wikipedia.org/wiki/Conformal_gravity
---

## Definition

Let $(M, g)$ be a four-dimensional [[Lorentzian manifold|BY4QYYS788]] and let $C_{abcd}$ be the [[Weyl tensor|SBHY31HESP]] of $g$.
*Conformal gravity* (Weyl gravity) is the theory of the metric $g$ with the action
$$S[g] = -\alpha \int_M C_{abcd} C^{abcd} \sqrt{-\det g} \; d^4x,$$
where $\alpha$ is a dimensionless coupling constant.
Its field equations, obtained by varying $g$, say that the Bach tensor
$$B_{ab} = \nabla^c \nabla^d C_{acbd} + \tfrac12 R^{cd} C_{acbd}$$
vanishes, where $R^{cd}$ is the Ricci tensor.

## Remarks

The action is invariant under the Weyl rescaling $g \mapsto \Omega^2 g$ for every smooth positive function $\Omega$ on $M$.
Indeed $C^a{}_{bcd}$ is unchanged, $C_{abcd}C^{abcd}$ is multiplied by $\Omega^{-4}$, and $\sqrt{-\det g}$ is multiplied by $\Omega^4$ in four dimensions.
Example: every Einstein metric, with $R_{ab} = \Lambda g_{ab}$, solves $B_{ab} = 0$, and so does every metric conformal to an Einstein metric.
Non-example: in dimension $n \ne 4$ the same integral is not Weyl invariant, since $\sqrt{-\det g}$ then scales by $\Omega^n$, which does not cancel $\Omega^{-4}$.
The theory belongs to [[conformal geometry|GTVQFG2SH9]]: it depends only on the conformal class of $g$.
