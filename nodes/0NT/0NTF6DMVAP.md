---
tag: 0NTF6DMVAP
kind: concept
name: Direct proof
msc: ["00A35", "97E50"]
topics: [G9JFJGY4TQ, 958EF46EYJ]
audience: school
specializes: [0B94TKFQJX]
uses: [0B94TKFQJX, 0ZNX6DQ3EJ, FA6YZGR2SS]
sources:
  - url: https://en.wikipedia.org/wiki/Direct_proof
    locator: lead section
  - book: isbn:9781108439534
    locator: Section 3.1
same_as:
  wikidata: Q3240280
  wikipedia: Direct proof
inventory: [33MF2VWC2Q]
---

## Summary

A direct proof of an [[implication|0ZNX6DQ3EJ]] "if $P$, then $Q$" assumes that the hypothesis $P$ is true and then derives the conclusion $Q$ by a finite chain of steps.
Each step is an axiom, a definition, an earlier theorem, or a valid inference from the steps before it.
The proof never assumes $Q$ and never assumes the negation of $Q$.
A direct proof of a statement $Q$ with no hypothesis is the same chain, started from axioms and known results.
Direct proof is the default [[proof method|G9JFJGY4TQ]], and most other methods reduce a goal to one or more direct proofs.

## Motivation

A [[conditional statement|FA6YZGR2SS]] "if $P$, then $Q$" is false in exactly one situation: $P$ is true and $Q$ is false.
So to prove it, it is enough to show that this situation cannot happen.
The most natural way is to take any situation in which $P$ is true and to show that $Q$ is true there too.
That is a direct proof.
The method also matches how definitions work: the hypothesis $P$ usually contains a defined word, such as "even" or "divides", and the definition turns $P$ into an equation or an inequality that can be manipulated.

## Notation

There is no special symbol for a direct proof.
Books write "Assume $P$." or "Suppose $P$." at the start and "Hence $Q$." or "Therefore $Q$." at the end.
Some books call the method "forward reasoning".
In the proof assistant Lean, the tactic `intro h` starts a direct proof of a goal `P → Q`: it adds the hypothesis `h : P` and leaves the goal `Q`.

## Remarks

### Examples

1. [[A direct proof that the square of an odd integer is odd|E330HD4J2D]]: write $n = 2k + 1$, then $n^2 = 2(2k^2 + 2k) + 1$.
2. [[A direct proof that divisibility is transitive|JZ6667K6YD]]: from $b = ak$ and $c = bl$ we get $c = a(kl)$.
3. [[A proof that the sum of two even integers is even|5M5Q062R1X]]: from $m = 2k$ and $n = 2l$ we get $m + n = 2(k + l)$.
4. If $x$ is a real number with $x > 1$, then $x^2 > x$. Multiply both sides of $x > 1$ by the positive number $x$.
5. Every [[group|28PKCPYA2V]] has [[exactly one identity element|GDBV09GFYB]]: if $e$ and $e'$ are identities, then $e = e e' = e'$. Each equality uses the definition of an identity once.

### Non-examples

1. [[An argument that starts from the conclusion a^2 + b^2 >= 2ab|2VA8Q8BG5Y]]: the chain runs from the goal to a true statement, so it proves the converse direction only.
2. The usual proof that $\sqrt{2}$ is irrational, [[by lowest terms|7GNMP4Q32W]], is not direct. It assumes the negation of the conclusion and reaches a contradiction, so it is a [[proof by contradiction|0J0XBKG64S]].
3. A proof of "if $n^2$ is even, then $n$ is even" through "if $n$ is odd, then $n^2$ is odd" is a [[proof by contrapositive|0BB5TPGQ1N]]. It is a direct proof of a different implication.

### Basic properties

