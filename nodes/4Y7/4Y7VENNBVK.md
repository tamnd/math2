---
tag: 4Y7VENNBVK
kind: concept
name: Approximately finite-dimensional C*-algebra
msc: [46L05, 46L35]
sources:
  - url: https://en.wikipedia.org/wiki/Approximately_finite-dimensional_C*-algebra
same_as:
  wikidata: Q291562
  wikipedia: Approximately finite-dimensional C*-algebra
---

## Summary

An approximately finite-dimensional (AF) C\*-algebra is a C*-algebra that is the closure of an increasing sequence of finite-dimensional C\*-subalgebras.
Finite-dimensional C\*-algebras are finite direct sums of matrix algebras, so an AF algebra is built from matrices by a limit process.
Bratteli described AF algebras by diagrams, and Elliott classified them by their ordered K_0 groups.
Examples are the compact operators, the UHF algebras such as the CAR algebra, and $C(X)$ for the Cantor set $X$.

## Explanations

### L1 human

Start with a matrix algebra, put it inside a bigger matrix algebra, then a bigger one, and so on, and take the closure of the union.
The resulting algebra is usually infinite-dimensional, but every element is a limit of matrices of finite size.
For example, $M_2 \subset M_4 \subset M_8 \subset \cdots$, with each matrix $a$ sent to the block matrix $\operatorname{diag}(a, a)$, gives the CAR algebra used for fermions in physics.
