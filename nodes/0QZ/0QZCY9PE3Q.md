---
tag: 0QZCY9PE3Q
kind: definition
name: Presentation of a group
aliases: [generators-and-relations]
msc: [20F05]
defines: 0JGEQXQ4AC
uses: [020Z5SEN27, 0W77CVBCHQ, 0YYWCNTPWR, 085PND4KNT]
sources:
  - url: https://en.wikipedia.org/wiki/Presentation_of_a_group
    locator: Definition
  - url: https://en.wikipedia.org/wiki/Presentation_of_a_group
    locator: Finitely presented groups
---

## Definition

Let $S$ be a set, let $F_S$ be the [[free group|0KTW26C80J]] on $S$, and let $R \subseteq F_S$.
Let $N$ be the smallest [[normal subgroup|0CB0DX5BVV]] of $F_S$ that contains $R$, the normal closure of $R$.
The group with presentation $\langle S \mid R \rangle$ is the [[quotient group|0KYX2N69J0]] $F_S / N$.
A group $G$ has the presentation $\langle S \mid R \rangle$ when $G$ is [[isomorphic|08MG7H8JW5]] to $F_S / N$.

## Remarks

The elements of $S$ are the generators and the elements of $R$ are the relators; a relation $x = y$ stands for the relator $y^{-1} x$.
The cyclic group of order $n$ has the presentation $\langle a \mid a^n \rangle$, and the dihedral group of order $16$ has the presentation $\langle r, f \mid r^8, f^2, (r f)^2 \rangle$.
Each group has a presentation, and each finite group has a presentation with $S$ and $R$ finite.
A group is finitely presented when it has a presentation with $S$ and $R$ finite.

## Explanations

### L1 human

A presentation lists generators and the rules that they obey.
The group is the largest group that these generators make, subject only to these rules.
Presentations are often the shortest way to describe a group.
