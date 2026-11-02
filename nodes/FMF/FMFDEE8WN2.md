---
tag: FMFDEE8WN2
kind: definition
name: Amalgamated free product
msc: [08B25, "20E06"]
defines: M848AHBRCM
uses: [AJNZJD8442, KBXSZC6BV1, HHNWHS1XTN]
sources:
  - url: https://en.wikipedia.org/wiki/Free_product
---

## Definition

Let $\mathcal{V}$ be a [[variety|AJNZJD8442]] of algebras and let $A$ be an algebra in $\mathcal{V}$.
Let $(B_i)_{i \in I}$ be a family of algebras in $\mathcal{V}$ with [[homomorphisms|KBXSZC6BV1]] $\alpha_i \colon A \to B_i$.
Call a family of homomorphisms $g_i \colon B_i \to D$ *compatible* if $g_i \circ \alpha_i = g_j \circ \alpha_j$ for all $i, j \in I$.
An *amalgamated free product* of the $B_i$ over $A$ is an algebra $C$ in $\mathcal{V}$ with homomorphisms $\beta_i \colon B_i \to C$ such that:

1. the family $(\beta_i)_{i \in I}$ is compatible;
2. for every algebra $D$ in $\mathcal{V}$ and every compatible family $g_i \colon B_i \to D$, there is a unique homomorphism $g \colon C \to D$ with $g \circ \beta_i = g_i$ for all $i$.

It is written $\mathop{\ast}_A B_i$, or $B_1 *_A B_2$ for two factors.

## Remarks

The amalgamated free product exists in every variety and is unique up to a unique compatible isomorphism.
It is the quotient of the [[free product|HHNWHS1XTN]] of the $B_i$ by the smallest congruence that identifies the images of $\alpha_i(a)$ and $\alpha_j(a)$ for all $a \in A$ and $i, j \in I$.
With $A$ the trivial group in the variety of groups, it is the free product.
Usually the $\alpha_i$ are embeddings; whether the $\beta_i$ are then embeddings depends on the variety, and for groups they always are.

Example: in the variety of groups, $\Z/4\Z *_{\Z/2\Z} \Z/6\Z$, with $\Z/2\Z$ mapped to the subgroups of order $2$, is isomorphic to $SL_2(\Z)$.

Non-example: in groups, the direct product $\Z \times \Z$ with the two coordinate inclusions is not $\Z *_{\set{0}} \Z$.
Clause 2 fails for $D = S_3$ and $g_1, g_2$ sending $1$ to two non-commuting transpositions, since the generators of $\Z \times \Z$ commute.

In Mathlib the construction for monoids and groups is `Monoid.PushoutI`.
