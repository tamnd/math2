---
tag: YAVH4RAEYJ
kind: definition
name: Lattice of subvarieties
msc: [08B15]
defines: GJAYCVYZYF
uses: [4YSCK1DF26, AJNZJD8442, D7A0ZGZT5S, 2R8QQTP1CE]
sources:
  - url: https://en.wikipedia.org/wiki/Variety_(universal_algebra)
---

## Definition

Let $\mathcal{V}$ be a [[variety|AJNZJD8442]] of algebras.
The *lattice of subvarieties* of $\mathcal{V}$ is the set $L(\mathcal{V})$ of all [[subvarieties|4YSCK1DF26]] of $\mathcal{V}$, ordered by inclusion.
In it, the meet of a family $(\mathcal{W}_i)_{i \in I}$ is the intersection $\bigcap_i \mathcal{W}_i$.
The join is the smallest subvariety that contains $\bigcup_i \mathcal{W}_i$, which is $HSP\left(\bigcup_i \mathcal{W}_i\right)$.

## Remarks

An intersection of varieties is a variety, since it is defined by the union of their identities.
So $L(\mathcal{V})$ is a [[complete lattice|D7A0ZGZT5S]], with least element the trivial variety and greatest element $\mathcal{V}$.
The maps $\mathcal{W} \mapsto \operatorname{Id}(\mathcal{W})$ and $T \mapsto \operatorname{Mod}(T)$ are inverse dual isomorphisms between $L(\mathcal{V})$ and the [[lattice of equational theories|2R8QQTP1CE]] that contain $\operatorname{Id}(\mathcal{V})$.
Example: for the variety of Boolean algebras, $L(\mathcal{V})$ has exactly two elements, the trivial variety and $\mathcal{V}$ itself.
Example: for abelian groups, the subvarieties are $\mathcal{A}_n = \operatorname{Mod}(nx \approx 0)$ for $n \ge 1$ and the whole variety, and $\mathcal{A}_n \subseteq \mathcal{A}_m$ if and only if $n \mid m$.
Non-example: the join is not the union in general, since the union of $\mathcal{A}_2$ and $\mathcal{A}_3$ does not contain $\Z / 2\Z \times \Z / 3\Z \in \mathcal{A}_6$.
