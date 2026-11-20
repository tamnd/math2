---
tag: Z3DE4R4RET
kind: concept
name: Algebraic logic
aliases: [algebraic-logic]
msc: ["03G27", "03G05", "03G15"]
topics: [QYA4H5Y7VR]
audience: grad
uses: [09K9MWD2QQ, 0XADJKM699, AJNZJD8442]
sources:
  - url: https://en.wikipedia.org/wiki/Algebraic_logic
    locator: lead section; History
  - url: https://en.wikipedia.org/wiki/Abstract_algebraic_logic
    locator: History
  - url: https://plato.stanford.edu/entries/logic-algebraic-propositional/
    locator: "Algebraic Propositional Logic, sections 1, 5 and 9"
  - book: isbn:9781848902077
same_as:
  wikidata: Q1005222
  wikipedia: Algebraic logic
---

## Summary

*Algebraic logic* is the study of a logic $\mathcal{L}$ through a class $\mathsf{K}$ of algebras of the same signature as the formulas of $\mathcal{L}$.
The link is a translation: a formula $\varphi$ is a theorem of $\mathcal{L}$ iff the equation $\varphi \approx 1$ (or a set of equations built from $\varphi$) holds in every algebra of $\mathsf{K}$.
The class $\mathsf{K}$ is often a [[variety|AJNZJD8442]], and it is found as the class of quotients of the formula algebra by provable equivalence, as in the [[Lindenbaum-Tarski algebra|QC9M3Q8B8Q]].
The field has a propositional branch (Boolean, Heyting, modal, MV and residuated algebras), a first-order branch (cylindric, polyadic and relation algebras) and an abstract branch ([[algebraizable logics|CESWST3NWA]] and the [[Leibniz hierarchy|6JT3CMJT8F]]).
It matters because it turns questions on proofs into questions on equations, where the tools of universal algebra apply.

## Motivation

A propositional formula such as $p \land (q \lor r)$ is a term of an algebra, and the connectives are operations.
Two formulas that the logic proves equivalent behave as one object, so the natural thing is to take the quotient.
For [[classical propositional logic|09K9MWD2QQ]] the quotient is a [[Boolean algebra|0XADJKM699]], and completeness becomes the statement that the two-element algebra separates the elements of this quotient.
The same pattern works for many other logics, and each time a property of the logic (interpolation, a deduction theorem, definability) matches a property of the class of algebras.
Algebraic logic studies this matching in general, so that one proof covers many logics.

## Notation

We write $\mathbf{Fm}$ for the algebra of formulas over a set of variables, $\vdash$ for the consequence relation of the logic and $\mathsf{K}$ for the class of algebras.
An equation is written $s \approx t$, and $\mathsf{K} \models s \approx t$ means that it holds in every algebra of $\mathsf{K}$ under every assignment.
Many authors write $\mathrm{Alg}(\mathcal{L})$ or $\mathbf{Alg}\,\mathcal{L}$ for the class of algebras of a logic $\mathcal{L}$.

## Remarks

### Examples

