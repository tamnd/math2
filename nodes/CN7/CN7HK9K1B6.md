---
tag: CN7HK9K1B6
kind: concept
name: Neighborhood semantics
msc: ["03B45"]
topics: [SKY7AQFG1V]
audience: research
uses: [~6197812b, ~b1c67ad7, NGHWZ9Y7ZV, G989VP2NGP, H9RGWCR10W, 0CQHFPGJ45, 0ZCY0Z80B6, 0RZH6W98HK, ~d626bd63]
aliases: [neighbourhood-semantics, scott-montague-semantics]
sources:
  - book: isbn:9780521295154
    locator: "Chellas, Modal Logic: An Introduction, chapters 7 to 9"
  - wikipedia: en:5809298@r1339444889
    locator: Neighborhood semantics
    note: adopted
    mention: wikipedia://en/5809298
    sections: [Summary]
same_as:
  wikidata: Q6988052
  wikipedia: Neighborhood semantics
inventory: [K2P1X1AQVB]
---

## Summary

Neighborhood semantics, also called Scott-Montague semantics, interprets the box by a set of propositions at each world instead of by an accessibility relation.
A [[neighbourhood frame|~6197812b]] gives each world $w$ a family $N(w)$ of sets of worlds.
Then $\square\varphi$ is true at $w$ when the truth set of $\varphi$ is in $N(w)$.
It is the standard semantics for the *classical* modal logics, which need not be [[normal|~b1c67ad7]].
It contains [[Kripke semantics|NGHWZ9Y7ZV]] as the special case of augmented frames.

## Motivation

In Kripke semantics, every frame validates axiom $\mathrm{K}$ and the rule of [[necessitation|G989VP2NGP]].
So an agent who knows $\varphi$ knows every consequence of $\varphi$.
Also, an obligation to do $\varphi$ is an obligation to do each consequence of $\varphi$.
For knowledge and belief this is the problem of logical omniscience, see [[epistemic closure|H9RGWCR10W]], and for obligation it leads to deontic paradoxes.
A semantics for weaker logics must let $\square\varphi$ hold without $\square\psi$, even when $\varphi$ implies $\psi$.
No truth table for the box does this, see [[no two-valued truth table for the box gives K|~81ccf77c]].
Neighbourhood frames are the simplest possible-worlds semantics that does.

## Notation

We use the notation of [[the definition|~6197812b]]: a frame is $(W, N)$, a model is $(W, N, V)$, and $[\![ \varphi ]\!]$ is the truth set of $\varphi$.
The closure conditions are (m) supplemented, (c) closed under intersections and (n) contains the unit.
The logics are named by Chellas's letters: $\mathsf{E}$ is the smallest classical modal logic.
The logics $\mathsf{EM}$, $\mathsf{EC}$, $\mathsf{EN}$, $\mathsf{EMC}$ and so on add the axioms $\mathrm{M}$, $\mathrm{C}$ and $\mathrm{N}$.
The logic $\mathsf{EM}$ is called the *monotonic* logic, and its frames are the supplemented frames.

## Remarks

### Examples

1. A Kripke frame gives the neighbourhood frame $N(w) = \set{X : R[w] \subseteq X}$, and the two clauses for $\square$ agree, see [[a Kripke frame as a neighbourhood frame|~33e4a57b]].
2. A frame where axiom $\mathrm{K}$ and necessitation fail, see [[a neighbourhood model in which axiom K fails|~3050f897]].
3. Majority. Take $W = \set{1, 2, 3}$ and $N(w) = \set{X \subseteq W : |X| \ge 2}$ for each $w$. Then $\square\varphi$ says that $\varphi$ holds at most worlds. The frame is supplemented and contains $W$. It is not closed under intersections: $\set{1, 2} \cap \set{2, 3} = \set{2}$. So it validates $\mathrm{M}$ and $\mathrm{N}$ but not $\mathrm{C}$.
4. Topology. For a [[topological space|0CQHFPGJ45]] $(W, \tau)$, let $N(w)$ be the set of [[neighbourhoods|0ZCY0Z80B6]] of $w$. Then $[\![ \square\varphi ]\!]$ is the [[interior|0RZH6W98HK]] of $[\![ \varphi ]\!]$. The frame is supplemented, closed under finite intersections and contains $W$; see [[the interior of the real line as an S4 box|~e8c76800]]. This is the source of the name.

### Non-examples

1. The majority frame of example 3 is not a Kripke frame: it fails only condition (c), closure under intersections.
2. The frame with $N(w) = \varnothing$ for each $w$ is supplemented and closed under intersections, but it fails condition (n): $\square\top$ is false everywhere. So it is not a Kripke frame either.
3. On $W = \mathbb{N}$, let $N(w)$ be the set of cofinite subsets of $\mathbb{N}$. It satisfies (m), (c) and (n), so it validates $\mathsf{K}$. It is not augmented: the core $\bigcap N(w)$ is empty, and $\varnothing \notin N(w)$. So it comes from no relation, although its logic contains $\mathsf{K}$.

