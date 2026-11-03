---
tag: 812BY9CDMC
kind: statement
role: theorem
name: Number of rooted binary phylogenetic trees
msc: [05A15, 92B10, 05C05]
uses: [5624H8KWKK]
about: [RK58WSHJSG]
sources:
  - url: https://en.wikipedia.org/wiki/Phylogenetic_tree
---

## Statement

Let $n \ge 2$ and let $X$ be a set of $n$ taxa.
The number of rooted binary [[phylogenetic trees|5624H8KWKK]] on $X$ is
$$(2n - 3)!! = 1 \cdot 3 \cdot 5 \cdots (2n - 3).$$
For $n \ge 3$, the number of unrooted binary phylogenetic trees on $X$ is $(2n - 5)!!$.
Here $(2k - 1)!!$ denotes the product of the odd numbers from $1$ to $2k - 1$, and $1!! = (-1)!! = 1$.

## Remarks

The proof is by induction on $n$.
A rooted binary tree with $n$ leaves has $2n - 1$ vertices and $2n - 2$ edges.
Every rooted binary tree on $n + 1$ taxa arises in exactly one way from a tree on the first $n$ taxa.
One attaches the new leaf to the middle of one of the $2n - 2$ edges or above the root, which gives $2n - 1$ choices.
So the number for $n + 1$ is $(2n - 1)$ times the number for $n$, starting from $1$ tree for $n = 2$.
For the unrooted count, delete one fixed leaf of an unrooted binary tree on $n$ taxa and take its neighbour as the root.
This gives a bijection with the rooted binary trees on the other $n - 1$ taxa.
Example: for $n = 3$ there are $3$ rooted trees, $((a,b),c)$, $((a,c),b)$ and $((b,c),a)$; for $n = 4$ there are $15$, and for $n = 10$ already $34\,459\,425$.

## Explanations

### L1 human

The number of possible family trees for a set of species grows extremely fast.
Each new species can be attached to any branch of an existing tree, and the number of branches keeps growing.
With $20$ species there are more than $10^{21}$ rooted trees, so no computer can check them all.

### L2 human

This count explains why phylogenetic inference relies on heuristics and on clever algorithms rather than exhaustive search.
The same numbers count perfect matchings of $2n - 2$ points and several other families of objects, through explicit bijections.
