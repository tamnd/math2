---
tag: TW1KWXYWN0
kind: definition
name: Congruence-permutable variety
msc: [08B05, 08A30]
defines: 1B3N9T68YV
uses: [AJNZJD8442, DCSXXT4SER, 2BCES6NPYM, 0PYSR20HGF]
sources:
  - url: https://en.wikipedia.org/wiki/Congruence-permutable_algebra
---

## Definition

Let $\mathcal{V}$ be a [[variety|AJNZJD8442]] of algebras.
The variety $\mathcal{V}$ is *congruence permutable* if every algebra $A$ in $\mathcal{V}$ has [[permuting congruences|2BCES6NPYM]].
That is, for all [[congruences|DCSXXT4SER]] $\alpha$ and $\beta$ of $A$,
$$\alpha \circ \beta = \beta \circ \alpha,$$
where $\circ$ is the [[composition of relations|0PYSR20HGF]].

## Remarks

Example: the variety of groups is congruence permutable.
Congruences of a group $G$ correspond to normal subgroups, and the composition of the congruences of $M$ and $N$ is the congruence relation $a^{-1} b \in MN$.
Since $MN = NM$ for normal subgroups, the two compositions are equal.
Non-example: the variety of lattices is not congruence permutable.
In the chain $0 < 1 < 2$, let $\alpha$ identify $0$ and $1$, and let $\beta$ identify $1$ and $2$.
The pair $(0, 2)$ is in one composition, through $0 \mathrel{\alpha} 1 \mathrel{\beta} 2$.
It is not in the other, because the only element $\beta$-related to $0$ is $0$, and $0$ is not $\alpha$-related to $2$.
For a single algebra, the congruences $\alpha$ and $\beta$ permute if and only if $\alpha \circ \beta$ is the join $\alpha \vee \beta$ in the congruence lattice.

## Explanations

### L1 human

In a congruence-permutable variety, two ways of identifying elements can be applied in either order with the same result.
