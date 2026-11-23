---
tag: FBWW4J1XWG
kind: topic
name: Completeness, compactness and interpolation
msc: ["03B10", "03C40"]
topics: [DYJ0KGTPMR]
---

## Summary

Add a new constant $c$ to the axioms of arithmetic, together with the sentences $c > 0$, $c > 1$, $c > 2$, and so on.
Every finite part of this list is true in the natural numbers, with $c$ a large enough number.
So the whole list has a model, and in that model $c$ is a number larger than every standard number.
The axioms of arithmetic cannot rule out such infinite numbers.

This one argument uses the three main results of the topic, which is a part of [[mathematical logic|DYJ0KGTPMR]].
[[Soundness|AVD7T7J063]] says that every derivable sentence is true in every model.
[[Gödel's completeness theorem|WQ1ZE255SF]] gives the converse: every sentence true in all models of a set of axioms is derivable from them.
Its modern proof, the [[Henkin construction|RY8KRKR097]], builds a model out of the names in the language.
The [[compactness theorem|1NR3HAWG9D]] follows, because a derivation uses finitely many axioms, and it gives the infinite numbers above.

Compactness also shows what first-order logic cannot say.
Finiteness, connectedness of a graph and well-order are not expressible by any set of first-order sentences.
The topic ends with results that relate two languages.
[[Herbrand's theorem|VZ21F10WRS]] reduces first-order validity to propositional tautologies.
The [[Craig interpolation theorem|E2CBFNAVZY]] finds, for a valid implication, a sentence in the shared symbols that sits between its two sides.
Interpolation proves the [[Beth definability theorem|RJBDSA2ETP]]: a symbol that a theory fixes implicitly has an explicit definition.

## Remarks

### Reading order

1. [[Soundness theorem for first-order logic|AVD7T7J063]]: you learn why a model is a certificate that a sentence is not derivable.
2. [[Lindenbaum's lemma|SC0BSJ3GT6]]: you learn to extend a consistent set until it decides every sentence.
3. [[Henkin construction|RY8KRKR097]]: you learn to build a model from closed terms, with witness constants for existential sentences.
4. [[Model existence theorem|G0DTR159RN]]: you get a model of every consistent set, with a bound on its size.
5. [[Gödel's completeness theorem|WQ1ZE255SF]]: you learn that truth in all models and derivability are the same.
6. [[Compactness theorem|1NR3HAWG9D]]: you get a model for a set of sentences as soon as each finite part has one.
7. [[Applications of first-order compactness|PES0S9XQZ5]]: you learn to build nonstandard models and to show that a property is not first-order.
8. [[Recursively axiomatizable theory|3ANXZC3BEG]]: you learn which theories have theorems that a machine can list.
9. [[Craig's theorem on axiomatizability|6AN62NQ8AN]]: you learn to replace a listable set of axioms by a decidable one.
10. [[Herbrand's theorem|VZ21F10WRS]]: you learn to test first-order validity by finitely many propositional instances.
11. [[Craig interpolation theorem|E2CBFNAVZY]]: you learn to explain a valid implication in the symbols that its two sides share.
12. [[Lyndon interpolation theorem|BRDT1BT7WW]]: you get an interpolant that also keeps the signs of the relation symbols.
13. [[Robinson's joint consistency theorem|R6AN38DNBD]]: you learn when two theories in different languages have a common model.
14. [[Completeness versus incompleteness|28AX3A4N86]]: you learn the two meanings of "complete", and how the theorems of 1929 and 1931 fit together.

### Prerequisites

- First-order languages, terms, formulas and sentences, from the topic [[first-order languages and syntax|PSRDJXRW53]].
- Structures, satisfaction, models and logical consequence, from the topic [[structures, satisfaction and truth|NJDME6F845]].
- The Hilbert system and the other proof systems, from the topic [[proof systems for first-order logic|TTCRX3NFNY]].
- The propositional versions of soundness, completeness, compactness and interpolation, from the topic [[the propositional calculus|JDK63589SA]].
- Consistency and soundness as general notions, from the topic [[logic, formal systems and foundations|H8QZY0RZXZ]].
- For uncountable languages: [[Zorn's lemma|04RXTQA5ZA]] and cardinal arithmetic.

### Watch out

Three facts here have similar names and different content.
Completeness of first-order logic is a property of the logic: every valid consequence is derivable.
A complete theory is a theory that decides every sentence of its language.
Gödel's incompleteness theorems say that some theories, such as Peano arithmetic, are not complete theories, although the logic they use is complete.
