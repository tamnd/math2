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

A conjecture is a precise guess: an exact mathematical statement that someone believes and that nobody has yet proved or disproved.
It marks the border between what mathematicians expect and what they know, and most research is aimed at that border.
A conjecture can end in three ways.
A [[proof|0B94TKFQJX]] turns it into a [[theorem|KK5F0F03ZW]].
A [[counterexample|0ED72CTBNP]] or another disproof shows that it is false.
A proof of independence shows that the accepted axioms cannot settle it either way.

## Motivation

Mathematicians often see a pattern long before they can explain it.
Look at the even numbers from $4$ on:
$$4 = 2 + 2, \quad 6 = 3 + 3, \quad 8 = 3 + 5, \quad 10 = 5 + 5, \quad 12 = 5 + 7.$$
Every even number that anyone has tried is a sum of two primes.
This is [[inductive reasoning|5V35SGEN1T]], and inductive reasoning cannot prove a statement about all even numbers.
The word "conjecture" is the honest label for such a statement: it is stated exactly, it has evidence behind it, and it is marked as unproved.
The label keeps apart two things that must stay apart, the expected and the known.

Conjectures also steer research.
A precise conjecture tells others what to try to prove and what kind of counterexample to look for.
The [[methodology of mathematics|3FJ3XMV9KD]] follows this cycle of guess, test and proof, and [[examples in mathematical practice|F3NNR77WKP]] shows how examples feed it.

## Notation

