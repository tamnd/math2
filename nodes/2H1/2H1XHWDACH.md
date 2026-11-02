---
tag: 2H1XHWDACH
kind: statement
role: theorem
name: Garden of Eden theorem
msc: [37B15, 68Q80]
uses: [2CM2MC5HQ6, 5QXNC6NTVN]
about: [5QXNC6NTVN]
sources:
  - url: https://en.wikipedia.org/wiki/Garden_of_Eden_(cellular_automaton)
same_as:
  wikidata: Q1974793
  wikipedia: Garden of Eden (cellular automaton)
---

## Statement

Let $A$ be a finite set, let $d \ge 1$, and let $F \colon A^{\Z^d} \to A^{\Z^d}$ be a [[cellular automaton|5QXNC6NTVN]].
Call two configurations $x, y$ asymptotic if they differ at only finitely many sites.
Call $F$ pre-injective if $F(x) \ne F(y)$ for all asymptotic configurations $x \ne y$.
Then $F$ is surjective if and only if $F$ is pre-injective.

## Remarks

A configuration outside the image of $F$ is called a Garden of Eden: it has no predecessor.
So the theorem says that a Garden of Eden exists exactly when two configurations that differ at finitely many sites have the same image.
The proof compares counts: in a large box of side $n$, the number of patterns grows like $\abs{A}^{n^d}$, while the boundary of the box has only about $n^{d-1}$ sites.
A missing pattern, or a pair of patterns with the same image, changes the exponential count by a factor that the boundary cannot compensate.
The theorem is due to Moore and Myhill.
Example: rule 90 in one dimension is surjective, so it is pre-injective.
It is not injective, since the all-$0$ and the all-$1$ configurations both map to the all-$0$ configuration, but these are not asymptotic.
Conway's Game of Life is not surjective: it has Garden of Eden configurations.
The theorem extends to cellular automata on amenable groups, and it fails for the free group on two generators.

## Explanations

### L1 human

A Garden of Eden is a picture that a cellular automaton can never produce, because nothing can lead to it.
The theorem says that such pictures exist exactly when the automaton loses information in a finite region.
Losing information means that two different finite changes of a picture give the same next picture.
So counting how much information is lost tells whether every picture can be reached.

### L2 human

Injective implies pre-injective, so every injective cellular automaton on $\Z^d$ is surjective.
This is a dynamical analogue of the fact that an injective map of a finite set to itself is onto.
The theorem is often used to show that a rule has Garden of Eden patterns by exhibiting two mutually erasable patterns.
Its extension to amenable groups by Ceccherini-Silberstein, Machì and Scarabotti links it to [[amenable group actions|ZCG4DJ7GH3]].
For the free group of rank two there are surjective cellular automata that are not pre-injective.
