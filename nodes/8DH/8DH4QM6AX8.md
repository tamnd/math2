---
tag: 8DH4QM6AX8
kind: concept
name: Fuzzy logic
aliases: [fuzzy-logic, mathematical-fuzzy-logic]
msc: ["03B52"]
topics: [WZP584JQ06]
audience: grad
uses: [DWYCKAKXZD, GV9NVFFFXF]
sources:
  - url: https://plato.stanford.edu/entries/logic-fuzzy/
    locator: lead section; 1. Fuzzy connectives based on t-norms; 10. Fuzzy logic and vagueness
  - url: https://en.wikipedia.org/wiki/Fuzzy_logic
    locator: lead section; Fuzzy systems; Logical analysis
  - book: isbn:9780792352389
---

## Summary

Suppose "Ann is tall" is true to degree $0.7$ and "Ann is rich" is true to degree $0.4$.
How true is "Ann is tall and rich"?
Fuzzy logic answers such questions with exact rules, and then asks which conclusions follow from premises that are only partly true.

The name has two uses, and they must be kept apart.
In the narrow sense, *mathematical fuzzy logic* is a family of [[many-valued logics|DWYCKAKXZD]] with truth values in $[0, 1]$, read as degrees of truth.
Each such logic has truth-functional connectives, a consequence relation that preserves the value $1$, a proof system and completeness theorems.
In the broad sense, used in engineering, "fuzzy logic" names methods that compute with degrees, such as fuzzy control and fuzzy classification.
These methods compute outputs, and they define no consequence relation.

## Motivation

Many predicates are vague: "tall", "young", "huge", "warm".
For a vague predicate there is no sharp line between the cases where it applies and the cases where it does not.
If one centimeter never turns a tall person into a person who is not tall, then by many small steps a short person is tall.
This is the sorites paradox, and it is the main test case for any logic of vagueness.

