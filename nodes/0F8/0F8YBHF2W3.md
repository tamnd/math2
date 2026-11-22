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

Double counting proves that two expressions are equal by showing that both count the same finite set.
Often one count is easy and the other is the quantity you want, so the easy count gives the hard one for free.

In the common form, $A$ and $B$ are finite sets and $R \subseteq A \times B$ is a [[relation|05AVARPXA2]] between them, a subset of the [[Cartesian product|09CEDJYBKP]].
For $a \in A$, let $d(a)$ be the number of $b \in B$ with $(a, b) \in R$, and for $b \in B$, let $e(b)$ be the number of $a \in A$ with $(a, b) \in R$.
Both sums below count the pairs in $R$, once sorted by the first entry and once sorted by the second:
$$\sum_{a \in A} d(a) = |R| = \sum_{b \in B} e(b).$$

## Motivation

At a party, some pairs of guests shake hands.
Is the number of guests who shake an odd number of hands always even?
You cannot list every party, but you can count the pairs (guest, handshake) with the guest taking part in the handshake.
Sorted by guest, the count is the sum of the numbers of handshakes of the guests.
Sorted by handshake, it is twice the number of handshakes, because each handshake has two guests.

So the sum of the guests' numbers is even, and a sum of integers is even only when it has an even number of odd terms.
This is the [[handshaking lemma|0XAP8WHNES]], and it needed no knowledge of the party.
The same move computes averages, proves identities between binomial coefficients and rules out designs that cannot exist.
It returns later as linearity of expectation in probability and as Fubini's theorem in analysis.

## Notation

The relation $R$ is often given by its incidence matrix $M$, the $|A| \times |B|$ [[matrix|0VD9ZSWWJG]] with $M_{a,b} = 1$ when $(a, b) \in R$ and $M_{a,b} = 0$ otherwise.
The row sums of $M$ are the numbers $d(a)$, and the column sums are the numbers $e(b)$.
Double counting says that the total of all entries is both the sum of the row sums and the sum of the column sums.
The [[incidence matrix|9DNFN8M83X]] of a graph is the standard case.
You can also read $R$ as a [[bipartite graph|0ZVQKTRKVQ]] with parts $A$ and $B$, and then $d(a)$ and $e(b)$ are degrees.
Other names are "counting in two ways" and "counting pairs".
A proof of an identity by double counting is also a [[combinatorial proof|SS07J9ZAQ7]], and many books use both names.

## Remarks

### A first count: the edges of a cube

How many edges does a cube have?
Let $R$ be the set of pairs $(v, e)$ where $v$ is a vertex, $e$ is an edge, and $v$ is an end of $e$.
Count by vertices: there are $8$ vertices and $3$ edges at each, so $|R| = 8 \cdot 3 = 24$.
Count by edges: each edge has $2$ ends, so $|R| = 2|E|$.
The two counts give
$$2|E| = 24, \qquad |E| = 12.$$
Check: the top face has $4$ edges, the bottom face has $4$, and there are $4$ vertical edges, so $12$ in all.

### Why it works and how to choose the pairs

The set $R$ is a table with one row for each $a$ and one column for each $b$, with a mark where $(a, b) \in R$.
Adding the marks row by row and column by column must give the same total, by the [[rule of sum|0EE2V3CHFK]] applied twice.
So the whole skill is to choose a set of pairs for which one side is the sum you want and the other side is a product of known numbers.
A good first try is "an object and a part of it": a vertex and an edge at it, a point and a line through it, a set and an element of it.
In Mathlib the identity is `Finset.sum_card_bipartiteAbove_eq_sum_card_bipartiteBelow`.

### More examples

In the [[Fano plane|7519W7BDKR]], the pairs (point, line through it) number $7 \cdot 3 = 21$, so a point lies on $3$ lines on average, and a second count shows that every point lies on exactly $3$.
For [[fixed points of permutations|SBC0RA543V]], the pairs $(\sigma, i)$ with $\sigma(i) = i$ number $n \cdot (n-1)! = n!$, so a permutation has $1$ fixed point on average.
The identity
$$\sum_{k=0}^{n} k \binom{n}{k} = n 2^{n-1}$$
counts the pairs $(S, x)$ with $S \subseteq \{1, \dots, n\}$ and $x \in S$: by $S$ we get the left side, and by $x$ we get $n$ elements each in $2^{n-1}$ subsets.
Check with $n = 3$: $3 + 6 + 3 = 12 = 3 \cdot 4$.
The [[combinatorial proof of k C(n, k) = n C(n - 1, k - 1)|TTQNN6XXQN]] counts the same pairs for one size of $S$.
In a plane graph each edge borders two face sides, so the face lengths add up to $2|E|$, and the [[proof of the edge bound for planar graphs|K90CGWAE6S]] starts there.
The [[average number of divisors|320MBBJETV]] of $1, \dots, n$ comes from the pairs $(j, k)$ with $j \mid k \le n$.

### When the method does not apply

For an [[infinite signed table|29XBXX10N8]] with $1$ on the diagonal and $-1$ just to the right of it, every row sums to $0$ but the columns sum to $1$ in total.
The condition that fails is finiteness: the method counts a finite set, or adds non-negative numbers.

