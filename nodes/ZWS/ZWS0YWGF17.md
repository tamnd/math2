---
tag: ZWS0YWGF17
kind: statement
role: theorem
name: Weak Nullstellensatz
msc: [13A15, 14A05]
uses: [0PF6TM8TWT, 0SDC934R52, 0PV74TR5FP, 096Z9MP2ME]
about: [0PV74TR5FP, 0SDC934R52]
sources:
  - url: https://en.wikipedia.org/wiki/Hilbert's_Nullstellensatz
---

## Statement

Let $k$ be an [[algebraically closed field|0PF6TM8TWT]] and let $n \ge 1$.

1. The [[maximal ideals|0PV74TR5FP]] of the [[polynomial ring|0SDC934R52]] $k[x_1, \ldots, x_n]$ are exactly the ideals $\mathfrak{m}_a = (x_1 - a_1, \ldots, x_n - a_n)$ for $a = (a_1, \ldots, a_n) \in k^n$.
2. If $I$ is an [[ideal|096Z9MP2ME]] of $k[x_1, \ldots, x_n]$ with $I \ne k[x_1, \ldots, x_n]$, then there is $a \in k^n$ with $f(a) = 0$ for all $f \in I$.

## Remarks

Each $\mathfrak{m}_a$ is maximal, since it is the kernel of the surjective evaluation map $f \mapsto f(a)$ onto the field $k$.
Conversely, let $\mathfrak{m}$ be maximal; then $k[x_1, \ldots, x_n]/\mathfrak{m}$ is a field finitely generated as a $k$-algebra.
So it is finite over $k$ by [[Zariski's lemma|YBJ2VQHFDQ]], hence equal to $k$ as $k$ is algebraically closed.
If $a_i \in k$ is the image of $x_i$, then $\mathfrak{m} \supseteq \mathfrak{m}_a$, so $\mathfrak{m} = \mathfrak{m}_a$.
Part 2 follows from part 1: a proper ideal lies in a maximal ideal $\mathfrak{m}_a$, and then every $f \in I$ vanishes at $a$.

Example: over $\C$, the ideal $(x^2 + y^2 - 1, x - 1)$ of $\C[x, y]$ is proper and the point $(1, 0)$ is a common zero.

The field must be algebraically closed: over $\R$, the ideal $(x^2 + 1)$ of $\R[x]$ is maximal, but it has no zero in $\R$ and is not of the form $(x - a)$.

## Explanations

### L1 human

Over the complex numbers, a system of polynomial equations has no solution only when the equations imply $1 = 0$ by algebra.
In other words, the points of $\C^n$ are the same thing as the maximal ideals of the polynomial ring.

### L2 human

The weak form is the step from which the full [[Nullstellensatz|D85VZWS9QK]] follows by the Rabinowitsch trick.
It identifies the points of affine space with the maximal ideals of the coordinate ring.
This is the starting point for the maximal spectrum and, later, for schemes.