A conjecture is often named after the person who first stated it, as in [[Goldbach's conjecture|063JNBSMJ0]].
Some carry other names for historical reasons.
The [[Riemann hypothesis|VCGF9YR36X]] is a conjecture called a "hypothesis", and [[Fermat's Last Theorem|0Y5X3SDBCZ]] was called a "theorem" for more than three hundred years before anyone proved it.
In a research paper, a statement labelled "Conjecture" is one that the author believes but cannot prove.
The word "hypothesis" also has a second meaning, an assumption of a theorem, as in [[hypotheses and conclusion of a theorem|W48XN2MEM9]].

## Remarks

### Evidence without proof

Goldbach's conjecture says that each even integer greater than $2$ is a sum of two primes.
The [[table of small cases|51WEX891JK]] checks it for every even number from $4$ to $30$, and computer searches have checked it up to $4 \cdot 10^{18}$.
It is still open.
Other famous open conjectures have the same shape.
The [[twin prime conjecture|0FER36N8SB]] says that there are infinitely many primes $p$ with $p + 2$ also prime, as for $11, 13$ and $17, 19$.
The [[Collatz conjecture|6PCQEXEX4N]] says that the rule "halve $n$ if it is even, replace it by $3n + 1$ if it is odd" reaches $1$ from every positive integer.
For $n = 6$ the path is $6, 3, 10, 5, 16, 8, 4, 2, 1$.

### Three ways a conjecture ends

The [[Poincaré conjecture|3R064KFF68]] ended with a proof.
Henri Poincaré asked his question in 1904, and Grigori Perelman proved it in work posted in 2002 and 2003, so it is now a theorem.

[[Fermat's conjecture on Fermat numbers|VDZY463EKP]] ended with a counterexample.
Fermat believed that every number $F_n = 2^{2^n} + 1$ is prime, and the first five, $3, 5, 17, 257, 65537$, are prime.
Euler found that the sixth is not:
$$F_5 = 2^{32} + 1 = 4294967297 = 641 \times 6700417.$$

The [[continuum hypothesis|0MN2MER9WN]] ended with independence.
Kurt Gödel showed in 1940 that the usual axioms of set theory cannot disprove it, and Paul Cohen showed in 1963 that they cannot prove it.

### When the evidence misleads

The danger of trusting cases is not theoretical.
The polynomial $n^2 + n + 41$ is prime for every $n$ from $0$ to $39$, and [[it fails at n = 40|H75AB4EJT5]]:
$$40^2 + 40 + 41 = 40 \cdot 41 + 41 = 41^2 = 1681.$$
The Pólya conjecture says that, for every $n \ge 2$, at least half of the numbers from $1$ to $n$ have an odd number of prime factors, counted with repetition.
It fails, and the first $n$ where it fails is $906150257$.
The [[Mertens conjecture|4Y4HWKA2MP]] held for every value that was computed, and Andrew Odlyzko and Herman te Riele disproved it in 1985 without finding an explicit counterexample.
[[Euler's sum of powers conjecture|E486QA4JS4]] was refuted by Leon Lander and Thomas Parkin in 1966 with
$$27^5 + 84^5 + 110^5 + 133^5 = 144^5.$$

### What it is not

A conjecture must be a statement with a definite truth value.
A [[vague claim|Q497S37Q6D]] such as "the primes behave randomly" is not one, because it does not say which property is random, so no proof or counterexample could settle it.
[[Euclid's theorem|0292EPPPT0]] that there are infinitely many primes is not a conjecture either, because it has a proof.
A question such as "how many twin primes are there below $10^{100}$?" is not a conjecture, because it asks for a value and does not claim anything.

### Watch out

A proof that uses an open conjecture proves only a conditional result.
Many papers prove theorems of the form "if the Riemann hypothesis holds, then $B$ holds", and they say so in the statement.
Treating the conjecture as known turns such a result into a false claim of proof.

A second trap is to read the word "hypothesis" in "Riemann hypothesis" as an assumption.
There it means a conjecture.
Read the context: "under the hypothesis that $f$ is continuous" names an assumption, while "the Riemann hypothesis is open" names a conjecture.

### History

Fermat wrote his "last theorem" in the margin of a book around 1637, and Goldbach stated his conjecture in a letter to Euler in 1742.
The [[four color theorem|0M406JC8J1]] was posed as a problem in 1852 and proved by Kenneth Appel and Wolfgang Haken in 1976 with the help of a computer.
Andrew Wiles proved Fermat's Last Theorem in 1994, with one step completed jointly with Richard Taylor, and the proof appeared in 1995.
Johannes Kepler stated the [[Kepler conjecture|AFMBQT06ZV]] on the packing of spheres in 1611, and Thomas Hales announced a proof in 1998.

### Try it

First, test the conjecture "$2^n - 1$ is prime whenever $n$ is prime" for $n = 2, 3, 5, 7, 11$.
The values are $3, 7, 31, 127$ and $2047$, and $2047 = 23 \times 89$, so $n = 11$ is a counterexample.

Second, is "every large even number is a sum of two primes in many ways" a conjecture as it stands?
No, because "large" and "many" are not fixed.
It becomes a precise statement only after you name the numbers, for example "every even number above $12$ has at least two ways", and the bound $12$ is needed because $12 = 5 + 7$ has only one.

## Explanations

### L1 human

A conjecture is a careful guess in mathematics.
Someone notices a pattern, writes it as an exact sentence, and says "I think this is always true".
For example, $10 = 3 + 7$, $12 = 5 + 7$ and $14 = 7 + 7$, and every even number above $2$ seems to be a sum of two primes.
Nobody has proved this, so it is still a guess, called Goldbach's conjecture.
A conjecture stays a guess until someone proves it or finds a case where it fails.

### L2 human

Here is a typical test of a made-up conjecture: "for each positive integer $n$, the number $n^2 - n + 41$ is prime".
Start with small cases.
$$n = 1: \ 41, \qquad n = 2: \ 43, \qquad n = 3: \ 47, \qquad n = 10: \ 131.$$
All four are prime.
For $131$, no prime up to $11$ divides it, and $13^2 = 169 > 131$, so no larger prime needs testing.
Now look at the form of the expression instead of trying more cases.
At $n = 41$ every term is a multiple of $41$:
$$41^2 - 41 + 41 = 41^2 = 1681.$$
So $n = 41$ is a counterexample, and the conjecture is false.
The search was not blind, because the form $n^2 - n + 41$ points at $n = 41$.
Watch out: the values for $n = 1$ to $40$ are all prime, so a student who checks forty cases and stops would believe a false statement.

### L3 human

The life of a conjecture shows how evidence and proof relate.
Heuristic models, such as probabilistic models of the primes, predict precise statements, and computation tests them.
The [[Riemann hypothesis|VCGF9YR36X]] is supported by computations of many zeros, by its analogue for curves over finite fields, which André Weil proved, and by its many equivalent forms, and none of this is a proof.
Some conjectures organize whole fields.
The [[abc conjecture|G7JH2NXPC0]] implies many results on Diophantine equations, so a large part of number theory is written as theorems conditional on it.
Independence gives a third ending.
For the continuum hypothesis the question "is it true?" is no longer a question about proofs from ZFC, and it became a question about which new axioms to accept.
The sub-area on [[plausible reasoning and experimental mathematics|DME0TPC348]] studies how conjectures are found and weighed.
