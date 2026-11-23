---
tag: PM1AYWABA7
kind: topic
name: Propositions, connectives and quantifiers
msc: ["03B05", "03B10"]
topics: [DYJ0KGTPMR]
---

## Summary

"If $n$ is even and $n > 2$, then $n$ is not prime" is a sentence that every reader understands, and it is built from small parts: "and", "if, then", "not", and a hidden "for every $n$".
This part of [[mathematical logic|DYJ0KGTPMR]] takes such sentences apart and makes each part exact.

The story starts with propositions, the sentences that are true or false, and with the principle of bivalence, which says there is no third value.
Then come the connectives "not", "and", "or", "exclusive or", "if, then" and "if and only if", each fixed by a truth table.
Every pair of truth values gives one of $16$ binary connectives, and the Sheffer stroke shows that one connective alone can express them all.

Truth tables turn questions about formulas into finite checks.
They find the tautologies and the logically equivalent formulas, and with them the laws of logic: excluded middle, noncontradiction, double negation, De Morgan's laws and the contrapositive.
The converse and the inverse show which rearrangements of an implication are not equivalent, and necessary and sufficient conditions give the two readings of one arrow.

The rules of inference turn these laws into steps of a proof: modus ponens, modus tollens, hypothetical syllogism and disjunctive syllogism.
The formal fallacies are their invalid look-alikes, each refuted by one row of a truth table, and vacuous truth explains why a conditional with a false hypothesis counts as true.

The last part adds predicates and the quantifiers "for all", "there exists" and "there exists exactly one".
It shows how to negate quantified statements, why the order of quantifiers matters, and how to translate English into logical form.
Knights and knaves puzzles close the topic and use every tool at once.

Two threads run through the pages.
One is [[intuitionistic logic|38EQ20GR7M]], which drops excluded middle: the pages show which laws survive, such as $p \to \neg\neg p$, and which fail, such as $\neg\neg p \to p$.
The other is Lean 4 and Mathlib, where each connective is a type, such as `And`, `Or`, `Not` and `Exists`, and each law has a name, such as `not_or` or `Classical.em`.

## Remarks

### Reading order: statements and connectives

1. [[Proposition|0ZGC7ZESYN]]: you learn which sentences have a truth value, and how compound statements are built from atomic ones.
2. [[Principle of bivalence|5DYNDW9526]]: you learn why each proposition is true or false, and which logics give this up.
3. [[Negation|029JBBF693]]: you learn how "not" swaps truth values, and how to negate a statement correctly.
4. [[Conjunction|025YZN3VJW]]: you learn when "and" is true, and how to prove and use it.
5. [[Disjunction|0F72FK8EKB]]: you learn the inclusive "or", and how proof by cases uses it.
6. [[Exclusive or|PTMR3P9J6C]]: you learn "one but not both", and see it as addition modulo $2$.
7. [[Material implication|0NMG7W7Q11]]: you learn why $p \to q$ is false only when $p$ is true and $q$ is false.
8. [[Biconditional|0S6GMNJ62Y]]: you learn what "if and only if" asserts, and how to prove it in two directions.
9. [[Logical connective|QS0XVAN9BG]]: you see connectives as truth functions, count the $16$ binary ones, and learn the bracket conventions.
10. [[Sheffer stroke|1NNYWRN6B8]]: you see how NAND alone, or NOR alone, expresses every other connective.
11. [[Truth table|05RSK4Q657]]: you learn to compute the truth value of any formula in each of its $2^n$ cases.
12. [[Tautology|05006AJ7DZ]]: you learn to recognize formulas true in every case, and to tell them from contradictions and contingencies.

### Reading order: laws and rules of inference

13. [[Logical equivalence|0JMR2HM2N2]]: you learn when two formulas say the same thing, and why you may replace one by the other.
14. [[Laws of propositional logic|A9CSGZNBV5]]: you get the algebra for simplifying formulas, with the duality principle.
15. [[Law of excluded middle|0RYYK8PG4S]]: you see why $p \lor \neg p$ holds classically, and why intuitionistic logic rejects it.
16. [[Law of noncontradiction|MP4R7T546Z]]: you see why $\neg (p \land \neg p)$ holds in both logics.
17. [[Double negation law|0NFAGWH84K]]: you learn which direction of $\neg \neg p \leftrightarrow p$ needs excluded middle.
18. [[De Morgan's laws (logic)|09PKJKA6J0]]: you learn to negate "and" and "or", and which direction fails intuitionistically.
19. [[Converse and inverse of an implication|09A3N7ZN5G]]: you learn which rearrangements of $p \to q$ do not follow from it.
20. [[Contrapositive|04T1CT7212]]: you learn the one rearrangement that is equivalent to $p \to q$.
21. [[Necessary and sufficient conditions|09BJQQB3VS]]: you learn the two readings of one arrow, and what a characterization is.
22. [[Modus ponens|0Y0MQYST0M]]: you learn the basic step of every proof, and why it cannot be replaced by a premise.
23. [[Modus tollens|32AQPJQQAM]]: you learn how a false consequence refutes a statement.
24. [[Hypothetical syllogism|7MT8CPCEM4]]: you learn to join implications into a chain.
25. [[Disjunctive syllogism|6EFJF9NAYX]]: you learn to eliminate one alternative of an "or".
26. [[Formal fallacies|T5BG7Y4J0T]]: you learn to spot invalid argument forms and refute each with one countermodel.
27. [[Vacuous truth|0V4QXPGJQK]]: you learn why a conditional with a false hypothesis is true, and why every statement about the empty set holds.

### Reading order: predicates and quantifiers

28. [[Predicate|0QHEWQD30B]]: you learn what an open sentence is, and why it needs a domain.
29. [[Universal quantifier|0GHS47PDAQ]]: you learn when "for all" is true, and how to prove and refute it.
30. [[Existential quantifier|0MSRQHCNN9]]: you learn when "there exists" is true, and what a witness is.
31. [[Uniqueness quantifier|0QAJHFGZZJ]]: you learn to write "exactly one" with $\exists$, $\forall$ and equality.
32. [[Negation of a universal statement|0P3A06QNDP]]: you learn that refuting "for all" means finding a counterexample, and why this needs classical logic.
33. [[Negation of an existential statement|05SZQKH75K]]: you learn that "there is none" means "every one fails", in both logics.
34. [[Order of quantifiers|0FYQMKFE77]]: you learn why $\forall x \exists y$ and $\exists y \forall x$ differ, as in continuity and uniform continuity.
35. [[Translating statements into logical form|WGZX7GV3PP]]: you learn a procedure for turning English and mathematical text into formulas.
36. [[Island of knights and knaves|MVADXMFV59]] and [[knights and knaves puzzles|K17GT0KGZF]]: you practice everything at once on puzzles solved by truth tables and by cases.

### Prerequisites

No earlier topic of logic is required, and the first pages need only school mathematics.
The examples use school algebra, the integers with even, odd and prime numbers, and a few facts about [[sets|0BSJ7RQ9BW]].
A few examples use limits or continuity, and they say so.
The topic [[the language of mathematical statements|WMY13MXY3W]] is a companion that shows how the same ideas appear in mathematical English.
The proof methods that rest on these rules are in [[basic proof methods|958EF46EYJ]].
The next step is [[the propositional calculus|JDK63589SA]], which treats these connectives as a formal system with proofs and completeness.