Adding sizes of overlapping sets is not double counting either.
The sum $\sum_i |A_i|$ counts the pairs $(i, x)$ with $x \in A_i$, while $|A_1 \cup \cdots \cup A_k|$ counts elements, so the two sides count different sets: for $A_1 = A_2 = \{1\}$ they are $2$ and $1$.

The proof of the [[symmetry of binomial coefficients|0R7JS3DP3W]] by $S \mapsto X \setminus S$ is a bijective proof, not a double count, because it compares two different sets.

### The rules you can use

In the regular case, with $d(a) = d$ for all $a$ and $e(b) = e$ for all $b$, the identity becomes $|A| \cdot d = |B| \cdot e$, which is $bk = vr$ for [[block designs|4JCSS2Z1BA]].
The weighted form swaps a finite double sum: for any $w : A \times B \to \mathbb{R}$,
$$\sum_{a \in A} \sum_{b \in B} w(a, b) = \sum_{b \in B} \sum_{a \in A} w(a, b),$$
and double counting is the case where $w$ is $1$ on $R$ and $0$ elsewhere.
The mean of the numbers $d(a)$ is $|R| / |A|$, so some $a$ has $d(a) \geq |R| / |A|$, which is the start of the [[averaging argument|HXP9VMXV8S]].
For infinite sums the swap needs a hypothesis such as non-negative terms or absolute convergence, as in [[interchange of summation order|MZM1AFXY82]] and [[Fubini's theorem|0R0T1VWH5X]].

### Watch out

The usual slip is the wrong multiplicity on one side.
In the cube, the sum $24$ looks like the number of edges until you remember that each edge has two ends.
In a graph with $T$ triangles, the pairs (edge, triangle containing it) number $3T$, not $T$, because each triangle has $3$ edges.
A second slip is to count two different sets and call them one.
Before you write either sum, write the set of pairs in words, and check that both sums count exactly that set.

### History

The handshaking lemma appears in the 1736 paper of Leonhard Euler on the bridges of Königsberg, and it is one of the oldest double counting arguments in graph theory.
The book "Proofs from THE BOOK" by Aigner and Ziegler has a chapter on the pigeonhole principle and double counting.

### Try it

A graph has $10$ vertices, each of degree $3$ or $4$, and $17$ edges.
How many vertices have degree $4$?
The degree sum is $2 \cdot 17 = 34$, and with $x$ vertices of degree $4$ it is $3(10 - x) + 4x = 30 + x$, so $x = 4$.

A soccer ball has $12$ pentagons and $20$ hexagons, and $3$ faces meet at each corner.
How many corners does it have?
The pairs (face, corner of it) number $12 \cdot 5 + 20 \cdot 6 = 180$, and each corner lies on $3$ faces, so there are $60$ corners.

## Explanations

### L1 human

Count the same collection of things in two ways, and the two answers must be equal.
For example, $4$ friends meet, and each pair of them shakes hands once.
Each person shakes $3$ hands, so adding up the handshakes of the people gives $4 \times 3 = 12$.
But each handshake involves $2$ people, so this sum counts each handshake twice.
So there are $12 / 2 = 6$ handshakes.
Check: the pairs from four friends $A, B, C, D$ are $AB, AC, AD, BC, BD, CD$, which is $6$.

### L2 human

Can $7$ committees of $3$ people each be formed from $7$ people so that every two people serve together on exactly one committee?
Suppose they can, and fix one person $p$ who serves on $r$ committees.
Count the pairs (another person $q$, a committee with $p$ and $q$).
Each of the $6$ other people shares exactly one committee with $p$, so there are $6$ pairs.
Each of the $r$ committees of $p$ has $2$ other members, so there are $2r$ pairs, and $2r = 6$ gives $r = 3$.
Now count (person, committee of that person): by committees $7 \cdot 3 = 21$, and by people $7 \cdot 3 = 21$, so the numbers agree.
The [[Fano plane|7519W7BDKR]] is such a system, so the answer is yes.
The typical use is shown here: double counting finds the parameters before you build anything, and a value that is not an integer would prove that no system exists.

### L3 human

The identity is the commutativity of a finite double sum, and it is the discrete case of [[Fubini's theorem|0R0T1VWH5X]] for the counting measure.
In matrix language, for the incidence matrix $M$ and the all-ones vector $\mathbf{1}$, the number $\mathbf{1}^{\top} M \mathbf{1}$ can be computed with the row sums or with the column sums.
Linear algebra on $M$ gives stronger results than the sums alone, for example Fisher's inequality for block designs.

In probability, double counting becomes linearity of [[expectation|0WQNRCNY3M]]: the expected number of fixed points of a random permutation is a sum of $n$ probabilities $1/n$.
Many inequalities of extremal combinatorics start with a double count and then apply an inequality to the result.
The [[proof of Mantel's theorem|TPQVT6GZAW]] shows $\sum_{xy \in E} (d(x) + d(y)) = \sum_{v} d(v)^2$ by a double count, and then it applies the [[Cauchy-Schwarz inequality|0RFWW56Y22]].
The [[proof of Sperner's theorem by Lubell|57DD99JPR1]] counts the pairs of a set of the family and a maximal chain through it.
Together with the [[bijection principle|0GV2573FP4]], double counting is one of the two basic tools of [[combinatorial proofs|SS07J9ZAQ7]].
