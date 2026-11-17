---
tag: B2D8PTFNN1
kind: concept
name: Induction on size
aliases: [induction-on-the-size, induction-on-the-number-of-vertices, induction-on-the-dimension]
msc: ["00A35", "05C99"]
topics: [EEH2F76CYQ, G9JFJGY4TQ]
audience: ug1
uses: [0ASJVEFA9J, 0KMVFSHFGZ]
sources:
  - url: https://en.wikipedia.org/wiki/Mathematical_induction
    locator: Complete (strong) induction
  - url: https://en.wikipedia.org/wiki/Tree_(graph_theory)
    locator: Properties
  - book: isbn:9781108439534
    locator: Chapter 6
---

## Summary

Induction on size is a proof method for a claim about all objects of some kind, such as all finite graphs, sets, matrices or polynomials.
We choose a size function $s$ that gives each object a natural number, such as the number of vertices, the number of edges, the number of elements or the degree.
Then we prove, by [[mathematical induction|0ASJVEFA9J]] or [[strong induction|0KMVFSHFGZ]] on $n$, the statement "the claim holds for every object $X$ with $s(X) = n$".
In the induction step we take an arbitrary object of size $n + 1$, break it into or reduce it to objects of smaller size, apply the induction hypothesis to these, and put the results back together.
The method matters because it turns a claim about infinitely many structures into one reduction step, and it is the standard first attempt in graph theory, combinatorics and linear algebra.

## Motivation

Many claims are about objects that have no natural "next" object.
There is no single graph after a given graph, so ordinary induction on the graphs themselves makes no sense.
But each finite graph has a number of vertices, and removing a vertex gives a graph with one vertex fewer.
So a claim about all finite graphs becomes a claim $P(n)$ about all graphs with $n$ vertices, and $P(n)$ can be proved by induction on $n$.
The same idea works whenever objects have a size and a way to shrink.

## Notation

1. The claim is written $P(n)$: "for every object $X$ with $s(X) = n$, the property $Q(X)$ holds". The quantifier "for every $X$" is part of $P(n)$.
2. Common size functions are $|V(G)|$ and $|E(G)|$ for a graph $G$, $|A|$ for a finite set $A$, $\deg f$ for a polynomial $f$, $\dim V$ for a vector space $V$, and $m + n$ for a pair of numbers.
3. Proofs say "by induction on the number of vertices" or "by induction on $|V(G)|$". When the size is a sum such as $r + s$, they say "by induction on $r + s$".

## Remarks

### The steps of the method

1. Choose the size function $s$. The size must be a natural number, and the reduction step must lower it.
2. State $P(n)$ with the quantifier over all objects of size $n$ inside it.
3. Prove the base case: the claim for all objects of the smallest size.
4. In the step, let $X$ be an arbitrary object of size $n + 1$ (or of size $n$, with the hypothesis for all smaller sizes).
5. Reduce $X$: delete a vertex, an edge or an element, factor out a root, or restrict to a subspace. Check that the smaller object still satisfies the hypotheses of the claim.
6. Apply the induction hypothesis to the smaller object, and deduce the claim for $X$.

### Breaking down, not building up

The step must start from an arbitrary object of size $n + 1$ and reduce it.
The opposite order, "take an object of size $n$ and add something", is called building up.
Building up proves the claim only for the objects of size $n + 1$ that arise by adding something to an object of size $n$ that satisfies the hypotheses.
Some objects of size $n + 1$ may not arise in this way, and then the proof misses them.
The [[build-up argument for graphs without isolated vertices|ECMJTM9A6C]] shows a false claim "proved" in this way.
A building-up step is correct only with an extra proof that every object of size $n + 1$ arises from an object of size $n$ that satisfies the hypotheses.

### Choosing the parameter

The size function must be chosen so that the reduction keeps the hypotheses of the claim.
For trees, removing a leaf gives a tree, so the number of vertices works; removing an arbitrary vertex can disconnect the tree.
For a claim about connected graphs, one often removes an edge that is not a bridge, or a vertex that is not a cut vertex, and must prove that such an edge or vertex exists.
When two parameters are involved, the sum $m + n$ or the lexicographic order on pairs can serve as the size, as in [[double induction|AABX4YPKRR]].
When no choice of parameter makes the step work, the claim often needs to be strengthened first, which is the method of [[strengthening the induction hypothesis|F94KJC2RXP]].

### Examples

1. [[A tree with $n$ vertices has $n - 1$ edges|RJB83Z4N9B]], by induction on $n$: remove a leaf and its edge.
2. [[A nonzero polynomial of degree $d$ over a field has at most $d$ roots|7TMGBKKMPE]], by induction on $d$: factor out $x - c$ for a root $c$.
3. A set with $n$ elements has $2^n$ subsets, by induction on $n$: fix one element $a$; the subsets that do not contain $a$ and those that contain $a$ are each in bijection with the subsets of a set with $n - 1$ elements.
4. Hall's marriage theorem has a [[proof by induction on the number of sets|NGB06K7WKZ]].
5. The [[tiling of a deficient $2^n \times 2^n$ board by L-trominoes|EXRJ0JF2Q3]] is an induction on $n$: the board splits into four boards of size $2^{n-1}$.
6. In linear algebra, the [[proof of triangularisation|PQ79GJDGRQ]] and the [[proof of the spectral theorem|A81KPS16D7]] are inductions on the dimension: split off one eigenvector and apply the hypothesis to a complement of smaller dimension.

