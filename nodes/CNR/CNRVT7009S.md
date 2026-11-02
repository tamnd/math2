---
tag: CNRVT7009S
kind: definition
name: Turing degree
msc: [03D28, 03D30]
defines: P5N2ND3VCG
uses: [PA4PYQ1PZ0, PPGD5KW8JC]
sources:
  - url: https://en.wikipedia.org/wiki/Turing_degree
---

## Definition

Let $\le_T$ be [[Turing reducibility|PA4PYQ1PZ0]] on subsets of $\N$, and let $A \equiv_T B$ mean $A \le_T B$ and $B \le_T A$.
The relation $\equiv_T$ is an equivalence relation on the power set of $\N$.
The *Turing degree* of a set $A \subseteq \N$ is its equivalence class
$$\deg(A) = \set{B \subseteq \N : B \equiv_T A}.$$
The degrees are partially ordered by $\deg(A) \le \deg(B)$ if and only if $A \le_T B$; this does not depend on the choice of representatives.

## Remarks

Example: the set $E$ of even numbers and the set $\set{0}$ have the same degree.
Both are [[computable sets|PPGD5KW8JC]], and every computable set is computable from every set, so $E \le_T \set{0}$ and $\set{0} \le_T E$.
This common degree is written $\mathbf{0}$; it is the least degree.

Non-example: the [[halting problem|Z7TN2B35B0]] $K$ does not belong to $\mathbf{0}$, because $K \not\le_T \emptyset$.
Its degree is written $\mathbf{0}'$.

Every degree is a countable set, since there are only countably many oracle machines.
Hence there are uncountably many degrees.
Any two degrees $\deg(A)$ and $\deg(B)$ have a least upper bound, the degree of $A \oplus B = \set{2n : n \in A} \cup \set{2n + 1 : n \in B}$.
