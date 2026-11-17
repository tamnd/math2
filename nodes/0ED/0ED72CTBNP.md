---
tag: 0ED72CTBNP
kind: concept
name: Counterexample
aliases: [disproof-by-counterexample]
msc: ["00A35", "97E50"]
topics: [G9JFJGY4TQ, 958EF46EYJ]
audience: school
uses: [0B88PQTJ66, 0P3A06QNDP]
sources:
  - url: https://en.wikipedia.org/wiki/Counterexample
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Euler%27s_sum_of_powers_conjecture
    locator: lead section
  - url: https://en.wikipedia.org/wiki/P%C3%B3lya_conjecture
    locator: lead section
same_as:
  wikidata: Q596077
  wikipedia: Counterexample
---

## Summary

A counterexample to a [[universal statement|0B88PQTJ66]] $\forall x \in X \; P(x)$ is an element $a \in X$ for which $P(a)$ is false.
For a statement of the form "for all $x$ in $X$, if $H(x)$, then $C(x)$", a counterexample is an element $a \in X$ with $H(a)$ true and $C(a)$ false.
One counterexample proves that the universal statement is false; this is a disproof by counterexample.
Counterexamples are the standard way to refute a conjecture and to show that a hypothesis of a theorem cannot be dropped.

## Motivation

A universal claim covers infinitely many cases, and a proof must handle all of them.
Its failure needs only one case.
This asymmetry makes counterexamples the first test of any conjecture: before searching for a proof, mathematicians try small cases, extreme cases and special shapes.
A theorem with several hypotheses is understood only when it is known which hypotheses matter, and a counterexample for each dropped hypothesis shows that it does.
Counterexamples also correct definitions, when an object that fits the definition does not fit the intended idea.

## Notation

A disproof usually reads "The statement is false; a counterexample is $x = a$", followed by the check that $a \in X$ and that $P(a)$ fails.
The logical basis is the [[negation of a universal statement|0P3A06QNDP]]: $\neg \forall x \, P(x)$ is equivalent to $\exists x \, \neg P(x)$, so a counterexample is a [[constructive proof|01XM7JEKHY]] of the negation.
In Lean, the tactic `push_neg` turns the goal `¬ ∀ x, P x` into `∃ x, ¬ P x`, and `use a` supplies the counterexample; Mathlib keeps a separate `Counterexamples` folder for longer ones.

## Remarks

### Examples

