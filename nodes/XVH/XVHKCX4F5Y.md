---
tag: XVHKCX4F5Y
kind: statement
role: theorem
name: Kruskal's tree theorem
msc: [05C05, 06A07]
uses: [0C9J6W2A8A]
about: [0C9J6W2A8A]
sources:
  - url: https://en.wikipedia.org/wiki/Kruskal's_tree_theorem
same_as:
  wikidata: Q3527100
  wikipedia: Kruskal's tree theorem
---

## Statement

For finite [[rooted trees|0C9J6W2A8A]] $T$ and $T'$, write $u \wedge v$ for the nearest common ancestor of vertices $u, v$ of $T$.
Say that $T$ embeds in $T'$ if some injective map $f$ from the vertices of $T$ to those of $T'$ satisfies $f(u \wedge v) = f(u) \wedge f(v)$ for all $u, v$.
Then the finite rooted trees are well-quasi-ordered by embedding.
That is, for every infinite sequence $T_1, T_2, T_3, \dots$ of finite rooted trees, there are indices $i < j$ such that $T_i$ embeds in $T_j$.

## Remarks

The labelled form also holds.
Let the vertices carry labels from a well-quasi-ordered set $(X, \le)$, and ask also that each label of $T$ is at most the label of its image.
Then the trees are still well-quasi-ordered.
Joseph Kruskal proved the theorem in 1960, and Crispin Nash-Williams gave a short proof by the minimal bad sequence argument.
That argument takes a bad sequence whose trees are as small as possible at each step.
It then applies Higman's lemma to the sets of subtrees at the roots to reach a contradiction.
Harvey Friedman showed that a finite form of the theorem, although true, is not provable in the subsystem $\mathrm{ATR}_0$ of second-order arithmetic.
The [[Robertson–Seymour theorem|WP3GDNWJJW]] on graph minors builds on its methods.

## Explanations

### L1 human

Write down an endless list of finite trees.
The theorem says that, no matter how you choose them, some tree in the list will be contained, in a branch-preserving way, in a later tree.
You cannot keep producing trees that avoid all earlier ones.

### L2 human

The theorem is a basic example of a well-quasi-order on structured objects, after Higman's lemma for finite words.
It is used in term rewriting to prove that certain orderings, such as recursive path orderings, are well-founded.
Its finite form grows so fast that it escapes strong formal systems, which makes it a standard example in proof theory.
