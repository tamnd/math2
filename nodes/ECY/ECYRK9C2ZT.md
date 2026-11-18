---
tag: ECYRK9C2ZT
kind: statement
role: proposition
name: The axioms of S5
msc: ["03B45"]
topics: [SKY7AQFG1V]
audience: grad
uses: [JS8W7PA6JK, FDFQFWPM4X, MT0CNMDT3R]
about: [VC3A2VWXND]
proofs: [6T67E2CT79]
sources:
  - url: https://en.wikipedia.org/wiki/S5_(modal_logic)
    locator: The axioms of S5
  - url: https://builds.openlogicproject.org/
    locator: Boxes and Diamonds
  - wikipedia: en:12708106@r1375088158
    locator: S5 (modal logic), section The axioms of S5
    note: adopted
    mention: wikipedia://en/12708106#MPF6
    sections: [Statement]
inventory: [7RRQE7VXRA]
---

## Statement

Write $\mathsf{K}\Sigma$ for the smallest [[normal modal logic|JS8W7PA6JK]] that contains the axioms in $\Sigma$, with
$$\mathrm{T}: \square p \to p, \quad \mathrm{B}: p \to \square\lozenge p, \quad \mathrm{4}: \square p \to \square\square p, \quad \mathrm{5}: \lozenge p \to \square\lozenge p.$$
Then the following four normal logics are equal:
$$\mathsf{KT5} = \mathsf{KTB4} = \mathsf{KT45} = \mathsf{KTB5}.$$
This logic is [[S5|MT0CNMDT3R]].
The proof is in [[the proof of the S5 axiom sets|6T67E2CT79]].

## Remarks

### Why each hypothesis is needed

1. The axiom $\mathrm{T}$ cannot be dropped. $\mathsf{K45}$ is valid on the frame $\set{(a,b), (b,b)}$, which is transitive and Euclidean but not reflexive, and $\mathrm{T}$ fails there, see [[the Euclidean example|NS4AC3W4FM]].
2. In $\mathsf{KTB4}$, neither $\mathrm{B}$ nor $\mathrm{4}$ can be dropped. $\mathsf{S4} = \mathsf{KT4}$ does not prove $\mathrm{5}$, see [[the non-theorem 5 in S4|A2JGSWCMT5]]. Also, $\mathsf{KTB}$ does not prove $\mathrm{4}$, see [[the reflexive symmetric frame|DJTASRZ6WC]].

### Consequences

1. $\mathsf{S5}$ contains $\mathsf{S4}$ and $\mathsf{B}$, so every theorem of these logics is a theorem of $\mathsf{S5}$.
2. Semantically, a frame validates $\mathsf{S5}$ if and only if its relation is reflexive and Euclidean. This is the same as an equivalence relation, by [[common modal axiom schemata|FDFQFWPM4X]].
3. The dual forms $\lozenge\square p \to \square p$ and $\lozenge\square p \to p$ are theorems of $\mathsf{S5}$.

### Converse

The statement is a list of equalities, so each inclusion has its converse in the list.
Without $\mathrm{T}$ the equalities fail: $\mathsf{KB4} \neq \mathsf{K45}$, since $\mathsf{K45}$ is valid on $\set{(a,b),(b,b)}$, where $\mathrm{B}$ fails at $a$ with $V(p) = \set{a}$.

### Generalizations

1. $\mathsf{KD45}$ is the analogue for belief: replacing $\mathrm{T}$ by $\mathrm{D}$ gives serial, transitive, Euclidean frames.
2. $\mathsf{KB4} = \mathsf{KB5} = \mathsf{KB45}$, since the proof of this page shows $\mathsf{KB5} \vdash \mathrm{4}$ and $\mathsf{KB4} \vdash \mathrm{5}$ without $\mathrm{T}$.

## History

Lewis and Langford defined $\mathsf{S5}$ in Symbolic Logic (1932) by an axiom system in the strict implication style.
The presentation as $\mathsf{KT5}$ in a normal Hilbert system is the later standard.

## Explanations

### L1 human

The logic $\mathsf{S5}$ has several equivalent lists of laws.
One list says: what is necessary is true, and what is possible is necessarily possible.
Another list says: what is necessary is true, what is true is necessarily possible, and what is necessary is necessarily necessary.
Both lists give the same set of laws.

### L2 human

We derive $\mathrm{B}$ in $\mathsf{KT5}$.

1. From $\mathrm{T}$ with $\neg p$: $\square\neg p \to \neg p$.
2. Contraposition: $p \to \neg\square\neg p$, which is $p \to \lozenge p$.
3. Axiom $\mathrm{5}$: $\lozenge p \to \square\lozenge p$.
4. Chaining 2 and 3: $p \to \square\lozenge p$, which is $\mathrm{B}$.

The typical use is to pick the axiom set that is easiest for the task: $\mathrm{5}$ for canonical models, $\mathrm{B}$ and $\mathrm{4}$ for frame arguments.
A trap: $\mathsf{KT5}$ and $\mathsf{KD45}$ differ; the second does not prove $\mathrm{T}$.

### L3 human

The equalities are the syntactic side of the fact that reflexive Euclidean relations are exactly the equivalence relations.
Algebraically, the $\mathsf{S5}$-algebras are the monadic Boolean algebras of Halmos, the algebras of one-variable first-order logic.