### Basic properties

1. The rule RE is valid on every neighbourhood frame. If $\varphi \leftrightarrow \psi$ holds at every world, then $[\![ \varphi ]\!] = [\![ \psi ]\!]$, so $\square\varphi$ and $\square\psi$ have the same truth value at each world.
2. Axiom $\mathrm{M}$ is valid on a frame if and only if the frame is supplemented. For one direction, $[\![ p \wedge q ]\!] \subseteq [\![ p ]\!]$. For the other, given $X \subseteq Y$ with $X \in N(w)$, put $V(p) = Y$ and $V(q) = X$.
3. In the same way, axiom $\mathrm{C}$ is valid if and only if the frame is closed under intersections. Axiom $\mathrm{N}$ is valid if and only if the frame contains the unit, since $[\![ \top ]\!] = W$.
4. $\mathsf{EMCN} = \mathsf{K}$. $\mathsf{K}$ proves RE, $\mathrm{M}$, $\mathrm{C}$ and $\mathrm{N}$. Conversely, from $\vdash \varphi$ we get $\vdash \varphi \leftrightarrow \top$, so $\vdash \square\varphi$ by RE and $\mathrm{N}$. By $\mathrm{C}$, then RE, then $\mathrm{M}$, $\square(p \to q) \wedge \square p$ implies $\square((p \to q) \wedge p)$, then $\square(q \wedge p)$, then $\square q$.
5. Completeness (Segerberg 1971, Chellas 1980). $\mathsf{E}$ is sound and complete for the class of all neighbourhood frames. Each logic obtained from $\mathsf{E}$ by adding some of $\mathrm{M}$, $\mathrm{C}$ and $\mathrm{N}$ is sound and complete for the frames with the matching conditions. The proof uses a canonical neighbourhood model built from maximal consistent sets, as in [[the canonical model|~d626bd63]].
6. Augmented frames are exactly the frames of the form in example 1. On a finite set every frame with (m), (c) and (n) is augmented, see [[the definition|~6197812b]].

### History

Dana Scott and Richard Montague introduced the semantics independently in 1970, Scott in "Advice on modal logic" and Montague in "Universal grammar".
Krister Segerberg developed the theory of the classical modal logics in "An essay in classical modal logic" (1971).
Brian Chellas gave the theory in his textbook "Modal Logic: An Introduction" (1980), chapters 7 to 9.
He used the letters $\mathsf{E}$, $\mathsf{M}$, $\mathsf{C}$ and $\mathsf{N}$ and the name *minimal models*.
The name recalls the neighbourhoods of a point in topology, as in example 4.

### Common errors

1. Reading the diamond as "some neighbourhood meets $[\![ \varphi ]\!]$". The clause is $W \setminus [\![ \varphi ]\!] \notin N(w)$. On a supplemented frame this is the same as "every neighbourhood meets $[\![ \varphi ]\!]$".
2. Treating (m), (c) and (n) as enough for a Kripke frame on an infinite set. The cofinite frame of non-example 3 satisfies them but is not augmented.
3. Assuming that the logic of all neighbourhood frames is normal. It is $\mathsf{E}$, which proves neither $\mathrm{K}$ nor $\square\top$.

## Explanations

### L1 human

In Kripke semantics, a world sees some other worlds, and a statement is necessary when it is true in all of them.
In neighbourhood semantics, each world has a list of propositions, each one a set of worlds, that count as necessary there.
A statement is necessary at a world when the set of worlds where it is true is on that list.
So necessity need not pass from a statement to its consequences.

### L2 human

We test axiom $\mathrm{C}$ on the majority frame of example 3, at the world $1$.

1. Put $V(p) = \set{1, 2}$ and $V(q) = \set{2, 3}$.
2. $[\![ p ]\!]$ has two elements, so it is in $N(1)$, and $\square p$ is true at $1$. In the same way, $\square q$ is true at $1$.
3. $[\![ p \wedge q ]\!] = \set{2}$ has one element, so it is not in $N(1)$, and $\square(p \wedge q)$ is false at $1$.
4. So $(\square p \wedge \square q) \to \square(p \wedge q)$ fails at $1$.

The typical use is a logic of "most", "probably" or "it is likely that", where two likely statements need not be likely together.
A trap: the axiom $\mathrm{M}$ still holds here, since a superset of a majority is a majority.

### L3 human

Neighbourhood frames are to the classical modal logics what Kripke frames are to the normal ones; Chellas calls them minimal models.
The neighbourhood frames on $W$ match the unary operations on $\mathcal{P}(W)$ one to one, and the Kripke frames match the operations that preserve all intersections.
Monotonic neighbourhood frames are used in game logic and in coalition logic.
In these logics, a coalition can force a set of outcomes, and every superset of that set.
