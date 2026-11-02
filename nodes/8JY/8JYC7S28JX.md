---
tag: 8JYC7S28JX
kind: definition
name: Root-finding algorithm
msc: [65H05, 65H04]
defines: TR4CNS5PMJ
uses: [0X3WGX95FE, 04CC6K5VDT, 05M5SWSZZD, YWZQC5E54B]
sources:
  - url: https://en.wikipedia.org/wiki/Root-finding_algorithm
---

## Definition

Let $D \subseteq \R^n$ and let $f \colon D \to \R^n$ be a [[continuous function|0X3WGX95FE]]; the case $n = 1$ is the most common, and $\C$ may replace $\R$.
A *zero* (or *root*) of $f$ is a point $r \in D$ with $f(r) = 0$.
A *root-finding algorithm* is a procedure that takes $f$ and starting data.
It produces a [[sequence|04CC6K5VDT]] $(x_k)$ in $D$, or a sequence of nested sets containing a zero.
It uses $f$ only through values of $f$ and possibly of its derivatives.
It is designed so that $(x_k)$ has a zero of $f$ as its [[limit|05M5SWSZZD]], or so that the sets shrink to a zero.

## Remarks

Example: the iteration $x_{k+1} = x_k - (x_k^2 - 2)/(2x_k)$ from $x_0 = 1$ gives $1, 1.5, 1.41667, 1.414216, \ldots$, which tends to the zero $\sqrt{2}$ of $f(x) = x^2 - 2$.
Non-example: the iteration $x_{k+1} = 2/x_k$ from $x_0 = 1$ oscillates between $1$ and $2$, so it does not tend to a zero of $x^2 - 2$, although $\sqrt{2}$ is its fixed point.
An algorithm is *globally convergent* on a class of functions if it converges from every admissible start, and *locally convergent* if it converges from starts close enough to a zero.
Its speed is measured by its order of convergence, see [[rate of convergence|YWZQC5E54B]].
