---
tag: 0F8YBHF2W3
kind: concept
name: Double counting
aliases: [counting-in-two-ways]
msc: ["05A19", "00A35"]
topics: [G9JFJGY4TQ, GB14W4SYPK]
audience: ug1
uses: [05099E1NMJ, 0EE2V3CHFK, 09CEDJYBKP, 05AVARPXA2]
sources:
  - url: https://en.wikipedia.org/wiki/Double_counting_(proof_technique)
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Handshaking_lemma
    locator: lead section
same_as:
  wikidata: Q1191750
  wikipedia: Double counting (proof technique)
---

## Summary

Double counting is a proof technique in combinatorics: to prove that two expressions are equal, we show that both expressions count the elements of the same finite set.
In the common form, $A$ and $B$ are finite sets and $R \subseteq A \times B$ is a [[relation|05AVARPXA2]] between them, a subset of the [[Cartesian product|09CEDJYBKP]].
For $a \in A$, let $d(a)$ be the number of $b \in B$ with $(a, b) \in R$, and for $b \in B$, let $e(b)$ be the number of $a \in A$ with $(a, b) \in R$.
Then both sums below count the pairs in $R$, once sorted by the first entry and once sorted by the second entry:
$$\sum_{a \in A} d(a) = |R| = \sum_{b \in B} e(b).$$
The technique turns a hard count into an easy one, and it gives identities, inequalities and impossibility results with very little computation.

## Motivation

Many sums in combinatorics are hard to compute term by term.
For example, the sum of the degrees of the vertices of a graph depends on the shape of the graph.
But each edge has two ends, so the sum of the degrees counts each edge twice.
This gives the value $2|E|$ with no knowledge of the individual degrees.

The pattern is general.
A set of pairs can be listed as a table, with one row for each $a \in A$ and one column for each $b \in B$.
The rows and the columns give two ways to add up the same marks, and the two totals must agree.
When one of the two totals is easy and the other is the quantity of interest, the technique gives that quantity.

## Notation

The relation $R$ is often given by its incidence matrix $M$, the $|A| \times |B|$ [[matrix|0VD9ZSWWJG]] with $M_{a,b} = 1$ if $(a, b) \in R$ and $M_{a,b} = 0$ otherwise.
The row sums of $M$ are the numbers $d(a)$, and the column sums are the numbers $e(b)$.
In this language, double counting says that the sum of all entries of $M$ is the sum of its row sums and also the sum of its column sums.
See the [[incidence matrix|9DNFN8M83X]] of a graph for the standard case.

The relation $R$ is also a [[bipartite graph|0ZVQKTRKVQ]] with parts $A$ and $B$, and $d(a)$ and $e(b)$ are the degrees of its vertices.
Other names are "counting in two ways" and "proof by counting pairs".
A proof of an identity that counts one set in two ways is also a [[combinatorial proof|~a16dfc7e]], and many books use both names for it.

## Remarks

### Examples

- The [[handshaking lemma|0XAP8WHNES]]. Take $A = V$, $B = E$ and $R = \set{(v, e) : v \in e}$. Each edge has $e(b) = 2$ ends, so the sum of the degrees is $2|E|$.
- [[Points and lines of the Fano plane|~59268d84]]. Count the pairs of a point and a line through it. The $7$ lines with $3$ points each give $21$ pairs, so on average a point lies on $21 / 7 = 3$ lines.
- [[Fixed points of permutations|~e9da7849]]. Count the pairs $(\sigma, i)$ with $\sigma(i) = i$. The total is $n!$, so a permutation of $n$ elements has $1$ fixed point on average.
- The identity $\sum_{k=0}^{n} k \binom{n}{k} = n 2^{n-1}$ comes from the pairs $(S, x)$ with $S \subseteq \set{1, \dots, n}$ and $x \in S$. Sorted by $S$, the count is the left side; sorted by $x$, each $x$ lies in $2^{n-1}$ subsets. The [[combinatorial proof of a related identity|~9956f43c]] counts the same pairs for a fixed size of $S$.
- Faces of a plane graph. Each edge borders two face sides, so the face lengths add up to $2|E|$. The [[proof of the edge bound for planar graphs|K90CGWAE6S]] starts with this count.
- [[The average number of divisors|~fb09547d]] of the integers up to $n$. Count the pairs $(j, k)$ with $j \mid k \le n$, once by $k$ and once by $j$.

### Non-examples

- [[Swapping an infinite signed double sum|~057b5cf9]]. The table with entries $1$ on the diagonal and $-1$ just to the right of it has row sums $0$ and column sums with total $1$. The condition that fails is finiteness: the technique counts a finite set, or adds non-negative numbers.
- For overlapping sets $A_1, \dots, A_k$, the sum $\sum_i |A_i|$ is not $|A_1 \cup \cdots \cup A_k|$. The sum counts the pairs $(i, x)$ with $x \in A_i$, and the union counts elements $x$. The two counts are counts of different sets, so they can differ: for $A_1 = A_2 = \set{1}$, the sum is $2$ and the union has $1$ element.
- The proof of the [[symmetry of binomial coefficients|0R7JS3DP3W]] by the map $S \mapsto X \setminus S$ is a bijective proof, not a double count. It compares two different sets, the $k$-subsets and the $(n - k)$-subsets of $X$. The condition that fails is that both sides count one and the same set.

