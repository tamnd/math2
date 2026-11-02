---
tag: CS7TWHY7JM
kind: problem
name: Moment problem
msc: [44A60, 47A57]
uses: [PR11BZQQPG, 0G9EKM0E15, 01XAHPADBA]
about: [01XAHPADBA, PR11BZQQPG]
sources:
  - url: https://en.wikipedia.org/wiki/Moment_problem
same_as:
  wikidata: Q3406268
  wikipedia: Moment problem
history:
  posed_by: "Thomas Joannes Stieltjes"
  first_stated: "1894"
---

## Problem

Let $K$ be a closed subset of $\R$ and let $(m_n)_{n \ge 0}$ be a [[sequence|0G9EKM0E15]] of real numbers.

1. Existence: decide whether there is a positive Borel [[measure|PR11BZQQPG]] $\mu$ on $\R$ with support in $K$ and the following property. Every $x^n$ is $\mu$-integrable and $m_n = \int x^n \, d\mu(x)$ for all $n \ge 0$.
2. Uniqueness: when such a measure exists, decide whether it is the only one.

The numbers $m_n$ are then the [[moments|01XAHPADBA]] of $\mu$.

## Remarks

The classical cases are named after the set $K$.
For $K = \R$ it is the [[Hamburger moment problem|TBNCFXTMMW]], for $K = [0, \infty)$ the [[Stieltjes moment problem|Y9KH8P9JC0]], and for $K = [0, 1]$ the [[Hausdorff moment problem|G7VG61YD4J]].
For these three cases the existence question is solved by positivity conditions on Hankel matrices built from the moments, or on differences of the sequence for $[0, 1]$.
For compact $K$ the measure is unique when it exists, since polynomials are dense in the continuous functions on $K$.
For unbounded $K$ uniqueness can fail; the log-normal distribution is the standard example.
Many variants are studied: finitely many moments (the truncated problem), measures on $\R^d$, and the trigonometric problem on the circle.

## Explanations

### L1 human

The moments of a mass distribution are its total mass, its average position, its average squared position, and so on.
The moment problem runs the other way: given a list of numbers, is there a distribution with exactly these moments, and is there only one?
The answer depends on where the mass may sit, on a bounded interval, a half-line or the whole line.
It matters in probability, where one often knows the moments of a random variable and wants to identify its law.
