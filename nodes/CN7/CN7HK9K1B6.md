---
tag: CN7HK9K1B6
kind: concept
name: Neighborhood semantics
msc: ["03B45"]
topics: [SKY7AQFG1V]
audience: research
uses: [RT7QEGZSTQ, JS8W7PA6JK, NGHWZ9Y7ZV, G989VP2NGP, H9RGWCR10W, 0CQHFPGJ45, 0ZCY0Z80B6, 0RZH6W98HK, TVE4F04KME]
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

Take three worlds, and call a statement "likely" at a world when it holds at two or more of the three worlds.
If $p$ holds at $1$ and $2$, and $q$ at $2$ and $3$, then $p$ and $q$ are both likely, but $p \wedge q$ holds only at $2$ and is not.
No accessibility relation behaves this way, since a Kripke box always passes through conjunctions.
Neighborhood semantics handles this case.

Exactly, neighborhood semantics, also called Scott-Montague semantics, interprets the box by a set of propositions at each world instead of by an accessibility relation.
A [[neighborhood frame|RT7QEGZSTQ]] gives each world $w$ a family $N(w)$ of sets of worlds.
Then $\square\varphi$ is true at $w$ when the truth set of $\varphi$ is in $N(w)$.
It is the standard semantics for the *classical* modal logics, which need not be [[normal|JS8W7PA6JK]].
It contains [[Kripke semantics|NGHWZ9Y7ZV]] as the special case of augmented frames.

## Motivation

In Kripke semantics, every frame validates axiom $\mathrm{K}$ and the rule of [[necessitation|G989VP2NGP]].
So an agent who knows $\varphi$ knows every consequence of $\varphi$.
Also, an obligation to do $\varphi$ is an obligation to do each consequence of $\varphi$.
For knowledge and belief this is the problem of logical omniscience, as in [[epistemic closure|H9RGWCR10W]], and for obligation it leads to deontic paradoxes.
A semantics for weaker logics must let $\square\varphi$ hold without $\square\psi$, even when $\varphi$ implies $\psi$.
No truth table for the box does this, by [[no two-valued truth table for the box gives K|H22GJGKD5M]].
Neighborhood frames are the standard possible-worlds semantics that does.

## Notation

We use the notation of [[the definition|RT7QEGZSTQ]]: a frame is $(W, N)$, a model is $(W, N, V)$, and $[\![ \varphi ]\!]$ is the truth set of $\varphi$.
The closure conditions are (m) supplemented, (c) closed under intersections and (n) contains the unit.
The logics are named by Chellas's letters, and $\mathsf{E}$ is the smallest classical modal logic.
The logics $\mathsf{EM}$, $\mathsf{EC}$, $\mathsf{EN}$, $\mathsf{EMC}$ and so on add the axioms $\mathrm{M}$, $\mathrm{C}$ and $\mathrm{N}$.
The logic $\mathsf{EM}$ is called the *monotonic* logic, and its frames are the supplemented frames.

## Remarks

### Three kinds of frames

A Kripke frame gives the neighborhood frame $N(w) = \{ X : R[w] \subseteq X \}$, and the two clauses for $\square$ agree, by [[a Kripke frame as a neighborhood frame|BJ59QH0AS8]].
In the majority frame of the Summary, $W = \{ 1, 2, 3 \}$ and $N(w) = \{ X \subseteq W : \lvert X \rvert \ge 2 \}$ for each $w$.
It is supplemented and contains $W$, but it is not closed under intersections, since $\{ 1, 2 \} \cap \{ 2, 3 \} = \{ 2 \}$.
So it validates $\mathrm{M}$ and $\mathrm{N}$ but not $\mathrm{C}$.
For a [[topological space|0CQHFPGJ45]], let $N(w)$ be the set of [[neighborhoods|0ZCY0Z80B6]] of $w$.
Then $[\![ \square\varphi ]\!]$ is the [[interior|0RZH6W98HK]] of $[\![ \varphi ]\!]$, as in [[the interior of the real line as an S4 box|WZF6Y41AEV]].
This frame is supplemented, closed under finite intersections and contains $W$.
A frame in which axiom $\mathrm{K}$ and necessitation fail is in [[a neighborhood model in which axiom K fails|G2X3PKG55F]].

### Frames that come from no relation

The majority frame is not a Kripke frame, and it fails only condition (c).
The frame with $N(w) = \varnothing$ for each $w$ is supplemented and closed under intersections.
It fails condition (n), since $\square\top$ is false everywhere, so it is not a Kripke frame either.
On $W = \mathbb{N}$, let $N(w)$ be the set of cofinite subsets of $\mathbb{N}$.
It satisfies (m), (c) and (n), so it validates $\mathsf{K}$.
Its core $\bigcap N(w)$ is empty, and $\varnothing \notin N(w)$, so it is not augmented.
So it comes from no relation, although its logic contains $\mathsf{K}$.

### Axioms and closure conditions

