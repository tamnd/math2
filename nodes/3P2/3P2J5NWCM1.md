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

König's lemma for trees in which each node has finitely many children needs the full strength of arithmetical comprehension, while the same lemma for binary trees is only weak König's lemma.

A *tree* is a set $T \subseteq \mathbb{N}^{<\mathbb{N}}$ of finite sequences that is closed under initial segments.
It is *finitely branching* when for every $\sigma \in T$ there is a number $b$ such that $\sigma v \in T$ implies $v < b$.
A *path* through $T$ is a function $g \colon \mathbb{N} \to \mathbb{N}$ with $g {\restriction} k \in T$ for all $k$.
Let $\mathrm{KL}$ be the sentence: every infinite finitely branching tree has a path.

**Theorem.** $\mathsf{RCA}_0 \vdash \mathrm{KL} \leftrightarrow \mathsf{ACA}_0$.

So König's lemma is equivalent to [[ACA0|K9XG0Z2N9V]] over [[RCA0|DNXCKXZZ08]], in the sense of [[reverse mathematics|TQTDKMBJ0F]].

## Remarks

### Why finite branching is needed

Without finite branching the lemma is false.
Take the tree that consists of $\langle \rangle$ and, for each $n \ge 1$ and $k < n$, the sequence $\langle n, 0, \ldots, 0 \rangle$ with $k$ zeros.
It is infinite, but each branch that starts with $n$ stops after $n$ entries, so it has no path.
The root has infinitely many children, and that is the condition that fails.

### Why the bound is the whole story

In the definition, the bound $b$ for the children of $\sigma$ exists, but it is not given as a function of $\sigma$.
If a bounding function $h$ with $\sigma v \in T \to v < h(\sigma)$ is part of the data, the statement is equivalent to [[weak König's lemma|K5YPW1NTHZ]] and not to $\mathsf{ACA}_0$.
With a bound in hand, the tree can be recoded as a binary tree, by writing each $v < h(\sigma)$ as a block of binary digits.
Without the bound we cannot even tell when we have seen all children of a node.

### What it gives you

$\mathsf{ACA}_0$ proves weak König's lemma, because every binary tree is finitely branching with bound $2$.
So $\mathsf{ACA}_0$ contains $\mathsf{WKL}_0$, and the [[low model|8B045KSKW5]] shows that the inclusion is strict.
The reversal in [[the proof|TTQ4KWMKMP]] uses a tree in which every node has at most two children, the child $0$ and possibly one child $j + 1$.
So even König's lemma for trees with at most two children per node, with labels from $\mathbb{N}$, implies $\mathsf{ACA}_0$.
The point is again that we do not know which labels the children carry.

### The converse

Both directions are part of the statement.
The forward direction is the classical proof that always steps to a child with infinitely many nodes above it.
The reversal builds, from a one-to-one function $f$, a tree whose only path codes the range of $f$, and then applies the [[range lemma|3MQ39PRCYJ]].

### Generalizations

The same equivalence holds for finitely branching trees of finite sequences from any countable set, after coding the set by natural numbers.
It also holds for the graph form of the lemma: every infinite, connected, locally finite graph contains an infinite simple path.

## History

Dénes Kőnig published the lemma in 1927, in his work on infinite graphs.
Its equivalence with $\mathsf{ACA}_0$ over $\mathsf{RCA}_0$ is one of the basic results of reverse mathematics in Simpson's book *Subsystems of Second Order Arithmetic* (1999).

## Explanations

### L1 human

König's lemma says: if a tree has infinitely many nodes and each node has finitely many children, then there is an infinite branch.
The classical proof always moves to a child that has infinitely many nodes above it.
Deciding which children have this property is like deciding whether a program halts.
That is why the lemma needs arithmetical comprehension and is not true in computable mathematics.

### L2 human

The reversal builds a tree whose only path codes the range of a one-to-one $f$.
Say $f(0) = 2$, $f(1) = 0$, and no other value is below $3$.
At level $i$ the tree guesses whether $i$ is in the range, and if so, which $j$ has $f(j) = i$: entry $0$ means "no", and entry $j + 1$ means "$f(j) = i$".
So the path begins $\langle 2, 0, 1 \rangle$: $0$ is $f(1)$, $1$ is not a value, and $2$ is $f(0)$.
A wrong guess "no" for a value of $f$ dies at a finite level, when the preimage appears, and a wrong guess $j + 1$ dies at once.
The trap is the bound on branching: when a computable bound is given, the principle is only weak König's lemma.

### L3 human

The difference between König's lemma and weak König's lemma is a difference of Turing degree.
Every infinite computable finitely branching tree has a path computable from $\emptyset''$, and the tree in the reversal has a single path, which computes $\emptyset'$.
In contrast, every infinite computable binary tree has a low path, which does not compute $\emptyset'$.
In the [[reverse mathematics zoo|E3X5B175ZR]], many principles are measured against these two levels.
