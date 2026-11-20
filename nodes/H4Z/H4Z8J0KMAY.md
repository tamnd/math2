---
tag: H4Z8J0KMAY
kind: concept
name: Routley-Meyer semantics
aliases: [ternary-semantics]
msc: ["03B47", "03B45"]
topics: [98QF5J4W16]
audience: research
uses: [KXTCZ2FY5M, NGHWZ9Y7ZV]
sources:
  - wikipedia: en:76765067@r1368301704
    locator: Glossary of logic, section T
    note: adopted
    mention: wikipedia://en/76765067#MEBD
    sections: [Summary]
  - url: https://en.wikipedia.org/wiki/Relevance_logic
    locator: Models, Routley-Meyer models
  - url: https://plato.stanford.edu/entries/logic-relevance/
    locator: 1 Semantics for Relevant Implication; 2 Semantics for Negation
    note: Mares, Relevance Logic, Stanford Encyclopedia of Philosophy, revision of 2020-11-13
  - url: https://plato.stanford.edu/entries/logic-substructural/
    locator: 4 Model Theory
    note: Restall, Substructural Logics, Stanford Encyclopedia of Philosophy, revision of 2024-08-15
  - doi: 10.1016/S0049-237X(08)71541-6
    locator: pages 199-243
    note: Routley and Meyer, The semantics of entailment, in Truth, Syntax and Modality, Studies in Logic and the Foundations of Mathematics 68 (1973)
inventory: [M9P728Y2FH]
---

## Summary

*Routley-Meyer semantics*, also called *ternary semantics*, interprets [[relevance logics|KXTCZ2FY5M]] in frames $(W, R, {}^*, 0)$.
Here $W$ is a nonempty set of points, $R$ is a ternary relation on $W$, ${}^*$ is a map from $W$ to $W$, and $0 \in W$ is the base point.
An implication $A \rightarrow B$ is true at $a$ if and only if, for all $b, c$ with $Rabc$, if $A$ is true at $b$ then $B$ is true at $c$.
A negation $\neg A$ is true at $a$ if and only if $A$ is false at $a^*$, the *Routley star* of $a$.
A formula holds in a model when it is true at $0$.
The [[precise definition|XHN0G5FFR5]] adds conditions on $R$ and ${}^*$; further conditions give models for stronger logics such as $\mathbf{R}$.
It gives one pattern of models for many substructural logics, and small models show that a formula is not a theorem.

## Motivation

In [[Kripke semantics|NGHWZ9Y7ZV]] for strict implication, $A \rightarrow B$ is true at $w$ when $B$ is true at every accessible point where $A$ is true.
Then $p \rightarrow (q \rightarrow q)$ is valid, since $q \rightarrow q$ is true everywhere.
The SEP entry on relevance logic explains that the ternary relation, together with inconsistent and incomplete points, blocks such paradoxes.
In the reading of the SEP entry on substructural logics, $Rxyz$ says that combining the information at $x$ with that at $y$ gives information at $z$.

## Notation

We write $a \leq b$ for $R0ab$.
Some authors write $\Vdash$ for truth at a point, and some write the base point as $e$ or use a set of base points.

## Remarks

### Examples

1. The [[two-point model|PSTKVCYKAB]] validates $\mathbf{R}$ and falsifies disjunctive syllogism at $0$.
2. The [[one-point frame|FVYRB36Z38]] with $0^* = 0$ gives exactly classical truth tables.
3. For the [[Lambek calculus|5FAC9KX4H0]], the SEP entry on substructural logics takes the points to be words, and $Rxyz$ to say that $x$ followed by $y$ is $z$.

### Non-examples

A structure whose star is [[not an involution|NY42G4JYKY]] is not a Routley-Meyer frame, and the axiom $\neg\neg A \rightarrow A$ fails in it.
The structure with $W = \set{0}$, $R = \emptyset$ and $0^* = 0$ is not a frame, since $0 \leq 0$ fails; in it every implication is true at $0$, even $p \rightarrow q$.

### Basic properties

1. Truth is *hereditary*: if $A$ is true at $a$ and $a \leq b$, then $A$ is true at $b$.
   The [[definition node|XHN0G5FFR5]] proves this.
2. The Wikipedia article states that the class of all Routley-Meyer frames validates the relevance logic $\mathbf{B}$.
3. The Wikipedia article lists frame conditions that validate further axioms; for example, $Rabc \Rightarrow Rbac$ validates assertion $A \rightarrow ((A \rightarrow B) \rightarrow B)$.
4. The SEP entry on substructural logics states that a symmetry condition on $R$ models commutative premise combination.

### History

The SEP entry on relevance logic attributes the ternary semantics to Routley and Meyer, as a development of the semilattice semantics of Urquhart (1972).
It attributes the star operator to Richard and Val Routley (1972).
The paper of Routley and Meyer cited in this node is from 1973.

### Common errors

The point $a^*$ is not the negation of $a$; $\neg A$ is true at $a$ when $A$ fails at another point, $a^*$.
Validity means truth at the base point $0$, not truth at every point: $q \rightarrow q$ can fail at other points.

## Explanations

### L1 human

Think of each point as a body of information.
"$A$ implies $B$" is true at a point $a$ when $a$, applied to any information that supports $A$, gives information that supports $B$.
The three places of $R$ record "rule", "input" and "output".

### L2 human

We check that $p \rightarrow p$ is true at $0$ in every Routley-Meyer model.

1. Let $R0bc$ hold, and let $p$ be true at $b$.
2. $R0bc$ means $b \leq c$, by the notation above.
3. $p$ is hereditary, so $p$ is true at $c$.
4. So $p \rightarrow p$ is true at $0$, by the truth condition for $\rightarrow$.

The typical use of the semantics is to show that a formula is not a theorem, by a small model.
A trap: the same argument does not show that $p \rightarrow p$ is true at every point, since $Rabc$ need not imply $b \leq c$ when $a \neq 0$.

### L3 human

The ternary relation is the frame counterpart of a binary operation, as the binary relation of Kripke semantics is the counterpart of a unary modal operator.
The SEP entry on substructural logics states that Dunn's gaggle theory charts this correspondence in general.
The SEP entry states that logics without distribution, such as [[linear logic|2P2184B6HE]], need a more complex clause for disjunction.
