---
tag: H8QZY0RZXZ
kind: topic
name: Logic, formal systems and foundations
msc: ["03B22", "03A05"]
topics: [DYJ0KGTPMR]
---

## Summary

Start with the string MI and four rules: add U after a final I, double the part after M, replace III by U, and delete UU.
Can you reach MU?
You cannot, because the number of letters I is never a multiple of 3.
That argument is a fact about all derivations at once, and not a derivation itself.
This part of [[mathematical logic|DYJ0KGTPMR]] is about that step back: treating proofs as mathematical objects and proving theorems about them.
It begins with the oldest formal logic, Aristotle's syllogisms, and the square of opposition for sentences such as "all swans are white".
Then it defines a formal system in general, separates the object language from the metalanguage, and studies rules of inference and consequence relations.
With these tools it states what it means for a theory to be consistent, for a proof system to be sound, and for a larger theory to add nothing new in the old language.
It ends with the foundational programs, above all Hilbert's, which asked for a finitary consistency proof of mathematics, and with the theorems of Gödel that limit what such a proof can do.

## Remarks

### Reading order

1. [[Mathematical logic|DYJ0KGTPMR]]: get a map of the four branches and of the main theorems, so you know where each later idea returns.
2. [[Foundations of mathematics|EFFRJFW67Y]]: see how numbers, pairs and functions are coded as sets, and what any foundation must supply.
3. [[History of mathematical logic|WP3602P9EH]]: follow the problems that shaped the field, from Aristotle and the Stoics to Gödel, Church and Turing.
4. [[Aristotelian syllogistic|MZBNX2T6Q6]]: test arguments such as Barbara and Darapti and learn why validity depends on form alone.
5. [[Square of opposition|VYNBSVZ2TH]]: work out how "all swans are white" relates to its three companions, and what existential import changes.
6. [[Syllogistic figures|S4BTTGFR6J]]: learn the four positions of the middle term that sort all syllogisms.
7. [[Syllogistic moods|1TD6HRM5NG]]: count the 256 forms and check which 24 are valid, 9 of them only with existential import.

### Reading order, continued: formal systems and consequence

8. [[Formal system|439M8B4DY2]]: play with the MIU system and meet the exact definition of axioms, rules, derivations and theorems.
9. [[Object language and metalanguage|D9G8M42GKC]]: separate statements in a formal language from statements about it, and use quotation correctly.
10. [[Rule of inference|QPD3X471Q1]]: learn schematic rules, and the difference between derivable and admissible rules.
11. [[Consequence relation|J78Y1M4GND]]: see the three properties, reflexivity, monotonicity and cut, that every reasonable notion of consequence shares.
12. [[Abstract logical systems|RQXV7PM2WT]]: view a logic as a consequence relation with a semantics, and compare logics in one frame.

### Reading order, continued: consistency and foundations

13. [[Consistency|VM8TQ70CVJ]]: learn when a theory is free of contradictions, how this matches having a model, and why it is hard to prove.
14. [[Post consistency and Post completeness|WK2P0E82B4]]: see that classical propositional logic cannot be strengthened without collapse.
15. [[Soundness|4A84VHDTHV]]: prove by induction on derivations that every provable formula is valid, the first half of completeness.
16. [[Conservative extension|N238J43XNE]]: test when new symbols or axioms prove nothing new in the old language.
17. [[Extension by definitions|GCK0NN60E4]]: see why defined symbols such as $\le$ in arithmetic are harmless abbreviations.
18. [[Relative consistency proof|X3G0RG2GPZ]]: reduce the consistency of one theory to another, as Beltrami did for hyperbolic geometry and Gödel for the axiom of choice.
19. [[Hilbert's program|P1RW6JWX73]]: understand the plan for a finitary consistency proof and how the second incompleteness theorem blocks it.
20. [[Existential graphs|D3ZS6WHPM1]]: try Peirce's diagrams, a complete proof system drawn on a sheet of paper.
21. [[Logical constants and logicality|2QQ7Q5SKP8]]: ask which symbols count as logical, by permutation invariance or by the harmony of their rules.

### Prerequisites

You need truth tables for the [[propositional connectives|PM1AYWABA7]] and simple facts about sets and functions.
No other part of [[mathematical logic|DYJ0KGTPMR]] is needed.
[[Reasoning and proof|SGSVYFDSYK]] helps, in particular [[the language of mathematical statements|WMY13MXY3W]] and [[proof, theorems and mathematical method|N4P3E53HM0]].

### Where the ideas return

Soundness is half of the completeness theorem, and consistency and conservativity are the language of the incompleteness theorems.
Derivations as objects and induction on derivations are the starting point of proof theory, and Hilbert's program leads to ordinal analysis and conservation results.
The use of logic in everyday proofs belongs to [[reasoning and proof|SGSVYFDSYK]].
