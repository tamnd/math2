---
tag: 2PYANBGXFD
kind: concept
name: Path algebra
msc: [16G20, 16S10]
specializes: [3CTW1P4HBP]
sources:
  - url: https://en.wikipedia.org/wiki/Quiver_(mathematics)
---

## Summary

The path algebra $kQ$ of a [[quiver|RE9YFFS3TS]] $Q$ over a field $k$ is the vector space with basis the paths in $Q$.
Its multiplication is concatenation of paths.
For a quiver with finitely many vertices, its modules are the same as the [[representations of the quiver|TXVWFWP6VQ]].
Every finite-dimensional algebra over an algebraically closed field is Morita equivalent to a quotient of a path algebra by an ideal of relations.
This makes path algebras the basic examples of representation theory of finite-dimensional algebras.

## Explanations

### L1 human

A quiver is a set of dots joined by arrows.
A path is a walk along arrows, head to tail, and each dot also counts as a path of length zero.
To multiply two paths you join them if the end of the first is the start of the second, and otherwise the product is zero.
The quiver with one dot and one loop gives the polynomial ring $k[x]$, where $x^n$ is the walk around the loop $n$ times.
The quiver $1 \to 2$ with one arrow gives a three-dimensional algebra, isomorphic to the upper triangular $2 \times 2$ matrices.
