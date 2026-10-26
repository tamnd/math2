---
tag: 0EZBG8SKJM
kind: statement
role: theorem
name: Cantor's intersection theorem
msc: [54D30]
uses: [00R0X1WGPX, 0G5AV9Q4RR]
sources:
  - url: https://en.wikipedia.org/wiki/Cantor%27s_intersection_theorem
    locator: Topological statement
same_as:
  wikidata: Q858052
  wikipedia: Cantor's intersection theorem
---

## Statement

Let $X$ be a [[topological space|0CNQXVBHCX]].
Let $(C_n)_{n \ge 1}$ be a sequence of nonempty [[compact|00R0X1WGPX]] [[closed|0G5AV9Q4RR]] subsets of $X$ with $C_1 \supseteq C_2 \supseteq C_3 \supseteq \cdots$.
Then the intersection $\bigcap_{n \ge 1} C_n$ is not empty.

## Remarks

The sets must be compact: in $\mathbb{R}$, the closed sets $[n, \infty)$ are nested and nonempty, but their intersection is empty.
For $X = \mathbb{R}$, the sets can be nested closed bounded intervals $[a_n, b_n]$.
There is a variant for metric spaces. A metric space is [[complete|08EWT7J0SC]] if and only if each nested sequence of nonempty closed sets whose [[diameters|0692CGQF00]] tend to $0$ has nonempty intersection. The intersection is then one point.

## Explanations

### L1 human

If you have a chain of nonempty compact sets, each inside the one before, at least one point is in all of them.
For example, the intervals $[0, 1/n]$ are nested, and $0$ is in all of them.
