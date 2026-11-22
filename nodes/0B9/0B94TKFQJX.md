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

A proof is an argument that shows a statement is true in every case that it covers, not only in the cases that someone checked.
It is how mathematics decides what it knows: a statement with a correct proof is a theorem, and no later test can overturn it.
Precisely, a *mathematical proof* of a statement is a finite sequence of steps that ends with the statement.
Each step is a hypothesis of the statement, an axiom, a definition, a result proved earlier, or a consequence of earlier steps by a valid rule of inference such as [[modus ponens|0Y0MQYST0M]].
An informal proof, the kind in books and papers, gives enough steps for a trained reader to supply the rest.
A formal proof gives every step in a formal language, so that a computer can check it.

## Motivation

Put $n = 0, 1, 2, 3$ into $n^2 + n + 41$ and you get $41$, $43$, $47$ and $53$, all prime.
The values stay prime for every $n$ from $0$ to $39$, so the guess "$n^2 + n + 41$ is always prime" looks safe.
It is false, because the next value is
$$40^2 + 40 + 41 = 40 \cdot 41 + 41 = 41 \cdot 41 = 1681.$$
Forty good cases did not settle a claim about infinitely many cases, as [[the full story of this polynomial|H75AB4EJT5]] shows.

A proof solves this problem.
It gives one argument that works for every case at once, because it uses only the properties that all the cases share.
The argument that the sum of two even integers is even uses only the form $2k$ of an even integer, so [[that proof|5M5Q062R1X]] covers every pair of even integers, including pairs that nobody will ever write down.
The rest of the area builds on this idea: the [[proof methods|G9JFJGY4TQ]] give standard shapes of argument, [[mathematical induction|0ASJVEFA9J]] handles statements about all natural numbers, and [[rigor and the acceptance of proofs|1BTHSHST4M]] asks how much detail a proof needs.

## Notation

A written proof usually starts with the word "Proof" and ends with a mark.
The common marks are the square $\square$, the filled square $\blacksquare$ and the letters [[QED|ET9J6R9T5C]], from the Latin "quod erat demonstrandum", "which was to be shown".
In logic, $\Gamma \vdash \varphi$ means that the formula $\varphi$ has a formal proof from the set of formulas $\Gamma$ in a fixed proof system.
Do not confuse it with $\Gamma \models \varphi$, which says that $\varphi$ is true in every model of $\Gamma$.

## Remarks

### A first proof, step by step

We prove that $n^2 + n$ is even for every integer $n$.
First factor: $n^2 + n = n(n + 1)$.
Every integer is even or odd, so we take two cases.
If $n$ is even, then $n = 2k$ for an integer $k$, and
$$n(n + 1) = 2 \cdot k(n + 1).$$
If $n$ is odd, then $n = 2k + 1$, so $n + 1 = 2(k + 1)$, and
$$n(n + 1) = 2 \cdot n(k + 1).$$
In both cases $n(n + 1)$ is $2$ times an integer, so it is even.

Look at what the proof used.
It used the hypothesis ($n$ is an integer), a definition (even means $2$ times an integer), an earlier fact (every integer is even or odd), and the fact that products of integers are integers.
It also used one rule of reasoning: if a claim holds in each of the cases, and the cases cover everything, the claim holds.
The result also explains the polynomial above: $n^2 + n + 41$ is always odd, so the number $2$ never divides it.

### Evidence is not proof

Checks of cases can support a claim, but they cannot prove a claim about infinitely many cases.
The forty prime values of $n^2 + n + 41$ are the standard warning, and some false claims survive far longer.
The Pólya conjecture says that, for every $n \ge 2$, at least half of the numbers from $1$ to $n$ have an odd number of prime factors, counted with repetition.
It holds for every $n$ below $906150257$ and fails there.

A checked list of cases is a proof only when the list contains all the cases.
"Every integer from $1$ to $10$ has a square below $101$" is proved by ten multiplications, because there are only ten cases.
In the other direction, one [[counterexample|0ED72CTBNP]] is enough to show that a statement of the form "for all" is false.
So $n = 40$ disproves the claim about $n^2 + n + 41$ in one line, while no number of good cases could have proved it.

### What a proof may start from

A proof starts from axioms, definitions and earlier theorems, and its result holds relative to them.
When the axioms change, the theorems can change.
The angles of a triangle add up to $180$ degrees in Euclidean geometry, where the [[parallel postulate|2PC3XY0PYZ]] holds.
In the hyperbolic plane of [[non-Euclidean geometry|SPCYMFN5V2]], where it fails, the sum is always less than $180$ degrees.

Earlier theorems serve as single steps.
A proof that there are [[infinitely many primes|0292EPPPT0]] uses the fact that every integer above $1$ has a prime factor, and it does not prove that fact again.
One theorem can also have several proofs.
The [[Pythagorean theorem|0VP3A1290K]] has proofs by rearranging areas, by similar triangles and by coordinates, and each proof shows a different reason for the same fact.

### What is not a proof

