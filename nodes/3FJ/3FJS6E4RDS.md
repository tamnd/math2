---
tag: 3FJS6E4RDS
kind: statement
role: theorem
name: McKelvey–Schofield chaos theorem
msc: [91B12, 91B14]
uses: [0XPR1E85W0, JGP0Q56FRY, WZYEADV8E1, 4J3G7Y0VYC]
about: [F17C7F17PM]
sources:
  - url: https://en.wikipedia.org/wiki/McKelvey%E2%80%93Schofield_chaos_theorem
same_as:
  wikidata: Q25099354
  wikipedia: McKelvey–Schofield chaos theorem
---

## Statement

Let the set of alternatives be [[Euclidean space|0XPR1E85W0]] $\R^k$ with $k \ge 2$.
Let there be $n$ voters, and let voter $i$ have an ideal point $p_i \in \R^k$ and Euclidean preferences: $x \succ_i y$ if and only if $\norm{x - p_i} < \norm{y - p_i}$.
Write $x \mathrel{M} y$ if more than half of the voters strictly prefer $x$ to $y$.
Assume that no point is undominated, that is, for every $z \in \R^k$ there is some $x$ with $x \mathrel{M} z$.
Then for any two points $x, y \in \R^k$ there is a finite sequence $x = z_0, z_1, \dots, z_m = y$ such that $z_{j+1} \mathrel{M} z_j$ for $j = 0, \dots, m - 1$.

## Remarks

The undominated points form the majority core; a point in the core is a [[Condorcet winner|WZYEADV8E1]] in a weak sense.
With an odd number $n \ge 3$ of voters in the plane, the core is nonempty only under strong symmetry conditions on the ideal points.
So the hypothesis holds for almost all configurations.
The theorem says that majority rule then has no structure at all: starting from any point, an agenda setter can reach any other point by a chain of majority votes.

Example: three voters with ideal points at the vertices of a triangle in $\R^2$ have no undominated point.
So an agenda can lead from the centroid to a point far outside the triangle.

In dimension $1$ the conclusion fails: by the [[median voter theorem|4J3G7Y0VYC]], with an odd number of voters the median ideal point is undominated.
The theorem was proved by McKelvey for Euclidean preferences and extended by Schofield to smooth preferences.

## Explanations

### L1 human

When voters judge proposals on several issues at once, majority voting usually has no stable winner.
Worse, a clever chair who picks the order of votes can lead the group from any proposal to any other, each step approved by a majority.
So the outcome may say more about the agenda than about the voters.

### L2 human

The theorem contrasts sharply with the one-dimensional median voter theorem.
It motivated the study of institutions, such as committee rules and agenda restrictions, that create stability where pure majority rule has none.
