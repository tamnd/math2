---
tag: YT42EZ7GQQ
kind: statement
role: theorem
name: Annihilator duality
msc: [43A40, 22B05]
uses: [ZR09S9R3AW, FMW57WNPDB, H1WNVN5V7F, 0KYX2N69J0, QTVC6F2P9D]
about: [FMW57WNPDB]
sources:
  - url: https://en.wikipedia.org/wiki/Pontryagin_duality
---

## Statement

Let $G$ be a [[locally compact abelian group|ZR09S9R3AW]] and let $\widehat{G}$ be its [[Pontryagin dual|FMW57WNPDB]].
Identify $G$ with the dual of $\widehat{G}$ by the [[Pontryagin duality theorem|QTVC6F2P9D]].
For a closed subgroup $H$ of $G$, its *annihilator* is
$$H^\perp = \set{\chi \in \widehat{G} : \chi(h) = 1 \text{ for all } h \in H}.$$
Then the following hold.

1. $H^\perp$ is a closed subgroup of $\widehat{G}$, and $(H^\perp)^\perp = H$.
2. The map that sends $\chi \in H^\perp$ to the [[character|H1WNVN5V7F]] $xH \mapsto \chi(x)$ of the [[quotient group|0KYX2N69J0]] $G/H$ is an isomorphism of topological groups $H^\perp \to \widehat{G/H}$.
3. Restriction $\chi \mapsto \chi|_H$ induces an isomorphism of topological groups $\widehat{G}/H^\perp \to \widehat{H}$.
4. The map $H \mapsto H^\perp$ is an inclusion-reversing bijection from the closed subgroups of $G$ onto the closed subgroups of $\widehat{G}$.

## Remarks

Proof idea: a continuous character of $G/H$ composed with the quotient map is a character of $G$ trivial on $H$, and every such character arises this way, which gives 2.
The inclusion $H \subseteq (H^\perp)^\perp$ is clear.
For the reverse, if $x \notin H$, then $xH$ is not the identity of the locally compact abelian group $G/H$, and the characters of $G/H$ separate points, so some $\chi \in H^\perp$ has $\chi(x) \ne 1$.
Statement 3 follows from 2 applied to the subgroup $H^\perp$ of $\widehat{G}$, together with duality.

Example: let $G = \R$ with characters $\chi_\xi(x) = e^{2\pi i \xi x}$, and let $H = \Z$.
Then $\chi_\xi$ is trivial on $\Z$ exactly when $\xi \in \Z$, so $H^\perp \cong \Z$, which is the dual of the circle $\R/\Z$.
Also $\widehat{\R}/H^\perp \cong \R/\Z$, which is the dual of $\Z$.

The subgroup must be closed.
For the dense subgroup $\Q$ of $\R$, a continuous character trivial on $\Q$ is trivial on $\R$, so $\Q^\perp$ is trivial and $(\Q^\perp)^\perp = \R \ne \Q$.

## Explanations

### L1 human

A subgroup $H$ of $G$ is matched with the set of waves on $G$ that do not see $H$, that is, that are constant equal to $1$ on it.
Big subgroups give few such waves and small subgroups give many.
This matching is perfect for closed subgroups, and it swaps subgroups with quotients.

### L2 human

Annihilator duality is the group form of the duality between subspaces and their annihilators in linear algebra.
It is used to compute duals of quotients and subgroups, for example $\widehat{\R/\Z} = \Z$ from $\Z^\perp$ in $\widehat{\R}$.
It is the setting of the Poisson summation formula, where a sum over $H$ equals a sum over $H^\perp$.
It also shows that a closed subgroup $H$ is determined by the characters that are trivial on it.
This makes it a tool in the structure theory of locally compact abelian groups.
