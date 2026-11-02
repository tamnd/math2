---
tag: 7DWHFWF1D8
kind: definition
name: Elementary class
msc: ["03C52", "03C07"]
defines: MEC3ZMC4F1
uses: [WDVVEYD6AT, 983GZBQYT4, 92SWXST1ZM, MVCH6N9SNW]
sources:
  - url: https://en.wikipedia.org/wiki/Elementary_class
---

## Definition

Let $\sigma$ be a first-order [[signature|WDVVEYD6AT]].
Let $K$ be a class of [[$\sigma$-structures|983GZBQYT4]].
Then $K$ is an *elementary class* if there is a first-order [[theory|92SWXST1ZM]] $T$ in $\sigma$ whose [[models|MVCH6N9SNW]] are exactly the members of $K$.

## Remarks

If $T$ can be chosen finite, or equivalently a single sentence, $K$ is called a *basic elementary class*.
Some authors write $\mathrm{EC}$ for basic elementary classes and $\mathrm{EC}_\Delta$ for elementary classes.

Example: groups, in the signature $(\cdot, {}^{-1}, e)$, form a basic elementary class, axiomatized by the three group axioms.
Fields of characteristic $0$ form an elementary class, using the infinitely many axioms $1 + \cdots + 1 \ne 0$; it is not a basic elementary class.

Non-example: torsion groups do not form an elementary class.
Suppose $T$ axiomatized them.
Add a new constant $c$ and the sentences $c^n \ne e$ for all $n \ge 1$.
Each finite subset of this theory has a model, namely a finite cyclic group of large order with $c$ a generator.
By the [[compactness theorem|1NR3HAWG9D]] the whole theory has a model, which is a model of $T$ with an element of infinite order, a contradiction.
