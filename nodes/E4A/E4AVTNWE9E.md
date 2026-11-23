---
tag: E4AVTNWE9E
kind: topic
name: Decidability of logics and theories
msc: ["03B25", "03D35"]
topics: [DYJ0KGTPMR]
---

## Summary

Is the sentence $\forall x \, \exists y \, (x = y + y \vee x = y + y + 1)$ true in the natural numbers with addition?
Here the answer is yes, since every number is even or odd, and Presburger showed in 1929 that one algorithm answers every such question about addition.
Decidability asks, for a logic or a theory of [[mathematical logic|DYJ0KGTPMR]], whether one algorithm answers all questions of this kind.

For first-order logic itself the answer is no.
Hilbert and Ackermann asked in 1928 for an algorithm that decides validity, and Church and Turing proved in 1936 that none exists.
Validity is still semi-decidable: a program that lists all proofs confirms every valid sentence, but on some invalid sentences it runs forever.
On finite structures the situation is worse, since by Trakhtenbrot's theorem finite validity is not even semi-decidable.

The positive results come in two families.
Fragments of first-order logic, such as the monadic fragment, some prefix classes, two-variable logic and the guarded fragment, are decidable because a satisfiable sentence has a small model.
Theories of particular structures, such as dense linear orders, Presburger arithmetic and the monadic second-order theories of words and trees, are decidable by quantifier elimination or by automata.

The negative results all come from reductions.
A theory that can describe the run of a Turing machine, or a grid of tiles, inherits the undecidability of the halting problem.
Robinson arithmetic is the key example, because every consistent theory that contains it is undecidable.

## Remarks

### Reading order

1. [[Entscheidungsproblem|DJNYM72Z4G]]: see the question that started the subject.
2. [[Decidable theory|HWC687ES0Q]]: learn why complete axiomatizable theories are decidable.
3. [[Church's theorem|VA6BNNY2YC]]: see why validity in first-order logic is semi-decidable but not decidable.
4. [[Trakhtenbrot's theorem|XP6FW2WDWT]]: see why validity in finite structures is not even semi-decidable.
5. [[Monadic predicate calculus|SERN6CRVWW]]: decide sentences about unary predicates by counting elements of each type.
6. [[Decidable prefix classes|ZF79MZRQ8V]]: learn which quantifier prefixes, such as $\exists^* \forall^*$, give decidable classes of sentences.
7. [[Two-variable logic|S7C3C7DJRF]]: see why two variables force small models.
8. [[Guarded fragment|Y7YS1C3GAE]]: relativize quantifiers to atoms and get a decidable logic that contains modal logic.
9. [[Presburger arithmetic|4W0E9G7PPV]]: decide the theory of addition on the natural numbers by quantifier elimination.
10. [[Skolem arithmetic|X86G2FXTPC]]: decide the theory of multiplication on the natural numbers through prime factorizations.
11. [[Büchi arithmetic|NSTECGT93D]]: read numbers as words for finite automata.
12. [[Büchi-Elgot-Trakhtenbrot theorem|AK66XQ59Z3]]: see that monadic second-order logic on finite words defines exactly the regular languages.
13. [[Büchi's theorem on S1S|YPDXVTH5JR]]: decide the monadic second-order theory of the successor function with automata on infinite words.
14. [[Rabin's tree theorem|PXKKP038RG]]: extend the automata method to the infinite binary tree.
15. [[Courcelle's theorem|DD4JB8XJ5A]]: check monadic second-order properties in linear time on graphs of bounded treewidth.
16. [[Seese's theorem|RT898AFHWT]]: see why a decidable monadic second-order theory of graphs forces bounded treewidth.
17. [[Essential undecidability|9JDDFN8PT7]]: learn why every consistent extension of Robinson arithmetic is undecidable.

### Prerequisites

- [[Structures, satisfaction and truth|NJDME6F845]]: structures, truth of a sentence and the theory of a structure.
- [[Completeness, compactness and interpolation|FBWW4J1XWG]]: Gödel's completeness theorem, which makes the valid sentences computably enumerable.
- [[Computable and computably enumerable sets|24YMRP8DF5]]: the notions of computable and computably enumerable sets of codes.
- [[The halting problem, Rice's theorem and undecidability by reduction|C86MFEQJN8]]: the [[halting problem|Z7TN2B35B0]] and reductions, the source of every undecidability proof here.
- [[Computability theory|ZNC3817RA6]]: the area that gives the precise notion of algorithm.
