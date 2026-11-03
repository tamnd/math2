---
tag: 4J3G7Y0VYC
kind: statement
role: theorem
name: Median voter theorem
msc: [91B12, 91B14]
uses: [JGP0Q56FRY, 0FRXBVVR03, WZYEADV8E1]
about: [F17C7F17PM, WZYEADV8E1]
sources:
  - url: https://en.wikipedia.org/wiki/Median_voter_theorem
same_as:
  wikidata: Q648511
  wikipedia: Median voter theorem
---

## Statement

Let $A$ be a set of alternatives with a [[linear order|0FRXBVVR03]] $<$ (for example a subset of $\R$).
Let $n$ be an odd number of voters, and let voter $i$ have a strict [[preference|JGP0Q56FRY]] $\succ_i$ on $A$ that is *single-peaked*.
This means that $\succ_i$ has a most preferred alternative $p_i$, its peak, and that for all $x, y \in A$:
if $y < x \le p_i$ or $p_i \le x < y$, then $x \succ_i y$.
Let $m$ be the median of the peaks $p_1, \dots, p_n$.
Then $m$ is a [[Condorcet winner|WZYEADV8E1]]: for every $y \in A$ with $y \ne m$, more than half of the voters prefer $m$ to $y$.

## Remarks

Take $y > m$.
Every voter with $p_i \le m$ has $p_i \le m < y$, so single-peakedness gives $m \succ_i y$.
Since $m$ is the median of an odd number of peaks, at least $(n + 1)/2$ voters have $p_i \le m$.
The case $y < m$ is symmetric, using the voters with $p_i \ge m$.

Example: three voters with peaks $10$, $40$ and $70$ on a tax rate scale, each preferring rates closer to their peak.
Then $40$ beats every other rate in a majority vote.
The first two voters prefer $40$ to any higher rate, and the last two prefer $40$ to any lower rate.

Without single-peakedness the conclusion fails, as the Condorcet paradox shows with three voters and three alternatives.
In two or more dimensions the analogue fails in general; this is the content of the McKelvey–Schofield chaos theorem.
Under the same hypotheses the majority relation is transitive.

## Explanations

### L1 human

Line the voters up from left to right by their favorite position, as on a political spectrum.
If each voter likes positions less the farther they are from their favorite, then the favorite of the voter in the middle wins every head-to-head vote.
This explains why candidates in a two-party race are often pulled toward the center.

### L2 human

The theorem, due to Duncan Black, is the main example of a domain restriction that escapes Arrow's impossibility theorem.
On single-peaked profiles pairwise majority is a transitive social welfare function, and the median rule is strategyproof.
In the Hotelling–Downs model of electoral competition it predicts that both parties choose the median position.
