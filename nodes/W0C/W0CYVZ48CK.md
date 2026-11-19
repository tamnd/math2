---
tag: W0CYVZ48CK
kind: concept
name: Jankov formula
aliases: [jankov-characteristic-formula, yankov-formula]
msc: ["03B55", "06D20"]
topics: [38EQ20GR7M]
audience: research
uses: [BND6A96S3D, TYYS649FAJ, H5NSKEP3P2]
sources:
  - arxiv: 1407.5823v1
    locator: Sections 1.2 to 1.5
  - url: https://eprints.illc.uva.nl/id/document/492
    locator: Sections 5.3 and 5.4
  - arxiv: 2502.05525v1
    locator: page 2
---

## Summary

Let $A$ be a finite subdirectly irreducible [[Heyting algebra|NG943XNQWH]], so $A$ has a unique coatom $s_A$.
With one variable $p_a$ for each $a \in A$, let $\delta(A)$ state that $a \mapsto p_a$ respects $\wedge$, $\vee$, $\to$ and $\neg$.
The *Jankov formula* of $A$ is $\chi(A) = \delta(A) \to p_{s_A}$; see [[the definition|CVGBEFQG0Q]].
By [[the Jankov-de Jongh theorem|D25R70HQ7C]], a Heyting algebra $B$ refutes $\chi(A)$ iff $A$ is a subalgebra of a homomorphic image of $B$.
For a finite rooted frame $F$, $\chi(F) = \chi(\mathrm{Up}(F))$ is refuted on a frame $G$ iff $F$ is a p-morphic image of a generated subframe of $G$.
Jankov formulas are the basic tool for building and separating [[intermediate logics|H5NSKEP3P2]].

## Motivation

A logic is a set of formulas, but its models are algebras or frames.
To compare logics one needs a formula that says "this finite model is excluded".
Jankov found that the propositional language can describe a finite algebra completely, through its operation tables.
Negating the description in the right way excludes exactly the algebras that contain the given one inside a quotient.

## Notation

We write $\chi(A)$ or $J(A)$, and $\chi(F)$ for frames.
The name is also spelled Yankov.
The frame form with fewer variables is due to de Jongh, and the modal analogue is the Jankov-Fine formula.

## Remarks

### Examples

1. [[The two-element Boolean algebra|YJV1J5PFKC]]: its Jankov formula has $\bot$ as a substitution instance. So every superintuitionistic logic other than the inconsistent one lies inside classical logic.
2. [[The two-element chain frame|8Q39BX0RF1]]: the short formula $\neg \neg p \to p$ is refuted on exactly the frames above it in the Jankov order. So every intermediate logic that does not prove $\neg\neg p \to p$ has the two-element chain as a frame.
3. Chains: a frame has depth at most $n$ iff the chain with $n + 1$ worlds is not a p-morphic image of a generated subframe. So the Jankov formula of that chain is refuted exactly on the frames of depth greater than $n$.
4. [[Jankov's continuum theorem|PSZKJY4QH3]] applies Jankov formulas to an infinite antichain of finite frames.

### Non-examples

1. [[The four-element Boolean algebra|K7NKMKY1C2]] is not subdirectly irreducible, and no formula is refuted exactly by the algebras that contain it in a quotient.
2. Not every intermediate logic is axiomatized by Jankov formulas. The logic of all frames of width at most 3 is an example. We cite this from Theorem 113 of the lecture notes of Bezhanishvili and de Jongh.

### Basic properties

1. $A$ refutes its own Jankov formula, by the valuation $p_a \mapsto a$.
2. [[Jankov-de Jongh theorem|D25R70HQ7C]]: $B \nvDash \chi(A)$ iff $A \in \mathbf{SH}(B)$.
3. Splitting: for every superintuitionistic logic $L$, either $L \subseteq \mathrm{Log}(A)$ or $\chi(A) \in L$, and not both.
4. For finite subdirectly irreducible $A$ and $B$, $\chi(A)$ is valid in $B$ iff $A \notin \mathbf{SH}(B)$. This order on finite rooted frames is used in [[the continuum theorem|PSZKJY4QH3]].

### History

Jankov introduced characteristic formulas in 1963 for finite subdirectly irreducible Heyting algebras.
In 1968 he used them to show that there are continuum many intermediate logics.
De Jongh gave the frame form with fewer variables.
Zakharyaschev's canonical formulas extend Jankov formulas so that they axiomatize every intermediate logic.

### Common errors

1. Expecting a Jankov formula for every finite algebra. Without a unique coatom there is no element $s_A$, and the defining property fails.
2. Reading $B \nvDash \chi(A)$ as "$A$ is a subalgebra of $B$". It means a subalgebra of a quotient of $B$; for frames, a p-morphic image of a generated subframe.
3. Assuming every intermediate logic is the logic of the frames that refute none of its Jankov formulas. This needs the logic to be axiomatized by Jankov formulas, which is not always the case.

## Explanations

### L1 human

A finite truth table can be written as a list of rules, one for each entry of the tables.
The Jankov formula says: "if these rules hold, then the second best value is true".
Any structure that contains a copy of the table can break this formula.
Every other structure satisfies it.
So the formula is a precise way to say "no copy of this table here".

### L2 human

1. Take the frame $C_2$: a root $r$ below a top $t$.
2. Its up-sets are $\emptyset$, $\set{t}$ and $\set{r, t}$, a three-element chain.
3. The unique coatom is $\set{t}$.
4. A frame $G$ refutes $\chi(C_2)$ iff some world of $G$ has a proper successor.
5. So $\chi(C_2)$ is valid exactly on the frames where every world is maximal, which are the frames of classical logic.

The typical use is to show that a logic $L$ contains $\chi(F)$ as soon as $F$ is not a frame of $L$.
A trap: this uses the algebraic form, because $L$ need not be complete for Kripke frames.

### L3 human

Jankov formulas show that each finite subdirectly irreducible Heyting algebra $A$ splits the lattice of varieties of Heyting algebras.
The variety generated by $A$ and the variety defined by $\chi(A)$ divide the lattice: every variety contains $A$ or satisfies $\chi(A)$, but not both.
The same construction works in every variety with equationally definable principal congruences, which covers modal algebras of finite height and many algebras of substructural logics.
In modal logic it gives the Jankov-Fine formulas, and splittings of $\mathrm{NExt}(\mathsf{K4})$ appear in [[the lattice of normal modal logics|EZ011FT3GT]].

The frame form ties Jankov formulas to the order "p-morphic image of a generated subframe".
Antichains in this order give independent axioms, and hence continuum many logics.
Zakharyaschev's canonical formulas add a set of closed domains to this order, and give axioms for all intermediate logics.
The algebraic side, the varieties of Heyting algebras, belongs to the algebra of logic.
