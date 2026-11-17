---
tag: 3P2J5NWCM1
kind: statement
role: theorem
name: König's lemma is equivalent to ACA0 over RCA0
msc: ["03B30", "03F35", "05C05"]
topics: [BY8AAFN7C5]
audience: grad
about: [NAASTN80QN, 7SQS69T17R]
uses: [DNXCKXZZ08, K9XG0Z2N9V, 3MQ39PRCYJ, K5YPW1NTHZ, TQTDKMBJ0F]
sources:
  - url: https://en.wikipedia.org/wiki/K%C5%91nig%27s_lemma
    locator: Computability aspects
  - url: https://en.wikipedia.org/wiki/Reverse_mathematics
    locator: Arithmetical comprehension ACA0
---

## Statement

A *tree* is a set $T \subseteq \N^{<\N}$ closed under initial segments.
It is *finitely branching* if for every $\sigma \in T$ there is $b$ such that $\sigma v \in T$ implies $v < b$.
A *path* through $T$ is a function $g \colon \N \to \N$ with $g {\restriction} k \in T$ for all $k$.

Let $\mathrm{KL}$ be the sentence: every infinite finitely branching tree has a path.
Then $\mathsf{RCA}_0 \vdash \mathrm{KL} \leftrightarrow \mathsf{ACA}_0$.
So König's lemma is equivalent to [[ACA0|K9XG0Z2N9V]] over [[RCA0|DNXCKXZZ08]], in the sense of [[reverse mathematics|TQTDKMBJ0F]].

## Remarks

### Why each hypothesis is needed

- Finite branching is needed. The tree of all sequences $\langle \rangle$ and $\langle n, 0, 0, \ldots, 0 \rangle$ with $k$ zeros, $k < n$, is infinite with only finite branches.
- The bound $b$ is not given as a function of $\sigma$. If a bounding function is part of the data, the statement is equivalent to [[weak König's lemma|K5YPW1NTHZ]], not to $\mathsf{ACA}_0$.

### Consequences

- $\mathsf{ACA}_0$ proves weak König's lemma, so it contains $\mathsf{WKL}_0$.
- König's lemma for trees in which every node has at most two immediate successors, with labels from $\N$, is already equivalent to $\mathsf{ACA}_0$, as the reversal shows.

### Converse

Both directions are part of the statement.

### Generalizations

The same equivalence holds for finitely branching trees of finite sequences from any countable set, after coding the set by natural numbers.
Without finite branching the statement is false, by the example above.

## Explanations

### L1 human

König's lemma says: if a tree has infinitely many nodes and each node has finitely many children, then there is an infinite branch.
The classical proof always moves to a child that has infinitely many nodes below it.
Deciding which children have this property needs arithmetical comprehension.

### L2 human

The reversal builds a tree whose only path codes the range of a one-to-one function $f$.
At level $i$ the tree guesses whether $i$ is in the range, and if so, which $j$ has $f(j) = i$; a wrong guess dies at a finite level.
The trap is the bound on branching: when the bound is computable, the principle is only weak König's lemma.
