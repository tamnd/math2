---
tag: VD8RCR44GQ
kind: statement
role: theorem
name: Arrow's impossibility theorem
msc: [91B14, 91B12, 91B10]
uses: [KH8ACT22FR, JGP0Q56FRY, PW2NKAPXWA, 0FRXBVVR03, V07KD5QYGV, V0EYM00JGK]
about: [KH8ACT22FR, F17C7F17PM]
sources:
  - url: https://en.wikipedia.org/wiki/Arrow%27s_impossibility_theorem
same_as:
  wikidata: Q33481
  wikipedia: Arrow's impossibility theorem
---

## Statement

Let $A$ be a finite set of at least $3$ alternatives and $N = \set{1, \dots, n}$ a finite set of $n \ge 2$ individuals.
Let $\mathcal{L}(A)$ be the set of [[linear orders|0FRXBVVR03]] of $A$ and $\mathcal{R}(A)$ the set of [[weak orderings|PW2NKAPXWA]] of $A$.
Let $F \colon \mathcal{L}(A)^n \to \mathcal{R}(A)$ be a [[social welfare function|KH8ACT22FR]] defined on all profiles, and write $\succ$ for the strict part of $F(\succ_1, \dots, \succ_n)$.
Assume that:

1. (weak Pareto) for every profile and all $x, y \in A$, if $x \succ_i y$ for every $i$, then $x \succ y$;
2. (independence of irrelevant alternatives) let $x, y \in A$, and take two profiles in which every individual ranks $x$ and $y$ in the same order. Then the social ranking of $x$ and $y$ is the same for both profiles.

Then $F$ is a dictatorship: there is an individual $d \in N$ such that for every profile and all $x, y \in A$, $x \succ_d y$ implies $x \succ y$.

## Remarks

A standard proof starts with an alternative $b$ that every individual puts at the top or at the bottom.
It shows that society then also puts $b$ at the top or the bottom.
One then moves $b$ from bottom to top one voter at a time and finds a pivotal voter whose switch moves $b$ from the social bottom to the social top.
Independence of irrelevant alternatives then shows that this voter dictates every pair not containing $b$, and a second argument extends this to all pairs.

Each hypothesis is needed.
With only $2$ alternatives, majority rule satisfies both conditions and is not a dictatorship.
The [[Borda count|V0EYM00JGK]] satisfies weak Pareto but violates independence of irrelevant alternatives.
The constant rule that always outputs one fixed ranking satisfies independence but violates weak Pareto.
Pairwise majority rule satisfies both conditions but, by the [[Condorcet paradox|V07KD5QYGV]], its output need not be transitive, so it is not a social welfare function.
The theorem also holds with weak orderings as individual preferences.

## Explanations

### L1 human

Arrow asked for a way to combine everyone's ranking into a ranking for the whole group, with two fair-sounding rules.
If everybody prefers one option to another, so should the group.
And the group's verdict between two options should depend only on how people rank those two.
With three or more options, the only rule that passes is to let one person decide everything.

### L2 human

Arrow's theorem is the founding result of social choice theory.
It shows that every ranked voting system violates some natural fairness condition, so the design of voting rules is a matter of tradeoffs.
The Gibbard–Satterthwaite theorem on manipulation and Sen's liberal paradox are closely related impossibility results.
Restricting the domain, for example to single-peaked preferences, avoids the conclusion: then pairwise majority is transitive.
