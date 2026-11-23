---
tag: VC3A2VWXND
kind: concept
name: Modal logic S5
msc: ["03B45"]
topics: [SKY7AQFG1V]
audience: grad
uses: [JS8W7PA6JK, FDFQFWPM4X, 0G8VEZ3WTK, MT0CNMDT3R]
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

Take three worlds $1, 2, 3$ in which every world sees every world, and let $p$ be true at $1$ and $2$.
Then $\square p$ is false at every world, because world $3$ lacks $p$, and $\lozenge p$ is true at every world.
The value of a boxed or diamond formula does not depend on where you stand.
$\mathsf{S5}$ is the modal logic of this picture, where "necessary" means "true in every world" and "possible" means "true in some world".

Exactly, $\mathsf{S5} = \mathsf{KT5}$ is the smallest [[normal modal logic|JS8W7PA6JK]] that contains the two axioms below, as in [[the definition|MT0CNMDT3R]]:
$$\mathrm{T}\colon \square p \to p, \qquad \mathrm{5}\colon \lozenge p \to \square\lozenge p.$$
It is sound and complete for the frames whose relation is an [[equivalence relation|0G8VEZ3WTK]], and also for the universal frames, where every world sees every world.

## Motivation

The oldest reading of necessity is truth in all possible worlds, with no restriction on which worlds count.
In that reading every world sees every world, so the frame is universal.
For knowledge, the worlds that an agent cannot tell apart from the actual world form a class of an equivalence relation.
The relation "cannot tell apart" is reflexive, symmetric and transitive, so the agent's knowledge obeys $\mathsf{S5}$.

$\mathsf{S5}$ is also the simplest of the standard systems to compute with.
Every formula is equivalent to one of modal depth at most $1$, and satisfiability is NP-complete, like that of propositional logic.
The logics of knowledge in [[applied modal logics|CQM9SRN8PM]] start from $\mathsf{S5}$, with one equivalence relation for each agent.

## Notation

Several axiom sets give the same logic, so $\mathsf{S5} = \mathsf{KT5} = \mathsf{KTB4} = \mathsf{KT45} = \mathsf{KTB5}$, by [[the axioms of S5|ECYRK9C2ZT]].
In epistemic logic the box of agent $i$ is written $K_i$, and the logic with $n$ agents is $\mathsf{S5}_n$.
On a universal frame the relation carries no information, so a model is often written as a pair $(W, V)$.

## Remarks

### Only the last operator counts

In $\mathsf{S5}$ the laws $\lozenge\square p \leftrightarrow \square p$ and $\square\lozenge p \leftrightarrow \lozenge p$ hold, together with $\square\square p \leftrightarrow \square p$ and $\lozenge\lozenge p \leftrightarrow \lozenge p$.
So a string of boxes and diamonds in front of $p$ is equivalent to its last operator, by [[the reduction of iterated modalities|GHPPQ19J6B]].
For example, $\lozenge\square\lozenge\lozenge\square p$ reduces to $\square p$.
There are three modalities without negation, $p$, $\square p$ and $\lozenge p$, and six with it.
A box also passes through a disjunction when one side is boxed, as in [[the law □(p ∨ □q) ↔ □p ∨ □q|BAV2SAADQT]].
These laws together rewrite every formula to modal depth at most $1$.

### Knowledge in a card game

Three cards are dealt to two players, one card each, and a player sees only her own card.
The deals that a player cannot tell apart are those with the same card in her hand, and this relation is an equivalence relation.
So her knowledge obeys $\mathsf{S5}$, as [[the card game example|81J8VDK9RX]] checks in detail.
If she holds the ace, she knows that she holds the ace, and she knows which deals remain possible.

### What is not S5

$\mathsf{S4}$ does not prove $\mathrm{5}$, because a preorder need not be symmetric; [[axiom 5 is not a theorem of S4|A2JGSWCMT5]] gives the two-world witness.
The frame with arrows $a R b$ and $b R b$ is serial, transitive and Euclidean, so it is a frame of $\mathsf{KD45}$, but it is not reflexive; see [[the Euclidean relation example|NS4AC3W4FM]].
The reflexive symmetric path on three worlds is a frame of $\mathsf{B}$ but not of $\mathsf{S5}$, because it is not transitive; see [[the failure of 4 on a reflexive symmetric frame|DJTASRZ6WC]].

