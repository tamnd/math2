---
tag: Y4AQFH6N3Y
kind: definition
name: Multialgebra
msc: [08A99, 20N20]
defines: 3C930MVM0T
uses: [0SJ3RX9TXA, 00E0YZCERH, MSXX2P86CY, 09CEDJYBKP]
sources:
  - url: https://en.wikipedia.org/wiki/Hyperstructure
---

## Definition

Let $\Sigma$ be a signature, a set of function symbols each with an [[arity|MSXX2P86CY]] $n \ge 0$.
For a [[set|0SJ3RX9TXA]] $A$, let $\mathcal{P}^*(A)$ be the set of nonempty subsets of $A$, a part of the [[power set|00E0YZCERH]].
A *multialgebra* of signature $\Sigma$ is a set $A$ together with a map $f^A \colon A^n \to \mathcal{P}^*(A)$ for each symbol $f \in \Sigma$ of arity $n$.
Here $A^n$ is the [[Cartesian power|09CEDJYBKP]] of $A$.
Each map $f^A$ is a *multioperation* on $A$.

## Remarks

An ordinary algebra is the same as a multialgebra in which every value $f^A(a_1, \dots, a_n)$ has exactly one element.
Some authors allow the empty set as a value; then partial algebras are also multialgebras.

Example: $A = \R$ with the binary multioperation $x \circ y = [\min(x, y), \max(x, y)]$.
Each value is a closed interval that contains $x$, so it is nonempty.

Non-example: $A = \set{0, 1, 2}$ with $x \circ y = \set{z \in A : z > x + y}$.
For $x = y = 1$ the value is $\set{z \in A : z > 2} = \emptyset$, so $\circ$ is not a multioperation in the sense above.
