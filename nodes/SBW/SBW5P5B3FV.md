---
tag: SBW5P5B3FV
kind: definition
name: F-space
msc: [46A16]
defines: 86BYEV9AX8
uses: [063W5JMY85, 08EWT7J0SC]
sources:
  - url: https://en.wikipedia.org/wiki/F-space
---

## Definition

Let $\mathbb{K}$ be $\R$ or $\C$, and let $E$ be a topological vector space over $\mathbb{K}$.
$E$ is an *F-space* if there is a [[metric|063W5JMY85]] $d$ on $E$ such that:

1. $d$ induces the topology of $E$.
2. $d$ is translation-invariant: $d(x + z, y + z) = d(x, y)$ for all $x, y, z \in E$.
3. The metric space $(E, d)$ is [[complete|08EWT7J0SC]].

## Remarks

Some authors use the name for a vector space with a metric satisfying 2 and 3 for which addition and scalar multiplication are continuous; this is the same notion.
Example: every Banach space is an F-space with $d(x, y) = \norm{x - y}$; this metric induces the norm topology, it is translation-invariant since $(x + z) - (y + z) = x - y$, and it is complete by definition of a Banach space.
Example: for $0 < p < 1$, $L^p([0, 1])$ with $d(f, g) = \int_0^1 \abs{f - g}^p$ is an F-space that is not locally convex.
Non-example: the space $c_{00}$ of finitely supported real sequences with $d(x, y) = \sup_n \abs{x_n - y_n}$ satisfies 1 and 2 but not 3: the sequences $x^{(k)} = (1, 1/2, \ldots, 1/k, 0, 0, \ldots)$ are Cauchy and have no limit in $c_{00}$.
Every metrizable topological vector space has a translation-invariant metric inducing its topology, so condition 2 matters only together with condition 3.
