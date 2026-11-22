---
tag: SGSVYFDSYK
kind: topic
name: Reasoning and proof
msc: ["00A35"]
---

## Summary

Reasoning and proof is about how mathematicians state results, prove them, write the proofs down and find them in the first place.
Its central object is the [[mathematical proof|0B94TKFQJX]], an argument that shows a statement follows from axioms, definitions and earlier results, so that it holds in every case and not only in the cases someone checked.
The area starts with what a proof is and what a theorem says, moves through the language, definitions and notation in which proofs are written, and then teaches the standard methods: direct proof, contradiction, cases, induction, and counting and extremal arguments.
It ends with the craft and the culture of proof: how to write a proof, what goes wrong, how results are discovered, how much rigor a proof needs, and how proof is taught.
Logic appears here as a working tool, while formal logic, set theory and constructive mathematics have topics of their own.

## Remarks

### What the area is about

Start with a claim that looks safe: $n^2 + n + 41$ is prime for every natural number $n$.
It is prime for $n = 0, 1, \dots, 39$, and it fails at $n = 40$, where the value is $41^2$.
Compare the claim that the sum of two even integers is even.
Writing the integers as $2a$ and $2b$ gives the sum $2(a + b)$, and that one line covers every pair at once.
The difference between those two situations, evidence against proof, is what the area is about.

The area asks four kinds of question.
The first is about language: what does a statement say, and how do "if", "or", "for all" and "there exists" work in mathematical English?
The second is about method: which patterns of argument exist, and which one fits a given statement?
The third is about writing: how do you present a proof so that a reader can check every step?
The fourth is about discovery: how do you find a conjecture and a proof before you can write either?

### History

