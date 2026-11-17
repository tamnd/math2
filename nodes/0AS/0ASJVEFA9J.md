---
tag: 0ASJVEFA9J
kind: concept
name: Mathematical induction
aliases: [principle-of-mathematical-induction, proof-by-induction]
msc: ["00A35", "03F30"]
topics: [G9JFJGY4TQ, EEH2F76CYQ]
audience: school
specializes: [0B94TKFQJX]
uses: [0MWKJ44V5A, 0B94TKFQJX]
sources:
  - url: https://en.wikipedia.org/wiki/Mathematical_induction
    locator: Description
  - url: https://en.wikipedia.org/wiki/Mathematical_induction
    locator: History
  - url: https://en.wikipedia.org/wiki/Mathematical_induction
    locator: Variants
  - book: isbn:9781108439534
    locator: Chapter 6
same_as:
  wikidata: Q178377
  wikipedia: Mathematical induction
---

## Summary

Mathematical induction is a method to prove that a property $P(n)$ holds for every [[natural number|0MWKJ44V5A]] $n \ge n_0$, where $n_0$ is a fixed natural number.
A proof by induction has two parts.
The base case proves $P(n_0)$.
The induction step proves, for an arbitrary natural number $n \ge n_0$, that $P(n)$ implies $P(n + 1)$.
In the induction step, the assumption $P(n)$ is called the induction hypothesis.
When both parts are proved, $P(n)$ holds for every $n \ge n_0$.
Induction matters because it proves infinitely many statements with one finite argument, and most facts about sums, recursive definitions and finite structures are proved with it.

## Motivation

Many statements speak about all natural numbers at once: $1 + 3 + \dots + (2n - 1) = n^2$, or "$3$ divides $n^3 - n$".
We can check such a statement for $n = 1, 2, \dots, 1000$, but checks of cases never cover all $n$.
A [[direct proof|0NTF6DMVAP]] for an arbitrary $n$ is sometimes hard to find.
Often the case $n + 1$ is easy to reach from the case $n$: the sum of the first $n + 1$ odd numbers is the sum of the first $n$ odd numbers plus one more term.
Induction turns this link between neighbouring cases into a proof for all cases.
The natural numbers are exactly the numbers that we reach from $0$ by adding $1$ again and again, and induction expresses this fact as a rule of proof.

## Notation

1. The property is written $P(n)$, $S(n)$ or $S_n$, and the variable $n$ is the induction variable.
2. Books start at $n_0 = 0$ or at $n_0 = 1$, because they differ on whether $0$ is a natural number. A proof must state its base case.
3. Some books write the step as "$P(k) \Rightarrow P(k + 1)$" with a new letter $k$, and others as "$P(n - 1) \Rightarrow P(n)$ for $n \ge n_0 + 1$". These forms say the same thing.
4. The abbreviations IH (induction hypothesis) and IS (induction step) are common in lecture notes.
5. "Ordinary", "weak" and "simple" induction all name the method of this page. [[Strong induction|0KMVFSHFGZ]] is a different form.

## Remarks

### The steps of a proof by induction

1. State the property $P(n)$ and the range $n \ge n_0$.
2. Base case: prove $P(n_0)$.
3. Induction step: let $n \ge n_0$ be arbitrary, assume $P(n)$, and prove $P(n + 1)$.
4. Conclude: by induction, $P(n)$ holds for all $n \ge n_0$.

The step must work for every $n \ge n_0$, with one argument for an arbitrary $n$.
The proof of $P(n + 1)$ must use the induction hypothesis $P(n)$ at some point, otherwise the proof is a direct proof in disguise.

### Why the method is valid

For $n_0 = 0$, the method is the induction axiom of the [[Peano axioms|0QFT7Z76N5]]: a set of natural numbers that contains $0$ and contains $n + 1$ whenever it contains $n$ is the whole set $\mathbb{N}$.
We apply the axiom to the set $\{n \in \mathbb{N} : P(n)\}$.
The [[induction from an arbitrary base case|0GF6AJEBZ0]] reduces a base $n_0$ to the base $0$ with the property $Q(k) = P(n_0 + k)$.
The method is also equivalent to the [[well-ordering principle|01BX15HSRR]]; the exact statement is [[equivalence of induction and well-ordering|J2P9FWBP3Q]].

### Examples

