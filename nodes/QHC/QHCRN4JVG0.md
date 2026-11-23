---
tag: QHCRN4JVG0
kind: topic
name: Formal arithmetic and its fragments
msc: ["03F30"]
topics: [DYJ0KGTPMR]
---

## Summary

Formal arithmetic studies the natural numbers through first-order theories, and asks what each theory can and cannot prove.
It starts with a small alphabet, $0$, $S$, $+$, $\cdot$ and $<$, in which "six is even" and Goldbach's conjecture become sentences.
The first theory, Robinson's $\mathsf{Q}$, has seven axioms and no induction.
It proves $2 + 2 = 4$ and every other true $\Sigma_1$ sentence, but not $\forall x\,(0 + x = x)$, and a model with two extra elements shows why.
Peano arithmetic adds the induction schema, and the fragments $\mathsf{I}\Delta_0$, $\mathsf{I}\Sigma_1$, $\mathsf{I}\Sigma_2, \ldots$ add it in measured amounts.
Primitive recursive arithmetic and elementary function arithmetic are natural stops between $\mathsf{Q}$ and $\mathsf{PA}$.
Coding ties all of this to computation: Cantor's pairing and Gödel's β function store finite lists in numbers, so that $\mathsf{Q}$ can represent every recursive function.
That coding is what the [[incompleteness theorems|HXHHWY3328]] need, and the sub-area ends with true arithmetic, the complete theory of $\mathbb{N}$ that no recursive set of axioms reaches.
These theories belong to [[mathematical logic|DYJ0KGTPMR]], and they are the base for the later work on incompleteness and independence.

## Remarks

### Reading order

1. [[Language of arithmetic|D8SD54M5PN]]: how to write facts about numbers with five symbols, and what numerals and bounded quantifiers are.
2. [[Robinson arithmetic|3K1AKGXF8A]]: a proof of $2 + 2 = 4$ from the axioms, and a model that shows why $0 + x = x$ is out of reach.
3. [[Weak theories of arithmetic|Q5MT8WY7JM]]: how little arithmetic is enough for undecidability, from $\mathsf{R}$ to the theory of concatenation.
4. [[Peano arithmetic|HACXBCM7SS]]: what the induction schema adds to $\mathsf{Q}$, and why first-order induction still has non-standard models.
5. [[Δ0, Σn and Πn formulas|GE43CSZTS9]]: how to measure a formula by its unbounded quantifiers, the scale used on every later page.
6. [[Σ1-completeness of Robinson arithmetic|69234Z1V00]]: why $\mathsf{Q}$ proves every true sentence of the form "this search succeeds".
7. [[Representability of recursive functions|BJF29XET83]]: how $\mathsf{Q}$ follows every computation, the bridge to incompleteness.
8. [[Gödel's β-function lemma|BM6P0C2AC2]]: how two numbers store a finite list, with Cantor's pairing as the first step.
9. [[Primitive recursive arithmetic|WCXH72T8D8]]: arithmetic without quantifiers, built from definitions such as the recursion for factorial.
10. [[Elementary function arithmetic|2JD80TE553]]: bounded induction plus the totality of exponentiation, and the functions it can prove total.
11. [[Fragments of Peano arithmetic|T70PYM1F36]]: the hierarchy $\mathsf{I}\Sigma_n$, and how much induction a proof really needs.
12. [[Peano arithmetic is not finitely axiomatizable|M5WNB181T7]]: why no finite list of axioms has the theorems of $\mathsf{PA}$.
13. [[True arithmetic|DX0KPMH4QZ]]: the set of all sentences true in $\mathbb{N}$, and why no recursive set of axioms captures it.

### Prerequisites

1. [[First-order languages and syntax|PSRDJXRW53]]: formulas, sentences, substitution and prenex form.
2. [[Structures, satisfaction and truth|NJDME6F845]]: truth of a sentence in a structure, and models of a theory.
3. [[Completeness, compactness and interpolation|FBWW4J1XWG]]: the completeness and compactness theorems, used for non-standard models.
4. [[Primitive recursive functions and subrecursive hierarchies|3S95HQ8Q17]]: the functions that representability and primitive recursive arithmetic are about.
5. [[The halting problem, Rice's theorem and undecidability by reduction|C86MFEQJN8]]: computably enumerable and undecidable sets.

The [[incompleteness theorems|HXHHWY3328]] build on items 6 to 8 of the reading order.
