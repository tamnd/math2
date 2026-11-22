---
tag: 0WCP0PVET6
kind: concept
name: Proof by cases
aliases: [proof-by-exhaustion, case-analysis]
msc: ["00A35", "97E50"]
topics: [G9JFJGY4TQ, 958EF46EYJ]
audience: school
specializes: [0B94TKFQJX]
uses: [0B94TKFQJX, 0H5GKDTB01, 0ZNX6DQ3EJ, 0NTF6DMVAP]
sources:
  - url: https://en.wikipedia.org/wiki/Proof_by_exhaustion
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Disjunction_elimination
    locator: lead section
  - book: isbn:9781108439534
    locator: Section 3.5
same_as:
  wikidata: Q9299950
  wikipedia: Proof by exhaustion
---

## Summary

A proof by cases splits the situation into a few kinds, proves the statement for each kind separately, and makes sure that no kind is left out.
It is the method to use when one argument does not fit every object, but two or three arguments do.

Here is a small one: for every integer $n$, the number $n^2 + n$ is even.
Every integer is even or odd, so there are two cases.
If $n = 2k$, then $n^2 + n = 4k^2 + 2k = 2(2k^2 + k)$.
If $n = 2k + 1$, then
$$n^2 + n = n(n + 1) = (2k + 1)(2k + 2) = 2(2k + 1)(k + 1).$$
In both cases $n^2 + n$ is twice an integer, so it is even.

In general, a *proof by cases* of a statement $R$ chooses statements $C_1, \ldots, C_k$ such that $C_1 \lor C_2 \lor \cdots \lor C_k$ is true, by a hypothesis or by a known fact, and it proves $C_i \Rightarrow R$ for each $i$.
The cases must be exhaustive, but they need not exclude each other.
The underlying rule is [[disjunction elimination|FTH70E7K1D]]: from $A \lor B$, $A \Rightarrow R$ and $B \Rightarrow R$, conclude $R$.

## Motivation

Many objects come in kinds that behave differently.
The [[absolute value|00S7C68D51]] $|x|$ is $x$ when $x \ge 0$ and $-x$ when $x < 0$, so a statement about $|x|$ has no single formula to compute with.
An integer is $2k$ or $2k + 1$, and the two forms behave differently when you square them.
A split into cases gives each part of the argument a formula of its own.

The price is completeness.
Every possibility must fall into some case, and a forgotten case is a gap in the proof, often exactly where the statement fails.
Case splits return all through mathematics: by the sign of a number, by the remainder of an integer, by whether a set is empty, and, in [[mathematical induction|0ASJVEFA9J]], by whether a natural number is $0$ or a successor.

## Notation

A proof by cases opens with a sentence that names the split and its reason, for example "Every integer is even or odd, so there are two cases."
Each case starts with a label such as "Case 1: $n$ is even." and ends with the conclusion in that case.
When there are many cases and each one is a finite check, the method is also called *proof by exhaustion*.
In Lean, `rcases h with h1 | h2` and `Or.elim` split a hypothesis `h : A ∨ B`, and `by_cases h : P` splits on a proposition `P` and its negation.

## Remarks

### Why the method is valid

Suppose $A \lor B$ is true, and you have proved $A \Rightarrow R$ and $B \Rightarrow R$.
In any situation at least one of $A$ and $B$ holds.
If $A$ holds, the first implication gives $R$; if $B$ holds, the second one does.
So $R$ holds in every situation, and that is disjunction elimination.
The same argument works for any finite number of cases.

The cases may overlap.
If $n = 0$ falls into both "$n \ge 0$" and "$n \le 0$", the statement is simply proved twice for $n = 0$, which does no harm.
A split into $P$ and $\neg P$ is always exhaustive by the [[law of excluded middle|0RYYK8PG4S]].
In intuitionistic logic disjunction elimination is still valid, but the disjunction $P \lor \neg P$ is not free: it must be proved for the particular $P$.
For the integers this is no problem, since "even or odd" is proved by the division algorithm.

### Choosing the split

A good split follows the definitions in the statement.
For [[the triangle inequality by cases|P4BF8XV06T]], $|x + y| \le |x| + |y|$, the split by the sign of $x + y$ matches the definition of $|x + y|$ and gives two cases.
A split by the signs of $x$ and $y$ also works, but it gives four cases, and the mixed ones need a further split.

For a statement about divisibility by $m$, split by the remainder modulo $m$.
For example, [[the square of an integer leaves remainder 0 or 1 on division by 3|N70XWKTVMC]] uses the three cases $n = 3k$, $3k + 1$ and $3k + 2$:
$$(3k)^2 = 3(3k^2), \quad (3k + 1)^2 = 3(3k^2 + 2k) + 1, \quad (3k + 2)^2 = 3(3k^2 + 4k + 1) + 1.$$
Check: $5 = 3 \cdot 1 + 2$ and $5^2 = 25 = 3 \cdot 8 + 1$.

Cases can nest.
Inside the case $x \ge 0$, a second split into $y \ge 0$ and $y < 0$ gives four cases in all.
When two cases are copies of each other with the letters exchanged, [[without loss of generality|Y7NE0E6PCV]] lets you write only one of them.

### Proof by exhaustion