### The rules you can use

$\mathsf{S5}$ is the logic of all equivalence relations and of all universal frames, by [[the completeness theorem|FXTCKYR3AQ]].
The two classes give the same logic because truth at a world $w$ depends only on the worlds that $w$ can reach, and in an equivalence relation these form the class of $w$, on which $R$ is universal.
A satisfiable formula is true in a universal model with at most $1 + m$ worlds, where $m$ is the number of subformulas of the form $\square\psi$.
Each false $\square\psi$ at the starting world needs one witness world, and nothing else is needed.
So $\mathsf{S5}$ has the [[finite model property|3NT8RCA6HE]], and its satisfiability problem is NP-complete, by [[the complexity theorem|1P2B0C7CQ4]].

### Watch out

$\mathsf{S5}$ is not the logic of a single world.
On one world with a loop, $\square p \leftrightarrow p$ is valid, and that gives the trivial logic, which is larger than $\mathsf{S5}$.
A second slip is to let the box pass through every disjunction.
On a universal frame with two worlds and $p$ true at one of them, $\square(p \vee \neg p)$ is true and $\square p \vee \square\neg p$ is false.
A third slip is to use $\mathsf{S5}$ for belief: beliefs can be false, so $\mathrm{T}$ fails, and $\mathsf{KD45}$ is the usual choice.

### History

Lewis and Langford presented $\mathsf{S5}$ in Symbolic Logic in 1932.
Carnap's semantics of state descriptions in Meaning and Necessity, 1947, fits $\mathsf{S5}$, with necessity as truth in every state description.
Kripke proved in 1959 the completeness of quantified $\mathsf{S5}$ for models with a set of worlds.
Ladner proved in 1977 that $\mathsf{S5}$-satisfiability is NP-complete.

### Try it

First, reduce $\square\lozenge\square\square\lozenge p$ in $\mathsf{S5}$.
The last operator is $\lozenge$, so the formula is equivalent to $\lozenge p$.

Second, on the three-world universal model of the Summary, where is $\lozenge\square p$ true?
$\square p$ is false at every world, so $\lozenge\square p$ is false at every world, which agrees with $\lozenge\square p \leftrightarrow \square p$.

## Explanations

### L1 human

In $\mathsf{S5}$, "necessary" means "true in every world", and all worlds can see all worlds.
So "possibly $p$" means that $p$ holds somewhere, and this does not depend on where you stand.
A card player knows exactly the deals that agree with her own card, and her knowledge follows the same laws.
If a player holds the ace, she knows that she holds the ace, and she knows that she knows it.

### L2 human

We decide whether $\varphi = \lozenge p \wedge \lozenge q \wedge \square\neg(p \wedge q)$ is satisfiable in $\mathsf{S5}$.
On a universal model, $\lozenge p$ asks for a world with $p$, $\lozenge q$ asks for a world with $q$, and $\square\neg(p \wedge q)$ asks that no world have both.
Take $W = \{ 1, 2 \}$ with $V(p) = \{ 1 \}$ and $V(q) = \{ 2 \}$.
All three conjuncts hold at world $1$, so $\varphi$ is satisfiable.
Check against the bound: the boxed subformulas are $\square\neg p$, $\square\neg q$ and $\square\neg(p \wedge q)$, so $m = 3$, and two worlds are within $1 + m = 4$.
This is the typical use of the universal semantics: boxes become "all worlds" and diamonds become "some world", and you search a small model.
Watch out: $\mathsf{S5}$ is complete for universal frames, but its canonical frame is an equivalence relation with many classes, not a universal relation.

### L3 human

On universal frames, $\mathsf{S5}$ is the one-variable fragment of first-order logic, with $\square$ as $\forall x$ and the variables as unary predicates.
Its algebras are the monadic Boolean algebras of Halmos.
The logic $\mathsf{S5}_n$ has one equivalence relation for each agent, and it is the base of epistemic logic and of the theory of common knowledge.
Products such as $\mathsf{S5} \times \mathsf{S5}$ are modal forms of first-order logic with two variables; see [[products of modal logics|JA2EBWVW8A]].
