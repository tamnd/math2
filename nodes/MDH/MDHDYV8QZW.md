---
tag: MDHDYV8QZW
kind: topic
name: Second-order logic and extensions of first-order logic
msc: ["03B16", "03C80", "03C85"]
topics: [DYJ0KGTPMR]
---

## Summary

First-order logic cannot say that a structure is finite, that a graph is connected, or that every set of numbers obeys induction.
Each of these properties speaks about all subsets of the domain, and first-order quantifiers range only over elements.
Add quantifiers over sets and relations, and each property becomes one sentence.
For example, induction for $0$ and the successor $S$ becomes this sentence:
$$\forall X \, \big( (X(0) \land \forall x \, (X(x) \to X(S(x)))) \to \forall x \, X(x) \big).$$
With two simple axioms about $S$, it fixes the natural numbers up to isomorphism, when $X$ ranges over all sets.

This topic is a part of [[mathematical logic|DYJ0KGTPMR]].
It studies [[second-order logic|G6X7SZSNC5]] and the price of its power.
With the full semantics, the completeness and compactness theorems fail.
With the [[Henkin semantics|KWEJFK5943]], they return, but the unintended models return with them.
The topic then turns to logics between the two extremes.
[[Monadic second-order logic|3WHQFSHR58]] quantifies only over sets, and its theories of words and trees are decidable.
[[Branching quantifiers|KMNVEGS34N]], [[independence-friendly logic|DPMKT2KRB8]] and [[dependence logic|DNAPTJ98WD]] control which choices a quantifier may see.
[[Generalized quantifiers|MFV98WTF4G]] such as "most" and "infinitely many" add one new quantifier at a time.

## Remarks

### Reading order

1. [[Second-order logic|G6X7SZSNC5]]: you learn what one sentence about all sets can say, and why no proof system captures the full semantics.
2. [[Henkin semantics|KWEJFK5943]]: you learn to let relation variables range over a chosen family, and you get the first-order theorems back.
3. [[Comprehension schema|5GS6DRJ5SY]]: you learn the axiom that every formula defines a relation, and why Henkin models need it.
4. [[Higher-order logic|K40YJX8K1G]]: you learn variables of every finite type, and why their validity reduces to second order.
5. [[Frege's theorem and Hume's principle|J36EHBHF6J]]: you learn to derive the Peano axioms from one principle about numbers of concepts.
6. [[Monadic second-order logic|3WHQFSHR58]]: you learn to quantify over sets only, and to link the logic with automata on words and trees.
7. [[Branching quantifier|KMNVEGS34N]]: you learn quantifier prefixes that are only partially ordered, as in the Henkin quantifier.
8. [[Independence-friendly logic|DPMKT2KRB8]]: you learn quantifiers that ignore some earlier choices, with a game semantics.
9. [[Dependence logic|DNAPTJ98WD]]: you learn to state dependence as an atom, and to evaluate formulas on teams of assignments.
10. [[Generalized quantifier|MFV98WTF4G]]: you learn to read a quantifier such as "most" as a class of structures.
11. [[Plural quantification|DZVEFDYYZX]]: you learn to read monadic second-order quantifiers as quantifiers over pluralities.

### Prerequisites

- [[First-order logic|086QKPF0A6]], with [[structures|983GZBQYT4]] and [[satisfaction|2RBQPV02AS]], from the topic [[structures, satisfaction and truth|NJDME6F845]].
- The [[completeness theorem|WQ1ZE255SF]], the [[compactness theorem|1NR3HAWG9D]] and the [[Löwenheim-Skolem theorem|484M0TZ1S7]], from the topic [[completeness, compactness and interpolation|FBWW4J1XWG]].
- The [[Peano axioms|0QFT7Z76N5]] and [[Gödel's incompleteness theorems|X9WYNYE29C]], for the failure of completeness.
- [[Power sets|00E0YZCERH]], [[Cantor's theorem|0WTEMGYV2C]] and the [[continuum hypothesis|0MN2MER9WN]] from set theory, for the full semantics.

### Watch out

The phrase "second-order logic" names one syntax with two semantics.
With the full semantics, a relation variable ranges over all relations, and no effective proof system is complete.
With the Henkin semantics, it ranges over a family that the model chooses, and the logic behaves like a many-sorted first-order logic.
So a claim about completeness, compactness or categoricity must name its semantics.