1. [[A counterexample to Euler's sum of powers conjecture|~16e76c93]]: $27^5 + 84^5 + 110^5 + 133^5 = 144^5$, found by L. J. Lander and T. R. Parkin in 1966.
2. [[The union of two subgroups need not be a subgroup|~116036ad]]: $2\mathbb{Z} \cup 3\mathbb{Z}$ contains $2$ and $3$ but not $5$.
3. The number $2$ is a counterexample to "every prime number is odd".
4. [[The absolute value function|0CQ9ZM383N]] is continuous but not differentiable at $0$, a counterexample to "every continuous function is differentiable".
5. For $n = 40$, $n^2 + n + 41 = 1681 = 41^2$ is not prime, which refutes "$n^2 + n + 41$ is prime for every natural number $n$"; see [[forty prime values of n^2 + n + 41|H75AB4EJT5]].

### Non-examples

1. [[Zero is not a counterexample to the positivity of squares of nonzero numbers|~bcd67756]]: $x = 0$ does not satisfy the hypothesis $x \neq 0$.
2. An instance where the statement holds is not a counterexample. The prime $3$ is odd, so it says nothing against "every prime is odd".
3. A counterexample to the converse is not a counterexample to the statement. The number $9$ is odd and not prime; this refutes "every odd number is prime", not "every prime other than $2$ is odd".

### Basic properties

1. One counterexample refutes a universal statement, and no number of examples proves it; see [[checking cases does not prove that 2^n > n^2|~bee4cb21]].
2. A counterexample to "if $H(x)$, then $C(x)$" must satisfy $H$ and fail $C$. Both checks belong to the disproof.
3. If a statement about natural numbers has a counterexample, it has a smallest one, by the [[well-ordering principle|01BX15HSRR]]. Proofs by minimal counterexample and by [[infinite descent|0EFYCFHYFG]] use this fact.
4. A computer search can find a counterexample, but a search that finds none proves nothing about the cases beyond the search.
5. The negation of "every $x$ has property $P$" is "some $x$ fails $P$", and not "no $x$ has $P$". A counterexample shows only that the statement fails at least once.

### History

The Pólya conjecture of 1919 states that for every $n > 1$ at least half of the integers from $1$ to $n$ have an odd number of prime factors counted with multiplicity.
Haselgrove disproved it in 1958, and in 1980 Tanaka found its smallest counterexample, $906150257$.
The books Counterexamples in Analysis by Bernard Gelbaum and John Olmsted (1964) and Counterexamples in Topology by Lynn Steen and Arthur Seebach (1970) collect counterexamples for the standard theorems; see also the topic [[counterexamples in topology|Y642RFZPF0]].
Imre Lakatos's Proofs and Refutations (1976) describes how counterexamples lead mathematicians to revise both proofs and definitions.
The Mertens conjecture was disproved in 1985 by Andrew Odlyzko and Herman te Riele, whose proof shows that a counterexample exists without exhibiting one.

### Common errors

1. A "counterexample" that does not satisfy the hypotheses, as in non-example 1. Each hypothesis must be checked for the proposed object.
2. Refuting a different statement, such as the converse, or a stronger version of the claim.
3. Believing a statement because the first few cases work. The counterexamples to Euler's conjecture and to the Pólya conjecture are far beyond any hand check.

## Explanations

### L1 human

Someone says: "all birds can fly".
One penguin is enough to show that this is wrong.
A penguin is a bird, and it cannot fly.
In mathematics this is called a counterexample.
For the claim "every whole number is smaller than its square", the number $1$ is a counterexample, since $1 \times 1 = 1$ is not bigger than $1$.

### L2 human

We disprove: for all positive integers $a$, $b$, $c$, if $a \mid bc$, then $a \mid b$ or $a \mid c$.

1. To refute the statement, we need $a$, $b$, $c$ with $a \mid bc$ true and both $a \mid b$ and $a \mid c$ false.
2. Take $a = 6$, $b = 2$, $c = 3$.
3. Hypothesis: $bc = 6$, and $6 \mid 6$. So the hypothesis holds.
4. Conclusion: $6 \nmid 2$ and $6 \nmid 3$. So the conclusion fails.
5. So $(6, 2, 3)$ is a counterexample, and the statement is false.

The typical use: a counterexample also shows what a correct statement needs.
Here the statement becomes true when $a$ is prime, by [[Euclid's lemma|051VYKA1EX]], and $6$ is not prime.

A trap: step 3 is part of the disproof.
A triple such as $(6, 2, 5)$ fails the conclusion too, but $6 \nmid 10$, so it is not a counterexample.

### L3 human

In logic, a counterexample to a universal sentence is a witness in one model, and a countermodel refutes the validity of a sentence.
By Gödel's completeness theorem, a first-order sentence that is not provable from a theory has a model of the theory in which it fails.
Independence proofs, such as the models of non-Euclidean geometry for the parallel postulate, are counterexamples at the level of whole structures.
In constructive mathematics, a Brouwerian counterexample shows that a classical statement would imply a principle that constructive mathematics does not accept, and a [[strong counterexample|7PQ85QF58H]] goes further and proves the negation of an instance of such a principle.
Lakatos's account of "monster-barring", in which a definition is changed to exclude a counterexample, describes one way in which [[pathological objects|WMBZPYPN2D]] shape definitions.
False proofs and the search for the error in them are treated in the topic [[fallacies and errors in proofs|T6QQ749DM5]].
