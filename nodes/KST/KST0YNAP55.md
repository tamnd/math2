---
tag: KST0YNAP55
kind: definition
name: Measure algebra
msc: [28A60, "06E10"]
defines: YZA1V04R96
uses: [0XADJKM699, PR11BZQQPG]
sources:
  - url: https://en.wikipedia.org/wiki/Measure_algebra
---

## Definition

A *measure algebra* is a pair $(\mathfrak{A}, \mu)$ such that:

1. $\mathfrak{A}$ is a [[Boolean algebra|0XADJKM699]] in which every countable subset has a supremum.
2. $\mu \colon \mathfrak{A} \to [0, \infty]$ satisfies $\mu(0) = 0$.
3. $\mu\left(\bigvee_{k} a_k\right) = \sum_k \mu(a_k)$ for every sequence $(a_k)_{k \in \N}$ of pairwise disjoint elements, that is, $a_j \wedge a_k = 0$ for $j \ne k$.
4. $\mu(a) > 0$ for every $a \ne 0$.

## Remarks

Example: let $(X, \Sigma, \nu)$ be a [[measure space|P15VQS5DJ9]] and $\mathcal{N} = \set{E \in \Sigma : \nu(E) = 0}$.
Call $E, F \in \Sigma$ equivalent when $\nu(E \mathbin{\triangle} F) = 0$.
The classes form a Boolean algebra $\Sigma / \mathcal{N}$ with countable suprema given by countable unions, and $\mu([E]) = \nu(E)$ is well defined.
Clauses 2 and 3 come from the measure $\nu$, and clause 4 holds since $[E] \ne 0$ means $\nu(E) > 0$.

Non-example: the [[sigma-algebra|0SV8K0TDGY]] of Borel subsets of $\R$ with Lebesgue measure satisfies clauses 1 to 3 but not 4.
The set $\set{0}$ is a nonzero element of measure $0$.

The quotient in the example is called the measure algebra of $(X, \Sigma, \nu)$.
