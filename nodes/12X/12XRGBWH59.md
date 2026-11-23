---
tag: 12XRGBWH59
kind: statement
role: theorem
name: Friedman's finite form of Kruskal's theorem
msc: ["03F35", "05C05", "06A07"]
topics: [T6FK1E7GJ1]
audience: grad
uses: [XVHKCX4F5Y, 0C9J6W2A8A, NH25G6GC07, DC60FYCSPM, 6QFEVWKE25, C72RBH0CDR]
about: [XVHKCX4F5Y, DC60FYCSPM]
history:
  notes: "Harvey Friedman found in the early 1980s that the finite form is unprovable in ATR0; the result appeared in Simpson's 1985 paper 'Nonprovability of certain combinatorial properties of finite trees'."
sources:
  - url: https://en.wikipedia.org/wiki/Kruskal's_tree_theorem
    locator: Friedman's work
  - url: https://en.wikipedia.org/wiki/Kruskal's_tree_theorem
    locator: Weak tree function
  - url: https://en.wikipedia.org/wiki/Kruskal's_tree_theorem
    locator: TREE function
---

## Statement

If the first tree of a list has $3$ vertices and each later tree has one vertex more, then by the third tree some tree contains an earlier one.
The theorem says that such a bound exists for every starting size, and $\mathsf{ATR}_0$ cannot prove it.

For finite [[rooted trees|0C9J6W2A8A]] $T$ and $T'$, write $T \le T'$ if $T$ embeds in $T'$ as in [[Kruskal's tree theorem|XVHKCX4F5Y]]: by an injective map that preserves the order of ancestors and the infimum of any two vertices.
For $n \ge 0$, let $P(n)$ be the following sentence.
There is $m$ such that for every sequence $T_1, \dots, T_m$ of finite rooted trees, where $T_i$ has $i + n$ vertices, there are $i < j$ with $T_i \le T_j$.

**Theorem** (Friedman).

1. $P(n)$ holds for every $n$.
2. The sentence $\forall n\, P(n)$, written in arithmetic, is not provable in $\mathsf{ATR}_0$, the subsystem of [[second-order arithmetic|DC60FYCSPM]] with arithmetical transfinite recursion.
3. $\forall n\, P(n)$ is provable in $\Pi^1_1\text{-}\mathsf{CA}_0$, the subsystem with $\Pi^1_1$ comprehension.

The [[proof|T9YXK7VPYG]] derives part 1 from Kruskal's theorem by a tree argument, and it outlines part 2 with the cited lemmas marked.

## Remarks

### A first case by hand

A sequence is *bad* if no tree embeds in a later one.
We find the least $m$ for $P(2)$, where $T_1$ has $3$ vertices, $T_2$ has $4$ and $T_3$ has $5$.
There are two rooted trees with $3$ vertices: the path $P_3$, and the root with two leaves, which we call $V$.
A tree contains $P_3$ when it has a chain of three vertices, each the parent of the next, and it contains $V$ when some vertex has two children.

If $T_1 = V$, then $T_2$ has no vertex with two children, so $T_2$ is the path $P_4$.
Every tree $T_3$ with $5$ vertices either has a vertex with two children, and contains $V$, or is the path $P_5$, and contains $P_4$.
If $T_1 = P_3$, then $T_2$ has no chain of three vertices, so it is the root with three leaves.
Then $T_3$ is the root with four leaves, and it contains $T_2$.
So the bad sequence $V, P_4$ has length $2$, no bad sequence has length $3$, and the least $m$ for $P(2)$ is $3$.

### Labels and the function TREE

Now let the trees carry labels from a set of $k$ labels, with $T_i$ of at most $i$ vertices, and let embeddings keep labels.
$\mathrm{TREE}(k)$ is the greatest length of a bad sequence.
With one label, $T_1$ is a single vertex and it embeds in every later tree, so $\mathrm{TREE}(1) = 1$.

With labels $a$ and $b$, say $T_1$ is the vertex $a$.
Then every later tree uses only $b$.
If $T_2$ is the single vertex $b$, nothing can follow, so take $T_2$ to be the edge $b - b$.
Then $T_3$ has at most $3$ vertices, all labeled $b$, and no edge, so $T_3$ is the single vertex $b$.
Every $T_4$ contains the vertex $a$ or the vertex $b$, so $\mathrm{TREE}(2) = 3$.
The value $\mathrm{TREE}(3)$ is finite by Kruskal's theorem, and it is far too large to write in any ordinary notation.

### Why each hypothesis is needed

The theory in part 2 is $\mathsf{ATR}_0$, which is much stronger than [[Peano arithmetic|MPSCREYC3M]].
The stronger theory $\Pi^1_1\text{-}\mathsf{CA}_0$ proves the statement.

