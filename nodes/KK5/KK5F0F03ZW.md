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

A proved statement in mathematics gets a label, and the label tells the reader what job the statement does in the text.
All the labels mean the same thing logically, "this has a [[proof|0B94TKFQJX]]", so a lemma is exactly as true as a theorem.
In common usage a *theorem* is a main result and a *proposition* is a result of less weight.
A *lemma* is a result proved mainly to help prove another result, and a *corollary* is a result that follows quickly from one just proved.
A *claim* is a statement proved inside a longer proof and used only there.
These are conventions of writing, not rules of logic, and authors differ in how they apply them.

## Motivation

A long proof is easier to read and to check when it is cut into parts.
The author proves the parts first, gives each a label and a number, and cites them in the main proof.
For example, the uniqueness of prime factorization in the [[fundamental theorem of arithmetic|084HH1NDCB]] rests on [[Euclid's lemma|051VYKA1EX]], and the irrationality of $\sqrt{2}$ then follows in a few lines.
[[The factorization chain|HGRAZBCXEQ]] works through all three results.
The labels act like road signs: they show which result is the destination and which ones are tools along the way.
The same structure returns in [[writing and reading proofs|STSM6PR7TX]], where a long argument is planned as a sequence of lemmas.

## Notation

Most texts number all results in one sequence, such as "Lemma 3.2", "Theorem 3.3", "Corollary 3.4", so that a reader can find any of them quickly.
Other texts number each kind separately.
The statement usually follows the label in italic type, and the proof follows the word "Proof".
A result can be named after a person ("Zorn's lemma"), after its content ("the pigeonhole principle"), or by its place ("Proposition I.47 of Euclid").

## Remarks

### A chain of three results

Here is a short chain with the usual labels.
Lemma: if $n^2$ is even, then $n$ is even.
The proof takes the contrapositive: if $n = 2k + 1$ is odd, then
$$n^2 = 4k^2 + 4k + 1 = 2(2k^2 + 2k) + 1$$
is odd.
Theorem: no integers $a$ and $b$ with $b \ne 0$ satisfy $a^2 = 2b^2$.
Corollary: $\sqrt{2}$ is irrational, because $\sqrt{2} = a/b$ would give $a^2 = 2b^2$.

The lemma matters mainly because the theorem needs it, and it is used twice in the proof of the theorem, once for $a$ and once for $b$.
The corollary is the result most readers remember, but it adds only one line.
Another author could call the theorem a lemma and the corollary the theorem, and both choices would be correct.

### What the labels signal

The labels describe the role of a result in one text, not its difficulty or its truth.
The same statement can be a theorem in one book, a lemma in a second and an exercise in a third.
"Proposition" often marks a result that is useful but not central, and many books use it for the routine facts of a chapter.

Watch out for a second meaning of the word.
In logic a [[proposition|0ZGC7ZESYN]] is any statement that is true or false, whether proved or not.
So "Proposition 2.1" in a textbook and "the proposition $P$" in a logic course use the word in different senses.

### Lemmas that outgrew their label

A result keeps the name it received first, even when later work makes it central.
[[Zorn's lemma|04RXTQA5ZA]] is equivalent to the axiom of choice over the other axioms of set theory, and it proves that every vector space has a basis.
The [[Yoneda lemma|D6DF1ARPVD]] is a basic tool of category theory, and [[Nakayama's lemma|15JHBYR6KH]] is one of commutative algebra.
[[Four named lemmas|H7PQD5G0CT]] are compared side by side, with a worked use of Burnside's lemma.
In each case the word "lemma" records an origin as a tool, not a measure of weight.

### Principles, laws, postulates and other labels

Some theorems carry traditional names.
The [[pigeonhole principle|0HGVCWQGY3]], the [[maximum modulus principle|048F2P90WR]], the [[law of cosines|060ZVZBV3E]] and the [[law of quadratic reciprocity|085MJS6907]] are all proved theorems.
[[Bertrand's postulate|0FJTGZA4GS]] says that for every $n > 1$ some prime $p$ satisfies $n < p < 2n$; for $n = 10$ the primes $11, 13, 17, 19$ qualify.
Despite the word "postulate", it is a theorem.

A few rarer labels also appear.
A remark or an observation is a short statement with a short proof or none.
A porism, in modern use, is a result of the form "if one solution exists, then infinitely many exist", as in Poncelet's porism about polygons inscribed in one conic and circumscribed about another.

### What is not a theorem

An axiom is not a theorem in this sense: a theory accepts it without proof, as Euclidean geometry accepts the [[parallel postulate|2PC3XY0PYZ]].
A definition is not a theorem either, because it names an idea and asserts nothing that needs proof.
A conjecture is not a theorem, even when its name says so.
[[Fermat's Last Theorem|0Y5X3SDBCZ]] had no accepted proof from about 1637 to 1994, and [[its story|AJR1GG3GF3]] shows that in that time it was a conjecture.

### Watch out

The first trap is to think that a lemma or a corollary is less certain than a theorem.
All three are proved, so each can be used in a later proof with the same confidence.
The second trap is to invent rules such as "a lemma has a short proof".
The proof of Zorn's lemma from the axiom of choice takes real work, and usage varies between authors.
The third trap is circular use: a corollary of a theorem cannot appear in the proof of that theorem.
For example, you may not use "$\sqrt{2}$ is irrational" while proving the theorem that $a^2 = 2b^2$ has no solution.

### History

The Greek word "theorema" comes from a verb that means "to look at".
In [[Euclid's Elements|83WHDAV68J]], a short consequence added after a proposition is called a porism, and modern texts call it a corollary.
Euclid also wrote a book called "Porisms", which is lost, and Pappus of Alexandria described its content.
Joseph Bertrand stated his postulate as a conjecture in 1845, and Pafnuty Chebyshev proved it in 1852, so the name no longer matches the status.

### Try it

First, a book proves that the angles of a triangle add up to $180$ degrees, and then states that each angle of an equilateral triangle is $60$ degrees; what label fits the second result?
A corollary, since three equal angles with sum $180$ degrees give $3x = 180$ at once.

Second, can a lemma from a famous paper be used with less confidence than its main theorem?
No: both are proved statements, and the label reflects only their roles in the paper.

## Explanations

### L1 human

In mathematics, a statement that has been proved gets a label.
The most important results are called theorems.
A lemma is a helper: it is proved first so that a bigger proof becomes shorter.
A corollary is a bonus: it follows in a few lines from a theorem just proved.
For example, "every whole number above $1$ splits into primes in only one way" is a theorem, and "$\sqrt{2}$ is not a fraction" is a corollary of it.
All these labels mean "proved", and only the role is different.

### L2 human

Here is the full proof of the theorem in the chain above, so that you can see where the lemma does its work.
Suppose integers $a$ and $b \ne 0$ satisfy $a^2 = 2b^2$, and choose such a pair with $|b|$ as small as possible.
Then $a^2$ is even, so $a$ is even by the lemma; write $a = 2c$.
Substitute:
$$4c^2 = 2b^2, \qquad \text{so} \qquad b^2 = 2c^2.$$
Now $b^2$ is even, so $b$ is even by the lemma; write $b = 2d$ with $d \ne 0$.
Substitute again: $4d^2 = 2c^2$, so $c^2 = 2d^2$.
The pair $c, d$ is another solution with $|d| = |b|/2 < |b|$, which contradicts the choice of $b$.
The lemma appeared twice, and that is the usual sign that a fact deserves its own label.

### L3 human

The labels form an informal layer above the logic of proof.
In a formal library such as Mathlib, a result is declared with the keyword `theorem` or `lemma`, and the proof checker treats the two keywords the same way.
The choice is left to the authors, as it is on paper.

Some lemmas became objects of study in their own right, and some "theorems" were conjectures for centuries.
The status of named but unproved statements belongs to the study of [[conjectures|WMEMMHZ3BH]].
How a long proof is organized into lemmas and claims is treated in [[writing and reading proofs|STSM6PR7TX]].
