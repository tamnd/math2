---
tag: SGHMSBHHA0
kind: statement
role: theorem
name: Excision theorem
msc: [55N10, 55N40]
uses: [4BVWH0BN28, M0Q5CFJ7ZH, 0QEAJB91GZ, 0RZH6W98HK, J5DZEYCEX2, NJQMWVK3QK]
about: [4BVWH0BN28]
sources:
  - url: https://en.wikipedia.org/wiki/Excision_theorem
same_as:
  wikidata: Q3526998
  wikipedia: Excision theorem
---

## Statement

Let $X$ be a topological space and let $A \subseteq X$ be a subspace.
Let $Z \subseteq A$ be a subset whose [[closure|0QEAJB91GZ]] in $X$ is contained in the [[interior|0RZH6W98HK]] of $A$.
Then the inclusion of pairs $(X \setminus Z, A \setminus Z) \to (X, A)$ induces isomorphisms of [[relative homology|4BVWH0BN28]] groups
$$H_n(X \setminus Z, A \setminus Z) \to H_n(X, A)$$
for every $n \ge 0$.

## Remarks

An equivalent form: if $A, B \subseteq X$ are subspaces whose interiors cover $X$, then the inclusion $(B, A \cap B) \to (X, A)$ induces isomorphisms on all $H_n$.
The proof uses repeated [[barycentric subdivision|J5DZEYCEX2]] to show that every singular chain is homologous to a sum of small simplices, each lying in the interior of $A$ or in $X \setminus Z$.
The chains made of such small simplices compute the same homology as all chains, and on them the excision map is an isomorphism at chain level.

Example: if $A$ is a nonempty closed subspace that is a deformation retract of some open neighbourhood in $X$, then excision gives $H_n(X, A) \cong \tilde H_n(X / A)$, where $\tilde H$ is [[reduced homology|NJQMWVK3QK]].
For $(D^n, S^{n-1})$ this gives $H_n(D^n, S^{n-1}) \cong \tilde H_n(S^n)$.

The closure hypothesis is needed.
Take $X = [-1, 1]$, $A = [0, 1]$ and $Z = A$; the closure of $Z$ is not inside the interior $(0, 1]$ of $A$.
Then $H_0(X \setminus Z, A \setminus Z) = H_0([-1, 0)) \cong \Z$, while $H_0(X, A) = 0$ because $X$ is path-connected and $A$ is nonempty.

## Explanations

### L1 human

Relative homology of $X$ modulo $A$ only depends on what happens near and outside $A$.
So one can cut away a piece deep inside $A$ without changing it.
This turns a hard global computation into a local one, for example the homology near a single point.

### L2 human

Excision is one of the Eilenberg–Steenrod axioms, and it is the axiom that fails for homotopy groups.
With the long exact sequence of a pair it gives the Mayer–Vietoris sequence and the suspension isomorphism $\tilde H_n(X) \cong \tilde H_{n+1}(\Sigma X)$.
For manifolds it gives $H_n(M, M \setminus \set{x}) \cong H_n(\R^n, \R^n \setminus \set{0}) \cong \Z$, the starting point of orientations.
