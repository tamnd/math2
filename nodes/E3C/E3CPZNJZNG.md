---
tag: E3CPZNJZNG
kind: statement
role: theorem
name: Completeness of the real numbers
msc: [26A03, 12J15]
uses: [0HQARMKEV5, 0AXWET80YW, 0QZMTN5AXX, 0KN22AAW5R, 0FM6N4R0VB, 0KDJD249DT]
about: [08J2M1JYAG, 0A9E6X0S3E]
sources:
  - url: https://en.wikipedia.org/wiki/Completeness_of_the_real_numbers
same_as:
  wikidata: Q1324487
  wikipedia: Completeness of the real numbers
---

## Statement

Let $F$ be an [[Archimedean ordered field|0HQARMKEV5]].
Then the following five conditions on $F$ are equivalent.

1. Each nonempty subset of $F$ that is bounded above has a supremum in $F$ (the [[least-upper-bound property|0AXWET80YW]]).
2. Each [[Cauchy sequence|0QZMTN5AXX]] in $F$ converges in $F$.
3. For each sequence of closed bounded intervals $[a_1, b_1] \supseteq [a_2, b_2] \supseteq \cdots$ in $F$, some point of $F$ lies in all of them (the [[nested intervals property|MF56GK7QY2]]).
4. Each bounded [[monotone sequence|0KN22AAW5R]] in $F$ converges in $F$.
5. Each bounded sequence in $F$ has a subsequence that converges in $F$.

The field $\R$ of [[real numbers|08J2M1JYAG]] satisfies all five conditions.

## Remarks

The standard proof goes in a cycle.
From (1), a bounded increasing sequence converges to the supremum of its terms, which gives (4).
From (4), each sequence has a monotone subsequence, which gives (5).
A Cauchy sequence is bounded, and if a subsequence converges then the whole sequence converges, so (5) gives (2).
From (2), repeated bisection between a point of a set and an upper bound gives a Cauchy sequence.
Its limit is the supremum, and the Archimedean property makes the interval lengths tend to $0$.
For (3), the left endpoints of nested closed intervals have a supremum under (1), and this supremum lies in every interval.
Conversely, (3) gives (1) by the same bisection, with the Archimedean property again making the lengths tend to $0$.
The field $\Q$ satisfies none of the conditions: the decimal approximations $1, 1.4, 1.41, 1.414, \ldots$ of $\sqrt 2$ form a Cauchy sequence with no limit in $\Q$.
The Archimedean hypothesis matters for (2): there are non-Archimedean ordered fields in which each Cauchy sequence converges, but which lack the least-upper-bound property.
Conditions (1), (4) and (5) each imply the Archimedean property by themselves.
Up to isomorphism, $\R$ is the only [[complete ordered field|0A9E6X0S3E]].

## Explanations

### L1 human

The real line has no gaps, and there are several ways to say this.
A bounded set has a least upper bound; a sequence whose terms crowd together has a limit; shrinking closed intervals always share a point.
These sound different, but each one implies the others.
The rational numbers fail all of them, because $\sqrt 2$ is missing.

### L2 human

In a course, one of the conditions is taken as an axiom or proved from a construction of $\R$, and the others follow as theorems.
Dedekind cuts give the least-upper-bound property directly, while Cauchy sequences give condition (2) directly.
The [[Bolzano–Weierstrass theorem|0KDJD249DT]] is condition (5), and the [[monotone convergence theorem|0FM6N4R0VB]] is condition (4).
The intermediate value theorem and the extreme value theorem both rest on completeness, and both fail over $\Q$.
