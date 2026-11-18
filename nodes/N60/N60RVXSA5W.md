---
tag: N60RVXSA5W
kind: concept
name: Modal logic S4
msc: ["03B45"]
topics: [SKY7AQFG1V]
audience: grad
uses: [JS8W7PA6JK, FDFQFWPM4X, 0VABYWJWH9, XVYMEZKH7R]
sources:
  - url: https://en.wikipedia.org/wiki/Normal_modal_logic
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Interior_algebra
    locator: lead section
  - url: https://builds.openlogicproject.org/
    locator: Boxes and Diamonds
---

## Summary

The modal logic $\mathsf{S4} = \mathsf{KT4}$ is the smallest [[normal modal logic|JS8W7PA6JK]] that contains $\square p \to p$ and $\square p \to \square\square p$, as in [[the definition|SADS3RT2V4]].
It is sound and complete for the frames whose relation is a [[preorder|0VABYWJWH9]], and for the finite preorders.
Read topologically, $\square$ is the [[interior|0RZH6W98HK]] operator of a [[topological space|0CQHFPGJ45]], and intuitionistic logic embeds into $\mathsf{S4}$ by the translation of Gödel.
These links make $\mathsf{S4}$ the meeting point of modal logic, topology and constructive logic.

## Motivation

For knowledge, the axiom $\mathrm{T}$ says that knowledge is true, and $\mathrm{4}$ says that an agent who knows also knows that she knows.
For time with "now or later", the relation $\le$ is reflexive and transitive.
So $\mathsf{S4}$ is the logic of "now and always in the future" on such frames.
For constructive reasoning, Gödel read $\square\varphi$ as "$\varphi$ is provable", and $\mathrm{T}$ and $\mathrm{4}$ are laws of this informal provability.
All three readings give preorders, and $\mathsf{S4}$ is the logic of all preorders.

## Notation

1. $\mathsf{S4}$ is also written $\mathsf{KT4}$.
2. Its extensions $\mathsf{S4.2}$ and $\mathsf{S4.3}$ add $\lozenge\square p \to \square\lozenge p$ and $\square(\square p \to q) \vee \square(\square q \to p)$.
3. In the topological reading, $[\![\square\varphi]\!] = \operatorname{int}[\![\varphi]\!]$ and $[\![\lozenge\varphi]\!] = \operatorname{cl}[\![\varphi]\!]$.

## Remarks

### Examples

1. $\mathsf{S4} \vdash \square\lozenge\square\lozenge p \leftrightarrow \square\lozenge p$, and $\mathsf{S4}$ has exactly seven modalities without negation, see [[the reduction in S4|G2ABW0XS0H]].
2. The real line with $\square$ as interior is a model of $\mathsf{S4}$, see [[the interior example|WZF6Y41AEV]].
3. The relation $\le$ on $\N$ is a preorder, so it is an $\mathsf{S4}$-frame; there $\square p$ means "$p$ now and at all later times".
4. Every equivalence relation is a preorder, so $\mathsf{S4} \subseteq \mathsf{S5}$.

### Non-examples

1. $\mathsf{S4} \nvdash \lozenge\square p \to \square\lozenge p$: a preorder with two maximal worlds refutes it, see [[the branching preorder|HWYJG3GCQJ]].
2. $\mathsf{S4} \nvdash \lozenge p \to \square\lozenge p$, so $\mathsf{S4} \neq \mathsf{S5}$, see [[the non-theorem 5 in S4|A2JGSWCMT5]].
3. $\mathsf{S4} \nvdash p \to \square\lozenge p$: the same two-world preorder refutes axiom $\mathrm{B}$, see [[the non-symmetric frame|X88XTHRFG9]].

### Basic properties

