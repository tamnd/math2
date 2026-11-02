---
tag: MC4EFHWRJG
kind: definition
name: Kleinian group
msc: [30F40, 57K32, 20H10]
defines: 27QRARKWD5
uses: [5M7D1BSHVZ, J58ED1GV6N, 0SG74WBFA2, 0J78KBPFZB]
sources:
  - url: https://en.wikipedia.org/wiki/Kleinian_group
---

## Definition

Let $\mathrm{PSL}_2(\C) = \mathrm{SL}_2(\C) / \set{\pm I}$, where [[SL(2,C)|J58ED1GV6N]] has the topology of a subset of $\C^4$ and $\mathrm{PSL}_2(\C)$ has the quotient topology.
A *Kleinian group* is a [[discrete subgroup|5M7D1BSHVZ]] of $\mathrm{PSL}_2(\C)$.

## Remarks

The group $\mathrm{PSL}_2(\C)$ acts on the [[Riemann sphere|0J78KBPFZB]] by [[Möbius transformations|0SG74WBFA2]] and on hyperbolic $3$-space $\mathbb H^3$ by isometries.
A subgroup is Kleinian if and only if its action on $\mathbb H^3$ is properly discontinuous.
Some authors also require that the group act properly discontinuously on a nonempty open subset of the Riemann sphere.

Example: the Picard group $\mathrm{PSL}_2(\Z[i])$, of matrices with Gaussian integer entries, is Kleinian.
Distinct Gaussian integers are at distance at least $1$, so a small neighbourhood of $\pm I$ contains no other element of the group.

Non-example: the group $\mathrm{PSL}_2(\Z[\sqrt2])$ is not Kleinian.
It contains the translations $z \mapsto z + a + b\sqrt2$ with $a, b \in \Z$, and their translation lengths come arbitrarily close to $0$ without being $0$.