1. The [[sum of the first $n$ odd numbers|QSWRESJAZ4]] is $n^2$, because the step adds $2n + 1$ to $n^2$ and gets $(n + 1)^2$.
2. The inequality [[$2^n > n^2$ for $n \ge 5$|ST5ZESV7ZR]] needs the base case $n_0 = 5$, because it fails for $n = 2, 3, 4$.
3. The [[divisibility of $n^3 - n$ by $3$|7RZDHDFSPT]]: the step adds $3n^2 + 3n$, a multiple of $3$.
4. The [[tiling of a deficient $2^n \times 2^n$ board by L-trominoes|EXRJ0JF2Q3]]: the step cuts the board of side $2^{n+1}$ into four boards of side $2^n$.
5. [[Bernoulli's inequality|0M1MX28VXK]] $(1 + x)^n \ge 1 + nx$ for $x \ge -1$: the step multiplies both sides by $1 + x \ge 0$.

### Non-examples

1. The [[check of $n^2 + n + 41$ for $n = 0$ to $39$|Q54K0J3PZ4]] is not a proof by induction, because it has no induction step. The claim fails at $n = 40$.
2. The argument that [[all horses are the same color|AJ2FDJJGTH]] is not a valid induction, because its induction step fails for $n = 1$.
3. A proof of $P(n + 1)$ from $P(n)$ alone, with no base case, is not a proof by induction. The [[false claim that $n^2 + n$ is odd|TYDB4F6J2F]] has a correct step and no true base case.

### Variants

1. [[Induction from an arbitrary base case|0GF6AJEBZ0]]: the base case is $n_0$ instead of $0$.
2. [[Induction on the integers|0HBS1F00DN]]: a base case at $0$ and two steps, $n \mapsto n + 1$ and $-n \mapsto -n - 1$, cover all of $\mathbb{Z}$.
3. [[Strong induction|0KMVFSHFGZ]]: the step may use all the cases below $n$.
4. [[Double induction|AABX4YPKRR]], [[forward-backward induction|QC9FKGZH1V]] and [[structural induction|12MQ2NJ29A]] change the order or the objects of the induction.
5. [[Infinite descent|0EFYCFHYFG]] and the [[minimal counterexample|JGRCNPKNGG]] method use the same principle in the contrapositive form.

### Basic properties

1. The conclusion of a proof by induction is certain. Induction is deductive reasoning, and it differs from the [[inductive reasoning|5V35SGEN1T]] of the sciences.
2. The base case and the step are both needed. Without the base case, the false property "$n = n + 1$" has a valid step. Without the step, a property can hold at $n_0$ and fail later.
3. To prove $P(n)$ by induction, it is often easier to prove a stronger property, because the induction hypothesis then gives more. This is [[strengthening the induction hypothesis|F94KJC2RXP]].
4. A proof by induction often gives a recursive algorithm, and the algorithm builds the object whose existence the proof shows.

### In Lean

In Lean 4 the tactic `induction n` splits a goal about a natural number `n` into the cases `zero` and `succ`.
The term form is the recursor `Nat.rec`.
Mathlib states induction from a base $m$ as `Nat.le_induction`.

### History

Francesco Maurolico used the method in 1575 to prove that the sum of the first $n$ odd numbers is $n^2$.
Blaise Pascal gave an explicit form of the method in his *Traité du triangle arithmétique* (1665).
Earlier implicit uses go back to al-Karaji, around the year 1000, and to Gersonides.
The modern formal treatment came in the 19th century, with Boole, De Morgan, Peirce, Dedekind and Peano.

### Common errors

1. A student checks the first few cases and stops. A [[check of cases|Q54K0J3PZ4]] is evidence, not a proof.
2. A student assumes $P(n + 1)$ in the induction step and derives a true statement from it. The step must start from $P(n)$ and end at $P(n + 1)$.
3. A student proves the step with an argument that fails for small $n$, as in the [[horse argument|AJ2FDJJGTH]]. The step must work for every $n \ge n_0$. More errors are in [[errors in induction proofs|V52HDTMPV5]].

## Explanations

### L1 human

Think of a line of dominoes that never ends.
If the first domino falls, and each falling domino knocks over the next one, then every domino falls.
The base case is the push on the first domino.
The induction step is the rule that each domino knocks over the next one.
For example, $1 = 1^2$, $1 + 3 = 2^2$ and $1 + 3 + 5 = 3^2$.
Each time we add the next odd number, the square grows by one row and one column, so the pattern continues forever.

### L2 human

We prove that $1 + 2 + \dots + n = \frac{n(n + 1)}{2}$ for every natural number $n \ge 1$.

1. Let $P(n)$ be the statement $1 + 2 + \dots + n = \frac{n(n + 1)}{2}$.
2. Base case: for $n = 1$, the left side is $1$ and the right side is $\frac{1 \cdot 2}{2} = 1$. So $P(1)$ holds.
3. Induction step: let $n \ge 1$ be arbitrary, and assume $P(n)$.
4. Then $1 + 2 + \dots + n + (n + 1) = \frac{n(n + 1)}{2} + (n + 1)$, by the induction hypothesis.
5. The right side is $\frac{n(n + 1) + 2(n + 1)}{2} = \frac{(n + 1)(n + 2)}{2}$, which is the right side of $P(n + 1)$.
6. So $P(n)$ implies $P(n + 1)$ for every $n \ge 1$.
7. By induction, $P(n)$ holds for every $n \ge 1$.

The typical use of induction is a statement about all $n$ in which the case $n + 1$ contains the case $n$ as a part.
A formula for a sum, a bound for a recursive sequence and a property of a structure with $n$ elements are of this kind.
A trap: induction proves a formula, but it does not find it.
The formula usually comes from experiments with small cases.

### L3 human

Induction says that $\mathbb{N}$ is the smallest set that contains $0$ and is closed under the successor map.
In the language of categories, $(\mathbb{N}, 0, S)$ is the initial algebra of the functor $X \mapsto 1 + X$, and induction is the statement that it has no proper subalgebra.
The same idea gives [[structural induction|12MQ2NJ29A]] over lists, trees and formulas, and well-founded induction over any well-founded relation.
In set theory the method extends to transfinite induction over the ordinals, and in type theory each inductive type has its own induction principle.
In first-order arithmetic, induction is an axiom schema, and the strength of the schema for restricted classes of formulas measures the strength of fragments of Peano arithmetic.
The later pages of this topic treat the [[equivalence with well-ordering|J2P9FWBP3Q]] and the methods that are built on it.
