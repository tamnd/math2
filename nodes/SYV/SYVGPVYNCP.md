---
tag: SYVGPVYNCP
kind: example
name: Reading a letter in front of another agent as an action model update
msc: ["03B42"]
topics: [CQM9SRN8PM]
audience: research
instance_of: [9465T2PWZT]
uses: [YDAHGYKQZN, MFGHDHGV1D, 0G8VEZ3WTK]
sources:
  - url: https://en.wikipedia.org/wiki/Dynamic_epistemic_logic
    locator: section Event Model, section Product Update
  - book: isbn:9781402058387
    locator: van Ditmarsch, van der Hoek and Kooi, Dynamic Epistemic Logic, chapter on action models
---

## Example

A letter says whether $p$ holds.
Ann reads it while Bob watches, so Bob sees that she reads it but not what it says.

1. Initial model $M$: worlds $w$ ($p$ true) and $v$ ($p$ false). Neither agent can tell them apart: both relations have the single class $\set{w, v}$.
2. Action model $\mathsf{E}$: events $e$ with precondition $p$ ("the letter says $p$") and $f$ with precondition $\neg p$.
3. Ann can tell $e$ from $f$: her event relation has classes $\set{e}$ and $\set{f}$. Bob cannot: his has the class $\set{e, f}$.

The product update $M \otimes \mathsf{E}$ has the pairs $(x, g)$ with $\mathrm{pre}(g)$ true at $x$, and $(x, g) \sim_c (y, h)$ iff $x \sim_c y$ and $g \sim_c h$.

4. The pairs are $(w, e)$ and $(v, f)$, since $p$ holds at $w$ only.
5. Ann: $w \sim_a v$ but $e \not\sim_a f$. So the two pairs are not related for Ann, and her classes are singletons.
6. Bob: $w \sim_b v$ and $e \sim_b f$. So the two pairs are related for Bob.
7. Valuations are copied from the first coordinate: $p$ holds at $(w, e)$ and fails at $(v, f)$.

Evaluate at the actual pair $(w, e)$.

8. $K_a p$ is true, since Ann's class is $\set{(w, e)}$.
9. $K_b p$ is false, since Bob's class contains $(v, f)$.
10. $K_b(K_a p \vee K_a \neg p)$ is true: at both pairs Ann knows whether $p$. Bob knows that Ann knows whether $p$.

## Remarks

A public announcement of $p$ would delete $v$, and Bob would learn $p$ too, as in [[the announcement example|YDAHGYKQZN]].
So this event is not a public announcement.
If Bob did not even see Ann read, one adds a third event with precondition $\top$, which Bob takes to be the actual one.
Then Bob's beliefs stay as before, and his relation is no longer reflexive.
Action models have reduction axioms like [[those of public announcements|MFGHDHGV1D]]: for example $[\mathsf{E}, e]K_b p \leftrightarrow (p \to (K_b[\mathsf{E}, e]p \wedge K_b[\mathsf{E}, f]p))$.

## Explanations

### L1 human

Ann reads a letter, and Bob watches her read it.
Afterwards Ann knows what it says.
Bob still does not know, but he knows that Ann knows.
A public announcement cannot model this, since it would tell Bob as well.
An action model lists the possible events and who can tell them apart.

### L2 human

The product update is a table.

1. List all pairs of a world and an event whose precondition holds at the world.
2. Join two pairs for an agent when she cannot tell the worlds apart and cannot tell the events apart.

Here only two of the four pairs survive, and only Bob joins them.
The typical use is to model partly private communication in card games and protocols.
A trap: the precondition is checked in the old model, before the event.

### L3 human

The product $M \otimes \mathsf{E}$ generalizes restriction: a public announcement is the action model with one event, precondition $\varphi$, seen by everyone.
Product updates can make the model larger, which is why iterated action model updates lead to undecidable planning problems.
