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

Induction on size proves a claim about all objects of some kind, such as all finite graphs or all polynomials, by induction on a number attached to each object.
You take an arbitrary object of size $n + 1$, cut it down to a smaller object, and use the claim for the smaller one.

Here is the standard first example.
Every [[tree|0MJ0JS72DZ]] with $n \ge 1$ vertices has $n - 1$ edges.
A tree with one vertex has $0$ edges.
A tree with $n + 1 \ge 2$ vertices has a leaf, a vertex with one edge, and deleting the leaf and its edge leaves a tree with $n$ vertices.
By the induction hypothesis that tree has $n - 1$ edges, so the original tree has $n$ edges, as claimed.

In general, we choose a size function $s$ that gives each object a natural number: the number of vertices, edges or elements, or the degree, or the dimension.
Then we prove, by [[mathematical induction|0ASJVEFA9J]] or [[strong induction|0KMVFSHFGZ]] on $n$, the statement
$$P(n): \text{ the claim holds for every object } X \text{ with } s(X) = n.$$
In the step, an arbitrary object of size $n + 1$ is reduced to objects of smaller size, the hypothesis is applied to them, and the results are put back together.

## Motivation

Graphs, sets and polynomials have no single "next" object, so ordinary induction on the objects themselves makes no sense.
But each finite graph has a number of vertices, and deleting a vertex gives a graph with one vertex fewer.
So a claim about all finite graphs becomes a claim $P(n)$ about all graphs with $n$ vertices, and $P(n)$ can be proved by induction on $n$.
The same idea works whenever the objects have a size and a way to shrink.

