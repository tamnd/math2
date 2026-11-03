---
tag: NXDWNMSF1Z
kind: proof
name: Proof that subgroups of abelian groups are normal
msc: [20A05]
proves: 0JPDTEDCFD
uses: [071DDFVG4J, 0N0PXCTYA7, 0W77CVBCHQ]
sources:
  - url: https://proofwiki.org/wiki/Subgroup_of_Abelian_Group_is_Normal
---

## Proof

1. Let $G$ be an [[abelian group|071DDFVG4J]] with identity $e$, and let $H$ be a [[subgroup|0N0PXCTYA7]] of $G$.
2. Let $g \in G$ and $h \in H$. Since $G$ is abelian, $gh = hg$.
3. Hence $ghg^{-1} = hgg^{-1} = he = h$.
4. So $ghg^{-1} = h \in H$ for all $g \in G$ and $h \in H$.
5. By the definition of a [[normal subgroup|0W77CVBCHQ]], $H$ is normal in $G$.

## Idea

Normality asks that conjugating an element of $H$ keeps it in $H$. In an abelian group, conjugation does not move any element at all.
