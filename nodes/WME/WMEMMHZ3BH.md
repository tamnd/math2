---
tag: WMEMMHZ3BH
kind: concept
name: Conjecture
aliases: [mathematical-conjecture]
msc: ["00A35"]
topics: [N4P3E53HM0]
audience: school
uses: [0B94TKFQJX, 5V35SGEN1T, KK5F0F03ZW, 0ED72CTBNP]
sources:
  - url: https://en.wikipedia.org/wiki/Conjecture
    locator: lead section
  - book: isbn:9781108439534
    locator: Introduction
---

## Summary

A conjecture is a precise mathematical statement that someone proposes as true, but that nobody has proved or disproved.
A conjecture ends in one of three ways.
A [[proof|0B94TKFQJX]] makes it a [[theorem|KK5F0F03ZW]].
A [[counterexample|0ED72CTBNP]] or another disproof shows that it is false.
A proof of independence shows that the accepted axioms cannot settle it.
Conjectures matter because they record what mathematicians expect, and they direct research toward the questions that are open.

## Motivation

Mathematicians often see a pattern before they can explain it.
For example, $4 = 2 + 2$, $6 = 3 + 3$, $8 = 3 + 5$ and $10 = 5 + 5$, and each even number that anyone tries is a sum of two primes.
The pattern is found by [[inductive reasoning|5V35SGEN1T]], and inductive reasoning does not prove a general statement.
A conjecture is the honest name for such a statement: it is stated exactly, it is supported by evidence, and it is marked as unproved.
This keeps two things apart that must stay apart, namely what we expect and what we know.

## Notation

