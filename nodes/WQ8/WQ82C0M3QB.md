---
tag: WQ82C0M3QB
kind: concept
name: Chain complex
msc: [18G35]
sources:
  - url: https://en.wikipedia.org/wiki/Chain_complex
same_as:
  wikidata: Q1143328
  wikipedia: Chain complex
---

## Summary

A chain complex is a sequence of objects, such as abelian groups or modules, joined by morphisms $d_n \colon C_n \to C_{n-1}$ with $d_{n-1} \circ d_n = 0$.
The condition says that the image of each map lies in the kernel of the next, so the [[homology|2J4JJJYP22]] $\ker d_n / \im d_{n+1}$ is defined.
Chain complexes are the central objects of [[homological algebra|SAHAEZNCVD]].
They arise from topological spaces as in [[singular homology|M0Q5CFJ7ZH]], and from modules through resolutions.

## Explanations

### L1 human

A chain complex is a row of objects with maps going down one step at a time, such that two steps in a row always give zero.
In topology, $C_n$ is built from $n$-dimensional pieces of a space and $d_n$ takes the boundary of a piece.
The boundary of a boundary is empty, which is the rule $d \circ d = 0$.
A small algebraic example is $\cdots \to \Z/4\Z \xrightarrow{2} \Z/4\Z \xrightarrow{2} \Z/4\Z \to \cdots$, where doing "multiply by $2$" twice multiplies by $4$, which is $0$ in $\Z/4\Z$.
