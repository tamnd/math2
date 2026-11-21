---
tag: KA80AZB1CX
kind: definition
name: Joint embedding property
msc: ["03C52"]
topics: [ZS8X8KS54R]
audience: grad
defines: 59FQ5Q2B8R
uses: [983GZBQYT4, WDVVEYD6AT, SCRB74SWQN, FZRMYTQFRR]
sources:
  - url: https://en.wikipedia.org/wiki/Joint_embedding_property
  - book: isbn:9780521587136
---

## Definition

Let $L$ be a [[signature|WDVVEYD6AT]], and let $\mathcal{K}$ be a class of [[$L$-structures|983GZBQYT4]] closed under isomorphism.
The class $\mathcal{K}$ has the *joint embedding property* if for all $A, B \in \mathcal{K}$ there are $C \in \mathcal{K}$ and [[embeddings|SCRB74SWQN]] $f \colon A \to C$ and $g \colon B \to C$.
A [[first-order theory|FZRMYTQFRR]] $T$ in $L$ has the joint embedding property if the class of models of $T$ has it.

## Notation

The property is abbreviated JEP.
No condition is placed on $f(A) \cap g(B)$.

## Remarks

Example: the class of finite graphs has JEP, since the disjoint union of $A$ and $B$ contains both as induced subgraphs; see [[this example|S7AMR4PSH0]].

Non-example: the class of finite fields fails JEP, since $\mathbb{F}_2$ and $\mathbb{F}_3$ have different characteristics; see [[this non-example|8DQKEDXM8S]].

If $\mathcal{K}$ has the [[amalgamation property|XSCSX39GEZ]] and some $A_0 \in \mathcal{K}$ embeds into every member, then $\mathcal{K}$ has JEP: amalgamate over $A_0$.

## Explanations

### L1 human

Any two members of the class fit together inside one member of the class.

### L2 human

We joint-embed two finite linear orders.

1. Let $A = \set{a_1 < a_2}$ and $B = \set{b_1}$.
2. Let $C = \set{1 < 2 < 3}$, with $a_i \mapsto i$ and $b_1 \mapsto 3$.
3. Both maps preserve and reflect the order, so they are embeddings.

A trap is to require the images to be disjoint; overlapping images are also allowed.
