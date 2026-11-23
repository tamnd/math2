---
tag: KRS3VTWCHJ
kind: statement
role: theorem
name: The Heine-Borel theorem for the unit interval is equivalent to WKL0 over RCA0
msc: ["03B30", "03F35", "54D30"]
topics: [BY8AAFN7C5]
audience: grad
about: [7W9EG02T79, 7SQS69T17R]
uses: [DNXCKXZZ08, K5YPW1NTHZ, 07PFYV65MB, TQTDKMBJ0F]
sources:
  - url: https://en.wikipedia.org/wiki/Reverse_mathematics
    locator: Weak Kőnig's lemma WKL0
  - url: https://en.wikipedia.org/wiki/Heine%E2%80%93Borel_theorem
    locator: lead section
---

## Statement

The compactness of $[0, 1]$ in the form "every countable open cover has a finite subcover" needs exactly weak König's lemma over the computable base system.

A *cover* of $[0, 1]$ is a sequence $(a_n, b_n)_{n \in \mathbb{N}}$ of pairs of rationals such that every real $x \in [0, 1]$ lies in some open interval $(a_n, b_n)$.
Let $\mathrm{HB}$ be the sentence of $L_2$: for every cover of $[0, 1]$ there is $N$ such that the intervals $(a_n, b_n)$ with $n < N$ also cover $[0, 1]$.

**Theorem.** $\mathsf{RCA}_0 \vdash \mathrm{HB} \leftrightarrow \mathrm{WKL}$.

So the [[Heine-Borel theorem|07PFYV65MB]] for $[0, 1]$ is equivalent to [[WKL0|K5YPW1NTHZ]] over [[RCA0|DNXCKXZZ08]], in the sense of [[reverse mathematics|TQTDKMBJ0F]].

## Remarks

### Why each hypothesis is needed

The cover must be one sequence, given as one set of the model.
A family such as "all open intervals with some property" is not an object of $L_2$ until it is listed as a sequence, and different listings may need different amounts of comprehension.

The intervals must be open.
The closed intervals $[0, 0]$ and $[2^{-n-1}, 2^{-n}]$ for $n \in \mathbb{N}$ cover $[0, 1]$, but each finite subfamily misses the points just above $0$ that are below its smallest positive left end.

The space must be closed and bounded.
The open intervals $(2^{-n-1}, 2)$ cover $(0, 1]$, but finitely many of them have a smallest left end $2^{-N-1}$, and the point $2^{-N-2}$ is not covered.

### What it gives you

In the $\omega$-model of the computable sets $\mathrm{HB}$ fails.
There is a computable sequence of rational intervals that covers every computable real in $[0, 1]$, while the total length of the intervals is less than $1$.
No finite part of it can cover $[0, 1]$, since finitely many intervals of total length less than $1$ leave a gap, and every gap contains a rational, which is computable.

Over $\mathsf{RCA}_0$, $\mathrm{HB}$ implies that every continuous function on $[0, 1]$ is bounded, by the usual proof: the intervals where $\lvert f \rvert < n$ form a cover.
So the boundedness of continuous functions also follows from $\mathrm{WKL}$, and it is in fact equivalent to it.

### The two directions

Both directions are part of the statement, and [[the proof|G7ZWWWXD3T]] gives both.
The forward direction is the classical bisection proof, where a tree of uncovered dyadic intervals replaces the choice of a bad half.
The reversal codes a tree into the Cantor middle-thirds set, so that a finite subcover would cut off all long nodes of the tree.

### Generalizations

The same equivalence holds for countable covers of $2^{\mathbb{N}}$ by basic open sets, and for countable covers of any compact metric space by open balls, with compactness coded as in Simpson's book.
Covers by arbitrary open sets, each coded as a union of rational intervals, also give a statement equivalent to $\mathsf{WKL}_0$.

## History

Émile Borel proved the classical theorem for countable covers of a closed interval in 1895.
Its equivalence with weak König's lemma over $\mathsf{RCA}_0$ belongs to the first group of results of reverse mathematics, and Simpson's book *Subsystems of Second Order Arithmetic* (1999) presents it among the basic equivalences of $\mathsf{WKL}_0$.

## Explanations

### L1 human

The Heine-Borel theorem says that if countably many open intervals cover $[0, 1]$, then finitely many of them already cover it.
In computable mathematics this needs exactly one extra principle, weak König's lemma.
The proof turns covers into trees and trees into covers.

### L2 human

Try the forward direction on the cover $(a_0, b_0) = (-1, 0.6)$ and $(a_1, b_1) = (0.4, 2)$, followed by any other intervals.
The dyadic intervals of length $\tfrac12$ are $[0, \tfrac12]$ and $[\tfrac12, 1]$, and each lies inside one of the first two intervals.
So no node of length $2$ survives in the tree of uncovered dyadic intervals, and $N = 2$ works.
In general we keep halving until every dyadic piece of length $2^{-k}$ sits inside one of the first $k$ intervals.
Weak König's lemma guarantees that this happens at some finite $k$, because an infinite path of uncovered pieces would shrink to a point that no interval covers.
The trap is to find $N$ by an unbounded search over subcovers: the bound comes from the level where the tree stops.

### L3 human

The theorem is the prototype of the equivalences of $\mathsf{WKL}_0$: compactness of Cantor space is weak König's lemma, and compactness of other spaces reduces to it through a continuous map from Cantor space.
The same pattern gives the extreme value theorem, the uniform continuity of continuous functions on $[0, 1]$, and Gödel's completeness theorem.
Since $\mathsf{WKL}_0$ is [[Π¹₁-conservative over RCA0|8G2GVRXWG5]], every arithmetical consequence of these compactness theorems is already provable in $\mathsf{RCA}_0$.
