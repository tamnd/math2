---
tag: ~fbf8ec6c
kind: statement
role: proposition
name: Subgroups of abelian groups are normal
msc: [20A05]
uses: [~4f5a4072, ~914d79a4]
sources:
  - url: https://en.wikipedia.org/wiki/Normal_subgroup
    locator: Examples
---

## Statement

Let $G$ be an [[abelian group|~b6df27fe]] and let $H$ be a [[subgroup|~b600248b]] of $G$.
Then $H$ is [[normal|~ebf813cb]] in $G$.

## Remarks

For $g \in G$ and $h \in H$, commutativity gives $ghg^{-1} = hgg^{-1} = h \in H$.
The converse is false: in the quaternion group $Q_8$ each subgroup is normal, but $Q_8$ is not abelian.
More generally, each subgroup of the center of any group is normal.

## Explanations

### L1 human

In an abelian group, conjugation does nothing, because $ghg^{-1} = h$.
So a subgroup can never be moved by conjugation.
Thus all subgroups are normal.
