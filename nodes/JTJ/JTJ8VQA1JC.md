---
tag: JTJ8VQA1JC
kind: definition
name: Fréchet algebra
msc: [46H05, 46A04]
defines: AW4T3NQYVF
uses: [3GAA614673, FP5GVCN8GV]
sources:
  - url: https://en.wikipedia.org/wiki/Fr%C3%A9chet_algebra
---

## Definition

Let $\mathbb{K}$ be $\R$ or $\C$.
A *Fréchet algebra* over $\mathbb{K}$ is an associative algebra $A$ over $\mathbb{K}$ with a topology such that:

1. $A$ with this topology is a [[Fréchet space|3GAA614673]], that is, a complete metrizable locally convex space;
2. the multiplication $A \times A \to A$, $(a, b) \mapsto ab$, is jointly continuous.

Let $(p_n)_{n \ge 1}$ be an increasing sequence of [[seminorms|FP5GVCN8GV]] defining the topology.
Then condition 2 holds if and only if for each $n$ there are $m \ge n$ and $C_n > 0$ with $p_n(ab) \le C_n \, p_m(a) \, p_m(b)$ for all $a, b \in A$.

## Remarks

The algebra is called *locally multiplicatively convex* (or m-convex) if the topology is given by seminorms with $p_n(ab) \le p_n(a) p_n(b)$.
Some authors include this condition in the definition.
Every Banach algebra is a Fréchet algebra, with the single seminorm given by the norm.

Example: $A = C(\R)$, the continuous complex functions on $\R$, with $p_n(f) = \max_{\abs{x} \le n} \abs{f(x)}$.
Each $p_n$ is a seminorm with $p_n(fg) \le p_n(f) p_n(g)$, and the sequence is increasing.
Convergence for all $p_n$ is uniform convergence on compact sets, and a locally uniform limit of continuous functions is continuous, so $A$ is complete.
So $C(\R)$ is an m-convex Fréchet algebra.

Non-example: the polynomials $\C[x]$ with the same seminorms satisfy every condition except completeness in clause 1.
The Taylor polynomials of $e^x$ form a Cauchy sequence for every $p_n$, but their limit $e^x$ is not a polynomial.
