---
tag: JS7BWX3HW3
kind: definition
name: Substructure
msc: [03C07]
defines: 676H7EGTKJ
uses: [983GZBQYT4, WDVVEYD6AT, 0BJR9QR08E]
sources:
  - url: https://en.wikipedia.org/wiki/Substructure_(mathematics)
---

## Definition

Let $L$ be a [[signature|WDVVEYD6AT]] and let $\mathcal{M}$ and $\mathcal{N}$ be $L$-[[structures|983GZBQYT4]] with domains $M$ and $N$.
The structure $\mathcal{N}$ is a substructure of $\mathcal{M}$, written $\mathcal{N} \subseteq \mathcal{M}$, when the following hold.

1. $N$ is a [[subset|0BJR9QR08E]] of $M$.
2. For each $n$-ary function symbol $f$, the map $f^{\mathcal{N}}$ is the restriction of $f^{\mathcal{M}}$ to $N^n$.
3. For each $n$-ary relation symbol $R$, $R^{\mathcal{N}} = R^{\mathcal{M}} \cap N^n$.
4. For each constant symbol $c$, $c^{\mathcal{N}} = c^{\mathcal{M}}$.

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