Fuzzy logic gives vague statements intermediate degrees and computes the degree of a compound statement from the degrees of its parts.
The sorites argument then loses a little truth at each step, as [[the sorites example|EP8J937EQC]] shows in numbers.
The same machinery returns throughout the later pages on t-norm logics: [[triangular norms|VR6D8JXX1W]] interpret "and", their residua interpret "if then", and [[Hájek's basic logic BL|3AQ5GHTXA4]] collects the laws that all continuous t-norms share.

## Notation

The truth values are $[0, 1]$, with $0$ for "totally false" and $1$ for "totally true".
The weak connectives are $x \land y = \min(x, y)$ and $x \lor y = \max(x, y)$.
The strong conjunction is a [[t-norm|BHGCVPAJW0]] $*$, and books write it as $\&$, $\otimes$ or $\odot$; we write $\otimes$ in general and $\odot$ for the Łukasiewicz t-norm.
Implication is the residuum $\Rightarrow_*$ of the t-norm, and negation is $\neg x = x \Rightarrow_* 0$.
Watch the two conjunctions: $\land$ is always the minimum, while $\otimes$ changes with the logic.

## Remarks

### Three answers for one conjunction

Return to Ann, with degrees $x = 0.7$ and $y = 0.4$.
The three basic t-norms give three answers.

$$\min(0.7, 0.4) = 0.4, \qquad 0.7 \cdot 0.4 = 0.28, \qquad \max(0, 0.7 + 0.4 - 1) = 0.1.$$

The first is Gödel logic, the second is [[product logic|YTHRDT9PDR]], and the third is [[Łukasiewicz logic|NFCEM44XYH]].
Each logic picks one rule and keeps it, so each has its own laws.
In Łukasiewicz logic the implication is $\min(1, 1 - x + y)$, so "if tall then rich" gets the value $0.7$.

Check: $1 - 0.7 + 0.4 = 0.7$, which is below $1$.

### Laws that change with the logic

Consider double negation, $\neg \neg p \to p$, at $p = \tfrac12$.
In Łukasiewicz logic $\neg x = 1 - x$, so $\neg \neg \tfrac12 = \tfrac12$ and the implication has value $1$.
In Gödel logic $\neg x = 0$ for every $x > 0$, so $\neg \neg \tfrac12 = 1$, and the implication is $1 \to \tfrac12 = \tfrac12$.
So double negation is a Łukasiewicz law and not a Gödel law, as [[the double negation example|XXVXP0S5Q0]] works out.

Some laws fail in every such logic.
Excluded middle $p \lor \neg p$ gets a value below $1$ at every $p$ strictly between $0$ and $1$.
The reason is that $p \Rightarrow_* 0 = 1$ only when $p = 0$, so both disjuncts are below $1$.
On the values $0$ and $1$, all these connectives agree with the classical truth tables.

### A family, not one logic

Every residuated t-norm gives a logic, and the main ones sit in a chain of extensions.
[[MTL|PT5PHKJDYM]] is the logic of all left-continuous t-norms.
BL adds divisibility and is the logic of all continuous t-norms.
Łukasiewicz, Gödel and product logic each add one more axiom to BL.
Strong conjunction implies weak conjunction in all of them, since $x * y \le \min(x, y)$ for every t-norm, but the converse fails.
Logics with truth constants, such as [[Pavelka logic|YG62F8YC0P]], add a constant for each rational degree.
For the decision problem, Mundici proved in 1987 that the Łukasiewicz tautologies are coNP-complete, the same complexity as classical logic.

### What it is not

A fuzzy controller is not a logic in the narrow sense.
It reads numbers, fires rules with degrees and returns a number, and nowhere does it ask which formulas follow from which premises; [[the fan controller|N9XZ3WAC2C]] computes one in full.
[[Probability logic|Z2WRGJDRQT]] is not fuzzy logic either.
Two events of probability $\tfrac12$ can have a conjunction of probability $0$, $\tfrac14$ or $\tfrac12$, so probability is not truth-functional.
A [[fuzzy set|GV9NVFFFXF]] alone is a membership function, a set-theoretic object, and it carries no consequence relation.

### Watch out

The trap named most often is to read "fuzzy logic" in an engineering text as a logic with theorems.
When a question asks about completeness, tautologies or proofs, it is about the narrow sense.
A second trap is to take $\min$, $\max$ and $1 - x$ as the whole logic.
With designated value $1$, these three connectives give no tautologies at all.
Every formula built from them gets the value $\tfrac12$ when all its variables get $\tfrac12$, since $\min$, $\max$ and $1 - x$ all send $\tfrac12$ to $\tfrac12$.

### History

Zadeh introduced fuzzy sets in 1965, and the name "fuzzy logic" comes from them.
Infinite-valued logic is older: Łukasiewicz and Tarski published a study of the Łukasiewicz logics in 1930.
Hájek's monograph *Metamathematics of Fuzzy Logic* of 1998 made the narrow sense a branch of mathematical logic.
It introduced BL and treated the three basic t-norm logics in propositional and first-order form.

### Try it

First, compute "tall and rich" for Ann in the three basic logics when both degrees are $0.5$.
The minimum gives $0.5$, the product gives $0.25$, and the Łukasiewicz t-norm gives $\max(0, 0.5 + 0.5 - 1) = 0$.

Second, is $p \to p$ a tautology of every t-norm logic?
Yes: $x \Rightarrow_* x = 1$, because $x \Rightarrow_* y = 1$ exactly when $x \le y$.

## Explanations

### L1 human

In ordinary logic a statement is true or false.
In fuzzy logic a statement can be true to a degree, such as $0.7$.
"Ann is tall" can be more true for a tall person than for a person of middle height.
A fuzzy logic gives rules to combine degrees, for example "and" as the smaller of two degrees.
Engineers also use the words "fuzzy logic" for controllers in machines, such as washing machines, and that is a different thing.

### L2 human

We test the formula $p \to (q \to p)$ in Łukasiewicz logic.
With $x = v(p)$ and $y = v(q)$, the inner implication is $\min(1, 1 - y + x)$, which is at least $x$.
An implication $a \to b$ has value $1$ when $a \le b$, so the whole formula has value $1$.
Now test the contraction law $p \to p \odot p$ at $x = 0.5$.

$$0.5 \odot 0.5 = \max(0, 0.5 + 0.5 - 1) = 0, \qquad 0.5 \to 0 = \min(1, 1 - 0.5 + 0) = 0.5.$$

So $p \to p \odot p$ is not a Łukasiewicz law, while in Gödel logic, where $\odot$ is replaced by $\min$, it has value $1$.
This is the typical use of the semantics: to test a law, fix the t-norm and look for values that push the formula below $1$.

### L3 human

Mathematical fuzzy logic studies these logics as objects of algebraic logic.
Their models are linearly ordered [[residuated lattices|E337A6WVH3]] and their subdirect products, and each of the main logics is complete for its algebras on $[0, 1]$.
Běhounek and Cintula proposed to call a logic fuzzy when it is complete with respect to linearly ordered algebras, and under this view MTL is the base of the family.
The first-order versions behave differently from each other: [[first-order Gödel logic|H8C323CV3T]] over $[0, 1]$ is recursively axiomatizable, while the first-order Łukasiewicz tautologies are not, as [[the complexity statement|VAHH1505Z0]] shows.
