---
tag: JS7BWX3HW3
kind: definition
name: Substructure
msc: ["03C07"]
topics: [AY09KYSW81]
audience: ug2
defines: 676H7EGTKJ
uses: [983GZBQYT4, WDVVEYD6AT, 0BJR9QR08E]
formal:
  - system: lean4
    library: mathlib
    decl: FirstOrder.Language.Substructure
    match: exact
sources:
  - url: https://en.wikipedia.org/wiki/Substructure_(mathematics)
    locator: Definition
  - book: isbn:9780387987606
    locator: Chapter 1
---

## Definition

Let $L$ be a [[signature|WDVVEYD6AT]] and let $\mathcal{M}$ and $\mathcal{N}$ be $L$-[[structures|983GZBQYT4]] with domains $M$ and $N$.
The structure $\mathcal{N}$ is a substructure of $\mathcal{M}$, written $\mathcal{N} \subseteq \mathcal{M}$, when the following hold.

1. $N$ is a [[subset|0BJR9QR08E]] of $M$.
2. For each $n$-ary function symbol $f$, the map $f^{\mathcal{N}}$ is the restriction of $f^{\mathcal{M}}$ to $N^n$.
3. For each $n$-ary relation symbol $R$, $R^{\mathcal{N}} = R^{\mathcal{M}} \cap N^n$.
4. For each constant symbol $c$, $c^{\mathcal{N}} = c^{\mathcal{M}}$.

## Notation

We also say that $\mathcal{M}$ is an extension of $\mathcal{N}$.
In Mathlib, `FirstOrder.Language.Substructure L M` is the type of subsets of $M$ that are closed under every function symbol of $L$, where constants are the $0$-ary function symbols.
The Mathlib notion allows the empty set when $L$ has no constant symbols; most textbooks require the domain of a structure to be nonempty.

## Remarks

Clause 2 forces $N$ to be closed under each $f^{\mathcal{M}}$, and clause 4 forces $N$ to contain each $c^{\mathcal{M}}$.
Conversely, a nonempty subset of $M$ with these two closure properties is the domain of exactly one substructure of $\mathcal{M}$.

Example: in the signature $\set{+, -, 0}$, the set $2\Z$ of even integers is closed under $+$ and $-$ and contains $0$.
So it carries a substructure of $(\Z, +, -, 0)$.

Non-example: the set $\N$ is not the domain of a substructure of $(\Z, +, -, 0)$, because $-1 \notin \N$ although $1 \in \N$.
In the smaller signature $\set{+, 0}$, the set $\N$ is the domain of a substructure of $(\Z, +, 0)$.

## Explanations

### L1 human

A substructure is a part of a structure that is a structure on its own, with the same operations and relations.
In the signature of groups, the substructures of a group are its subgroups.

### L2 human

We check that $3\Z$ carries a substructure of $(\Z, +, -, 0, <)$.

1. Clause 1: $3\Z \subseteq \Z$.
2. Clause 2: for $3a, 3b \in 3\Z$, the sum $3(a + b)$ and the difference $3(a - b)$ lie in $3\Z$, so the restrictions of $+$ and $-$ map into $3\Z$.
3. Clause 3: the relation $<$ on $3\Z$ is the restriction of $<$ on $\Z$, by definition.
4. Clause 4: $0 = 3 \cdot 0 \in 3\Z$.

A trap is clause 3: a relation on $N$ that is smaller than the restriction, such as the empty relation, does not give a substructure.
