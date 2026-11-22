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

A claim about every object of some kind can be destroyed by one object for which it fails.
That one object is a counterexample, and finding it is the standard way to show that a general claim is false.

Here is a famous one.
The numbers $2^{2^n} + 1$ for $n = 0, 1, 2, 3, 4$ are $3$, $5$, $17$, $257$ and $65537$, and all five are prime.
So it is tempting to claim that $2^{2^n} + 1$ is prime for every $n \ge 0$.
The next case breaks the claim:
$$2^{2^5} + 1 = 2^{32} + 1 = 4294967297 = 641 \cdot 6700417.$$
So $n = 5$ is a counterexample, and the claim is false.

In general, a *counterexample* to a [[universal statement|0B88PQTJ66]] $\forall x \in X \; P(x)$ is an element $a \in X$ for which $P(a)$ is false.
For a statement "for all $x$ in $X$, if $H(x)$, then $C(x)$", a counterexample is an element $a \in X$ with $H(a)$ true and $C(a)$ false.
Exhibiting one counterexample proves that the universal statement is false, and this is called *disproof by counterexample*.

## Motivation

A universal claim may cover infinitely many cases, and a proof has to handle all of them.
A failure needs only one case.
This imbalance makes counterexamples the first test of any conjecture: before anyone looks for a proof, they try small cases, extreme cases and odd shapes.

Counterexamples also explain theorems.
A theorem with several hypotheses is understood only when you know which hypotheses matter, and a counterexample for each dropped hypothesis shows that it does.
They correct definitions too, when an object fits the words of a definition but not the idea behind it.
The method of [[minimal counterexample|JGRCNPKNGG]] and [[infinite descent|0EFYCFHYFG]], in the topic [[induction and well-ordering|EEH2F76CYQ]], turns the search for a counterexample into a proof that none exists.

## Notation

A disproof usually reads "The statement is false; a counterexample is $x = a$", followed by the check that $a \in X$ and that $P(a)$ fails.
The logical basis is the [[negation of a universal statement|0P3A06QNDP]]:
$$\neg \forall x \, P(x) \iff \exists x \, \neg P(x).$$
So a counterexample is a [[constructive proof|01XM7JEKHY]] of the negation.
In Lean, the tactic `push_neg` turns a goal `¬ ∀ x, P x` into `∃ x, ¬ P x`, and `use a` supplies the counterexample.

## Remarks

### What a counterexample must satisfy

