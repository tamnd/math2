---
tag: KM2BKWZKW8
kind: example
name: The second-order translation of T
msc: ["03B45"]
topics: [SKY7AQFG1V]
audience: grad
instance_of: [YW6YGBMVQY]
uses: [YW6YGBMVQY, 1HQ1W36J4V, G6X7SZSNC5, FDFQFWPM4X, 0X8NMST0J2, 6BQ71KQ6QT]
sources:
  - url: https://en.wikipedia.org/wiki/Standard_translation
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Kripke_semantics
    locator: Correspondence and completeness
---

## Example

Let $\mathrm{T}$ be the axiom $\square p \to p$.
By [[the correctness of the standard translation|1HQ1W36J4V]], a [[frame|6BQ71KQ6QT]] $\mathfrak{F} = (W, R)$ validates $\mathrm{T}$ if and only if it satisfies this [[second-order|G6X7SZSNC5]] sentence:
$$\forall P\, \forall x\, \big( \forall y\, (Rxy \to Py) \to Px \big).$$
We show that this sentence is equivalent to the first-order sentence $\forall x\, Rxx$.

### From reflexivity to the sentence

Assume $\forall x\, Rxx$, so $R$ is [[reflexive|0X8NMST0J2]].
Let $P \subseteq W$ and $x \in W$, and assume $\forall y\, (Rxy \to Py)$.
Take $y = x$: then $Rxx$ holds, so $Px$ holds.
As $P$ and $x$ were arbitrary, the second-order sentence holds.

### From the sentence to reflexivity

Assume the second-order sentence, and let $x_0 \in W$.
Choose $P = \{ y \in W : R x_0 y \}$, the minimal valuation that makes $\square p$ true at $x_0$.
Then $\forall y\, (R x_0 y \to Py)$ holds by the choice of $P$.
The sentence, with this $P$ and $x = x_0$, gives $P x_0$, which by the definition of $P$ means $R x_0 x_0$.
As $x_0$ was arbitrary, $\forall x\, Rxx$ holds.

### Check

Take $W = \{ a, b \}$ and $R = \{ (a, b), (b, b) \}$, which is not reflexive at $a$.
The minimal valuation at $x_0 = a$ is $P = \{ b \}$.
Then $\square p$ is true at $a$, since its only successor $b$ is in $P$, while $p$ is false at $a$.
So $\mathrm{T}$ fails at $a$ under $V(p) = \{ b \}$, as the argument predicts.

## Remarks

### What the minimal valuation does

The quantifier $\forall P$ ranges over all subsets of $W$, so the frame condition looks second-order.
The minimal valuation removes it: one well-chosen $P$ decides the whole quantifier.
This is the method of [[common modal axiom schemata|FDFQFWPM4X]] written in the language of the [[standard translation|YW6YGBMVQY]].

### How far the method goes

[[Sahlqvist's theorem|S4SSDMETJM]] makes the method uniform for a large class of formulas.
Some formulas admit no such elimination over all frames, for example the [[McKinsey formula|4N4ZNWZRE2]].

### Watch out

The minimal valuation depends on $x$, so the substitution for $P$ is made after $x$ is fixed.
And the equivalence is between frame validity and a first-order condition: truth of $\mathrm{T}$ in one model is a different and weaker notion, and it does not force reflexivity.

## Explanations

### L1 human

"What is necessary is true" holds on a frame exactly when every world sees itself.
To test the law at a world, we make $p$ true exactly at the worlds it sees.
Then "necessarily $p$" holds there by design.
The law then forces $p$ at the world itself, so the world sees itself.

### L2 human

The computation has three moves.
Write frame validity of $\mathrm{T}$ as $\forall P\, \forall x\, ( \forall y\, (Rxy \to Py) \to Px )$.
Put $P$ equal to the set of successors of $x$, so that the antecedent holds.
Read off $Rxx$ from the consequent.
The typical use is to compute the first-order correspondent of an axiom by one substitution for $P$.
Try the same moves on $\square p \to \square\square p$: the minimal valuation is again the successors of $x$, and the consequent says that every world two steps from $x$ is a successor of $x$, which is transitivity.

### L3 human

In Sahlqvist's method, the minimal valuation is read off from the antecedent of the formula, and the same recipe works for every Sahlqvist formula.
The resulting first-order condition is the correspondent of the formula, and [[correspondence theory|3RYBWYPJVD]] studies which formulas have one.
