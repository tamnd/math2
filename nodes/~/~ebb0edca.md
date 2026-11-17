---
tag: ~ebb0edca
kind: statement
role: theorem
name: The Heine-Borel theorem for the unit interval is equivalent to WKL0 over RCA0
msc: ["03B30", "03F35", "54D30"]
topics: [BY8AAFN7C5]
audience: grad
about: [~e7c6fa0e, 7SQS69T17R]
uses: [~59f891e2, ~b501e994, 07PFYV65MB, TQTDKMBJ0F]
sources:
  - url: https://en.wikipedia.org/wiki/Reverse_mathematics
    locator: Weak Kőnig's lemma WKL0
  - url: https://en.wikipedia.org/wiki/Heine%E2%80%93Borel_theorem
    locator: lead section
---

## Statement

A *cover* of $[0, 1]$ is a sequence $(a_n, b_n)_{n \in \N}$ of pairs of rationals such that every real $x \in [0, 1]$ lies in some open interval $(a_n, b_n)$.
Let $\mathrm{HB}$ be the sentence of $L_2$: for every cover of $[0, 1]$ there is $N$ such that the intervals $(a_n, b_n)$ with $n < N$ also cover $[0, 1]$.

Then $\mathsf{RCA}_0 \vdash \mathrm{HB} \leftrightarrow \mathrm{WKL}$.
So $\mathrm{HB}$ is equivalent to [[WKL0|~b501e994]] over [[RCA0|~59f891e2]], in the sense of [[reverse mathematics|TQTDKMBJ0F]].

## Remarks

### Why each hypothesis is needed

- The cover must be a sequence, given as one set. A cover by "all open intervals with some property" is not an object of $L_2$ unless it is coded as a sequence.
- The intervals are open. Closed intervals $[a_n, b_n]$ can cover $[0, 1]$ without a finite subcover, for example $[0, 0]$ together with $[2^{-n-1}, 2^{-n}]$ for all $n$.
- The space is $[0, 1]$. The open cover of $(0, 1]$ by the intervals $(2^{-n-1}, 2)$ has no finite subcover.

### Consequences

- In the $\omega$-model of the computable sets, $\mathrm{HB}$ fails: there is a computable sequence of rational intervals that covers every computable real in $[0, 1]$ with total length less than $1$.
- Over $\mathsf{RCA}_0$, $\mathrm{HB}$ implies that every continuous function on $[0, 1]$ is bounded, by the usual proof.

### Converse

Both directions are part of the statement.
The forward direction is the classical proof of the [[Heine-Borel theorem|07PFYV65MB]] by bisection, done with a tree.
The reversal uses a cover built from the Cantor middle-thirds intervals.

### Generalizations

The same equivalence holds for countable covers of any compact separable metric space by open balls, and for Cantor space $2^\N$ with covers by basic open sets.
The version with covers by arbitrary open sets, coded as unions of rational intervals, is also equivalent to $\mathsf{WKL}_0$.

## Explanations

### L1 human

The Heine-Borel theorem says that if countably many open intervals cover $[0, 1]$, then finitely many of them already cover it.
In the theory of computable mathematics this needs exactly one extra principle: weak König's lemma.
The proof turns covers into trees and trees into covers.

### L2 human

The forward proof builds the tree of dyadic intervals that are not yet covered by an early interval of the cover.
A path would give a point of $[0, 1]$ that the cover misses, so the tree is finite, and the level where it stops gives the finite subcover.
The reversal builds, from a tree with no path, a cover of $[0, 1]$ by intervals around the Cantor intervals of nodes outside the tree, together with the middle-third gaps.
A trap in the forward direction is to choose the subcover with an unbounded search: the bound $N$ comes from the length where the tree stops.
