---
tag: EB7FFD48W8
kind: definition
name: Elementary amenable group
msc: ["43A07", "20F65", "20F19"]
defines: N8RM4Q6W4S
uses: [G5S1M9, 082GHNPJ53, 0X1JXT47GA, 0KYX2N69J0, MF4N3VGGFV, X9HEQ29Q49, CEAT9BESKK]
sources:
  - url: https://en.wikipedia.org/wiki/Elementary_amenable_group
---

## Definition

The class $EG$ of *elementary amenable groups* is the smallest class of [[groups|G5S1M9]] with these properties.

1. $EG$ contains every finite group and every [[abelian group|082GHNPJ53]].
2. If $G \in EG$ and $H$ is a [[subgroup|0X1JXT47GA]] of $G$, then $H \in EG$.
3. If $G \in EG$ and $N$ is a normal subgroup of $G$, then the [[quotient|0KYX2N69J0]] $G/N$ is in $EG$.
4. If $N$ is a normal subgroup of $G$ with $N \in EG$ and $G/N \in EG$, then $G \in EG$; that is, $EG$ is closed under [[extensions|MF4N3VGGFV]].
5. If $G$ is the union of a family of subgroups in $EG$ that is directed by inclusion, then $G \in EG$.
So $EG$ is closed under [[directed unions|X9HEQ29Q49]].

A group is *elementary amenable* if it belongs to $EG$.

## Remarks

The intersection of all classes with properties 1 to 5 again has these properties, so the smallest such class exists.
Every elementary amenable group is [[amenable|CEAT9BESKK]], since the class of amenable groups has properties 1 to 5.

Example: the infinite dihedral group $D_\infty = \Z \rtimes \Z/2$ has the normal subgroup $\Z$ with quotient $\Z/2$.
Both are abelian, so $D_\infty$ is elementary amenable by property 4.
In the same way, every solvable group is elementary amenable, by induction on the length of its derived series.

Non-example: the free group $F_2$ on two generators is not elementary amenable, since it is not amenable.
The [[Grigorchuk group|M0WAT1VQZH]] is amenable but not elementary amenable, because it has intermediate growth, and no elementary amenable finitely generated group has intermediate growth.
