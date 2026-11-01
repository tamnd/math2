---
tag: FJ92Q6VTJH
kind: statement
role: theorem
name: Erdős–Ko–Rado theorem
msc: [05D05]
uses: [0C21Q694AG, 0GBZM0MT0F]
about: [0C21Q694AG]
sources:
  - url: https://en.wikipedia.org/wiki/Erdős–Ko–Rado_theorem
same_as:
  wikidata: Q718875
  wikipedia: Erdős–Ko–Rado theorem
---

## Statement

Let $n$ and $k$ be positive integers with $n \ge 2k$.
Let $\mathcal{F}$ be a [[family|0C21Q694AG]] of $k$-element subsets of $\set{1, \ldots, n}$ that is intersecting: $A \cap B \ne \emptyset$ for all $A, B \in \mathcal{F}$.
Then
$$|\mathcal{F}| \le \binom{n - 1}{k - 1}.$$

## Remarks

Katona's proof places $1, \ldots, n$ around a circle in a random order.
An intersecting family contains at most $k$ of the $n$ arcs of $k$ consecutive points, when $n \ge 2k$.
Each $k$-set is such an arc with probability $n / \binom{n}{k}$, so averaging gives $|\mathcal{F}| \cdot n / \binom{n}{k} \le k$, that is, $|\mathcal{F}| \le \frac{k}{n} \binom{n}{k} = \binom{n-1}{k-1}$.

Example: the star of all $k$-sets that contain the element $1$ is intersecting and has exactly $\binom{n-1}{k-1}$ members.
For $n > 2k$ the stars are the only families that attain the bound.
For $n = 2k$ there are others, for example one set from each complementary pair.
The hypothesis $n \ge 2k$ is necessary: if $k < n < 2k$, any two $k$-subsets intersect, and there are $\binom{n}{k} = \frac{n}{k} \binom{n-1}{k-1} > \binom{n-1}{k-1}$ of them.

## Explanations

### L1 human

Suppose every two committees of $k$ people, chosen from $n$ people, must share a member.
How many committees can there be?
The simple answer is to give every committee one fixed common member.
The theorem says that you cannot do better, provided the group is at least twice the committee size.

### L2 human

The theorem is a basic result of extremal set theory, with many extensions: to $t$-intersecting families, to vector spaces, to permutations, and to other structures.
Its circle proof is an averaging argument of the same kind as the proof of the [[LYM inequality|D1GQNNRDDN]].
The [[Kruskal–Katona theorem|G6WNYB0WMY]] gives another proof.
In graph language it gives the independence number of the Kneser graph.
