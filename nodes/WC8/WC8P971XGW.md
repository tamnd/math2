---
tag: WC8P971XGW
kind: concept
name: Sparse approximation
msc: [41A46, 94A12, 65F50]
specializes: [YS1GRQRVY7]
sources:
  - url: https://en.wikipedia.org/wiki/Sparse_approximation
same_as:
  wikidata: Q28684319
  wikipedia: Sparse approximation
---

## Summary

Let $A$ be a matrix with more columns than rows and let $b$ be a vector.
Sparse approximation looks for a vector $x$ with few nonzero entries such that $Ax$ is close to $b$.
The columns of $A$ form a redundant dictionary, so $b$ has many representations, and one wants the sparsest.
The exact problem is NP-hard in general.
In practice one uses greedy methods such as [[matching pursuit|8KJ9P9KQ5H]], or convex relaxations such as basis pursuit and the [[Lasso|KZ226116HW]].
It is the core of signal compression, denoising and [[compressed sensing|6V8E0AQNHA]].

## Explanations

### L1 human

Think of the columns of a [[matrix|0VD9ZSWWJG]] $A$ as building blocks, and of $b$ as a signal to build.
When there are more blocks than dimensions, the [[system of linear equations|0GT4WWGWH2]] $Ax = b$ has many solutions.
Sparse approximation asks for a solution, or a near solution, that uses as few blocks as possible.
For example, with $A = \begin{pmatrix} 1 & 0 & 1 \\ 0 & 1 & 1 \end{pmatrix}$ and $b = (1, 1)$, both $x = (1, 1, 0)$ and $x = (0, 0, 1)$ solve $Ax = b$.
The second one uses a single column, so it is the sparsest solution.
