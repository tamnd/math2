---
tag: BQTM3PBQC9
kind: definition
name: Algebra of sets
msc: [28A05]
defines: PFMGZ7988V
uses: [0SJ3RX9TXA, 0BC7KX51Z8, 0B1FSS1VZW, 07KVB4JSC7, KWE1DBMN9B, 04WSW8T3SY]
sources:
  - url: https://en.wikipedia.org/wiki/Field_of_sets
---

## Definition

Let $X$ be a [[set|0SJ3RX9TXA]].
An *algebra of sets* on $X$ is a subset $\mathcal{A}$ of the [[power set|0BC7KX51Z8]] of $X$ such that:

1. $X \in \mathcal{A}$.
2. If $A \in \mathcal{A}$, then its [[complement|0B1FSS1VZW]] $X \setminus A$ is in $\mathcal{A}$.
3. If $A, B \in \mathcal{A}$, then the [[union|07KVB4JSC7]] $A \cup B$ is in $\mathcal{A}$.

## Remarks

On $X = \N$, the family $\mathcal{A}$ of the subsets $A$ such that $A$ is finite or $\N \setminus A$ is finite is an algebra.
Clause 1 holds since $\N \setminus \N = \varnothing$ is finite.
Clause 2 holds since the condition is symmetric in $A$ and $\N \setminus A$.
Clause 3 holds since a union of two finite sets is finite, and a union that contains a set with finite complement has finite complement.
This algebra is not a [[σ-algebra|04WSW8T3SY]]: the set of even numbers is a countable union of singletons, but neither it nor its complement is finite.
The family of all finite subsets of $\N$ is not an algebra, since clause 1 fails: $\N$ is not finite.
An algebra contains $\varnothing$ and is closed under finite intersections and differences, by De Morgan's laws.
So an algebra of sets is exactly a [[ring of sets|KWE1DBMN9B]] that contains $X$.
The name *field of sets* is also common.
