---
tag: 0B94TKFQJX
kind: concept
name: Mathematical proof
aliases: [proof]
msc: ["00A35"]
topics: [N4P3E53HM0]
audience: school
uses: [0Y0MQYST0M]
sources:
  - url: https://en.wikipedia.org/wiki/Mathematical_proof
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Mathematical_proof
    locator: History and etymology
  - url: https://en.wikipedia.org/wiki/Formal_proof
    locator: lead section
  - book: isbn:9781108439534
    locator: Introduction
same_as:
  wikidata: Q11538
  wikipedia: Mathematical proof
---

## Summary

A mathematical proof of a statement is a finite chain of steps that ends with the statement.
Each step is a hypothesis of the statement, an axiom, a definition, a result that is already proved, or a consequence of earlier steps by a valid rule of inference, such as [[modus ponens|0Y0MQYST0M]].
A statement with a proof is a theorem, and the proof shows that the statement holds in every case that its hypotheses allow.
Proof is the standard by which mathematics accepts a result, and it is what separates a theorem from a well-tested guess.

## Motivation

The expression $n^2 + n + 41$ gives a prime number for $n = 0, 1, 2, \ldots, 39$.
Forty successful checks make the guess "it is always prime" look safe.
But for $n = 40$ the value is $1681 = 41^2$, which is not prime, as [[this example|H75AB4EJT5]] shows.
Thus checks of single cases, however many, do not settle a statement about infinitely many cases.

A proof solves this problem.
It gives one argument that works for each case at once, because it uses only the properties that all the cases share.
For example, the argument that the sum of two even integers is even uses only the form $2k$ of an even integer, so it covers every pair of even integers, as [[this example|5M5Q062R1X]] shows.

## Notation

A written proof usually starts with the word "Proof" and ends with a mark that shows its end.
The common end marks are the square $\square$ (also filled, $\blacksquare$) and the letters [[QED|ET9J6R9T5C]], from the Latin "quod erat demonstrandum" ("which was to be shown").
In logic, $\Gamma \vdash \varphi$ means that the formula $\varphi$ has a formal proof from the set of formulas $\Gamma$ in a fixed proof system.
The page [[proof methods|G9JFJGY4TQ]] collects the names of the standard methods, such as direct proof and proof by contradiction.

## Remarks

### Examples

