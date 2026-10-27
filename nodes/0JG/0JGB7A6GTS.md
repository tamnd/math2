---
tag: 0JGB7A6GTS
kind: definition
name: Rank of a linear map
msc: [15A03, 15A04]
defines: 0ZZXSBTR4J
uses: [0JB228DCWB, 05G2G0P224]
sources:
  - url: https://en.wikipedia.org/wiki/Rank_(linear_algebra)
    locator: lead section
inventory: [J89PWVW5GR]
---

## Definition

Let $F$ be a field, let $V$ and $W$ be vector spaces over $F$, and let $T \colon V \to W$ be a [[linear map|0NRYHJPQG2]].
The *rank* of $T$ is
$$\rank T = \dim \im T,$$
the [[dimension|03GSZ8RTZJ]] of the [[image|0WSFKKT6FF]] of $T$.

## Remarks

For the map $x \mapsto Ax$ of a matrix $A$, the rank is the [[rank of the matrix|0ZC9YTXZRY]].
The rank satisfies $\rank T \le \dim V$ and $\rank T \le \dim W$.
The [[rank–nullity theorem|0W4FSW1TVB]] relates the rank and the [[nullity|0APCFW7639]].
The rank of a composition satisfies $\rank(T \circ S) \le \min(\rank T, \rank S)$.

## Explanations

### L1 human

The rank of a linear map counts the dimensions of its output.
A map from space onto a plane has rank $2$.
The zero map has rank $0$.
