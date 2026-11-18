---
tag: VC3A2VWXND
kind: concept
name: Modal logic S5
msc: ["03B45"]
topics: [SKY7AQFG1V]
audience: grad
uses: [~b1c67ad7, FDFQFWPM4X, 0G8VEZ3WTK, ~3595c3e8]
aliases: [axiom-s5, logic-s5]
sources:
  - url: https://en.wikipedia.org/wiki/S5_(modal_logic)
    locator: lead section
  - url: https://builds.openlogicproject.org/
    locator: Boxes and Diamonds
  - wikipedia: en:12708106@r1375088158
    locator: S5 (modal logic)
    note: adopted
    mention: wikipedia://en/12708106
    sections: [Summary]
same_as:
  wikidata: Q7388341
  wikipedia: S5 (modal logic)
inventory: [D5JKKWKM27]
---

## Summary

The modal logic $\mathsf{S5} = \mathsf{KT5}$ is the smallest [[normal modal logic|~b1c67ad7]] that contains $\square p \to p$ and $\lozenge p \to \square\lozenge p$, as in [[the definition|~3595c3e8]]; it equals $\mathsf{KTB4}$.
It is sound and complete for the frames whose relation is an [[equivalence relation|0G8VEZ3WTK]].
It is also sound and complete for the universal frames, where $\square\varphi$ means "$\varphi$ at every world".
Every formula is $\mathsf{S5}$-equivalent to one of modal depth at most 1, and $\mathsf{S5}$-satisfiability is NP-complete.
It is the logic of the alethic reading "true in all possible worlds" and of knowledge with full introspection.

## Motivation

The oldest reading of necessity is truth in all possible worlds, with no restriction on which worlds count.
In this reading every world sees every world, so the frame is universal.
For knowledge, the worlds that an agent cannot tell apart from the actual one form a class of an equivalence relation.
The relation "cannot tell apart" is reflexive, symmetric and transitive.
So $\mathsf{S5}$ is the logic of these two readings, and its frames are the equivalence relations.

## Notation

1. $\mathsf{S5} = \mathsf{KT5} = \mathsf{KTB4} = \mathsf{KT45} = \mathsf{KTB5}$, see [[the axioms of S5|ECYRK9C2ZT]].
2. In epistemic logic the box of agent $i$ is written $K_i$, and the multi-agent logic is $\mathsf{S5}_n$.
3. On a universal frame a model is often written $(W, V)$, without $R$.

## Remarks

### Examples

1. In a card game, the relation "same own card" between deals is an equivalence relation. So the knowledge of a player obeys $\mathsf{S5}$, see [[the card game|~17a97e87]].
2. Every string of boxes and diamonds before $p$ reduces to its last operator, so $\mathsf{S5}$ has six modalities, see [[the reduction in S5|~4e438511]].
3. $\mathsf{S5} \vdash \square(p \vee \square q) \leftrightarrow (\square p \vee \square q)$, while $\mathsf{S4}$ does not prove it, see [[the distribution example|~8b657ee8]].
4. The universal frame on two worlds with $V(p) = \set{1}$ makes $\lozenge p \wedge \lozenge\neg p$ true at both worlds.

### Non-examples

1. $\mathsf{S4} \nvdash \lozenge p \to \square\lozenge p$, so $\mathsf{S4} \subsetneq \mathsf{S5}$, see [[the non-theorem 5 in S4|~d69eee52]].
2. The Euclidean, transitive and serial frame $\set{(a,b),(b,b)}$ is a frame of $\mathsf{KD45}$ but not of $\mathsf{S5}$, see [[the Euclidean example|~1ea6939a]].
3. The reflexive symmetric path on three worlds is a frame of $\mathsf{B}$ but not of $\mathsf{S5}$, see [[the reflexive symmetric frame|~1d7e3826]].

### Basic properties

1. $\mathsf{S5}$ is the logic of all equivalence relations and of all universal frames, see [[the completeness theorem|~1d9447ce]].
2. $\mathsf{S5} \vdash \lozenge\square p \leftrightarrow \square p$ and $\mathsf{S5} \vdash \square\lozenge p \leftrightarrow \lozenge p$.
3. Every formula is $\mathsf{S5}$-equivalent to a formula of modal depth at most 1. The proof uses these two equivalences and distribution laws such as those of [[the distribution example|~8b657ee8]].
4. A formula $\varphi$ is $\mathsf{S5}$-satisfiable if and only if it is true in a universal model with at most $1 + m$ worlds. Here $m$ is the number of subformulas $\square\psi$ of $\varphi$. So $\mathsf{S5}$-satisfiability is NP-complete, see [[the complexity theorem|~c5e1a419]].
5. $\mathsf{S5}$ has the [[finite model property|~11053ef0]] and is decidable.

### History

Lewis and Langford presented $\mathsf{S5}$ in Symbolic Logic (1932).
Carnap's semantics of state descriptions in Meaning and Necessity (1947) fits $\mathsf{S5}$, with necessity as truth in every state description.
Kripke proved completeness of quantified $\mathsf{S5}$ for models with a set of worlds in 1959.
Ladner proved in 1977 that $\mathsf{S5}$-satisfiability is NP-complete.

### Common errors

1. Taking $\mathsf{S5}$ for the logic of a single world; one world gives the trivial logic with $\square p \leftrightarrow p$.
2. Thinking that $\square$ distributes over $\vee$ in $\mathsf{S5}$; $\square(p \vee \neg p) \to (\square p \vee \square\neg p)$ fails on two worlds.
3. Using $\mathsf{S5}$ for belief; belief can be false, so $\mathrm{T}$ fails, and $\mathsf{KD45}$ is the usual choice.

## Explanations

### L1 human

In $\mathsf{S5}$, "necessary" means "true in every world", with all worlds visible from all worlds.
So "possibly $p$" means that $p$ holds somewhere, and this does not depend on where we stand.
A card player knows exactly the deals that agree with her own card, and her knowledge follows the same laws.
For example, if a player holds the ace, she knows that she holds the ace, and she knows that she knows it.

### L2 human

We decide whether $\varphi = \lozenge p \wedge \lozenge q \wedge \square\neg(p \wedge q)$ is $\mathsf{S5}$-satisfiable.

1. On a universal model, $\lozenge p$ asks for a world with $p$, and $\lozenge q$ for a world with $q$.
2. $\square\neg(p \wedge q)$ asks that no world has both.
3. Take $W = \set{1, 2}$, $V(p) = \set{1}$, $V(q) = \set{2}$; all three conjuncts hold at world 1.
4. So $\varphi$ is satisfiable with 2 worlds, within the bound $1 + m = 4$; here $m = 3$ counts $\square\neg p$, $\square\neg q$ and $\square\neg(p \wedge q)$.

The typical use of the universal semantics is quick model checking and satisfiability checking in $\mathsf{S5}$.
A trap: $\mathsf{S5}$ is complete for universal frames, but the canonical frame of $\mathsf{S5}$ is an equivalence relation with many classes, not a universal relation.

### L3 human

On universal frames, $\mathsf{S5}$ is the one-variable fragment of first-order logic, with $\square$ as $\forall x$ and the variables as unary predicates.
Its algebras are the monadic Boolean algebras of Halmos.
The multi-agent logic $\mathsf{S5}_n$ has one equivalence relation for each agent.
It is the base of epistemic logic and of the theory of common knowledge, treated in [[applied modal logics|CQM9SRN8PM]].
Products such as $\mathsf{S5} \times \mathsf{S5}$ model two-variable first-order logic and belong to [[modal model theory|SPQVNPZDTB]].
