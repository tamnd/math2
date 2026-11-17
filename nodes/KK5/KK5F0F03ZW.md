---
tag: KK5F0F03ZW
kind: concept
name: Theorems, lemmas, corollaries and propositions
aliases: [theorem, lemma, corollary, kinds-of-mathematical-results, porism]
msc: ["00A35"]
topics: [N4P3E53HM0]
audience: school
uses: [0B94TKFQJX]
sources:
  - url: https://en.wikipedia.org/wiki/Theorem
    locator: Terminology
  - url: https://en.wikipedia.org/wiki/Lemma_(mathematics)
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Corollary
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Porism
    locator: lead section
  - book: isbn:9781108439534
---

## Summary

A theorem is a mathematical statement that has a [[proof|0B94TKFQJX]].
The words theorem, proposition, lemma, corollary and claim all name proved statements, and they differ only in the role that the author gives to the statement.
A theorem is a main result, and a proposition is a result of smaller weight.
A lemma is a result proved mainly to help prove another result.
A corollary is a result that follows quickly from a result just proved.
A claim is a statement proved inside a longer proof.
These labels are conventions of writing, not parts of logic: each of them is proved in the same way, and no fixed rule decides which label a result gets.
The labels help a reader to find the main line of a text and to see which results serve which purpose.

## Motivation

