---
tag: N66FHFG5B6
kind: definition
name: Reduct and expansion of a structure
msc: ["03C07"]
topics: [AY09KYSW81]
audience: ug2
defines: EY20BF96SJ
uses: [983GZBQYT4, WDVVEYD6AT, CY1TXHF6KQ]
sources:
  - url: https://en.wikipedia.org/wiki/Reduct
    locator: Definition
  - book: isbn:9780387987606
    locator: Chapter 1
---

## Definition

Let $L \subseteq L'$ be [[signatures|WDVVEYD6AT]].

1. Let $\mathcal{M}'$ be an $L'$-[[structure|983GZBQYT4]] with domain $M$. The *reduct* $\mathcal{M}' \restriction L$ is the $L$-structure with domain $M$ and with $s^{\mathcal{M}' \restriction L} = s^{\mathcal{M}'}$ for each symbol $s$ of $L$.
2. An $L'$-structure $\mathcal{M}'$ is an *expansion* of an $L$-structure $\mathcal{M}$ when $\mathcal{M}' \restriction L = \mathcal{M}$.
3. An expansion $\mathcal{M}'$ of $\mathcal{M}$ is *definitional* when, for each symbol $s$ of $L' \setminus L$, the interpretation $s^{\mathcal{M}'}$ is [[definable|CY1TXHF6KQ]] without parameters in $\mathcal{M}$. For a relation symbol this means that the relation is $\emptyset$-definable, for a function symbol that its graph is $\emptyset$-definable, and for a constant symbol that the singleton is $\emptyset$-definable.
4. For $A \subseteq M$, the *expansion by constants* $\mathcal{M}_A$ is the expansion of $\mathcal{M}$ to $L_A = L \cup \set{c_a : a \in A}$, with new constant symbols $c_a$ and $c_a^{\mathcal{M}_A} = a$.

## Notation

Other notations for the reduct are $\mathcal{M}'|_L$ and $\mathcal{M}'|L$.
Many books write $(\mathcal{M}, a)_{a \in A}$ for $\mathcal{M}_A$.

## Remarks

Example: the ordered field $(\R, +, \cdot, <)$ has the reduct $(\R, +)$ to the signature $\set{+}$, with the same domain $\R$.

Non-example: $(\Z, +)$ is not a reduct of $(\Q, +, \cdot)$, because a reduct has the same domain as the original structure.

Every structure is a reduct and an expansion of itself, and a reduct of a reduct is a reduct.
The expansion of a structure to a larger signature is not unique: $(\Z, <)$ and $(\Z, >)$ are two expansions of the structure $\Z$ in the empty signature.

## Explanations

### L1 human

The reduct keeps the elements and forgets some of the operations or relations.
The expansion keeps the elements and adds new operations or relations.

### L2 human

We check that $(\Z, +, 0)$ is the reduct of $(\Z, +, \cdot, 0, 1)$ to $L = \set{+, 0}$.

1. The domain of the reduct is $\Z$, the same as the domain of the ring.
2. The symbol $+$ is interpreted as addition of integers in both.
3. The constant $0$ is interpreted as the integer $0$ in both.
4. The symbols $\cdot$ and $1$ are not in $L$, so they are forgotten.

A trap is to think that a reduct must be a substructure: the reduct changes the symbols, not the elements.