Some proofs check a large but finite list of cases.
The [[four color theorem|0M406JC8J1]] says that the regions of every plane map can be colored with four colors so that neighboring regions differ.
Its proof reduces the problem to a finite set of configurations and checks each one by computer.
The logic is the same as in the two-case proof of the Summary; only the size is different.
Such proofs raise questions about checking and trust, which the topic [[rigor and the acceptance of proofs|1BTHSHST4M]] discusses.

### What is not a proof by cases

[[A case split that misses the interval 0 < x < 1|QEGHS9BAS2]] tries to prove $x^2 \ge x$ for every real $x$ with the cases $x \ge 1$ and $x \le 0$.
Each case is proved correctly, but the numbers between $0$ and $1$ are in neither case, and the claim fails at $x = \tfrac{1}{2}$.

Checking the integers from $1$ to $100$ is not a proof by cases for a statement about all integers, because the cases do not cover all integers.
A second case dismissed with the word "similar" is not proved either, unless the second case really is the first one after a change of letters that you can name.

### Watch out

The most common gap is a missing case.
Typical ones are $x = 0$ between "positive" and "negative", equality between "$<$" and "$>$", and the remainder $2$ when only $n = 3k$ and $n = 3k + 1$ are checked.
Before you prove any case, write the list of cases and check that it covers everything.

The second trap is to use the assumption of one case inside another.
Each case may use its own assumption and the common hypotheses, and nothing else.

The third trap is to confuse splitting a hypothesis with proving a disjunction.
To use a hypothesis "$A$ or $B$", you prove the goal in both cases.
To prove a goal "$A$ or $B$", you prove one of the two, or, in classical logic, you assume not $A$ and prove $B$.

### Writing it up

State the split and say why it is exhaustive ("By the division algorithm, $n = 3k$, $3k + 1$ or $3k + 2$.").
Label each case, prove the goal inside it, and end the case with the goal.
Finish with one sentence that collects the cases ("The three cases cover all integers, so the statement holds.").

### History

The name "proof by exhaustion" refers to exhausting all the cases.
It is unrelated to the method of exhaustion of Eudoxus and Archimedes, which computes areas by approximation.
In 1976 Kenneth Appel and Wolfgang Haken proved the four color theorem by a case analysis checked by computer.
Thomas Hales announced a proof of the [[Kepler conjecture|AFMBQT06ZV]] in 1998 that also relies on a computer check of many cases, and a formal verification of that proof was completed in 2014.

### Try it

First, prove that $|xy| = |x| \, |y|$ for all real $x$ and $y$.
Split by the signs: if $x, y \ge 0$, both sides are $xy$; if $x \ge 0 > y$, then $xy \le 0$ and both sides are $-xy$; the case $x < 0 \le y$ is the same with the letters exchanged; if $x, y < 0$, then $xy > 0$ and both sides are $xy = (-x)(-y)$.

Second, find the gap in "for every integer $n$, $n^2 \equiv n \pmod 3$; if $n = 3k$, both sides are $0$; if $n = 3k + 1$, both sides are $1$".
The case $n = 3k + 2$ is missing, and there the claim fails: $2^2 = 4 \equiv 1$, but $2 \not\equiv 1 \pmod 3$.

## Explanations

### L1 human

Suppose we want to show that a whole number times the next one is always even.
Whole numbers come in two kinds: even and odd.
If the first number is even, the product is even, for example $4 \times 5 = 20$.
If the first number is odd, the next one is even, for example $5 \times 6 = 30$, so again the product is even.
There is no third kind of whole number, so the claim holds for all of them.
That is a proof by cases: split into kinds, check each kind, and make sure that no kind is missing.

### L2 human

Let us prove that $n^3 - n$ is divisible by $3$ for every integer $n$.
First factor the expression, so that each case has something to work with:
$$n^3 - n = (n - 1) \, n \, (n + 1).$$
By the [[division algorithm|0CHQKZFK5S]], every integer is $3k$, $3k + 1$ or $3k + 2$, so three cases cover all integers.
If $n = 3k$, the factor $n$ is a multiple of $3$.
If $n = 3k + 1$, the factor $n - 1 = 3k$ is a multiple of $3$.
If $n = 3k + 2$, the factor $n + 1 = 3(k + 1)$ is a multiple of $3$.
In each case one factor is a multiple of $3$, so the product is too.
Check: $n = 5$ gives $125 - 5 = 120 = 3 \cdot 40$.
The problem shows the typical use: split by the remainder modulo $m$ when a statement about integers involves divisibility by $m$, and name every remainder.

### L3 human

In natural deduction, proof by cases is the elimination rule for disjunction, and it is valid in intuitionistic logic; what intuitionistic logic rejects is the free use of $P \lor \neg P$ to create the cases.
In type theory, a proof by cases on a hypothesis $A \lor B$ is a function defined by pattern matching on the two constructors of a sum type, and induction is pattern matching on a recursive type, as the topic [[induction and well-ordering|EEH2F76CYQ]] shows.
Large proofs by exhaustion raise the question of who checks the checker: the four color theorem was formally verified in the proof assistant Coq by Georges Gonthier and coworkers.
Case splits are also a source of symmetry arguments, and [[without loss of generality|Y7NE0E6PCV]] reduces symmetric cases to one.
