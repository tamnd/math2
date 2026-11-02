---
tag: 4GG1HGDEZC
kind: statement
role: theorem
name: XYZ inequality
msc: [06A07, "60E15"]
uses: [0QV2JS9RJ3, W8DZ5KGGHN, DCXJGS6E6D]
about: [W8DZ5KGGHN]
sources:
  - url: https://en.wikipedia.org/wiki/XYZ_inequality
same_as:
  wikidata: Q5454716
  wikipedia: XYZ inequality
---

## Statement

Let $(P, \le)$ be a finite [[partially ordered set|0QV2JS9RJ3]] and let $x, y, z \in P$.
Choose a [[linear extension|W8DZ5KGGHN]] $\prec$ of $P$ uniformly at random among all linear extensions, and write $\Pr$ for the resulting probability.
Then
$$\Pr(x \prec y \text{ and } x \prec z) \ge \Pr(x \prec y) \, \Pr(x \prec z).$$

## Remarks

Shepp proved the inequality using the [[FKG inequality|DCXJGS6E6D]] on a suitable distributive lattice of integer labellings of $P$.
It says that the events "$x$ comes before $y$" and "$x$ comes before $z$" are positively correlated.
This matches intuition: if $x$ comes early relative to $y$, it tends to come early in general.

Example: let $P$ be the antichain on $\set{x, y, z}$.
All $6$ orderings are linear extensions, so $\Pr(x \prec y) = \Pr(x \prec z) = 1/2$, and $x$ comes first in $2$ of the $6$ orderings, so the left side is $1/3 \ge 1/4$.

## Explanations

### L1 human

Put the elements of a poset in a random order that respects the poset.
Knowing that $x$ comes before $y$ makes it more likely, or at least not less likely, that $x$ also comes before $z$.
The XYZ inequality states this in numbers.

### L2 human

The inequality belongs to the family of correlation inequalities for linear extensions, studied in connection with sorting and with the 1/3–2/3 conjecture.
Its proof is a model use of the FKG inequality.
One looks at order-preserving labellings of $P$ by a large chain, which form a distributive lattice.
One applies FKG there and then lets the chain grow.
