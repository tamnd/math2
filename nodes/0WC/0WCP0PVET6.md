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

A proof by cases splits the situation into finitely many cases $C_1, \ldots, C_k$ such that at least one case always holds, and it proves the statement separately in each case.
The cases must be exhaustive: in symbols, $C_1 \lor C_2 \lor \cdots \lor C_k$ must be true, either by a hypothesis or by a known fact.
The cases need not exclude each other, although they often do.
The basic rule is [[disjunction elimination|FTH70E7K1D]]: from $A \lor B$, $A \Rightarrow R$ and $B \Rightarrow R$, conclude $R$.
The method applies whenever different inputs need different arguments, for example even and odd integers, or positive and negative real numbers.

## Motivation

One argument does not always fit all elements of a set.
The absolute value $|x|$ is $x$ for $x \geq 0$ and $-x$ for $x < 0$, so a statement about $|x|$ has no single formula to compute with.
An integer is either $2k$ or $2k + 1$, and the two forms behave differently under multiplication.
Splitting into cases gives each part of the argument a formula to work with.
The price is that every case must be covered, and a forgotten case is a gap in the proof.

## Notation

A proof by cases opens with a sentence that names the split and its reason, for example "Every integer is even or odd, so there are two cases."
Each case starts with "Case 1: $n$ is even." and ends with the conclusion in that case.
When the cases are many and each one is a finite check, the method is called proof by exhaustion, or the brute force method.
In Lean, `rcases h with h1 | h2` and `Or.elim` split a hypothesis `h : A ∨ B`, and `by_cases h : P` splits on a proposition `P` and its negation.

## Remarks

### Examples

1. [[The square of an integer leaves remainder 0 or 1 on division by 3|~d6037862]]: three cases by the remainder of $n$.
2. [[The triangle inequality for real numbers by cases|~04dd66a7]]: two cases by the sign of $x + y$.
3. For every integer $n$, $n^2 + n$ is even. If $n$ is even, then $n^2$ and $n$ are even. If $n$ is odd, then $n^2$ and $n$ are odd. In both cases the sum is even.
4. For real $x$ and $y$, $\max(x, y) \geq \frac{x + y}{2}$. If $x \geq y$, then $\max(x, y) = x = \frac{x + x}{2} \geq \frac{x + y}{2}$; the case $y \geq x$ is the same with $x$ and $y$ exchanged. A symmetric split like this one is often shortened by [[without loss of generality|~804de89a]].
5. The [[four colour theorem|0M406JC8J1]] was proved by Appel and Haken in 1976 with a computer check of a large finite set of configurations, a proof by exhaustion.

### Non-examples

1. [[A case split that misses the interval 0 < x < 1|~ed492ca3]]: the "proof" that $x^2 \geq x$ for all real $x$ checks $x \geq 1$ and $x \leq 0$ only, and the claim fails at $x = \frac{1}{2}$.
2. Checking the first hundred integers is not a proof by cases for a statement about all integers. The cases do not cover all integers.
3. A case split whose cases are not proved separately. "Case 1: $n$ even, done. Case 2: similar." is not a proof unless case 2 is in fact the same argument after a change of variable.

### Basic properties

1. The cases must cover all possibilities, and each case may use its own assumption. They need not be disjoint, since a statement proved twice on an overlap is still proved.
2. A split into $P$ and $\neg P$ is always exhaustive by the [[law of excluded middle|0RYYK8PG4S]]. So in intuitionistic logic, a proof by cases needs the disjunction itself to be proved.
3. Cases can be nested: inside the case "$x \geq 0$" a second split "$y \geq 0$ or $y < 0$" gives four cases in total.
4. Splitting a hypothesis of the form $A \lor B$ is a proof by cases; proving a goal of the form $A \lor B$ is different, and the usual method is to assume not $A$ and prove $B$.
5. A proof by [[mathematical induction|0ASJVEFA9J]] splits the natural numbers into the base case and the successor case, so it contains a proof by cases.

### History

The name "proof by exhaustion" refers to the exhaustion of all cases; it is unrelated to the method of exhaustion of Eudoxus and Archimedes, which computes areas by approximation.
In 1976 Kenneth Appel and Wolfgang Haken proved the [[four colour theorem|0M406JC8J1]] by a case analysis checked by computer.
Thomas Hales announced a proof of the [[Kepler conjecture|AFMBQT06ZV]] in 1998 that also relies on a computer check of many cases, and a formal verification of that proof was completed in 2014.

### Common errors

1. A missing case. Typical gaps are $x = 0$ between "positive" and "negative", equality between "$<$" and "$>$", and the integers $n \equiv 2 \pmod 3$ when only $n = 3k$ and $n = 3k + 1$ are checked.
2. A case assumption that is used in another case. Each case may only use its own assumption and the common hypotheses.
3. "The other case is similar" when it is not. The writer must check that the second case really follows by the same steps, or by a symmetry that is stated.

## Explanations

### L1 human

Suppose we want to show that a whole number times the next one is always even.
Whole numbers come in two kinds: even and odd.
If the first number is even, the product is even, for example $4 \times 5 = 20$.
If the first number is odd, the next one is even, for example $5 \times 6 = 30$, so again the product is even.
There is no third kind of whole number, so the claim holds for all of them.
That is a proof by cases: split into kinds, check each kind, and make sure that no kind is missing.

### L2 human

We prove: for every integer $n$, $n^3 - n$ is divisible by $3$.

1. Factor: $n^3 - n = (n - 1) n (n + 1)$.
2. By division by $3$, every integer has the form $3k$, $3k + 1$ or $3k + 2$ for an integer $k$. So there are three cases.
3. Case $n = 3k$: the factor $n$ is $3k$, so $3$ divides the product.
4. Case $n = 3k + 1$: the factor $n - 1$ is $3k$, so $3$ divides the product.
5. Case $n = 3k + 2$: the factor $n + 1$ is $3k + 3 = 3(k + 1)$, so $3$ divides the product.
6. The three cases cover all integers, so $3 \mid n^3 - n$ for every integer $n$.

The typical use: split by the remainder modulo $m$ when a statement about integers involves divisibility by $m$.

A trap: step 2 must name all remainders.
A proof that treats only $3k$ and $3k + 1$ looks complete, because two cases feel like "even and odd", but it misses one third of the integers.

### L3 human

In natural deduction, proof by cases is the elimination rule for disjunction, and it is valid in intuitionistic logic; what intuitionistic logic rejects is the free use of $P \lor \neg P$ to create the cases.
In type theory, a proof by cases on a hypothesis $A \lor B$ is a function defined by pattern matching on the two constructors of the sum type, and induction is pattern matching on a recursive type.
Large proofs by exhaustion raise questions of checking and trust, which the topic [[rigour and the acceptance of proofs|1BTHSHST4M]] treats: the four colour theorem was formally verified in the proof assistant Coq by Georges Gonthier and coworkers.
Case splits are also a source of symmetry arguments, and the method [[without loss of generality|~804de89a]] reduces symmetric cases to one.