A conjecture is often named after the person who stated it, as in [[Goldbach's conjecture|063JNBSMJ0]].
Some conjectures have other names for historical reasons.
The [[Riemann hypothesis|VCGF9YR36X]] and the [[continuum hypothesis|0MN2MER9WN]] are conjectures called "hypotheses".
[[Fermat's Last Theorem|0Y5X3SDBCZ]] was called a "theorem" for more than three hundred years before anyone proved it.
In a research paper, a statement labelled "Conjecture" is a claim that the author believes but cannot prove.
The word "hypothesis" also has a second meaning: an assumption of a theorem, as in [[hypotheses and conclusion of a theorem|W48XN2MEM9]].

## Remarks

### Examples

- [[Goldbach's conjecture|063JNBSMJ0]]: each even integer greater than $2$ is a sum of two primes. It is open, and [[small cases|51WEX891JK]] are easy to check.
- The [[twin prime conjecture|0FER36N8SB]]: there are infinitely many primes $p$ such that $p + 2$ is also prime. It is open.
- The [[Collatz conjecture|6PCQEXEX4N]]: the map $n \mapsto n/2$ for even $n$ and $n \mapsto 3n + 1$ for odd $n$ reaches $1$ from each positive integer. It is open.
- The [[Poincaré conjecture|3R064KFF68]] was stated by Henri Poincaré in 1904 and proved by Grigori Perelman in 2002 and 2003. It is now a theorem.
- [[Fermat's conjecture on Fermat numbers|VDZY463EKP]]: each number $2^{2^n} + 1$ is prime. Euler disproved it in 1732.
- The [[continuum hypothesis|0MN2MER9WN]] was shown to be independent of the usual axioms of set theory by Kurt Gödel in 1940 and Paul Cohen in 1963.

### Non-examples

- A [[vague claim|Q497S37Q6D]] such as "the prime numbers behave randomly" is not a conjecture, because it is not a precise statement.
- [[Euclid's theorem|0292EPPPT0]] that there are infinitely many primes is not a conjecture, because it has a proof.
- An open question such as "how many twin primes are there below $10^{100}$?" is not a conjecture, because it asks for a value and does not claim a statement.

### Basic properties

- A conjecture is a statement, so it is true or false in the intended structure. Its status as a conjecture is a fact about our knowledge, not about the statement.
- A universal conjecture "each $n$ has property $P$" is disproved by one counterexample. No number of confirming cases proves it.
- Evidence for a conjecture can be numerical, heuristic or structural. The [[Mertens conjecture|4Y4HWKA2MP]] held for all values that were computed, and Andrew Odlyzko and Herman te Riele disproved it in 1985.
- A conjecture can be shown to be independent of a set of axioms. Then neither it nor its negation follows from those axioms, as for the [[continuum hypothesis|0MN2MER9WN]].
- Conjectures often imply each other. A proof of one conjecture "conditional on" another is a theorem of the form "if conjecture A holds, then B holds".

### History

Many old problems were stated as conjectures long before the word was common in mathematics.
Fermat stated his "last theorem" around 1637, and Goldbach stated his conjecture in a letter to Euler in 1742.
Several famous conjectures were settled in the late twentieth and early twenty-first centuries.
The [[four colour theorem|0M406JC8J1]] was stated as a problem in 1852 and proved by Kenneth Appel and Wolfgang Haken in 1976 with the help of a computer.
Andrew Wiles proved [[Fermat's Last Theorem|0Y5X3SDBCZ]] in 1994, with a step completed jointly with Richard Taylor, and the proof appeared in 1995.
Johannes Kepler stated the [[Kepler conjecture|AFMBQT06ZV]] in 1611, and Thomas Hales announced a proof in 1998.
Some conjectures turned out false: [[Euler's sum of powers conjecture|E486QA4JS4]] was disproved by Leon Lander and Thomas Parkin in 1966 with the identity $27^5 + 84^5 + 110^5 + 133^5 = 144^5$.

### Common errors

- To treat a conjecture as known. A proof that uses an open conjecture proves only a conditional result, and it must say so.
- To take many examples as a proof. The [[Mertens conjecture|4Y4HWKA2MP]] shows that a pattern can hold for every computed case and still fail.
- To think that "hypothesis" in "Riemann hypothesis" means an assumption. Here it means a conjecture.

## Explanations

### L1 human

A conjecture is a careful guess in mathematics.
Someone notices a pattern, writes it as an exact sentence, and says "I think this is always true".
For example, $10 = 3 + 7$, $12 = 5 + 7$ and $14 = 7 + 7$, and every even number above $2$ seems to be a sum of two primes.
Nobody has proved this, so it is still a guess, called Goldbach's conjecture.
A conjecture stays a guess until someone proves it or finds a case where it fails.

### L2 human

We test a made-up conjecture: "for each positive integer $n$, the number $n^2 - n + 41$ is prime".

1. For $n = 1, 2, 3$ the values are $41$, $43$ and $47$, and these are primes.
2. For $n = 10$ the value is $100 - 10 + 41 = 131$, and $131$ is prime: it is not divisible by $2$, $3$, $5$, $7$ or $11$, and $13^2 = 169 > 131$.
3. For $n = 41$ the value is $41^2 - 41 + 41 = 41^2 = 1681$, which is not prime.
4. So $n = 41$ is a counterexample, and the conjecture is false.

The typical use of a conjecture is to organize the search: we state the guess exactly, test it, and then look for a proof or a counterexample.
In step 3 we did not search blindly: the form $n^2 - n + 41$ shows that $n = 41$ makes each term a multiple of $41$.
A trap is to stop after step 2 and believe the statement, because the first $40$ values are all prime.

### L3 human

The life of a conjecture shows the relation between evidence and proof.
Heuristic models, such as probabilistic models of the primes, predict precise statements, and computation tests them.
The [[Riemann hypothesis|VCGF9YR36X]] is supported by computations of many zeros, by its analogue for curves over finite fields, which André Weil proved, and by its many equivalent forms.
None of this evidence is a proof.
Some conjectures organize whole fields.
The [[abc conjecture|G7JH2NXPC0]] implies many results in Diophantine equations, so a large part of number theory is written as theorems conditional on it.
Independence results show a third possible end.
For the [[continuum hypothesis|0MN2MER9WN]], the question "is it true?" is no longer a question about proofs from ZFC; it became a question about which new axioms to accept.
The role of conjectures in the growth of mathematics is studied in the [[methodology of mathematics|3FJ3XMV9KD]] and in the topic on [[plausible reasoning and experimental mathematics|DME0TPC348]].