1. $\mathsf{S4}$ is the logic of all preorders and of all finite preorders, see [[the completeness theorem|FXTCKYR3AQ]] and [[the finite model property theorem|XNPJK6B921]].
2. $\mathsf{S4}$ is decidable, and its satisfiability problem is PSPACE-complete, see [[the complexity theorem|1P2B0C7CQ4]].
3. $\mathsf{S4} \vdash \square\square p \leftrightarrow \square p$ and $\mathsf{S4} \vdash \lozenge\lozenge p \leftrightarrow \lozenge p$, so every modality is equivalent to one of $p$, $\square p$, $\lozenge p$, $\square\lozenge p$, $\lozenge\square p$, $\square\lozenge\square p$, $\lozenge\square\lozenge p$.
4. $\mathsf{S4.2}$ is the logic of directed preorders and $\mathsf{S4.3}$ the logic of connected preorders, by the same canonical model method.
5. Gödel's translation $t$ boxes atoms and implications, with $t(p) = \square p$ and $t(\varphi \to \psi) = \square(t\varphi \to t\psi)$. An intuitionistic formula $\varphi$ is a theorem of [[intuitionistic logic|Q11N8X99FK]] if and only if $\mathsf{S4} \vdash t\varphi$.

### History

Lewis and Langford introduced $\mathsf{S4}$ in Symbolic Logic (1932).
Gödel gave in 1933 the axiomatization by $\mathrm{K}$, $\mathrm{T}$, $\mathrm{4}$ and necessitation, noted its equivalence with Lewis's $\mathsf{S4}$, and proposed the translation of intuitionistic logic.
McKinsey proved the decidability of $\mathsf{S2}$ and $\mathsf{S4}$ in 1941, and McKinsey and Tarski proved the faithfulness of Gödel's translation in 1948.

### Common errors

1. Thinking that $\square\lozenge p$ and $\lozenge\square p$ are equivalent in $\mathsf{S4}$; neither implies the other.
2. Confusing $\square\lozenge p$ with $\lozenge p$; in $\mathsf{S4}$ only $\square\lozenge p \to \lozenge p$ holds.
3. Assuming that every $\mathsf{S4}$-frame is a partial order; preorders may have clusters of worlds that see each other.

## Explanations

### L1 human

In $\mathsf{S4}$, "necessary" behaves like "true now and at every later time".
If something will always hold, then it holds now, which is axiom $\mathrm{T}$.
If something will always hold, then at every later time it will still always hold, which is axiom $\mathrm{4}$.
For example, if from Monday on the shop is always open, then from Tuesday on it is always open too.

### L2 human

We read $\mathsf{S4}$ on the real line with $\square$ as interior.

1. Let $[\![ p ]\!] = [0, 1]$.
2. Then $[\![\square p]\!] = (0, 1)$, the interior of $[0, 1]$.
3. And $[\![\lozenge p]\!] = [0, 1]$, the closure of $[0, 1]$.
4. The axiom $\mathrm{T}$ holds since $(0, 1) \subseteq [0, 1]$, and $\mathrm{4}$ holds since the interior of $(0, 1)$ is $(0, 1)$.
5. The axiom $\mathrm{5}$, $\lozenge p \to \square\lozenge p$, fails at 0: $0 \in [0, 1]$ but $0 \notin (0, 1)$.

The typical use of $\mathsf{S4}$ is as the modal companion of intuitionistic logic: intuitionistic questions become questions about preorders and interiors.
A trap: the reading of $\square$ as interior gives $\mathsf{S4}$ for every space, but a single space can validate more.
An example is a discrete space, which validates $\square p \leftrightarrow p$.

### L3 human

The algebras of $\mathsf{S4}$ are the [[interior algebras|BDEX7HET71]], Boolean algebras with an interior operator.
Their open elements form a Heyting algebra; this is the algebraic form of Gödel's translation.
McKinsey and Tarski showed that $\mathsf{S4}$ is the logic of every dense-in-itself metric space, such as the real line.
This and the faithfulness of the translation belong to [[modal model theory|SPQVNPZDTB]].
The logics between $\mathsf{S4}$ and $\mathsf{S5}$, such as $\mathsf{S4.2}$ and $\mathsf{S4.3}$, and the logic $\mathsf{Grz}$ of [[provability logics|3E7M66WW6Q]], are the modal companions of intermediate logics.