- The sum of two even integers is even. [[This proof|5M5Q062R1X]] writes the integers as $2a$ and $2b$, and it writes the sum as $2(a + b)$.
- There are infinitely many prime numbers. [[Euclid's proof|0292EPPPT0]] shows that each finite list of primes misses a prime, so no finite list contains all primes.
- The number $\sqrt{2}$ is irrational. [[This proof|0DZGSDHD92]] assumes $\sqrt{2} = a/b$ and derives a contradiction, so it is a [[proof by contradiction|0J0XBKG64S]].
- The formula $1 + 2 + \cdots + n = n(n+1)/2$ holds for each positive integer $n$. A proof by [[mathematical induction|0ASJVEFA9J]] proves the case $n = 1$ and the step from $n$ to $n + 1$.
- The equation $2 + 2 = 4$ in the natural numbers has a proof that a computer checks, in the proof assistant Lean, as [[this example|QF0Q7B5Q73]] shows. The proof is a term, and the program checks that the term has the type of the statement.

### Non-examples

- The forty checks of $n^2 + n + 41$ for $n = 0$ to $39$ are not a proof that the value is always prime. The statement is false, as [[this example|H75AB4EJT5]] shows.
- The argument "if $n$ is even then $n^2$ is even, and $n^2$ is even, so $n$ is even" is not a proof. Its last step uses the [[converse|09A3N7ZN5G]] of the first statement, and the converse needs its own proof.
- A drawing of one equilateral triangle does not prove a statement about all triangles. A property of the drawing can depend on its special shape.

### Basic properties

- A proof is relative to its starting points. When the axioms change, the theorems can change: the [[parallel postulate|2PC3XY0PYZ]] holds in Euclidean geometry and fails in [[non-Euclidean geometry|SPCYMFN5V2]].
- Proofs can be combined. A proved result can serve as one step of a later proof, and this is the role of a lemma.
- One [[counterexample|0ED72CTBNP]] shows that a universal statement is false. No finite number of confirming examples shows that a statement about infinitely many cases is true.
- A theorem can have many different proofs. The [[Pythagorean theorem|0VP3A1290K]] has proofs by areas, by similar triangles and by algebra.
- An informal proof is an argument for a human reader, and it leaves out routine steps. A formal proof is a sequence of formulas in a formal system, such as a [[Hilbert system|1MGMQX43B8]], in which each formula follows by a stated rule.

### History

[[Euclid's Elements|83WHDAV68J]], written around 300 BC, organized geometry as definitions, postulates and propositions, each proposition with a proof.
In 1879 Gottlob Frege published the Begriffsschrift, a formal language in which each step of a proof follows a stated rule.
In 1976 Kenneth Appel and Wolfgang Haken proved the [[four colour theorem|0M406JC8J1]] with an essential computer check of many cases.
Today proof assistants such as Lean, Coq and Isabelle check formal proofs of large theorems.

### Common errors

- To check many cases and to call this a proof. A check of cases proves a statement only when the cases are all the cases, as in a finite check of a statement about finitely many objects.
- To use the statement that is to be proved as a step of its own proof. This is circular reasoning.
- To prove the converse of the statement instead of the statement. The statement "if $P$ then $Q$" and its converse "if $Q$ then $P$" are different statements.

## Explanations

### L1 human

A proof is an argument that shows that a statement is true in every case, not only in the cases that someone tested.
It starts from facts that are already accepted, and each step follows from the steps before it.
Take the claim "the sum of two even numbers is even".
The numbers $4$ and $6$ give $10$, which is even, but that is only one case.
A proof says: an even number is two times a whole number, so the sum is two times a whole number plus two times a whole number.
This is two times one whole number, so the sum is even.
The argument does not depend on which even numbers we take, so it covers all of them at once.

### L2 human

We prove that the product of two odd integers is odd.

1. Let $m$ and $n$ be odd integers. This is the hypothesis.
2. By the definition of an odd integer, $m = 2a + 1$ for some integer $a$.
3. By the same definition, $n = 2b + 1$ for some integer $b$. We use a new letter $b$, because $n$ need not be equal to $m$.
4. We multiply: $mn = (2a + 1)(2b + 1) = 4ab + 2a + 2b + 1$.
5. We factor: $4ab + 2a + 2b + 1 = 2(2ab + a + b) + 1$.
6. The number $k = 2ab + a + b$ is an integer, because sums and products of integers are integers.
7. So $mn = 2k + 1$ with $k$ an integer, and $mn$ is odd by the definition of an odd integer.

The typical use of this pattern is a [[direct proof|0NTF6DMVAP]]: we unfold the definitions in the hypothesis, compute, and fold the result back into the definition in the conclusion.
A trap is step 3 written with the same letter: "$m = 2a + 1$ and $n = 2a + 1$".
That version proves the statement only for $m = n$, so it is not a proof of the general statement.

### L3 human

There are two views of a proof.
In practice, a proof is an argument written for other mathematicians, and it is accepted when competent readers agree that each step can be filled in.
In logic, a proof is a formal derivation: a finite sequence of formulas in a formal language, each an axiom or the result of a rule of inference applied to earlier formulas.
[[Proof theory|N4EDJNMTEF]] studies formal derivations as mathematical objects, and the [[soundness|4A84VHDTHV]] and completeness theorems connect them with truth in all models.

The two views meet in proof assistants.
In Lean, a statement is a type, a proof is a term of that type, and a small kernel checks the type of each term.
This is the [[Curry-Howard correspondence|A77FER1Q5H]] between proofs and programs.
The library Mathlib holds a large body of formal proofs of undergraduate and research mathematics, and the topic [[mathematical software and formalization|F3F5GGYHMM]] treats it.
The questions of how much detail a proof needs and of who accepts it belong to [[rigour and the acceptance of proofs|1BTHSHST4M]], and the question of what a proof is in principle belongs to the [[philosophy of mathematics|NTJ5XW0PVD]].
