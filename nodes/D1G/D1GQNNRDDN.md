---
tag: D1GQNNRDDN
kind: statement
role: theorem
name: LYM inequality
msc: [05D05, 06A07]
uses: [00E0YZCERH, 03HF498P1J, 0GBZM0MT0F, 0C21Q694AG]
about: [03HF498P1J]
sources:
  - url: https://en.wikipedia.org/wiki/Lubell–Yamamoto–Meshalkin_inequality
same_as:
  wikidata: Q1872826
  wikipedia: Lubell–Yamamoto–Meshalkin inequality
---

## Statement

Let $n \ge 1$ be an integer and let $\mathcal{F}$ be a [[family|0C21Q694AG]] of subsets of $[n] = \set{1, \ldots, n}$.
Suppose that $\mathcal{F}$ is an [[antichain|03HF498P1J]] in the [[power set|00E0YZCERH]] ordered by inclusion: no member of $\mathcal{F}$ is a proper subset of another.
Then
$$\sum_{A \in \mathcal{F}} \frac{1}{\binom{n}{|A|}} \le 1.$$

## Remarks

A maximal chain $\emptyset \subset \set{a_1} \subset \set{a_1, a_2} \subset \cdots \subset [n]$ corresponds to an ordering $a_1, \ldots, a_n$ of $[n]$, so there are $n!$ of them.
A set $A$ with $|A| = k$ lies on exactly $k! (n - k)!$ maximal chains.
A chain meets an antichain at most once, so $\sum_{A \in \mathcal{F}} |A|! (n - |A|)! \le n!$, and division by $n!$ gives the inequality.

Since $\binom{n}{k} \le \binom{n}{\floor{n/2}}$ for all $k$, the inequality gives $|\mathcal{F}| \le \binom{n}{\floor{n/2}}$, which is [[Sperner's theorem|0J87V9K1GE]].
Equality holds for the family of all $k$-subsets of $[n]$, for any $k$.
Without the antichain hypothesis the sum can exceed $1$: for $\mathcal{F} = \set{\emptyset, [n]}$ it equals $2$.

## Explanations

### L1 human

Each set of size $k$ gets the weight $1/\binom{n}{k}$, so a full layer of sets of the same size has total weight $1$.
The inequality says that a family in which no set contains another can never have total weight more than one full layer.
So sets of rare sizes are expensive, and sets of the middle size are cheap.

### L2 human

The LYM inequality is the strong form of [[Sperner's theorem|0J87V9K1GE]], and its chain-counting proof is a model double-counting argument.
It extends to posets with a suitable chain structure, called LYM posets.
It is also used, through the same idea of averaging over orderings, in Katona's proof of the [[Erdős–Ko–Rado theorem|FJ92Q6VTJH]].
The [[Kruskal–Katona theorem|G6WNYB0WMY]] gives the exact minimum size of the shadow of a family of sets of one size.