Three common arguments look like proofs and are not.
The forty checks of $n^2 + n + 41$ are evidence, and the claim they support is false.
The argument "if $n$ is even then $n^2$ is even; here $n^2$ is even; so $n$ is even" is invalid.
It uses the [[converse|09A3N7ZN5G]] of the first statement, and the same pattern would show that $-3$ is $3$ because both have square $9$.
A drawing of one triangle proves nothing about all triangles, because the drawing can have a special shape, such as a right angle, that the general triangle lacks.

### Informal and formal proofs

The proof that $n^2 + n$ is even is informal.
It does not prove that every integer is even or odd, and it does not cite the distributive law, because a trained reader can supply both.
A formal proof leaves nothing out.
It is a list of formulas in a formal system, such as a [[Hilbert system|1MGMQX43B8]], and each formula is an axiom or follows from earlier ones by a stated rule.

Formal proofs are long, but a computer can check them.
In the proof assistant Lean, the line `example : 2 + 2 = 4 := rfl` is a complete formal proof, and [[the Lean example|QF0Q7B5Q73]] explains how the program checks it.
If you change $4$ to $5$, Lean computes both sides, finds different values and rejects the proof.

### Watch out

The most common error in a first proof is to reuse a letter.
To prove that the sum of two even integers is even, a student writes $m = 2k$ and $n = 2k$.
That argument covers only the case $m = n$: it says nothing about $m = 2$ and $n = 4$.
Two arbitrary even integers need two letters, $m = 2a$ and $n = 2b$.

A second error is to use the statement as a step in its own proof.
"The sum of two even numbers is even, because even numbers add to even numbers" is circular: the reason is the claim.
A third error is to prove the converse.
The statement "if $P$ then $Q$" and its converse "if $Q$ then $P$" are different, as $P$: "$n = 3$" and $Q$: "$n^2 = 9$" show.

### History

[[Euclid's Elements|83WHDAV68J]], written around 300 BC, set out geometry as definitions, postulates and propositions, each proposition with a proof.
In 1879 Gottlob Frege published the Begriffsschrift, a formal language in which every step of a proof follows a stated rule.
In 1976 Kenneth Appel and Wolfgang Haken proved the [[four color theorem|0M406JC8J1]] with a computer check of many cases that no person could check by hand.
Today proof assistants such as Lean and Isabelle check formal proofs of large theorems.

### Try it

First, prove that the sum of two odd integers is even.
Write them as $2a + 1$ and $2b + 1$; the sum is $2a + 2b + 2 = 2(a + b + 1)$, which is $2$ times an integer.

Second, the polynomial $n^2 - n + 41$ is prime for $n = 1, \dots, 40$; find a value of $n$ where it is not prime without a search.
Take $n = 41$: the value is $41^2 - 41 + 41 = 41^2$.

Third, say what is wrong with "$x^2 = 4$ implies $x = 2$, because $x = 2$ implies $x^2 = 4$."
It proves the converse, and $x = -2$ shows that the claim itself is false.

## Explanations

### L1 human

A proof is an argument that shows that a statement is true in every case, not only in the cases that someone tried.
Take the claim "the sum of two even numbers is even".
The numbers $4$ and $6$ give $10$, which is even, but that is one case out of infinitely many.
A proof says: an even number is two times a whole number, so the sum is two times one number plus two times another.
That is two times their sum, which is again a whole number, so the sum is even.
The argument never used the values $4$ and $6$, so it works for all even numbers at once.

### L2 human

Here is a typical first proof: the product of two odd integers is odd.
Let $m$ and $n$ be odd, so $m = 2a + 1$ and $n = 2b + 1$ for integers $a$ and $b$.
We use two letters because $m$ and $n$ need not be equal.
Multiply out:
$$mn = (2a + 1)(2b + 1) = 4ab + 2a + 2b + 1 = 2(2ab + a + b) + 1.$$
The number $2ab + a + b$ is an integer, because sums and products of integers are integers, so $mn$ is $2$ times an integer plus $1$.
That is the definition of an odd integer, and the proof is complete.
Check: $3 \cdot 5 = 15$, and the formula with $a = 1$, $b = 2$ gives $2(4 + 1 + 2) + 1 = 15$.
This is the pattern of a [[direct proof|0NTF6DMVAP]]: unfold the definitions in the hypothesis, compute, and fold the result back into the definition in the conclusion.

### L3 human

A proof has two lives.
In practice it is an argument written for other mathematicians, and it is accepted when competent readers agree that every step can be filled in.
In logic it is a formal derivation, and [[proof theory|N4EDJNMTEF]] studies such derivations as mathematical objects.
The [[soundness|4A84VHDTHV]] theorem says that what has a formal proof is true in every model, and Gödel's completeness theorem gives the converse for first-order logic.

The two lives meet in proof assistants.
In Lean a statement is a type, a proof is a term of that type, and a small kernel checks the type of each term, which is the [[Curry-Howard correspondence|A77FER1Q5H]].
The library Mathlib holds formal proofs of a large part of undergraduate mathematics, and [[mathematical software and formalization|F3F5GGYHMM]] treats it.
What a proof is in principle, and why it gives knowledge, are questions for the [[philosophy of mathematics|NTJ5XW0PVD]].
