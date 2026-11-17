---
tag: NXDWNMSF1Z
kind: proof
name: Proof that subgroups of abelian groups are normal
msc: ["20A05"]
topics: [E1506A5A55]
audience: ug1
proves: 0JPDTEDCFD
uses: [082GHNPJ53, 0X1JXT47GA, 0CB0DX5BVV]
methods: [0NTF6DMVAP]
sources:
  - url: https://en.wikipedia.org/wiki/Normal_subgroup
    locator: Examples
  - url: https://proofwiki.org/wiki/Subgroup_of_Abelian_Group_is_Normal
---

## Proof

1. Let $G$ be an [[abelian group|082GHNPJ53]] with identity $e$, and let $H$ be a [[subgroup|0X1JXT47GA]] of $G$.
2. Let $g \in G$ and $h \in H$.
3. $gh = hg$, because $G$ is abelian. This step uses the hypothesis that $G$ is abelian.
4. So $ghg^{-1} = (gh)g^{-1} = (hg)g^{-1} = h(gg^{-1}) = he = h$, by step 3 and associativity.
5. So $ghg^{-1} = h \in H$ for each $g \in G$ and each $h \in H$.
6. By the definition of a [[normal subgroup|0CB0DX5BVV]], $H$ is normal in $G$.

## Idea

Normality asks that conjugation keeps the elements of $H$ inside $H$.
In an abelian group, conjugation does not move any element at all.

## Variants

Step 3 uses commutativity only for the pairs $(g, h)$ with $h \in H$.
So the same proof shows that each subgroup of the centre of any group is normal.