This is the first method to try in graph theory, combinatorics and linear algebra.
The [[L-tromino tiling|EXRJ0JF2Q3]] is an induction on the exponent $n$ of a $2^n \times 2^n$ board.
The [[proof of the spectral theorem|A81KPS16D7]] is an induction on the dimension, and a [[proof of Hall's marriage theorem|NGB06K7WKZ]] is an induction on the number of sets.

## Notation

Proofs say "by induction on the number of vertices", "by induction on $|V(G)|$" or "by induction on $\deg f$".
Common sizes are $|V(G)|$ and $|E(G)|$ for a graph $G$, $|A|$ for a finite set $A$, $\deg f$ for a polynomial $f$, $\dim V$ for a vector space $V$, and $m + n$ for a pair of numbers.
The claim $P(n)$ always has the form "for every object $X$ with $s(X) = n$, $X$ has the property".
The inner "for every" is a part of $P(n)$, and it is the part that beginners leave out.

## Remarks

### Why the method is valid

Induction on size is ordinary or strong induction on the natural number $n$, applied to the statement $P(n)$ with its inner quantifier.
When $P(n)$ holds for every $n$, every object $X$ has the property, because $X$ has some size $s(X)$.
So the method is valid exactly when induction on $\mathbb{N}$ is.

Strong induction is often the right form, because a reduction can lower the size by more than one.
Splitting a disconnected graph into two parts gives two smaller graphs of any sizes.
Read backward, the method is a [[minimal counterexample|JGRCNPKNGG]]: a counterexample of least size exists by the [[well-ordering principle|01BX15HSRR]], and the reduction turns it into a smaller one.

### Breaking down, not building up

The step must start from an arbitrary object of size $n + 1$ and reduce it.
The opposite order, "take an object of size $n$ and add something", is called building up.
Building up proves the claim only for the objects of size $n + 1$ that arise from an object of size $n$ by the chosen addition.
Some objects of size $n + 1$ may not arise in this way, and then the proof misses them.

The [[build-up argument for graphs without isolated vertices|ECMJTM9A6C]] "proves" a false claim in this way.
It misses the graph made of two separate edges, which is not built from any smaller graph of the claim.
A building-up step is correct only with an extra proof that every object of size $n + 1$ arises from an object of size $n$ that satisfies the hypotheses.

### Choosing the parameter

The size must be chosen so that the reduction keeps the hypotheses of the claim.
For trees, deleting a leaf gives a tree, so the number of vertices works.
Deleting an arbitrary vertex does not: the middle vertex of a path with $3$ vertices leaves two separate vertices.
For connected graphs one deletes an edge that is not a bridge, or a vertex that is not a cut vertex, and proves first that such an edge or vertex exists.

For polynomials over a field, the [[root bound example|7TMGBKKMPE]] factors out $x - c$ for a root $c$, which lowers the degree by exactly $1$.
When two parameters are involved, the sum $m + n$ or the lexicographic order on pairs can serve as the size, as in [[double induction|AABX4YPKRR]].
When no parameter makes the step work, the claim often needs to be stronger first, which is the method of [[strengthening the induction hypothesis|F94KJC2RXP]].

### A count of subsets

A set with $n$ elements has $2^n$ subsets, by induction on $n$.
The empty set has the one subset $\emptyset$, and $2^0 = 1$.
For a set $A$ with $n + 1$ elements, fix an element $a$ and put $A' = A \setminus \{a\}$.
The subsets of $A$ without $a$ are the subsets of $A'$, and the subsets with $a$ are the sets $B \cup \{a\}$ for $B \subseteq A'$.
Each kind has $2^n$ members by the hypothesis, so
$$2^n + 2^n = 2^{n+1}.$$
Check: $\{1, 2\}$ has the $4$ subsets $\emptyset$, $\{1\}$, $\{2\}$, $\{1, 2\}$.

### What is not induction on size

An argument on the real numbers with a step from $x$ to $x + 1$ is not induction on size.
The reals have no natural-number size that each step lowers, and the argument reaches only $x_0, x_0 + 1, x_0 + 2, \ldots$.
A computer check of all graphs with at most $5$ vertices is not induction on size either.
It proves the claim for those graphs only, and no step carries it further.

### Watch out

The most common error is building up, as described above.
The second is to apply the hypothesis to a smaller object that fails the hypotheses of the claim, for example a subgraph that is no longer connected after a vertex is deleted.
The third is to fix one object first and then to induct on its size.
Then the hypothesis is about that one object only, and it cannot be applied to the smaller object of the step; the quantifier "for every $X$ of size $n$" must sit inside $P(n)$.

### History

Golomb introduced polyominoes in 1954, and the induction proof that a deficient $2^n \times 2^n$ board can be tiled by L-trominoes is due to him.

### Try it

First, prove that a graph with $n$ vertices has at most $n(n - 1)/2$ edges.
Delete a vertex $v$: it has at most $n - 1$ edges, and the rest has at most $(n - 1)(n - 2)/2$, so the total is at most $(n - 1)(n - 2)/2 + (n - 1) = n(n - 1)/2$.

Second, say what is wrong with "add a leaf to a tree with $n$ vertices; it gains one vertex and one edge, so every tree with $n + 1$ vertices has $n$ edges".
It builds up, so it needs the extra fact that every tree with $n + 1$ vertices comes from a smaller tree by adding a leaf, which is the leaf lemma.

## Explanations

### L1 human

Suppose that we want to show something about every possible road network.
There are infinitely many networks, so we cannot check them all.
Instead, we count the towns in a network.
We show the claim for a network with one town.
Then we show that the claim for all networks with $5$ towns gives it for every network with $6$ towns, by removing one town and using the smaller network.
The same argument works from each number of towns to the next, so the claim holds for networks of every size.

### L2 human

We prove that a finite graph $G$ with $n$ vertices and $m$ edges has at least $n - m$ connected components, by induction on $m$.
Here the size is the number of edges, and $P(m)$ says "every graph with $m$ edges and any number $n$ of vertices has at least $n - m$ components".
For $m = 0$ each vertex is its own component, so there are exactly $n = n - 0$ components.
For the step, take an arbitrary graph $G$ with $m + 1$ edges and delete one edge $e$.
The smaller graph $G - e$ has $n$ vertices and $m$ edges, so it has at least $n - m$ components by $P(m)$.
Putting $e$ back joins at most two components into one, so $G$ has at least
$$(n - m) - 1 = n - (m + 1)$$
components, which is $P(m + 1)$.

Check: a tree with $n$ vertices has $m = n - 1$ edges and $1 = n - m$ component, so the bound can be reached.
The typical use is a claim about all finite structures of a kind, where deleting one part gives a smaller structure of the same kind.
Watch out: the step started from an arbitrary graph with $m + 1$ edges, and the inner quantifier over $n$ in $P(m)$ is what allowed the hypothesis to apply to $G - e$.

### L3 human

Induction on size is induction along a map $s \colon \mathcal{C} \to \mathbb{N}$ from a class of objects to the natural numbers.
The relation "$s(Y) < s(X)$" is [[well-founded|0DQPNJNPYK]], because it is the inverse image of the well-founded order of $\mathbb{N}$.
So the method is a case of well-founded induction, and any well-founded measure can replace $s$: the lexicographic order on pairs for [[double induction|AABX4YPKRR]], or the multiset order in termination proofs of programs.
In graph theory the measure is often $|V(G)| + |E(G)|$.
In algebra it is the dimension, as in the [[proof of triangularization|PQ79GJDGRQ]], the length of a composition series, or the order of a group, as in the [[proof of the first Sylow theorem|23T9VNK7W8]].