1. Classical propositional logic and Boolean algebras: a formula is a theorem iff it takes the value $1$ in every Boolean algebra; see [[the algebraic completeness theorem|J2GTJ8FKF2]].
2. [[Intuitionistic logic|Q11N8X99FK]] and [[Heyting algebras|NG943XNQWH]]: a formula is a theorem iff it is valid in every Heyting algebra, by [[Heyting algebra semantics|JM1XJXWZYH]].
3. Normal [[modal logics|C3RZY20ETK]] and [[modal algebras|3H85NSFWHK]]: each normal modal logic is the set of formulas valid in a variety of modal algebras, by [[the algebraic completeness of normal modal logics|Z0S91AK9WG]].
4. [[Infinite-valued Łukasiewicz logic|NFCEM44XYH]] and [[MV-algebras|8T4M7RN9AC]]: [[Chang's completeness theorem|QM0F33QE9P]] shows that the standard MV-algebra $[0, 1]$ generates the variety of all MV-algebras.
5. [[First-order logic|086QKPF0A6]] with equality and [[cylindric algebras|1MDT9BF81H]]: formulas modulo equivalence in a theory form a locally finite cylindric algebra; see [[this example|5MH9ZKCEHV]].

### Non-examples

1. A single truth table is a computation in one algebra, the two-element algebra; it is not a study of a logic through a class of algebras.
2. The algebra of formulas itself, without the quotient, is not a Boolean algebra, since $p \land q$ and $q \land p$ are different terms; see [[this non-example|S563QJHDTK]].
3. The $\{\land, \lor\}$-fragment of classical logic has a class of algebras (distributive lattices), but it is not [[algebraizable|CESWST3NWA]]; see [[this non-example|N1FSY99EQ8]].

### Basic properties

1. For classical logic the [[Lindenbaum-Tarski algebra|QC9M3Q8B8Q]] of the empty theory is the free Boolean algebra on the variables; see [[this theorem|JVZ8APEV7A]].
2. For a normal modal logic $\Lambda$, the normal extensions of $\Lambda$ match the subvarieties of its variety of modal algebras, by [[the algebraic completeness theorem|Z0S91AK9WG]].
3. For an algebraizable logic, the lattice of its extensions is dually isomorphic to the lattice of subquasivarieties of its equivalent algebraic semantics, and the axiomatic extensions match the relative subvarieties, by [[the correspondence theorem|8ZFJ67HTWR]].
4. Bridge theorems relate logical and algebraic properties, for example interpolation and amalgamation; see [[the bridge theorems|C3DC1C23SQ]].

### History

Boole treated classical propositional reasoning as calculation in an algebra in 1847, and Peirce and Schröder extended this work.
Lindenbaum used the quotient of formulas by provable equivalence in Łukasiewicz's seminar from 1926 to 1927, and Tarski later developed the method.
Tarski and his students introduced cylindric algebras and revived the study of relation algebras.
Abstract algebraic logic grew from the work of Rasiowa, Sikorski, Łoś and Suszko, and it took its present form in the 1980s with Czelakowski, Blok and Pigozzi.

### Common errors

1. Identifying a logic with one algebra. A logic corresponds to a class of algebras, and one algebra can fail to generate the whole class.
2. Assuming that every logic has a good algebraic counterpart. The $\{\land, \lor\}$-fragment of classical logic and first-degree entailment are not protoalgebraic; see [[the Leibniz hierarchy|6JT3CMJT8F]].
3. Confusing the algebra of formulas with the Lindenbaum-Tarski algebra. Only the quotient by provable equivalence satisfies the laws of the algebras of the logic.

## Explanations

### L1 human

In school algebra we calculate with numbers by rules such as $a + b = b + a$.
Algebraic logic calculates with statements in the same way: "$p$ and $q$" equals "$q$ and $p$", and "not not $p$" equals "$p$" in classical logic.
The statements, up to logical equivalence, form an algebra.
Questions about the logic then become questions about that algebra.
For example, a formula is a theorem of classical propositional logic exactly when it takes the value $1$ in every Boolean algebra under every assignment.
With the two values $0$ and $1$, the formula "$p$ or not $p$" has the value $1$ for $p = 0$ and for $p = 1$, so it is a theorem.

### L2 human

A worked example: classical logic and the four-element Boolean algebra.

1. Take $B = \set{0, a, b, 1}$, the [[power set Boolean algebra|004J7ZEFAT]] of a two-element set, with $a$ and $b = \neg a$ the two singletons.
2. Assign $p \mapsto a$ and $q \mapsto b$.
3. The formula $p \lor \neg p$ gets the value $a \lor b = 1$.
4. The formula $p \to q$, read as $\neg p \lor q$, gets the value $b \lor b = b \ne 1$.
5. So $p \to q$ is not a theorem of classical logic, and $p \lor \neg p$ passes this test.

The typical use: to show that a formula is not a theorem, find one algebra of the class and one assignment where the formula is not $1$.
The trap: one algebra that validates a formula does not show that the formula is a theorem; the formula must hold in every algebra of the class.

### L3 human

Algebraic logic has two levels.
At the first level one studies a fixed logic and its algebras: Boolean algebras with [[Stone duality|B9T33D5MJK]], Heyting algebras with [[Esakia duality|CD9Y7YP4EJ]], modal algebras with [[the Jónsson-Tarski theorem|HC5V2QFFWB]], MV-algebras with [[Mundici's equivalence|64NDFWQEZ2]], cylindric and relation algebras with their representation problems.
At the second level, abstract algebraic logic studies the process itself: when does a logic have an equivalent algebraic semantics, and what does the Leibniz operator do.
This second level is to the first what universal algebra is to the theory of groups and rings.
The results of the second level are the bridge theorems, which turn a metalogical property into an algebraic property for a whole class of logics.
The duality theories of the order, lattices and universal algebra area then turn the algebraic property into a property of spaces or frames.
