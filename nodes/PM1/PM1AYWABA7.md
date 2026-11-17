---
tag: PM1AYWABA7
kind: topic
name: Propositions, connectives and quantifiers
msc: ["03B05", "03B10"]
topics: [DYJ0KGTPMR]
---

## Summary

This topic is a part of [[mathematical logic|DYJ0KGTPMR]].
It covers the logic that every mathematics course uses: statements, connectives and their truth tables, the laws of logic, the basic rules of inference and the use of quantifiers.
The pages give the precise logical definitions: truth tables, the laws of logic, the rules of inference, and the formal behaviour of the quantifiers.
The reading of these words in mathematical English is in the topic [[the language of mathematical statements|WMY13MXY3W]], and the proof methods that rest on them are in the topic [[basic proof methods|958EF46EYJ]].

## Remarks

### Reading order

1. [[Proposition|0ZGC7ZESYN]]: a declarative sentence with a truth value, atomic or compound.
2. [[Principle of bivalence|5DYNDW9526]]: each proposition is true or false, and the logics that drop this.
3. [[Negation|029JBBF693]]: "not", its truth table and its rules.
4. [[Conjunction|025YZN3VJW]]: "and", true when both parts are true.
5. [[Disjunction|0F72FK8EKB]]: the inclusive "or", and proof by cases as its use.
6. [[Exclusive or|PTMR3P9J6C]]: "one or the other but not both", as addition modulo $2$.
7. [[Material implication|0NMG7W7Q11]]: the conditional $p \to q$, false only when $p$ is true and $q$ is false.
8. [[Biconditional|0S6GMNJ62Y]]: "if and only if", true when both parts have the same truth value.
9. [[Logical connective|QS0XVAN9BG]]: connectives as truth functions, the $16$ binary connectives, and the conventions for brackets.
10. [[Sheffer stroke|1NNYWRN6B8]]: NAND and NOR, each enough to express all the other connectives.
11. [[Truth table|05RSK4Q657]]: the method that computes the truth value of a formula in each of the $2^n$ cases.
12. [[Tautology|05006AJ7DZ]]: formulas true in every case, with contradictions and contingencies.
13. [[Logical equivalence|0JMR2HM2N2]]: formulas with the same truth value in every case, and the replacement of equivalents.
14. [[Laws of propositional logic|A9CSGZNBV5]]: the commutative, associative, distributive and other laws, and the duality principle.
15. [[Law of excluded middle|0RYYK8PG4S]]: $p \lor \neg p$, and its failure in intuitionistic logic.
16. [[Law of noncontradiction|MP4R7T546Z]]: $\neg (p \land \neg p)$, valid classically and intuitionistically.
17. [[Double negation law|0NFAGWH84K]]: $\neg \neg p \leftrightarrow p$, and the direction that needs excluded middle.
18. [[De Morgan's laws (logic)|09PKJKA6J0]]: the negation of a conjunction and of a disjunction.
19. [[Converse and inverse of an implication|09A3N7ZN5G]]: $q \to p$ and $\neg p \to \neg q$, which do not follow from $p \to q$.
20. [[Contrapositive|04T1CT7212]]: $\neg q \to \neg p$ is equivalent to $p \to q$.
21. [[Necessary and sufficient conditions|09BJQQB3VS]]: the two readings of $p \to q$, and characterization theorems.
22. [[Modus ponens|0Y0MQYST0M]]: from $p$ and $p \to q$, infer $q$.
23. [[Modus tollens|32AQPJQQAM]]: from $p \to q$ and $\neg q$, infer $\neg p$.
24. [[Hypothetical syllogism|7MT8CPCEM4]]: from $p \to q$ and $q \to r$, infer $p \to r$.
25. [[Disjunctive syllogism|6EFJF9NAYX]]: from $p \lor q$ and $\neg p$, infer $q$.
26. [[Formal fallacies|T5BG7Y4J0T]]: invalid argument forms, each refuted by a countermodel.
27. [[Vacuous truth|0V4QXPGJQK]]: conditionals with a false hypothesis, and universal statements over the empty set.
28. [[Predicate|0QHEWQD30B]]: an open sentence with free variables over a domain of discourse.
29. [[Universal quantifier|0GHS47PDAQ]]: "for all", its truth condition and its restricted form.
30. [[Existential quantifier|0MSRQHCNN9]]: "there exists", witnesses and the restricted form.
31. [[Uniqueness quantifier|0QAJHFGZZJ]]: "there exists exactly one", defined from $\exists$, $\forall$ and equality.
32. [[Negation of a universal statement|0P3A06QNDP]]: $\neg \forall x\, P(x)$ is equivalent to $\exists x\, \neg P(x)$.
33. [[Negation of an existential statement|05SZQKH75K]]: $\neg \exists x\, P(x)$ is equivalent to $\forall x\, \neg P(x)$.
34. [[Order of quantifiers|0FYQMKFE77]]: $\forall x \exists y$ against $\exists y \forall x$, and the dependence of witnesses.
35. [[Translating statements into logical form|WGZX7GV3PP]]: a procedure that turns English and mathematical text into formulas.
36. [[Knights and knaves puzzles|K17GT0KGZF]]: logic puzzles solved by truth tables and by cases.

### Prerequisites

1. No earlier topic of logic is required, and the first pages need only school mathematics.
2. The examples use school algebra, the integers with even, odd and prime numbers, and a few facts about [[sets|0BSJ7RQ9BW]]. A few examples use limits or continuity, and they say so.
3. The topic [[the language of mathematical statements|WMY13MXY3W]] is a gentle companion: it shows how the same ideas appear in mathematical English.
4. The next topic of the area is [[the propositional calculus|JDK63589SA]], which treats these connectives as a formal system.
