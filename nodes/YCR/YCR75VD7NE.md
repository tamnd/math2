---
tag: YCR75VD7NE
kind: definition
name: Algebraic K-theory of spaces
msc: [19D10, 57Q10, 55P42]
defines: 7TNSX75XTP
uses: [X7JG1QEB9Q, ZPNXVVZY1J, 0CQHFPGJ45, 5W95QFHXPR]
sources:
  - url: https://en.wikipedia.org/wiki/Algebraic_K-theory
---

## Definition

Let $X$ be a [[topological space|0CQHFPGJ45]].
A *retractive space* over $X$ is a space $Y$ with maps $s \colon X \to Y$ and $r \colon Y \to X$ such that $r \circ s = \id_X$.
A map of retractive spaces is a map $Y \to Y'$ that commutes with the maps $s$ and with the maps $r$.
The retractive space $Y$ is *finite* if $Y$ is obtained from $s(X)$ by attaching finitely many cells.
Then $(Y, X)$ is a finite relative [[CW complex|5W95QFHXPR]].
Let $R_f(X)$ be the category of finite retractive spaces over $X$.
Make it a [[Waldhausen category|X7JG1QEB9Q]] as follows:

1. the cofibrations are the maps isomorphic to the inclusion of a relative CW subcomplex;
2. the weak equivalences are the maps that are weak homotopy equivalences of underlying spaces.

The *algebraic K-theory of $X$* is the space $A(X) = \Omega \abs{w S_\bullet R_f(X)}$, where $S_\bullet$ is the [[Waldhausen S-construction|ZPNXVVZY1J]] and $w$ denotes the subcategory of weak equivalences.

## Remarks

Iterating the $S$-construction makes $A(X)$ the zeroth space of a spectrum, also written $A(X)$.
The construction is a homotopy functor of $X$.
Example: for $X$ a point, $R_f(\ast)$ is the category of finite pointed CW complexes, and $A(\ast)$ is the K-theory of the sphere spectrum.
For connected $X$, Waldhausen showed that $A(X)$ is equivalent to the K-theory of the ring spectrum $\Sigma^\infty_+ \Omega X$.
Taking cellular chains gives a linearization map $A(X) \to K(\Z[\pi_1 X])$ to the K-theory of the group ring.
Non-example: if the cell condition is dropped, the category of all retractive spaces admits an Eilenberg swindle by infinite wedges, and its K-theory is trivial.
The stable parametrized h-cobordism theorem of Waldhausen, Jahren and Rognes relates $A(X)$ to the stable smooth h-cobordism space of $X$.
