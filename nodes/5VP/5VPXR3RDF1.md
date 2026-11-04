---
tag: 5VPXR3RDF1
kind: statement
role: theorem
name: Mirsky's theorem
msc: [06A07]
uses: [0QV2JS9RJ3, 0S8FE7ZMFM, 03HF498P1J, MPR6MH4YSQ]
about: [0S8FE7ZMFM, 03HF498P1J, MPR6MH4YSQ]
sources:
  - url: https://en.wikipedia.org/wiki/Mirsky's_theorem
  - url: https://github.com/mitchkeller/applied-combinatorics/blob/ebd95d6bd59e23c633c65cf560bcb93efa912aae/source/s_posets_dilworth.ptx#L25
    locator: source/s_posets_dilworth.ptx:25
same_as:
  wikidata: Q6874717
  wikipedia: Mirsky's theorem
---

## Statement

Let $(P, \le)$ be a finite [[partially ordered set|0QV2JS9RJ3]].
Let $h$ be the largest number of elements of a [[chain|0S8FE7ZMFM]] in $P$, that is, the [[height|MPR6MH4YSQ]] of $P$.
Then $P$ is the union of $h$ pairwise disjoint [[antichains|03HF498P1J]], and $P$ is not the union of fewer than $h$ antichains.

## Remarks

A chain meets an antichain in at most one element, so a chain with $h$ elements needs $h$ different antichains to cover it.
For the other half, let $f(x)$ be the largest number of elements of a chain whose greatest element is $x$.
If $x < y$, then a chain ending at $x$ extends by $y$, so $f(x) < f(y)$.
Thus each level set $\set{x \in P : f(x) = k}$ is an antichain, and the values of $f$ are $1, \ldots, h$.
Example: in the divisors of $12$ ordered by divisibility, the chain $1, 2, 4, 12$ has $4$ elements, and the levels $\set{1}$, $\set{2, 3}$, $\set{4, 6}$, $\set{12}$ are $4$ antichains that cover the set.
The same proof works for an infinite partially ordered set of finite height.
The theorem is the dual of [[Dilworth's theorem|GT224XDA4E]], which exchanges the roles of chains and antichains, but its proof is much easier.

## Explanations

### L1 human

Think of the elements as tasks, where $x < y$ means that $x$ must be done before $y$.
An antichain is a set of tasks that can be done in the same round.
The theorem says that the least number of rounds equals the length of the longest sequence of tasks that must be done one after the other.

### L2 human

The proof gives an explicit partition: put each element into the level given by the longest chain that ends at it.
This is the layering used in scheduling and in drawing directed acyclic graphs.
In the language of graphs, the comparability graph of a poset has chromatic number equal to its clique number.
The same holds for each induced subgraph, so comparability graphs are perfect.
Together with Dilworth's theorem it gives the [[Erdős–Szekeres theorem|0SNJM8HSD3]] on monotone subsequences.
