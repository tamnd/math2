---
tag: TJKANTKASZ
kind: concept
name: Finitely presented group
msc: [20F05]
specializes: [082DWWXMRJ]
sources:
  - url: https://en.wikipedia.org/wiki/Presentation_of_a_group
---

## Summary

A finitely presented group is a group that has a [[presentation|0JGEQXQ4AC]] with finitely many generators and finitely many relations.
Such a group can be described by a finite amount of data, so it can be handled by algorithms and computers.
Finitely presented groups are the natural objects of combinatorial group theory and arise as fundamental groups of compact manifolds and finite complexes.

## Explanations

### L1 human

A finitely presented group is given by a finite list of letters and a finite list of rules that say which words equal the identity.
For example, $\langle a, b \mid a b a^{-1} b^{-1} \rangle$ has two letters and one rule, $ab = ba$, and it is the group $\Z^2$.
Every finite group is finitely presented, since its whole multiplication table is a finite list of rules.
Some finitely generated groups need infinitely many rules, however one chooses the generators.
