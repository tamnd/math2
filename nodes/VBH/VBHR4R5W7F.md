---
tag: VBHR4R5W7F
kind: concept
name: q-convex manifold
msc: [32F10]
sources:
  - url: https://en.wikipedia.org/wiki/Andreotti%E2%80%93Grauert_theorem
---

## Summary

A $q$-convex manifold is a complex manifold with a smooth exhaustion function whose [[Levi form|80MTNXWW80]] has many positive eigenvalues outside a compact set.
When this holds everywhere, the manifold is called $q$-complete.
For $q = 1$ one gets the strongly pseudoconvex manifolds and the Stein manifolds.
These classes measure how far a manifold is from being Stein, and the [[Andreotti–Grauert theorem|67RJ0S8F74]] controls their cohomology.

## Explanations

### L1 human

A Stein manifold has an exhaustion function that is convex in every complex direction.
A $q$-convex manifold has one that is convex at least in $n - q + 1$ independent complex directions at each point far out, where $n$ is the dimension.
So the larger $q$ is, the weaker the condition.
For example, $\C^n$ with the origin removed is not Stein when $n \ge 2$.
The function $\abs{z}^2 + 1/\abs{z}^2$ grows to infinity near the origin and near infinity, and its Levi form is positive in the radial direction $w = z$.
So $\C^n \setminus \set{0}$ is $n$-complete in the convention used here.