Take the claim "for all positive integers $a$, $b$ and $c$, if $a \mid bc$, then $a \mid b$ or $a \mid c$".
A counterexample must make the hypothesis true and the conclusion false, so both checks are part of the disproof.
Try $a = 6$, $b = 2$ and $c = 3$.
The hypothesis holds, because $bc = 6$ and $6 \mid 6$.
The conclusion fails, because $6 \nmid 2$ and $6 \nmid 3$.
So $(6, 2, 3)$ is a counterexample.
The triple $(6, 2, 5)$ also fails the conclusion, but it is no counterexample, because $6 \nmid 10$ and the hypothesis fails.
The counterexample also tells you what a true statement needs: the claim holds when $a$ is prime, by [[Euclid's lemma|051VYKA1EX]], and $6$ is not prime.

### Counterexamples that show a hypothesis is needed

The [[intersection|0ZNMMA9TF5]] of two subgroups is always a subgroup, and many students expect the same of unions.
[[The union of two subgroups need not be a subgroup|PFKKERWYZ0]] gives the counterexample $2\mathbb{Z} \cup 3\mathbb{Z}$ in the integers: it contains $2$ and $3$ but not their sum $5$.

In analysis, the [[absolute value function|0CQ9ZM383N]] is continuous at $0$ but has no derivative there, since its difference quotient is $1$ from the right and $-1$ from the left.
That refutes "every continuous function is differentiable", and it shows that differentiability is a real extra hypothesis in many theorems.

### Smallest and simplest counterexamples

When a claim about natural numbers is false, it has a smallest counterexample, by the [[well-ordering principle|01BX15HSRR]].
A smallest counterexample is often the clearest one, and sometimes it is surprisingly large.
Goldbach conjectured that every odd composite number is a prime plus twice a nonzero square, as in $9 = 7 + 2 \cdot 1^2$ and $15 = 7 + 2 \cdot 2^2$.
The smallest counterexample is $5777 = 53 \cdot 109$, and a short computer search confirms that $5777 - 2a^2$ is not prime for any $a$ from $1$ to $53$.

Size is not the only measure of simplicity.
The claim "every prime is odd" has the one counterexample $2$, and the claim "every integer is smaller than its square" has the counterexamples $0$ and $1$.

### Disproof versus proof

One counterexample settles a universal claim, but no number of confirming cases proves it, as [[checking cases does not prove that 2^n > n^2|3K78AT7X0R]] shows.
[[Euler's sum of powers conjecture|A59Q4KDFQB]] survived for nearly two centuries before a computer search found
$$27^5 + 84^5 + 110^5 + 133^5 = 144^5.$$
A search that finds nothing proves nothing about the cases beyond the search.

Watch the form of the negation as well.
The negation of "every $x$ has property $P$" is "some $x$ fails $P$", not "no $x$ has $P$".
A counterexample to "every prime is odd" does not show that most primes are even.

### What is not a counterexample

An object that fails a hypothesis is not a counterexample.
For the claim "if $x \neq 0$, then $x^2 > 0$", the number $0$ has $0^2 = 0$, but it does not satisfy $x \neq 0$, as [[zero is not a counterexample to the positivity of squares|7681GJR0GP]] explains.
An instance where the claim holds is no counterexample either: the prime $3$ is odd, so it says nothing against "every prime is odd".
A counterexample to the converse is a third trap.
The number $9$ is odd and not prime, which refutes "every odd number is prime", but not "every prime other than $2$ is odd".

### Watch out

The most common error is to refute a different statement.
To refute "for every $\varepsilon > 0$ there is $\delta > 0$ with ...", you need one $\varepsilon$ for which every $\delta$ fails, not one pair $\varepsilon, \delta$ that fails.
So write out the negation with its quantifiers first, and then look for the object.
The second error is to believe a claim because the first cases work: Fermat's numbers above were prime for five cases in a row.

### History

Fermat believed that every number $2^{2^n} + 1$ is prime, and Euler found the factor $641$ of $2^{32} + 1$ in 1732.
The Pólya conjecture of 1919 says that for every $n > 1$, at least half of the integers from $1$ to $n$ have an odd number of prime factors counted with multiplicity.
Haselgrove disproved it in 1958, and in 1980 Tanaka found its smallest counterexample, $906150257$.
Lander and Parkin found the counterexample to Euler's conjecture in 1966.
The Mertens conjecture was disproved in 1985 by Andrew Odlyzko and Herman te Riele, whose proof shows that a counterexample exists without exhibiting one.

Collections of counterexamples became a genre of their own, with Counterexamples in Analysis by Bernard Gelbaum and John Olmsted (1964) and Counterexamples in Topology by Lynn Steen and Arthur Seebach (1970); see also the topic [[counterexamples in topology|Y642RFZPF0]].
Imre Lakatos's Proofs and Refutations (1976) describes how counterexamples lead mathematicians to revise both proofs and definitions.

### Try it

First, find a counterexample to "for all real $a$ and $b$, if $a^2 = b^2$, then $a = b$".
Take $a = 1$ and $b = -1$: the hypothesis $1 = 1$ holds and the conclusion $1 = -1$ fails.

Second, is $x = 1$ a counterexample to "for every real $x > 1$, $x^2 > x$"?
No, because $1 > 1$ is false, so $x = 1$ fails the hypothesis; in fact the claim is true, since multiplying $x > 1$ by $x > 0$ gives $x^2 > x$.

## Explanations

### L1 human

Someone says that all birds can fly.
One penguin is enough to show that this is wrong, because a penguin is a bird and it cannot fly.
In mathematics such a case is called a counterexample.
For the claim "every whole number is smaller than its square", the number $1$ is a counterexample, since $1 \times 1 = 1$ is not bigger than $1$.

### L2 human

Is $n^2 - n + 11$ prime for every natural number $n$?
Try the first values:
$$n = 0, 1, 2, 3, 4, 5 \quad \text{give} \quad 11, 11, 13, 17, 23, 31,$$
and all of these are prime, as are the values up to $n = 10$.
Now look for a value where every term has a common factor.
At $n = 11$ the terms $n^2$ and $n$ cancel to leave $11 \cdot 11$:
$$11^2 - 11 + 11 = 121 = 11 \cdot 11.$$
So $n = 11$ is a counterexample.
Check: $121 = 11^2$ is not prime.
The problem shows the usual way to hunt: test small cases, then use algebra to find a value where a factor appears.

### L3 human

In logic, a counterexample to a universal sentence is a witness in one structure, and a countermodel refutes the validity of a sentence.
By Gödel's completeness theorem, a first-order sentence that is not provable from a theory fails in some model of the theory.
Independence proofs, such as the models of non-Euclidean geometry for the parallel postulate, are counterexamples at the level of whole structures.
In constructive mathematics, a Brouwerian counterexample shows that a classical statement would imply a principle that constructive mathematics does not accept, and a [[strong counterexample|7PQ85QF58H]] goes further and proves the negation of an instance of such a principle.
Lakatos's account of "monster-barring", in which a definition is changed to exclude a counterexample, describes one way in which [[pathological objects|WMBZPYPN2D]] shape definitions.
False proofs and the search for their errors are treated in the topic [[fallacies and errors in proofs|T6QQ749DM5]].
