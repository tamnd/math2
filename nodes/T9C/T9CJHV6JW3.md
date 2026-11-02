---
tag: T9CJHV6JW3
kind: statement
role: theorem
name: Szpilrajn extension theorem
msc: [06A05, 06A06, "03E25"]
uses: [0QV2JS9RJ3, 0FRXBVVR03, W8DZ5KGGHN, 04RXTQA5ZA]
about: [W8DZ5KGGHN]
sources:
  - url: https://en.wikipedia.org/wiki/Szpilrajn_extension_theorem
same_as:
  wikidata: Q869647
  wikipedia: Szpilrajn extension theorem
---

## Statement

Let $X$ be a set and let $\le$ be a [[partial order|0QV2JS9RJ3]] on $X$.
Then there is a [[total order|0FRXBVVR03]] $\preceq$ on $X$ such that $x \le y$ implies $x \preceq y$ for all $x, y \in X$.
In other words, every partial order has a [[linear extension|W8DZ5KGGHN]].

## Remarks

For a finite set, take a minimal element of $X$, put it first, and repeat with the remaining elements; this is topological sorting.
For an infinite set, apply [[Zorn's lemma|04RXTQA5ZA]] to the set of partial orders on $X$ that contain $\le$, ordered by inclusion.
A maximal such order is total: if $a$ and $b$ were incomparable in it, adding the pairs $(u, v)$ with $u \preceq a$ and $b \preceq v$ would give a strictly larger partial order.
The same argument shows more: if $a$ and $b$ are incomparable for $\le$, then some linear extension puts $a$ before $b$.
Hence $\le$ is the intersection of all its linear extensions.
Example: the divisibility order on $\set{1, 2, 3, 6}$ has the linear extensions $1, 2, 3, 6$ and $1, 3, 2, 6$, and $2$ and $3$ are incomparable because they appear in both relative orders.

## Explanations

### L1 human

A partial order says that some things come before others, but leaves some pairs undecided.
The theorem says that one can always decide the remaining pairs and line up all the elements in one row without breaking any of the given rules.
For a list of tasks with prerequisites, this is a schedule that does the tasks one at a time.

### L2 human

The theorem is what makes the order dimension of a poset well defined: the set of all linear extensions realizes the order.
For finite posets the proof is an algorithm, and counting the linear extensions is a central problem of order combinatorics.
For infinite sets the proof uses the axiom of choice through Zorn's lemma.
