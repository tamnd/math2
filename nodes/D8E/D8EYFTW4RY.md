---
tag: D8EYFTW4RY
kind: definition
name: Commutative diagram
msc: [18A10]
defines: WV898P4X16
uses: [A2DE66937D, 859F0TFVA3]
sources:
  - url: https://en.wikipedia.org/wiki/Commutative_diagram
---

## Definition

Let $\mathcal{C}$ be a [[category|A2DE66937D]].
A *diagram* in $\mathcal{C}$ is a directed graph with each vertex labelled by an object and each edge labelled by a [[morphism|859F0TFVA3]] of $\mathcal{C}$.
An edge from a vertex labelled $A$ to a vertex labelled $B$ must be labelled by a morphism $A \to B$.
The composite of a directed path of edges $e_1, \dots, e_n$ with $n \ge 1$ and labels $f_1, \dots, f_n$ is $f_n \circ \dots \circ f_1$.
The diagram *commutes* if any two directed paths of length at least $1$ with the same start and the same end have the same composite.

## Remarks

Example: the square with vertices $A, B, C, D$ and edges $f \colon A \to B$, $g \colon B \to D$, $h \colon A \to C$, $k \colon C \to D$ commutes exactly when $g \circ f = k \circ h$.
For instance, in the category of sets with $A = B = C = D = \R$, the maps $f = k = (x \mapsto 2x)$ and $g = h = (x \mapsto 3x)$ give a commuting square, since both composites are $x \mapsto 6x$.
Non-example: with $f = k = (x \mapsto x + 1)$ and $g = h = (x \mapsto 2x)$, the square does not commute.
Indeed $g(f(x)) = 2x + 2$ while $k(h(x)) = 2x + 1$.
In practice one only asks for commutativity of the paths that the text names.
For a diagram with a loop $f$, the convention above would force $f = f \circ f$.
More formally, a diagram of shape $J$ is a functor from a category $J$ to $\mathcal{C}$.