The size bound $i + n$ is needed.
Without it, the stars with $m, m - 1, \dots, 1$ leaves form a bad sequence of length $m$, for every $m$, because a star never embeds in a star with fewer leaves.

The quantifier over $n$ matters too.
Each fixed instance $P(n)$ is a true $\Sigma_1$ sentence, so even $\mathsf{PA}$ proves it by checking a finite computation.
The unprovable sentence is $\forall n\, P(n)$.

### What it gives you

For $n = 0$ the least $m$ is $2$, because $T_1$ is the one-vertex tree and it embeds in every tree.
For $n = 1$ the least $m$ is also $2$, because $T_1$ is the edge and every tree with $3$ vertices contains an edge.
For $n = 2$ it is $3$, by the case above.
The least $m$, as a function of $n$, is total by part 1, and by part 2 it is not provably total in $\mathsf{ATR}_0$.

The converse question asks whether $\mathsf{ATR}_0$ proves the negation.
It does not, because $\forall n\, P(n)$ is true and $\mathsf{ATR}_0$ proves only true arithmetic sentences.

### Generalizations

The *weak tree function* $\mathrm{tree}(n)$ is the greatest length of a bad sequence of unlabeled trees where $T_i$ has at most $i + n$ vertices.
Its first values are $\mathrm{tree}(1) = 2$ and $\mathrm{tree}(2) = 5$.
For $n = 2$ one bad sequence of length $5$ is the path $P_3$, the root with three leaves, the root with two leaves, the edge, and the single vertex.

With Friedman's gap condition on the labels, the finite form is not provable even in $\Pi^1_1\text{-}\mathsf{CA}_0$.
The [[unprovability of the graph minor theorem|WXNTPQGJ38]] goes through this stronger form.

### Watch out

The embedding is not the subgraph relation.
It may stretch an edge into a path, so the path $P_3$ embeds in the path $P_5$, and the root with two leaves embeds in every tree with a vertex of two children.
It must also keep infima: the root with two leaves does not embed in a path, even a long one.

### Try it

First, show that the least $m$ for $P(1)$ is $2$.
The tree $T_1$ has $2$ vertices, so it is an edge, and every $T_2$ with $3$ vertices contains an edge.

Second, show that $\mathrm{tree}(1) = 2$.
If $T_1$ is a single vertex, nothing follows; if $T_1$ is the edge, then $T_2$ is the single vertex, and no $T_3$ avoids both.

## History

Joseph Kruskal proved the tree theorem in 1960.
Harvey Friedman found in the early 1980s that its finite form is unprovable in $\mathsf{ATR}_0$, and the result appeared in a 1985 paper of Stephen Simpson.
Friedman also showed that the form with the gap condition is unprovable in $\Pi^1_1\text{-}\mathsf{CA}_0$.

## Explanations

### L1 human

Write down trees one by one, where the first tree is small and each later tree may have one more vertex.
Kruskal's theorem says that some tree will always contain an earlier one.
Friedman's version asks how long a list can be before this happens.
The answer is always finite, but it grows so fast that strong systems of axioms cannot prove that it exists for every starting size.

### L2 human

We check the bad sequence of length $5$ for $\mathrm{tree}(2)$, where $T_i$ may have up to $i + 2$ vertices.
The tree $T_1 = P_3$ has $3$ vertices, so every later tree must have height at most $1$, that is, a root with some leaves.
We take $T_2$ to be the root with three leaves, and $T_3$ the root with two leaves, which avoids $T_2$ because it has fewer leaves.
$T_4$ must avoid the root with two leaves, and we take the edge.
$T_5$ must avoid the edge, so it is the single vertex.
No $T_6$ avoids the single vertex.

The pattern is typical: a bad sequence starts with a tree that forbids a shape, and each later tree uses up a smaller shape.
The size bound is what keeps the sequence finite, and Kruskal's theorem is what makes the bound exist.

### L3 human

The proof-theoretic strength comes from ordinals: finite trees code ordinal terms built with the [[Veblen functions|6QFEVWKE25]], and embedding of trees implies the order of the ordinals.
So a slowly descending sequence of ordinal terms gives a bad sequence of trees.
The [[proof-theoretic ordinal|C72RBH0CDR]] of $\mathsf{ATR}_0$ is the Feferman-Schütte ordinal $\Gamma_0$, so $\mathsf{ATR}_0$ cannot follow this descent.
This is the basic example of a miniaturization: a $\Pi^1_1$ theorem about infinite sequences becomes a $\Pi^0_2$ theorem about finite ones.
