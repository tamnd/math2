---
tag: 0JPDTEDCFD
kind: statement
role: proposition
name: Subgroups of abelian groups are normal
msc: [20A05]
uses: [0W77CVBCHQ, 071DDFVG4J]
sources:
  - url: https://en.wikipedia.org/wiki/Normal_subgroup
    locator: Examples
---

## Statement

Let $G$ be an [[abelian group|082GHNPJ53]] and let $H$ be a [[subgroup|0X1JXT47GA]] of $G$.
Then $H$ is [[normal|0CB0DX5BVV]] in $G$.

## Remarks

For $g \in G$ and $h \in H$, commutativity gives $ghg^{-1} = hgg^{-1} = h \in H$.
The converse is false: in the quaternion group $Q_8$ each subgroup is normal, but $Q_8$ is not abelian.
More generally, each subgroup of the center of any group is normal.

## Explanations

### L1 human

In an abelian group, conjugation does nothing, because $ghg^{-1} = h$.
So a subgroup can never be moved by conjugation.
Thus all subgroups are normal.