### Non-examples

1. The [[build-up argument for graphs without isolated vertices|ECMJTM9A6C]] is not a valid induction on size. Its step adds a vertex to a smaller graph, and it does not reach the graph made of two disjoint edges.
2. An "induction on the size" of real numbers, with the step from $x$ to $x + 1$, is not an induction on size. The real numbers have no natural-number size that each step lowers, and the argument reaches only the numbers $x_0, x_0 + 1, x_0 + 2, \ldots$.
3. A proof that checks all graphs with at most $5$ vertices by computer is not an induction on size. It proves the claim only for those graphs, and no step carries it further.

### Basic properties

1. Induction on size is a case of ordinary or strong induction on the natural number $n$, applied to the statement $P(n)$ with its inner quantifier over all objects of size $n$. So it is valid exactly when ordinary induction is.
2. Strong induction on size is often needed, because a reduction can lower the size by more than one. Splitting a graph into two components gives two smaller graphs of any sizes.
3. Induction on size is equivalent to a [[minimal counterexample|JGRCNPKNGG]] argument: take a counterexample of least size, which exists by the [[well-ordering principle|01BX15HSRR]], and reduce it to a smaller counterexample.

### History

Golomb's 1954 proof that a deficient $2^n \times 2^n$ board can be tiled by L-trominoes is an induction on the size parameter $n$.
Induction on the dimension is the standard proof form for structure theorems of linear algebra, such as the triangularisation of complex matrices.

### Common errors

1. Building up instead of breaking down, as described above.
2. Applying the induction hypothesis to a smaller object that does not satisfy the hypotheses of the claim, for example a subgraph that is no longer connected after a vertex is removed.
3. Fixing the object first and then inducting on its size. The statement $P(n)$ must quantify over all objects of size $n$, or the hypothesis is about one object only and cannot be applied to the smaller object of the step.

## Explanations

### L1 human

Suppose that we want to show something about every possible road network.
There are infinitely many networks, so we cannot check them all.
Instead, we count the towns in a network.
We show the claim for a network with one town.
Then we show: if the claim holds for all networks with $5$ towns, it holds for every network with $6$ towns, because we can remove one town and use the smaller network.
The same argument works from any number of towns to the next, so the claim holds for networks of every size.

### L2 human

We prove that every finite set $A$ with $n$ elements has exactly $2^n$ subsets, by induction on $n$.

1. Let $P(n)$ be the statement "every set with $n$ elements has exactly $2^n$ subsets".
2. Base case: a set with $0$ elements is $\emptyset$. Its only subset is $\emptyset$, and $2^0 = 1$.
3. Induction step: assume $P(n)$, and let $A$ be an arbitrary set with $n + 1$ elements.
4. Since $n + 1 \ge 1$, the set $A$ has an element $a$. Let $A' = A \setminus \{a\}$, a set with $n$ elements.
5. Each subset of $A$ either does not contain $a$, and then it is a subset of $A'$, or it contains $a$, and then it is $B \cup \{a\}$ for exactly one subset $B$ of $A'$.
6. By $P(n)$, $A'$ has $2^n$ subsets, so each of the two kinds has $2^n$ members.
7. So $A$ has $2^n + 2^n = 2^{n+1}$ subsets, and $P(n + 1)$ holds.

The typical use is a claim about all finite structures of a kind, where removing one part gives a smaller structure of the same kind.
The trap is in step 3: the step starts from an arbitrary set of size $n + 1$, not from a set of size $n$ with an element added.
Here both orders happen to work, because every set of size $n + 1$ is a set of size $n$ with one element added; for graphs with extra hypotheses this is often false.

### L3 human

Induction on size is induction along the map $s \colon \mathcal{C} \to \mathbb{N}$ from the class of objects to the natural numbers.
The relation "$Y$ is smaller than $X$" defined by $s(Y) < s(X)$ is [[well-founded|0DQPNJNPYK]], because it is the inverse image of the well-founded order of $\mathbb{N}$, and every inverse image of a well-founded relation is well-founded.
So induction on size is a special case of well-founded induction, and any well-founded measure can replace $s$: ordinals for transfinite constructions, the lexicographic order on pairs for [[double induction|AABX4YPKRR]], or the multiset order in termination proofs.
In graph theory, the method is often refined to induction on $|V(G)| + |E(G)|$, or to the study of a minimal counterexample, as in the proofs of the four colour theorem.
In algebra, induction on the dimension, on the length of a composition series, or on the order of a group (as in the [[proof of the first Sylow theorem|23T9VNK7W8]]) is the same method with a different measure.