A long proof is easier to read and to check when it is cut into parts.
An author proves the parts first, gives each part a label and a number, and then cites the parts in the main proof.
For example, the uniqueness of prime factorization in the [[fundamental theorem of arithmetic|084HH1NDCB]] rests on [[Euclid's lemma|051VYKA1EX]], and the irrationality of $\sqrt{2}$ then follows as a corollary, as [[this example|HGRAZBCXEQ]] shows.
The labels tell the reader which part is the goal and which parts are tools.

## Notation

Most texts number their results in one sequence, for example "Lemma 3.2", "Theorem 3.3", "Corollary 3.4".
Other texts number each kind separately.
The statement comes after the label in italic type, and the proof follows after the word "Proof".
A result is often named after a person ("Zorn's lemma"), after its content ("the pigeonhole principle"), or by its place ("Proposition I.47 of Euclid").

## Remarks

### Examples

- Theorem: the [[fundamental theorem of arithmetic|084HH1NDCB]], which says that each positive integer has exactly one prime factorization. It is a main result of elementary number theory.
- Lemma: [[Euclid's lemma|051VYKA1EX]], which says that a prime that divides a product divides one of the factors. Its main role is to prove the uniqueness part of the fundamental theorem.
- Corollary: the [[irrationality of $\sqrt{2}$|0DZGSDHD92]] follows in a few lines from unique factorization, as [[this example|HGRAZBCXEQ]] shows.
- Named lemmas that are major results: [[Zorn's lemma|04RXTQA5ZA]], the [[Yoneda lemma|D6DF1ARPVD]] and [[Nakayama's lemma|15JHBYR6KH]], as [[this example|H7PQD5G0CT]] shows.
- Principle and law: the [[pigeonhole principle|0HGVCWQGY3]], the [[maximum modulus principle|048F2P90WR]], the [[law of cosines|060ZVZBV3E]] and the [[law of quadratic reciprocity|085MJS6907]] are theorems with traditional names.
- Postulate: [[Bertrand's postulate|0FJTGZA4GS]], that each interval $n < p < 2n$ with $n > 1$ contains a prime $p$, is a theorem. Joseph Bertrand stated it as a conjecture in 1845, and Pafnuty Chebyshev proved it in 1852.

### Non-examples

- An axiom is not a theorem in this sense. It is a starting point that a theory accepts without proof, for example the [[parallel postulate|2PC3XY0PYZ]] in Euclidean geometry.
- A conjecture is not a theorem, even when its name says "theorem". [[Fermat's Last Theorem|0Y5X3SDBCZ]] was a conjecture until 1994, as [[this example|AJR1GG3GF3]] shows.
- A definition is not a theorem. It gives a name to an idea and asserts nothing that needs a proof.

### Basic properties

- Each label names a proved statement, so a lemma or a corollary has exactly the same logical status as a theorem.
- The label of a result can change over time. A lemma that turns out to be widely useful keeps its name, but it is cited as a main result.
- The same statement can be a theorem in one book and a lemma or an exercise in another, because the label depends on the role in the text.
- A corollary of a theorem depends on the theorem, so it cannot be used to prove that theorem. This would be circular.
- The word "proposition" has a second meaning in logic: a [[proposition|0ZGC7ZESYN]] is a statement that is true or false, proved or not.

### Other labels

- A claim is a statement inside a proof, stated and proved there, and used only in that proof.
- A porism has two uses. In ancient Greek mathematics it named a kind of proposition in Euclid's lost book "Porisms". In modern use it names a result of the form "if one solution exists, then infinitely many solutions exist", as in Poncelet's porism.
- A remark or an observation is a short statement with a short proof or none, given for orientation.
- A scholium is an old word for a comment added to a proof.

### History

The Greek word "theorema" comes from a verb that means "to look at".
In [[Euclid's Elements|83WHDAV68J]], a short consequence that is added after a proposition is called a porism, and modern texts call it a corollary.
Euclid also wrote a book with the title "Porisms", which is lost, and Pappus of Alexandria described its content.
[[Bertrand's postulate|0FJTGZA4GS]] and [[Fermat's Last Theorem|0Y5X3SDBCZ]] keep names that do not match their present status.

### Common errors

- To think that a lemma is less true or less certain than a theorem. Both are proved.
- To give fixed rules for the labels, for example "a lemma has a short proof". Many lemmas have long proofs, and the usage varies between authors.
- To use a result that has the name of a theorem, but that is still a conjecture, as a step of a proof.

## Explanations

### L1 human

In mathematics, a statement that has been proved gets a label.
The most important results are called theorems.
A lemma is a helper: it is proved first so that a bigger proof becomes shorter.
A corollary is a bonus: it follows in a few lines from a theorem just proved.
For example, "every whole number above $1$ splits into primes in only one way" is a theorem, and "$\sqrt{2}$ is not a fraction" is a corollary of it.
All these labels mean "proved", and only the role is different.

### L2 human

We read a short chain of results and name the role of each one.

1. Lemma: if $n^2$ is even, then $n$ is even. Proof: if $n = 2k + 1$ is odd, then $n^2 = 2(2k^2 + 2k) + 1$ is odd.
2. Theorem: there are no integers $a$ and $b$ with $b \neq 0$ and $a^2 = 2b^2$. For the proof, assume such $a$ and $b$ exist, and choose them with $|b|$ as small as possible.
3. Proof of the theorem, part 1: $a^2 = 2b^2$ is even, so $a$ is even by the lemma. We write $a = 2c$.
4. Part 2: then $4c^2 = 2b^2$, so $b^2 = 2c^2$ is even, and $b$ is even by the lemma. We write $b = 2d$ with $d \neq 0$.
5. Part 3: then $4d^2 = 2c^2$, so $c^2 = 2d^2$. The pair $c$, $d$ is a solution with $|d| < |b|$, which contradicts the choice of $b$.
6. Corollary: $\sqrt{2}$ is irrational. Proof: if $\sqrt{2} = a/b$ with integers $a$ and $b \neq 0$, then $a^2 = 2b^2$, which the theorem excludes.

The typical use of the labels is to show the structure of a text: the lemma is a tool, the theorem is the goal, and the corollary is a consequence.
A trap is to think that the labels follow rules.
Another author could call step 2 a lemma and step 6 the theorem, and both choices are correct.

### L3 human

The labels form an informal layer on top of the logic of proof.
In a formal library such as Mathlib, each result is a declaration with the keyword `theorem` or `lemma`, and the two keywords are synonyms for the proof checker.
The choice between them is left to the authors, in the same way as on paper.

Some lemmas became central objects of study.
The [[Yoneda lemma|D6DF1ARPVD]] is a basic tool of category theory, and [[Zorn's lemma|04RXTQA5ZA]] is equivalent to the axiom of choice over the other axioms of set theory.
In the other direction, some "theorems" were conjectures for a long time, and the names of conjectures are the subject of the page on [[conjectures|WMEMMHZ3BH]].
The structure of a written proof, with its lemmas and claims, is treated in [[writing and reading proofs|STSM6PR7TX]].
