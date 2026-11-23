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

Four different lists of axioms give the same logic $\mathsf{S5}$.
Write $\mathsf{K}\Sigma$ for the smallest [[normal modal logic|JS8W7PA6JK]] that contains the axioms named in $\Sigma$, where:
$$\mathrm{T}\colon \square p \to p, \quad \mathrm{B}\colon p \to \square\lozenge p, \quad \mathrm{4}\colon \square p \to \square\square p, \quad \mathrm{5}\colon \lozenge p \to \square\lozenge p.$$
Then the following four normal modal logics are equal:
$$\mathsf{KT5} = \mathsf{KTB4} = \mathsf{KT45} = \mathsf{KTB5}.$$
This logic is [[S5|MT0CNMDT3R]], and [[the proof that the four axiom sets agree|6T67E2CT79]] derives each axiom from the others.

## Remarks

### Why each hypothesis is needed

The axiom $\mathrm{T}$ cannot be dropped.
The frame with arrows $a R b$ and $b R b$ is transitive and Euclidean, so it validates $\mathsf{K45}$, but $\mathrm{T}$ fails at $a$ when $V(p) = \{ b \}$; see [[the Euclidean relation example|NS4AC3W4FM]].

In $\mathsf{KTB4}$ neither $\mathrm{B}$ nor $\mathrm{4}$ can be dropped.
Without $\mathrm{B}$ you get $\mathsf{S4} = \mathsf{KT4}$, which does not prove $\mathrm{5}$, by [[axiom 5 is not a theorem of S4|A2JGSWCMT5]].
Without $\mathrm{4}$ you get $\mathsf{B} = \mathsf{KTB}$, which does not prove $\mathrm{4}$, by [[the reflexive symmetric frame|DJTASRZ6WC]].

### What it gives you

$\mathsf{S5}$ contains $\mathsf{S4}$ and $\mathsf{B}$, so every theorem of either logic is a theorem of $\mathsf{S5}$.
The dual forms $\lozenge\square p \to \square p$ of $\mathrm{5}$ and $\lozenge\square p \to p$ of $\mathrm{B}$ are theorems as well.
On frames, the statement matches a fact about relations: a reflexive Euclidean relation is the same as an equivalence relation, by the [[common modal axiom schemata|FDFQFWPM4X]].
In practice you pick the axiom set that suits the task, $\mathrm{5}$ for canonical models and $\mathrm{B}$ with $\mathrm{4}$ for arguments on frames.

### The converse and the case without T

The statement is a list of equalities, so each inclusion comes with its converse.
Without $\mathrm{T}$ the equalities fail.
On the frame $a R b$, $b R b$ with $V(p) = \{ a \}$, the formula $p$ is true at $a$, but $b$ sees only $b$, so $\lozenge p$ is false at $b$ and $\square\lozenge p$ is false at $a$.
So $\mathrm{B}$ fails while $\mathsf{K45}$ holds, and $\mathsf{K45} \ne \mathsf{KB4}$.

### Generalizations

Replacing $\mathrm{T}$ by $\mathrm{D}$ gives $\mathsf{KD45}$, the logic of serial, transitive and Euclidean frames, which is the usual logic of belief.
Without $\mathrm{T}$ the axioms $\mathrm{B}$, $\mathrm{4}$ and $\mathrm{5}$ still interact: $\mathsf{KB4} = \mathsf{KB5} = \mathsf{KB45}$.
On frames this says that a symmetric relation is transitive exactly when it is Euclidean.

## History

Lewis and Langford defined $\mathsf{S5}$ in Symbolic Logic (1932), by an axiom system in the style of strict implication.
The presentation as $\mathsf{KT5}$ over the normal logic $\mathsf{K}$ became the standard one later.

## Explanations

### L1 human

The logic $\mathsf{S5}$ has several lists of laws that give the same result.
One list says: what is necessary is true, and what is possible is necessarily possible.
Another list says: what is necessary is true, what is true is necessarily possible, and what is necessary is necessarily necessary.
Both lists prove the same formulas.

### L2 human

We derive $\mathrm{B}$ in $\mathsf{KT5}$, which is one step of the proof.
Substitute $\neg p$ for $p$ in $\mathrm{T}$:
$$\square\neg p \to \neg p.$$
Contraposition gives $p \to \neg\square\neg p$, which is $p \to \lozenge p$.
Axiom $\mathrm{5}$ gives $\lozenge p \to \square\lozenge p$, and chaining the two gives $p \to \square\lozenge p$, which is $\mathrm{B}$.
Watch out: this step uses $\mathrm{T}$, so it does not work in $\mathsf{KD45}$, and indeed $\mathsf{KD45}$ proves neither $\mathrm{B}$ nor $\mathrm{T}$.

### L3 human

The equalities are the syntactic side of the fact that the reflexive Euclidean relations are exactly the equivalence relations.
Algebraically, the $\mathsf{S5}$-algebras are the monadic Boolean algebras of Halmos, which are the algebras of one-variable first-order logic.
