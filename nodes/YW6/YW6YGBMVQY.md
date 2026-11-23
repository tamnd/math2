---
tag: YW6YGBMVQY
kind: concept
name: Standard translation
msc: ["03B45", "03C80"]
topics: [SKY7AQFG1V]
audience: grad
uses: [G8VGTW9P4F, NGHWZ9Y7ZV, 086QKPF0A6, G6X7SZSNC5, X27BR4YP2Y]
sources:
  - url: https://en.wikipedia.org/wiki/Standard_translation
    locator: lead section
  - url: https://builds.openlogicproject.org/
    locator: Boxes and Diamonds, chapter on frame definability
---

## Summary

The standard translation rewrites a [[modal formula|G8VGTW9P4F]] as a formula of [[first-order logic|086QKPF0A6]] that says the same thing about a world $x$.

Here is one formula translated.
The modal formula $\square\lozenge p$ says at a world $x$: every world that $x$ sees can see a world where $p$ holds.
Its translation says this with quantifiers:
$$\mathrm{ST}_x(\square\lozenge p) = \forall y\, \big( R(x, y) \to \exists x\, ( R(y, x) \wedge P(x) ) \big).$$
The arrows of the frame become a binary relation symbol $R$, and the variable $p$ becomes a unary predicate $P$.
The inner $\exists x$ reuses the letter $x$, and two variables are enough for every modal formula.

In general, a [[Kripke model|NGHWZ9Y7ZV]] is a first-order structure for the language with $R$ and one predicate for each variable.
By [[the correctness theorem|1HQ1W36J4V]], $\varphi$ is true at $w$ exactly when $\mathrm{ST}_x(\varphi)$ holds of $w$.
Validity on a frame becomes a [[second-order|G6X7SZSNC5]] sentence, and this is the start of [[correspondence theory|3RYBWYPJVD]].

## Motivation

The truth clause of $\square$ already reads like first-order logic: "for every $v$, if $w R v$, then $\varphi$ holds at $v$".
Writing this out turns modal logic into a fragment of first-order logic.
Then the tools of first-order logic, such as compactness and the Löwenheim-Skolem theorem, apply to modal formulas.
It also lets us ask which first-order properties modal formulas can express, and which frame properties they define.

## Notation

Fix two individual variables $x$ and $y$.
The translations $\mathrm{ST}_x$ and $\mathrm{ST}_y$ are defined together by [[structural induction|12MQ2NJ29A]], with these clauses for $\mathrm{ST}_x$:
$$\mathrm{ST}_x(p) = P(x), \quad \mathrm{ST}_x(\bot) = \bot, \quad \mathrm{ST}_x(\varphi \to \psi) = \mathrm{ST}_x(\varphi) \to \mathrm{ST}_x(\psi), \quad \mathrm{ST}_x(\square\varphi) = \forall y\, ( R(x, y) \to \mathrm{ST}_y(\varphi) ).$$
$\mathrm{ST}_y$ is defined in the same way with $x$ and $y$ exchanged.
Then $\mathrm{ST}_x(\lozenge\varphi)$ is equivalent to $\exists y\, ( R(x, y) \wedge \mathrm{ST}_y(\varphi) )$.
Some books use a new variable at each box, which gives an equivalent formula with more variables.

## Remarks

### Three translations

The frame validity of $\square p \to p$ is $\forall P\, \forall x\, ( \forall y\, ( R(x, y) \to P(y) ) \to P(x) )$, which is equivalent to $\forall x\, R(x, x)$, as in [[the second-order translation of T|KM2BKWZKW8]].
$\mathrm{ST}_x(\square\bot)$ is $\forall y\, ( R(x, y) \to \bot )$, which says that $x$ has no successor.
The translation of $\square\lozenge p$ from the summary is worked out on a model in [[the translation of a box and a diamond|ZWH6KH29YT]].

### What it cannot say