### Basic properties

- The basic identity is the [[rule of sum|0EE2V3CHFK]], applied twice: $R$ is the disjoint union of its rows, and also of its columns. In Mathlib it is `Finset.sum_card_bipartiteAbove_eq_sum_card_bipartiteBelow`.
- Regular case. If $d(a) = d$ for all $a$ and $e(b) = e$ for all $b$, then $|A| \cdot d = |B| \cdot e$. This is the identity $bk = vr$ for [[block designs|4JCSS2Z1BA]].
- Weighted form. For a function $w : A \times B \to \mathbb{R}$, $\sum_{a \in A} \sum_{b \in B} w(a, b) = \sum_{b \in B} \sum_{a \in A} w(a, b)$. Double counting is the case where $w$ is the indicator of $R$.
- Averaging consequence. The mean of the numbers $d(a)$ is $|R| / |A|$, so some $a$ has $d(a) \geq |R| / |A|$. The [[averaging argument|~f5987d03]] uses this step.
- For infinite sums, the weighted form needs a hypothesis such as non-negative terms or absolute convergence; see [[interchange of summation order|MZM1AFXY82]] and [[Fubini's theorem|0R0T1VWH5X]].

### History

The handshaking lemma appears in the 1736 paper of Leonhard Euler on the bridges of Königsberg, and it is one of the oldest double counting arguments in graph theory.
The book "Proofs from THE BOOK" by Aigner and Ziegler has a chapter on the pigeonhole principle and double counting.

### Common errors

- Counting the pairs from one side with the wrong multiplicity. In a graph, a triangle contains $3$ edges and $3$ vertices, so the counts through edges and through vertices both give $3T$.
- Counting a set that is not the same on both sides. Before a double count, write down the set of pairs explicitly, and check that both sums count exactly this set.
- Using the technique for infinite signed sums with no convergence hypothesis.

## Explanations

### L1 human

Count the same collection of things in two ways, and the two answers must be equal.
For example, $4$ friends meet, and each pair of them shakes hands once.
Each person shakes $3$ hands, so adding up the handshakes of the people gives $4 \times 3 = 12$.
But each handshake involves $2$ people, so this sum counts each handshake twice.
So there are $12 / 2 = 6$ handshakes.
The same idea shows that in every group, the total number of handshakes counted person by person is an even number.

### L2 human

We find the number of edges of the cube, with the vertices and edges of the usual cube in space.

1. The set to count is the set $R$ of pairs $(v, e)$ where $v$ is a vertex, $e$ is an edge, and $v$ is an end of $e$.
2. Count by vertices. The cube has $8$ vertices, and each vertex is an end of $3$ edges. So $|R| = 8 \cdot 3 = 24$.
3. Count by edges. Each edge has exactly $2$ ends. So $|R| = 2 \cdot |E|$.
4. The two counts give $2|E| = 24$, so the cube has $|E| = 12$ edges.
5. Check: the cube has $4$ edges on the top face, $4$ edges on the bottom face and $4$ vertical edges, so $12$ edges.

The typical use is to compute one side of the identity from the other side.
Often one side is a sum of unknown numbers and the other side is a product of known numbers.
A trap is to forget the multiplicity of one side: without step 3, the sum $24$ looks like the number of edges.

### L3 human

The identity is the commutativity of a finite double sum, and it is the discrete case of [[Fubini's theorem|0R0T1VWH5X]] for the counting measure.
In matrix language, for the incidence matrix $M$ and the all-ones vectors $\mathbf{1}$, the number $\mathbf{1}^{\top} M \mathbf{1}$ can be computed with the row sums or with the column sums.
Linear algebra on $M$ gives stronger results than the sums alone, for example Fisher's inequality for block designs.

In probability, double counting becomes linearity of [[expectation|0WQNRCNY3M]]: the expected number of fixed points of a random permutation is a sum of $n$ probabilities $1/n$.
Many inequalities of extremal combinatorics start with a double count and then apply an inequality to the result.
The [[proof of Mantel's theorem|TPQVT6GZAW]] shows $\sum_{xy \in E} (d(x) + d(y)) = \sum_{v} d(v)^2$ by a double count, and then it applies the [[Cauchy-Schwarz inequality|0RFWW56Y22]].
The [[proof of Sperner's theorem by Lubell|57DD99JPR1]] counts the pairs of a set of the family and a maximal chain through it.
The technique is a special case of the [[combinatorial proofs|~a16dfc7e]] of this sub-area, and the [[bijection principle|0GV2573FP4]] is the other basic tool of those proofs.
