---
tag: FW83WPH44N
kind: definition
name: Kuratowski closure axioms
msc: [54A05]
defines: NS9VED3XG2
uses: [00E0YZCERH, 0CQHFPGJ45, 0QEAJB91GZ, 0ZCK8DQYN1]
sources:
  - url: https://en.wikipedia.org/wiki/Kuratowski_closure_axioms
---

## Definition

Let $X$ be a set and let $\mathcal{P}(X)$ be its [[power set|00E0YZCERH]].
A map $c \colon \mathcal{P}(X) \to \mathcal{P}(X)$ satisfies the *Kuratowski closure axioms* if, for all subsets $A, B \subseteq X$:

1. $c(\emptyset) = \emptyset$.
2. $A \subseteq c(A)$.
3. $c(c(A)) = c(A)$.
4. $c(A \cup B) = c(A) \cup c(B)$.

Such a map is a *closure operator* on $X$.

## Remarks

Given a closure operator $c$, the sets $F$ with $c(F) = F$ are the [[closed sets|0ZCK8DQYN1]] of a unique topology on $X$.
The [[closure|0QEAJB91GZ]] of each $A$ in this topology is $c(A)$.
Conversely, the closure in any [[topological space|0CQHFPGJ45]] satisfies the four axioms.
So closure operators on $X$ and topologies on $X$ correspond one to one.

Axiom 4 implies that $c$ is monotone: if $A \subseteq B$, then $c(A) \subseteq c(B) = c(A) \cup c(B \setminus A)$.

Example: on $\R$, let $c(A)$ be the set of limits of convergent sequences of points of $A$.
This $c$ is the usual closure, and it satisfies the four axioms.

Non-example: fix a point $x_0$ of a nonempty set $X$ and let $c(A) = A \cup \set{x_0}$.
Axioms 2, 3 and 4 hold, but $c(\emptyset) = \set{x_0} \ne \emptyset$, so axiom 1 fails.