The first-order formula $R(x, x)$ is not equivalent to any $\mathrm{ST}_x(\varphi)$, since it is not invariant under [[bisimulation|X27BR4YP2Y]], as [[the reflexive point|SB9HMACX5D]] shows.
The formula "$x$ has two different successors" is not equivalent to any $\mathrm{ST}_x(\varphi)$ either.
A world with one successor and a world with two successors, with all variables false at all successors, are bisimilar.
On frames, Löb's axiom $\square(\square p \to p) \to \square p$ says "transitive and conversely well-founded", which no first-order sentence expresses.

### The rules you can use

$\mathrm{ST}_x(\varphi)$ has at most the free variable $x$, and it uses only the variables $x$ and $y$.
Truth at a world, truth in a model and validity on a frame become, in turn, the formula $\mathrm{ST}_x(\varphi)$, the sentence $\forall x\, \mathrm{ST}_x(\varphi)$, and the $\Pi^1_1$ sentence $\forall P_1 \dots \forall P_n\, \forall x\, \mathrm{ST}_x(\varphi)$.
The modal consequence relation over all models is compact, since first-order logic is compact.
Modal satisfiability is decidable, since the two-variable fragment of first-order logic is decidable, and Mortimer proved in 1975 that this fragment has the finite model property.
Up to equivalence, the translations are exactly the first-order formulas in $x$ that are [[invariant under bisimulation|TKFFTAX30E]], which is [[van Benthem's theorem|Y89MGMWE4H]].

### Watch out

In $\mathrm{ST}_y(\square\varphi)$ the quantifier is on $x$, and the new $x$ shadows the old one, so the inner $x$ does not name the outer world.

Frame validity is not first-order in general.
The quantifiers over $P$ are second-order, and some formulas, such as Löb's axiom, have no first-order equivalent on frames.

Distinguish truth in a model from validity on a frame: the first fixes the predicates, and the second quantifies over them.

### History

Kanger and Hintikka in the 1950s and Kripke in 1959 and 1963 read the truth clauses as conditions on worlds and a relation.
Van Benthem's dissertation of 1976, Modal Correspondence Theory, made the translation the basis of correspondence theory and proved the bisimulation characterization.

### Try it

Translate $\square(p \to \square q)$.
The outer box gives $\forall y\, ( R(x, y) \to \mathrm{ST}_y(p \to \square q) )$.
Then $\mathrm{ST}_y(p \to \square q) = P(y) \to \forall x\, ( R(y, x) \to Q(x) )$.
So the result is $\forall y\, ( R(x, y) \to ( P(y) \to \forall x\, ( R(y, x) \to Q(x) ) ) )$, and its only free variable is the first $x$.

## Explanations

### L1 human

A modal statement talks about worlds and arrows without naming them.
The standard translation names them: "necessarily $p$ at $x$" becomes "for every $y$ that $x$ can reach, $p$ holds at $y$".
After the translation, ordinary logic with "for all" and "there is" can study modal statements.

### L2 human

The translation is a recipe with one rule per connective, and the only real rule is the one for the box.
Each box becomes a guarded quantifier "for all $y$ with $R(x, y)$", and each diamond becomes "there is $y$ with $R(x, y)$".
Because each quantifier needs only the world it starts from, the variables can alternate, $x$ then $y$ then $x$, however deep the formula is.
The typical use is to move a question about modal formulas into first-order logic, where compactness and other tools apply.
Watch out: a formula true in one model is a first-order fact, but a formula valid on a frame is a second-order fact.

### L3 human

The standard translation embeds the basic modal language into the two-variable fragment and into the guarded fragment, two decidable fragments of first-order logic.
Correspondence theory studies when the $\Pi^1_1$ translation of frame validity is equivalent to a first-order sentence.
[[Sahlqvist's theorem|S4SSDMETJM]] gives a large syntactic class where it is, and the minimal valuation of [[the second-order translation of T|KM2BKWZKW8]] is the simplest case of its method.
