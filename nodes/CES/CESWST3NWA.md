---
tag: CESWST3NWA
kind: concept
name: Algebraizable logic
aliases: [algebraizable-logic, blok-pigozzi-algebraizability]
msc: ["03G27"]
topics: [QYA4H5Y7VR]
audience: research
uses: [XADWEW9TNP, FCXHSC6Z4R, WRXEKT4NQS, QC9M3Q8B8Q, 09K9MWD2QQ, Q11N8X99FK, 0XADJKM699, NG943XNQWH, 8T4M7RN9AC, E337A6WVH3]
sources:
  - url: https://en.wikipedia.org/wiki/Abstract_algebraic_logic
  - url: https://en.wikipedia.org/wiki/Algebraic_logic
  - book: isbn:9781848902077
---

## Summary

A propositional logic is algebraizable if its [[consequence relation|FCXHSC6Z4R]] and the equational consequence of a class $K$ of algebras can be translated into each other, by a set $E(x)$ of equations and a set $\Delta(x, y)$ of formulas; see [[the definition|XADWEW9TNP]].
The class $K$ is then the equivalent algebraic semantics of the logic, and it can be taken to be a [[quasivariety|WRXEKT4NQS]].
Blok and Pigozzi introduced the notion in 1989, as the abstract form of the method of [[Lindenbaum-Tarski algebras|QC9M3Q8B8Q]].
Their main theorem matches the theories of the logic with the relative congruences of the formula algebra, and the extensions of the logic with the subquasivarieties of $K$; see [[this theorem|8ZFJ67HTWR]].

## Motivation

For [[classical logic|09K9MWD2QQ]], the passage to [[Boolean algebras|0XADJKM699]] works in both directions: formulas become equations $\varphi \approx 1$, and equations $s \approx t$ become formulas $s \leftrightarrow t$.
Many other logics have such a pair of translations, and the same arguments work for all of them.
Algebraizability states exactly what the pair must satisfy, so that the arguments can be done once.
It also gives a criterion for when a logic has no good algebraic counterpart.

## Notation

We write $\vdash$ for the logic, $K$ for an equivalent algebraic semantics, $E(x)$ for the defining equations and $\Delta(x, y)$ for the equivalence formulas.
$E[\Gamma]$ and $\Delta[\Theta]$ apply the translations to sets, and $\models_K$ is equational consequence relative to $K$.

## Remarks

### Examples

1. [[Classical propositional logic and Boolean algebras|X3EQTPS85Z]].
2. [[Intuitionistic logic and Heyting algebras|Y1DVDH3EYH]], with the same $E$ and $\Delta$ as in the classical case.
3. Łukasiewicz infinite-valued logic and [[MV-algebras|8T4M7RN9AC]], with $E(x) = \set{x \approx 1}$ and $\Delta(x, y) = \set{x \to y, y \to x}$.
4. The full Lambek calculus with exchange and [[commutative residuated lattices|E337A6WVH3]], with $E(x) = \set{x \wedge 1 \approx 1}$.
5. The global consequence of a normal modal logic and its variety of modal algebras.

### Non-examples

1. [[The conjunction and disjunction fragment of classical logic|N1FSY99EQ8]] has no theorems, so it is not algebraizable.
2. First-degree entailment is not algebraizable, for the same reason.

### Basic properties

1. The equivalent quasivariety semantics is unique, and $E$ and $\Delta$ are unique up to interderivability.
2. Every algebraizable logic is protoalgebraic: $\vdash \Delta(x, x)$ and $x, \Delta(x, y) \vdash y$.
3. The theories of $\vdash$ correspond to the congruences $\theta$ of $\mathrm{Fm}$ with $\mathrm{Fm}/\theta \in K$, by $T \mapsto \set{(\varphi, \psi) : \Delta(\varphi, \psi) \subseteq T}$.
4. For a finitary logic with $E$ finite, the extensions of $\vdash$ match the subquasivarieties of $K$, in the reverse order.

### History

Rasiowa studied implicative logics, a class of logics with an algebraic semantics given by an implication.
Blok and Pigozzi defined algebraizable logics in their memoir "Algebraizable logics" of 1989, and proved the main theorems.
Their work, with that of Czelakowski, Font and Jansana, became the core of abstract algebraic logic.

### Common errors

1. Thinking that a logic is algebraizable as soon as it is complete for a class of algebras. Completeness gives only (A1), and the conjunction and disjunction fragment of classical logic is complete for distributive lattices.
2. Assuming that the defining equations are always $x \approx 1$. In the full Lambek calculus with exchange the designated elements are those above $1$, so $E(x) = \set{x \wedge 1 \approx 1}$.
3. Taking the class of all algebras that validate the theorems. The equivalent algebraic semantics is fixed by the consequence relation, not only by the theorems.

## Explanations

### L1 human

Some logics are algebra in disguise: every proof from premises is a calculation with equations, and every calculation with equations is a proof.
These logics are called algebraizable, and each comes with its own class of algebras.

### L2 human

1. In intuitionistic logic, $p, p \to q \vdash q$.
2. Translate with $E(x) = \set{x \approx 1}$: from $p \approx 1$ and $p \to q \approx 1$ infer $q \approx 1$.
3. This holds in every Heyting algebra, since $p \wedge (p \to q) \le q$.
4. Conversely, the equation $p \approx q$ translates into the formulas $p \to q$ and $q \to p$.

The typical use: to study the extensions of a logic, study the subquasivarieties of its algebras.
The trap: the translations must be inverse to each other; a semantics with only one direction can exist for logics that are not algebraizable.

### L3 human

Algebraizability is a property of the Leibniz operator: by a theorem of Blok and Pigozzi, a logic is algebraizable iff the operator is injective and order-preserving on theories and commutes with inverse substitutions; see [[the Leibniz hierarchy|6JT3CMJT8F]].
The equivalent quasivariety semantics is then the class of algebra reducts of the reduced matrix models, and the matrix semantics collapses to an algebraic one.
Bridge theorems translate interpolation, definability and deduction theorems into amalgamation, epimorphism and congruence properties of $K$.