The rule RE is valid on every neighborhood frame.
If $\varphi \leftrightarrow \psi$ holds at every world, then $[\![ \varphi ]\!] = [\![ \psi ]\!]$, so $\square\varphi$ and $\square\psi$ agree at each world.
Axiom $\mathrm{M}$ is valid on a frame exactly when the frame is supplemented.
One direction uses $[\![ p \wedge q ]\!] \subseteq [\![ p ]\!]$.
For the other, given $X \subseteq Y$ with $X \in N(w)$, put $V(p) = Y$ and $V(q) = X$.
In the same way, $\mathrm{C}$ is valid exactly when the frame is closed under intersections, and $\mathrm{N}$ exactly when it contains the unit, since $[\![ \top ]\!] = W$.

$\mathsf{EMCN} = \mathsf{K}$.
$\mathsf{K}$ proves RE, $\mathrm{M}$, $\mathrm{C}$ and $\mathrm{N}$.
Conversely, from $\vdash \varphi$ we get $\vdash \varphi \leftrightarrow \top$, so $\vdash \square\varphi$ by RE and $\mathrm{N}$.
For axiom $\mathrm{K}$, $\mathrm{C}$ turns $\square(p \to q) \wedge \square p$ into $\square((p \to q) \wedge p)$.
RE turns that into $\square(q \wedge p)$, and $\mathrm{M}$ gives $\square q$.

### Completeness

$\mathsf{E}$ is sound and complete for the class of all neighborhood frames.
Each logic obtained from $\mathsf{E}$ by adding some of $\mathrm{M}$, $\mathrm{C}$ and $\mathrm{N}$ is sound and complete for the frames with the matching conditions.
The proof uses a canonical neighborhood model built from maximal consistent sets, as in [[the canonical model|TVE4F04KME]].
Augmented frames are exactly the frames that come from a Kripke frame.
On a finite set every frame with (m), (c) and (n) is augmented, by [[the definition|RT7QEGZSTQ]].

### Watch out

Do not read the diamond as "some neighborhood meets $[\![ \varphi ]\!]$".
The clause is $W \setminus [\![ \varphi ]\!] \notin N(w)$, and on a supplemented frame this is the same as "every neighborhood meets $[\![ \varphi ]\!]$".
On an infinite set, (m), (c) and (n) are not enough for a Kripke frame, as the cofinite frame shows.
The logic of all neighborhood frames is $\mathsf{E}$, which proves neither $\mathrm{K}$ nor $\square\top$, so it is not normal.

### History

Dana Scott and Richard Montague introduced the semantics independently.
Krister Segerberg developed the theory of the classical modal logics in An Essay in Classical Modal Logic, 1971.
Brian Chellas presented the theory in his textbook Modal Logic: An Introduction, 1980, chapters 7 to 9.
He used the letters $\mathsf{E}$, $\mathsf{M}$, $\mathsf{C}$ and $\mathsf{N}$ and the name *minimal models*.
The name of the semantics recalls the neighborhoods of a point in topology.

### Try it

First, take $W = \{ 1, 2 \}$ with $N(1) = \{ \{ 1 \} \}$ and $N(2) = \{ \{ 1 \}, W \}$.
Is the frame supplemented?
No: $\{ 1 \} \in N(1)$ and $\{ 1 \} \subseteq W$, but $W \notin N(1)$.
The family $N(2)$ is closed under supersets, so the failure is at $1$ only.

Second, find the neighborhood frame of the Kripke frame on $\{ 1, 2 \}$ with $R = \{ (1, 2), (2, 2) \}$.
Here $R[1] = R[2] = \{ 2 \}$, so $N(1) = N(2) = \{ \{ 2 \}, W \}$.

## Explanations

### L1 human

In Kripke semantics, a world sees some other worlds, and a statement is necessary when it is true in all of them.
In neighborhood semantics, each world has a list of propositions, each one a set of worlds, that count as necessary there.
A statement is necessary at a world when the set of worlds where it is true is on that list.
So necessity need not pass from a statement to its consequences.

### L2 human

We test axiom $\mathrm{C}$ on the majority frame at the world $1$.

1. Put $V(p) = \{ 1, 2 \}$ and $V(q) = \{ 2, 3 \}$.
2. $[\![ p ]\!]$ has two elements, so it is in $N(1)$, and $\square p$ is true at $1$.
   In the same way, $\square q$ is true at $1$.
3. $[\![ p \wedge q ]\!] = \{ 2 \}$ has one element, so it is not in $N(1)$, and $\square(p \wedge q)$ is false at $1$.
4. So $(\square p \wedge \square q) \to \square(p \wedge q)$ fails at $1$.

You use such frames for a logic of "most", "probably" or "it is likely that", where two likely statements need not be likely together.
Watch out: the axiom $\mathrm{M}$ still holds here, since a superset of a majority is a majority.

### L3 human

Neighborhood frames are to the classical modal logics what Kripke frames are to the normal ones, and Chellas calls them minimal models.
The neighborhood frames on $W$ match the unary operations on $\mathcal{P}(W)$ one to one, and the Kripke frames match the operations that preserve all intersections.
Monotonic neighborhood frames are used in game logic and in coalition logic.
In these logics, a coalition can force a set of outcomes, and every superset of that set.
[[Impossible worlds|8PAJMAN8DM]] give another way to weaken the normal laws, by letting some worlds ignore the classical clauses.
