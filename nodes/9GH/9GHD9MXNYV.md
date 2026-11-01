---
tag: 9GHD9MXNYV
kind: concept
name: Idele class group
msc: [11R56, 11R37]
sources:
  - url: https://en.wikipedia.org/wiki/Adelic_algebraic_group
---

## Summary

The idele class group of a [[number field|MWBDFS2KJ5]] $K$ is the quotient $C_K = I_K / K^\times$ of the idele group $I_K$ by the nonzero elements of $K$.
The idele group $I_K$ is the group of units of the [[adele ring|SEH68BA1QQ]] of $K$, with its own restricted product topology.
In [[class field theory|BEKCEYHCHX]], the [[Artin reciprocity map|7938EKMMVR]] goes from $C_K$ onto the Galois group of the maximal abelian extension of $K$.
The finite abelian extensions of $K$ then match the open subgroups of finite index of $C_K$.

## Explanations

### L1 human

An idele is a list with one nonzero entry for each completion of $K$, one entry for every [[place|BT5V3TSNY6]].
Almost all entries must be units, so the list is "small" at almost every prime.
The number field $K$ sits inside diagonally: an element $a$ gives the list $(a, a, a, \ldots)$.
Dividing out by these lists gives the idele class group.
For $K = \Q$, every idele is a rational number times an idele with a positive real entry and unit entries at all primes.
So $C_\Q$ is the product of the positive reals and the group $\prod_p \Z_p^\times$.