Greek mathematicians made proof the standard of mathematical knowledge.
Aristotle described deductive reasoning in the fourth century BC, and [[Euclid's Elements|83WHDAV68J]], written around 300 BC, derived the geometry of its time from definitions, postulates and common notions.

In the nineteenth century the standards became stricter.
The discovery of [[non-Euclidean geometry|SPCYMFN5V2]] showed that the [[parallel postulate|2PC3XY0PYZ]] does not follow from Euclid's other axioms.
Augustin-Louis Cauchy and Karl Weierstrass gave analysis precise definitions of limit and continuity.
Gottlob Frege published a formal language for logic in 1879, Giuseppe Peano published his [[axioms for arithmetic|0QFT7Z76N5]] in 1889, and David Hilbert gave a complete system of [[axioms for geometry|KM1FB8XZ2R]] in 1899.

In the twentieth century proof itself became an object of study.
Kurt Gödel proved his [[incompleteness theorems|X9WYNYE29C]] in 1931, which set limits on what a formal system can prove.
George Pólya wrote on discovery in "How to Solve It" (1945) and "Mathematics and Plausible Reasoning" (1954).
Imre Lakatos described how a theorem grows through proofs and counterexamples in "Proofs and Refutations", published as a book in 1976.
In the same year Kenneth Appel and Wolfgang Haken proved the [[four color theorem|0M406JC8J1]] with the help of a computer.
Thomas Hales announced a proof of the [[Kepler conjecture|AFMBQT06ZV]] in 1998, and a formal proof of it was completed in 2014.
Today [[proof assistants|YM6PRDE88V]] check long proofs step by step.

### How to read the area

If you are meeting proofs for the first time, read the first four sub-areas in order.
[[Proof, theorems and mathematical method|N4P3E53HM0]] explains what a proof is and what kinds of results it establishes.
[[The language of mathematical statements|WMY13MXY3W]] shows how to read a statement, and [[definitions in mathematics|BP0WAF23HB]] shows what a definition does.
[[Notation, conventions and jargon|Z2WNQ1DNTX]] collects the symbols and the special words of mathematical writing.

The next four sub-areas form the core of a transition course.
[[Basic proof methods|958EF46EYJ]] gives the standard patterns, and [[induction and well-ordering as proof methods|EEH2F76CYQ]] gives the methods for statements about all natural numbers.
[[Counting, invariant and extremal arguments|GB14W4SYPK]] gives combinatorial methods that work in many fields.
[[Proof patterns for common goals|MEKKHHQTKB]] shows which method fits which goal, such as an equality of sets or the injectivity of a function.

Two sub-areas then teach the craft.
[[Writing and reading proofs|STSM6PR7TX]] explains how to present a proof, and [[fallacies and errors in proofs|T6QQ749DM5]] shows what goes wrong, with arguments that look right and are not.

The remaining sub-areas can be read in any order.
[[Heuristics of discovery|X1NSTVGDNQ]] and [[plausible reasoning and experimental mathematics|DME0TPC348]] explain how results and proofs are found.
[[Rigor and the acceptance of proofs|1BTHSHST4M]] asks when a proof is complete, and how computer proofs and very long proofs are checked.
[[Teaching reasoning and proof|VHGA6J4NZK]] is for readers who teach these topics.

### Related areas

[[Mathematical logic|DYJ0KGTPMR]] studies proof as a formal object, with formal languages, rules of inference, soundness and completeness.
[[Set theory|G9W9J6KPAR]] gives the common language of sets, relations and functions, and [[type theory and constructive mathematics|K6P3NSQEZ3]] gives another foundation.
[[Mathematical software and formalization|F3F5GGYHMM]] holds the proof assistants and [[automated theorem proving|A51M1KK9DJ]].
[[Philosophy of mathematics|NTJ5XW0PVD]] asks what a proof is and why it gives knowledge, and [[history of mathematics|EJZNJJ6M7S]] tells how proof developed.
[[Problem solving and competitions|2HNEG88WT8]] trains the methods of the area on hard problems, and [[recreational mathematics|N7E1QW0W50]] holds the puzzles that illustrate them.
[[Mathematics education|9622VKAWMZ]] studies how students learn mathematics in general, and [[mathematics and culture|FWE06TZ36P]] holds mathematical beauty.
Many examples come from [[elementary number theory|7XZ94HTPQT]] and [[Euclidean geometry|D1SR8GDYJX]], which hold the theorems themselves.

### Sub-areas

1. [[Proof, theorems and mathematical method|N4P3E53HM0]]: what a proof is, and what theorems, axioms and conjectures are.
2. [[The language of mathematical statements|WMY13MXY3W]]: connectives, quantifiers and negation as they are used in mathematical English.
3. [[Definitions in mathematics|BP0WAF23HB]]: the logical form of a definition, well-definedness and equivalent definitions.
4. [[Notation, conventions and jargon|Z2WNQ1DNTX]]: symbols, conventions and the informal vocabulary of mathematicians.
5. [[Basic proof methods|958EF46EYJ]]: direct proof, contrapositive, contradiction, cases, construction and counterexample.
6. [[Induction and well-ordering as proof methods|EEH2F76CYQ]]: ordinary and strong induction, minimal counterexamples and descent.
7. [[Counting, invariant and extremal arguments|GB14W4SYPK]]: pigeonhole, double counting, invariants and the extremal principle.
8. [[Proof patterns for common goals|MEKKHHQTKB]]: which method fits which kind of goal.
9. [[Writing and reading proofs|STSM6PR7TX]]: how to present a proof and how to read one.
10. [[Fallacies and errors in proofs|T6QQ749DM5]]: arguments that look right and are not.
11. [[Heuristics of discovery|X1NSTVGDNQ]]: how proofs and results are found.
12. [[Plausible reasoning and experimental mathematics|DME0TPC348]]: evidence, computation and conjecture.
13. [[Rigor and the acceptance of proofs|1BTHSHST4M]]: formal and informal proof, computer proofs and long proofs.
14. [[Teaching reasoning and proof|VHGA6J4NZK]]: how proof is taught and learned.
