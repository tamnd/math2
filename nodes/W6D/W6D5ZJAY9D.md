---
tag: W6D5ZJAY9D
kind: statement
role: theorem
name: Tennenbaum's theorem
msc: [03C62, 03H15, 03C57]
uses: [0QFT7Z76N5, MVCH6N9SNW, KZSB5E471K, 01TQB88H4C]
about: [MVCH6N9SNW]
sources:
  - url: https://en.wikipedia.org/wiki/Tennenbaum's_theorem
same_as:
  wikidata: Q2226803
  wikipedia: Tennenbaum's theorem
---

## Statement

Let $M = (\N, 0^M, S^M, \oplus, \otimes)$ be a [[model|MVCH6N9SNW]] of the [[Peano axioms|0QFT7Z76N5]] $\mathsf{PA}$ whose domain is $\N$, and suppose $M$ is not isomorphic to the standard model.
Then neither $\oplus \colon \N^2 \to \N$ nor $\otimes \colon \N^2 \to \N$ is a [[computable function|KZSB5E471K]].
In particular, no [[countable|01TQB88H4C]] non-standard model of $\mathsf{PA}$ is computable.

## Remarks

Proof idea: take two computably enumerable sets $A$ and $B$ that are disjoint but cannot be separated by any computable set.
Let $p_n$ be the $n$-th prime.
Using coding of finite sets inside $M$ and overspill, one finds an element $c$ of $M$ such that $X = \set{n \in \N : M \models p_n \mid c}$ satisfies $A \subseteq X$ and $X \cap B = \emptyset$.
Suppose $\oplus$ is computable.
For a standard number $p_n$, the product of $p_n$ and $q$ in $M$ is the sum of $p_n$ copies of $q$, so it is computable from $q$.
In $M$ there are unique $q$ and $r < p_n$ with $c = p_n q + r$, and $r$ is standard, so a search for $q$ and $r$ finds them and decides whether $p_n$ divides $c$.
Then $X$ would be a computable set separating $A$ and $B$, a contradiction.
The case of $\otimes$ needs a further argument.

The theorem uses that the model is non-standard: the standard model $\N$ has computable addition and multiplication.

## Explanations

### L1 human

The natural numbers can be built on a computer: addition and multiplication are computable.
Other models of the axioms of arithmetic exist, but none of them can be built on a computer in this way.
So among the countable models of arithmetic, the standard one is the only one that is computable.

### L2 human

The theorem gives a computational characterization of the standard model among countable [[non-standard models of arithmetic|1QWN5CV4CG]].
It contrasts with weaker theories: for Presburger arithmetic, or for Robinson arithmetic $\mathsf{Q}$, there are computable non-standard models.
