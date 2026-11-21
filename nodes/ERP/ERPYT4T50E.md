---
tag: ERPYT4T50E
kind: example
name: The Rado graph indexed by itself is an indiscernible family
msc: ["03C30", "03C15", "05C80"]
topics: [W9CHA4PD9H]
audience: research
instance_of: [RQS808ZC8T]
uses: [RQS808ZC8T, RMXR0FEF54, H8VM37SSAX, DSQ17TNW1C, 9V71Q3SD1G, 4016QKAHFB]
sources:
  - url: https://en.wikipedia.org/wiki/Indiscernibles
    locator: Generalizations
  - url: https://en.wikipedia.org/wiki/Rado_graph
    locator: lead section
---

## Example

Let $R = (V, E)$ be the [[Rado graph|RMXR0FEF54]], as a structure in the signature $\set{E}$ with one binary relation.
Take $R$ both as the index structure and as the model, and let $a_v = v$ for $v \in V$.
We show that $(a_v)_{v \in R}$ is an $R$-indexed [[indiscernible family|RQS808ZC8T]] over $\emptyset$.

1. Let $\bar{u} = (u_1, \dots, u_n)$ and $\bar{v} = (v_1, \dots, v_n)$ have the same quantifier-free type in $R$. The atomic formulas are $x_k = x_l$ and $x_k E x_l$, so $u_k = u_l$ exactly when $v_k = v_l$, and $u_k E u_l$ exactly when $v_k E v_l$.
2. By the first equivalence, the map $u_k \mapsto v_k$ is well defined and injective on $\set{u_1, \dots, u_n}$.
3. By the second equivalence, it is an isomorphism between the induced subgraphs on $\set{u_1, \dots, u_n}$ and $\set{v_1, \dots, v_n}$.
4. The Rado graph is [[ultrahomogeneous|H8VM37SSAX]], so this isomorphism extends to an [[automorphism|DSQ17TNW1C]] $\sigma$ of $R$.
5. Automorphisms preserve all formulas, so $\bar{u}$ and $\bar{v}$ have the same [[type|9V71Q3SD1G]] in $R$. This is the condition of the definition, since $a_{\bar{u}} = \bar{u}$.

## Remarks

The example shows that the right index structure for a family can be richer than a linear order.
For any linear order on $V$, the family is not an [[order-indiscernible sequence|4016QKAHFB]].
Indeed, $R$ has an edge and a non-edge, and listing each pair in increasing order gives increasing pairs on which $x_1 E x_2$ has different truth values.
If one adds a parameter $w \in V$, the family is no longer indiscernible over $\set{w}$: the formula $x E w$ separates the neighbors of $w$ from the other vertices.
It becomes indiscernible over $\set{w}$ again for the index structure $R$ expanded by a constant for $w$, since automorphisms of $R$ that fix $w$ give the same argument.
The same steps work for every ultrahomogeneous relational structure, such as the Henson graphs and $(\Q, <)$.

## Explanations

### L1 human

The Rado graph is a network with infinitely many points, in which every possible finite pattern of links appears everywhere.
Take two pairs of points that are linked, for example.
There is a symmetry of the whole network that moves the first pair onto the second.
So nothing in the language of links can tell the two pairs apart, and the same holds for two unlinked pairs.

### L2 human

We check the definition for two pairs with an edge and one pair without.

1. Let $u_1 E u_2$ and $v_1 E v_2$, with $u_1 \ne u_2$ and $v_1 \ne v_2$. Then the two pairs have the same quantifier-free type.
2. The map $u_1 \mapsto v_1$, $u_2 \mapsto v_2$ is an isomorphism of induced subgraphs with one edge, so it extends to an automorphism.
3. So the formula $\exists z \, (z E x_1 \wedge \neg z E x_2)$ holds at $(u_1, u_2)$ exactly when it holds at $(v_1, v_2)$. By the extension property of $R$ it holds at both.
4. A pair $(w_1, w_2)$ with $w_1 \ne w_2$ and no edge has a different quantifier-free type, so the definition says nothing about it and $(u_1, u_2)$.

The typical use is as the model case of graph-indexed indiscernibles in the study of NIP theories.
The trap is to forget the equalities: a pair $(u, u)$ and a pair $(u, v)$ with $u \ne v$ have different quantifier-free types even if neither has an edge.
