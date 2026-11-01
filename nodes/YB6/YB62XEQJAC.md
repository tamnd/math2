---
tag: YB62XEQJAC
kind: object
name: Ree groups
msc: [20D06, 20G40, 20G41]
uses: [NPEBABQ49M, 0YMYMNQ0QZ, 0B85S2V2DR]
sources:
  - url: https://en.wikipedia.org/wiki/Ree_group
same_as:
  wikidata: Q7306554
  wikipedia: Ree group
---

## Description

The Ree groups are two infinite families of finite [[groups of Lie type|NPEBABQ49M]], found by Rimhak Ree.

1. For $q = 3^{2n+1}$ with $n \ge 0$, the group ${}^2G_2(q)$ is the subgroup of $G_2(\F_q)$ fixed by a twisted automorphism of characteristic $3$.
2. For $q = 2^{2n+1}$ with $n \ge 0$, the group ${}^2F_4(q)$ is the subgroup of $F_4(\F_q)$ fixed by a twisted automorphism of characteristic $2$.

Each twisted automorphism combines the exceptional graph automorphism of the Dynkin diagram with a field automorphism.
Their orders are
$$\abs{{}^2G_2(q)} = q^3 (q^3 + 1)(q - 1), \qquad \abs{{}^2F_4(q)} = q^{12} (q^6 + 1)(q^4 - 1)(q^3 + 1)(q - 1).$$
For $n \ge 1$ these groups are non-abelian [[simple groups|0YMYMNQ0QZ]].

## Remarks

The construction is possible because the algebraic group $G_2$ in characteristic $3$, and the algebraic group $F_4$ in characteristic $2$, has an exceptional endomorphism that exchanges long and short roots.
The smallest cases are not simple.
${}^2G_2(3)$ has order $1512$ and its [[commutator subgroup|0ASGSTXSBW]] is $\mathrm{SL}_2(\F_8)$, of index $3$.
${}^2F_4(2)$ has order $35942400$ and its commutator subgroup, of index $2$, is the [[Tits group|WC16TBY3FN]], which is simple.
The [[Suzuki groups|36X3GET13B]] arise from $B_2$ in characteristic $2$ in the same way.

## Explanations

### L1 human

The Ree groups are twisted versions of two exceptional matrix groups, $G_2$ and $F_4$, over special finite fields.
The twist is a symmetry that exists only in characteristic $3$ for $G_2$ and characteristic $2$ for $F_4$.
They give two more infinite families of finite simple groups.
