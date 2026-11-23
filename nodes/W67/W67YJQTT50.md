---
tag: W67YJQTT50
kind: statement
role: theorem
name: Kripke incompleteness
msc: ["03B45"]
topics: [SPQVNPZDTB]
audience: research
uses: [NGHWZ9Y7ZV, 6W9MEGN982, F5WN5GCAEQ, C3RZY20ETK]
about: [C3RZY20ETK, NGHWZ9Y7ZV]
proofs: [XJR2Z2PY92]
history:
  first_stated: "Thomason 1972 (tense logic) and 1974, Fine 1974, first Kripke incomplete logics"
  notes: "The logic KvB below is van Benthem's example."
sources:
  - url: https://en.wikipedia.org/wiki/Kripke_semantics
    locator: General frame semantics
  - url: https://en.wikipedia.org/wiki/General_frame
    locator: Completeness
---

## Statement

Some normal modal logics cannot be captured by any class of Kripke frames, and the van Benthem formula gives a short example.
The van Benthem formula is the following.
$$\mathrm{vB} = \square \lozenge \top \to \square(\square(\square p \to p) \to p)$$
On Kripke frames it says exactly what the variable-free formula $\square \lozenge \top \to \square \bot$ says, yet the logic of $\mathrm{vB}$ cannot prove that formula.

A normal modal logic $L$ is *Kripke complete* if there is a class $\mathsf{C}$ of [[Kripke frames|NGHWZ9Y7ZV]] such that $L$ is the set of formulas valid on every frame of $\mathsf{C}$.
Equivalently, every formula valid on all Kripke frames of $L$ is a theorem of $L$.
A logic that is not Kripke complete is *Kripke incomplete*.
Let $\mathsf{KvB}$ be the smallest normal modal logic that contains $\mathrm{vB}$, and let $\mathrm{E}$ be $\square \lozenge \top \to \square \bot$.

**Theorem.**

1. A Kripke frame validates $\mathrm{vB}$ if and only if it validates $\mathrm{E}$.
2. The formula $\mathrm{E}$ is not a theorem of $\mathsf{KvB}$.
3. So $\mathsf{KvB}$ is Kripke incomplete, and not every normal modal logic is Kripke complete.

The [[proof|XJR2Z2PY92]] uses a [[general frame|6W9MEGN982]] for item 2.

## Remarks

### Why the formula collapses on frames

Take any world $y$ of any Kripke frame, and make $p$ true everywhere except at $y$.
Then $p$ fails at $y$, while every successor $z$ of $y$ satisfies $\square p \to p$.
If $z \ne y$, the reason is that $p$ holds at $z$.
If $z = y$, the reason is that $y$ sees a world without $p$, so $\square p$ fails at $y$.
So $\square(\square p \to p) \to p$ fails at $y$, and $\square(\square(\square p \to p) \to p)$ can hold at $x$ under every valuation only if $x$ has no successors.
That turns $\mathrm{vB}$ into $\mathrm{E}$ on every frame.

### Why each hypothesis is needed

The theorem is about Kripke frames only.
Every normal modal logic is complete for its general frames, and even for its descriptive frames, so incompleteness disappears in general frame semantics.
The antecedent $\square \lozenge \top$ also matters.
Without it, the formula $\square(\square(\square p \to p) \to p)$ is valid only on frames with no arrows, by the argument above.
The antecedent restricts the claim to worlds whose successors all have successors, and the general frame in the proof has such a world.

### What it gives you

Frame validity does not determine a logic: $\mathsf{KvB}$ and $\mathsf{KvB} \oplus \mathrm{E}$ are distinct logics with the same Kripke frames.
So each completeness theorem is a real theorem that needs a proof, by [[canonical models|TVE4F04KME]], [[filtration|6ZZSHAKG5F]] or another method.
Algebraically, the complex algebras of Kripke frames are the complete atomic modal algebras with a completely additive operator, and they do not generate every variety of modal algebras.

### The converse and wider results

Many logics are Kripke complete.
Every logic axiomatized over $\mathsf{K}$ by [[Sahlqvist formulas|S4SSDMETJM]] is complete, and so is every normal extension of $\mathsf{S4.3}$; see the [[lattice of normal modal logics|EZ011FT3GT]].
Incompleteness reaches strong logics too: Kit Fine gave an incomplete logic that contains $\mathsf{S4}$.
The *degree of incompleteness* of $L$ is the number of normal logics with exactly the same Kripke frames as $L$.
Blok proved that in $\mathrm{NExt}(\mathsf{K})$ this degree is always $1$ or $2^{\aleph_0}$, and he described the logics of degree $1$ through splittings.
Incompleteness also occurs in [[quantified modal logic|D2H3S12V7X]].

### Watch out

An incomplete logic still has models and frames.
By Makinson's theorem it is valid on a one-point frame, so it has at least one Kripke frame.
What it lacks is enough Kripke frames to refute each of its non-theorems, and general frames supply the missing ones.

## History

Steven Thomason gave the first Kripke incomplete logics: a tense logic in 1972 and a logic with one box in 1974.
Kit Fine published an incomplete extension of $\mathsf{S4}$ in 1974.
Johan van Benthem later gave the short example $\mathsf{KvB}$ used here.
Willem Blok then proved his dichotomy theorem on the degree of incompleteness.

## Explanations

### L1 human

A modal logic is a set of laws about "necessarily" and "possibly".
Pictures of points and arrows give a way to test these laws.
One hopes that a logic is exactly the set of laws true in all pictures that fit it.
For some logics this hope fails: a law holds in every fitting picture, yet the logic cannot prove it.
The van Benthem formula is such a logic: in every picture it says "a point whose next points all have next points has no next points at all", but its logic does not prove that.

### L2 human

We test $\mathrm{vB}$ on one frame.
Let $x$ see $y$, and let $y$ see itself, with nothing else.
At $x$ the antecedent holds, because the only successor $y$ has the successor $y$:
$$x \models \square \lozenge \top.$$
Make $p$ false at $y$ and true at $x$.
At $y$, the only successor is $y$ itself, and $\square p$ fails there, so $\square p \to p$ holds at $y$, and $y \models \square(\square p \to p)$.
But $p$ fails at $y$, so the consequent of $\mathrm{vB}$ fails at $x$.
So the frame refutes $\mathrm{vB}$, as item 1 predicts, since it also refutes $\mathrm{E}$ at $x$.
The typical use of $\mathsf{KvB}$ is as the shortest example of incompleteness.

### L3 human

Algebraically, $L$ is Kripke complete when the variety of modal algebras of $L$ is generated by complex algebras of frames.
Incompleteness shows that these algebras do not generate all varieties.
Completeness can be recovered by changing the notion of frame: descriptive frames for normal logics, neighborhood frames for non-normal ones, or algebras.
The question of which logics are complete led to the study of canonicity and persistence, and to [[Sahlqvist's theorem|S4SSDMETJM]].