1. A direct proof is valid in classical logic and in intuitionistic logic. It uses neither the [[law of excluded middle|0RYYK8PG4S]] nor the [[double negation law|0NFAGWH84K]], unless a step quotes them.
2. Direct proofs compose: from a direct proof of $P \Rightarrow Q$ and one of $Q \Rightarrow R$, putting the chains one after the other gives a direct proof of $P \Rightarrow R$.
3. A [[proof by contrapositive|0BB5TPGQ1N]] is a direct proof of $\neg Q \Rightarrow \neg P$, and each case of a [[proof by cases|0WCP0PVET6]] is usually a direct proof.
4. If the hypothesis $P$ is false in every situation, then "if $P$, then $Q$" is vacuously true, and a direct proof has nothing to show.

### History

Most propositions in [[Euclid's Elements|83WHDAV68J]] are proved by chains of steps from the postulates and earlier propositions, and many of them are direct proofs.
The name "direct proof" contrasts the method with the indirect proofs, the proofs by contradiction, which the Greek geometers also used.

### Common errors

1. Starting from the conclusion $Q$ and deriving a true statement. This shows $Q \Rightarrow \text{true}$, which says nothing about $Q$. The fix is to reverse the chain and check that each step can be reversed.
2. Using an example instead of a general element. "Take $n = 3$; then $n^2 = 9$ is odd" proves one case only. The proof must work with $n = 2k + 1$ for an arbitrary integer $k$.
3. Using the same letter for two different objects. If $m$ and $n$ are even, writing $m = 2k$ and $n = 2k$ forces $m = n$. Two even integers need two letters, $m = 2k$ and $n = 2l$.

## Explanations

### L1 human

A direct proof starts from what is given and walks step by step to what is wanted.
Each step must have a reason, such as a rule of algebra or the meaning of a word.
For example, take the claim "if a number is odd, then its square is odd".
An odd number is one more than an even number, for example $7 = 6 + 1$.
Then $7 \cdot 7 = 49 = 48 + 1$, and $48$ is even, so $49$ is odd.
A direct proof does the same computation with a letter in place of $7$, so that it works for every odd number at once.

### L2 human

We prove: for all integers $a$ and $b$, if $a$ and $b$ are odd, then $ab$ is odd.

1. Assume that $a$ and $b$ are odd integers. This is the hypothesis.
2. By the definition of odd, there are integers $k$ and $l$ with $a = 2k + 1$ and $b = 2l + 1$. We use two letters, because $a$ and $b$ can differ.
3. Multiply: $ab = (2k + 1)(2l + 1) = 4kl + 2k + 2l + 1$.
4. Factor $2$ from the first three terms: $ab = 2(2kl + k + l) + 1$.
5. The number $m = 2kl + k + l$ is an integer, because integers are closed under addition and multiplication.
6. So $ab = 2m + 1$ with $m$ an integer, and $ab$ is odd by the definition of odd.

The typical use: unfold each defined word in the hypothesis into an equation, compute, and fold the result back into the defined word of the conclusion.
Most proofs about parity, divisibility, set inclusion and continuity start this way.

A trap: the proof must end in the exact form that the definition requires.
"$ab = 4kl + 2k + 2l + 1$" is not yet a proof that $ab$ is odd, because the definition asks for the form $2m + 1$ with $m$ an integer.

### L3 human

In natural deduction, a direct proof of $P \to Q$ is an application of the rule of implication introduction: from a derivation of $Q$ under the open assumption $P$, conclude $P \to Q$ and close the assumption.
This rule is valid in intuitionistic logic, so direct proofs are constructive whenever their steps are.
Under the Curry-Howard correspondence, a direct proof of $P \to Q$ is a function that takes a proof of $P$ to a proof of $Q$; this is why Lean writes the step as `intro` or as `fun h => ...`.
Much of the craft of proof lies in the choice of the intermediate statements, and the [[forward-backward method|V8ZB838JY5]] is a systematic way to find them.
The other methods of this topic change the goal before the direct work starts: the [[contrapositive|0BB5TPGQ1N]] replaces the goal, [[proof by contradiction|0J0XBKG64S]] adds an assumption, and [[mathematical induction|0ASJVEFA9J]] splits a universal goal into a base case and a step.
