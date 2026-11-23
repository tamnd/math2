---
tag: PSRDJXRW53
kind: topic
name: First-order languages and syntax
msc: ["03B10"]
topics: [DYJ0KGTPMR]
---

## Summary

The sentence $\forall x \, \exists y \, (x < y)$ says "there is no largest element", and it is true in $\mathbb{N}$ but false in $\{ 0, 1, 2 \}$.
Before we can ask where a sentence like this is true, we need exact rules for which strings of symbols are sentences at all.
This topic of [[mathematical logic|DYJ0KGTPMR]] gives those rules for first-order logic.

The story has three layers.
A signature fixes the symbols, such as $<$, $+$ or $0$, with their arities.
Terms built from these symbols name elements, and formulas built from terms make claims.
Quantifiers bind variables, and a formula with no free variables is a sentence, which is true or false in each structure.
Substitution puts a term in place of a variable, and it must avoid capture by a quantifier.
On top of this sit theories, the treatment of equality, logics with several sorts, and normal forms that move quantifiers to the front or replace them by function symbols.
The meaning of formulas in structures is given by [[satisfaction|2RBQPV02AS]], which belongs to semantics, not syntax.

## Remarks

### Reading order

1. [[First-order logic|086QKPF0A6]]: you learn what first-order logic can say about a structure, and what it cannot.
2. [[Signature|WDVVEYD6AT]]: you learn to fix the symbols of a language and their arities.
3. [[Term|6D3WA7N2W4]]: you learn to build names for elements and to read each one in exactly one way.
4. [[Atomic formula|MCZRXR3SVB]]: you learn the simplest claims, an equation or a relation symbol applied to terms.
5. [[Well-formed formula|HYJ10AF6RT]]: you learn to build all formulas from atomic ones by connectives and quantifiers.
6. [[Free and bound variables|9CNGDRAMGC]]: you learn to tell which variable occurrences a quantifier binds.
7. [[Sentence|DKFGQTRYZE]]: you learn which formulas are true or false in a structure without further data.
8. [[Substitution|NCDZ969V7X]]: you learn to replace a free variable by a term without capture.
9. [[First-order theory|92SWXST1ZM]]: you learn to collect axioms as a set of sentences over a signature.
10. [[First-order logic with equality|Q1494G7FBM]]: you learn why equality is a logical symbol and which axioms govern it.
11. [[Many-sorted logic|7TDHDN8P96]]: you learn to work with several domains and to reduce them to one sort.
12. [[Prenex normal form|CS82V969DE]]: you learn to move all quantifiers to the front of a formula.
13. [[Skolem normal form|GCPQGMJYEV]]: you learn to replace existential quantifiers by new function symbols.
14. [[Hilbert's epsilon calculus|TH5ZKCKN3W]]: you learn a logic with a choice term for each formula, and the epsilon theorems.
15. [[Definite description|PD2R4XT79Q]]: you learn to handle "the $x$ such that" by Russell's analysis with quantifiers.
16. [[Standard first-order languages|CG8FE46WJC]]: you learn the usual signatures of orders, groups, rings, arithmetic and set theory.

### Prerequisites

You need the [[propositional calculus|JDK63589SA]], with its connectives, truth tables and propositional formulas.
You also need to read quantified statements in mathematics, as in [[propositions, connectives and quantifiers|PM1AYWABA7]].
The distinction between object language and metalanguage comes from [[logic, formal systems and foundations|H8QZY0RZXZ]].
Most proofs about terms and formulas use [[structural induction|12MQ2NJ29A]].
