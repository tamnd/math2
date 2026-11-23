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
Ann opens it and reads it while Bob watches, so Bob sees that she reads it but not what it says.
Afterwards Ann knows whether $p$, Bob does not, and Bob knows that Ann knows.
We get exactly this from an action model of [[dynamic epistemic logic|9465T2PWZT]].

### The two models

The initial model $M$ has worlds $w$, where $p$ is true, and $v$, where $p$ is false.
Neither agent can tell them apart, so both relations have the single class $\{w, v\}$.
The action model $\mathsf{E}$ has an event $e$ with precondition $p$, "the letter says $p$", and an event $f$ with precondition $\neg p$.
Ann can tell $e$ from $f$, so her event relation has classes $\{e\}$ and $\{f\}$.
Bob cannot, so his has the single class $\{e, f\}$.

### The product update

The product $M \otimes \mathsf{E}$ has a world $(x, g)$ for each world $x$ and event $g$ with $\mathrm{pre}(g)$ true at $x$.
Two pairs $(x, g)$ and $(y, h)$ are linked for agent $c$ when $x \sim_c y$ and $g \sim_c h$.
Since $p$ holds at $w$ only, the pairs are $(w, e)$ and $(v, f)$.
For Ann, $w \sim_a v$ but $e \not\sim_a f$, so the two pairs are not linked, and her classes are singletons.
For Bob, $w \sim_b v$ and $e \sim_b f$, so the two pairs are linked.
The valuation is copied from the first coordinate, so $p$ holds at $(w, e)$ and fails at $(v, f)$.

### Reading off knowledge

At the actual pair $(w, e)$, $K_a p$ is true, since Ann's class is $\{(w, e)\}$.
$K_b p$ is false, since Bob's class contains $(v, f)$.
$K_b(K_a p \vee K_a \neg p)$ is true, because Ann knows whether $p$ at both pairs, so Bob knows that Ann knows whether $p$.

## Remarks

A public announcement of $p$ would delete $v$, and Bob would learn $p$ too, as in [[the announcement example|YDAHGYKQZN]].
So this event is not a public announcement.
If Bob did not even see Ann read, one adds a third event with precondition $\top$, which Bob takes to be the actual one.
Then Bob's beliefs stay as before, and his relation is no longer reflexive.

Action models have reduction axioms like [[those of public announcements|MFGHDHGV1D]].
Here $[\mathsf{E}, e]K_b p \leftrightarrow (p \to (K_b[\mathsf{E}, e]p \wedge K_b[\mathsf{E}, f]p))$.
Since $[\mathsf{E}, e]p$ is $p \to p$ and $[\mathsf{E}, f]p$ is $\neg p \to p$, which is $p$, the right side simplifies to $p \to K_b p$.
It is false at $w$, which matches $K_b p$ failing at $(w, e)$.

## Explanations

### L1 human

Ann reads a letter, and Bob watches her read it.
Afterwards Ann knows what it says.
Bob still does not know, but he knows that Ann knows.
A public announcement cannot model this, since it would tell Bob as well.
An action model lists the possible events and who can tell them apart.

### L2 human

The product update is a table.
List all pairs of a world and an event whose precondition holds at the world.
Then link two pairs for an agent when she cannot tell the worlds apart and cannot tell the events apart.
Here only two of the four pairs survive, and only Bob links them.
The typical use is to model partly private communication in card games and protocols.
Watch out: the precondition is checked in the old model, before the event.

### L3 human

The product $M \otimes \mathsf{E}$ generalizes restriction, since a public announcement is the action model with one event, precondition $\varphi$, seen by everyone.
Product updates can make the model larger, which is why iterated action model updates lead to undecidable planning problems.
