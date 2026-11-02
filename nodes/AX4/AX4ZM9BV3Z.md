---
tag: AX4ZM9BV3Z
kind: statement
role: theorem
name: Long exact sequence of a pair
msc: [55N10]
uses: [4BVWH0BN28, M0Q5CFJ7ZH, JB7ZBFBA9C, NJQMWVK3QK]
about: [4BVWH0BN28]
sources:
  - url: https://en.wikipedia.org/wiki/Relative_homology
---

## Statement

Let $X$ be a topological space and let $A \subseteq X$ be a subspace.
Let $i \colon A \to X$ be the inclusion and $j \colon (X, \emptyset) \to (X, A)$ the identity map seen as a map of pairs.
For $n \ge 1$ let $\partial \colon H_n(X, A) \to H_{n-1}(A)$ send the class of a relative cycle $c$ to the class of the cycle $\partial c$ in $A$.
Then the sequence of [[singular homology|M0Q5CFJ7ZH]] and [[relative homology|4BVWH0BN28]] groups
$$\cdots \to H_n(A) \xrightarrow{i_*} H_n(X) \xrightarrow{j_*} H_n(X, A) \xrightarrow{\partial} H_{n-1}(A) \xrightarrow{i_*} \cdots \to H_0(X) \xrightarrow{j_*} H_0(X, A) \to 0$$
is [[exact|JB7ZBFBA9C]].
It is natural with respect to maps of pairs.

## Remarks

The chain complexes form a short exact sequence $0 \to C_\bullet(A) \to C_\bullet(X) \to C_\bullet(X, A) \to 0$.
The long exact sequence in homology of a short exact sequence of chain complexes gives the result, and its connecting map is the $\partial$ above.
If $A$ is nonempty, the same sequence holds with [[reduced homology|NJQMWVK3QK]] $\tilde H_n(A)$ and $\tilde H_n(X)$ in place of $H_n(A)$ and $H_n(X)$.

Example: for $(D^n, S^{n-1})$ with $n \ge 1$, the disc has $\tilde H_k(D^n) = 0$ for all $k$.
Exactness of the reduced sequence then forces $\partial \colon H_k(D^n, S^{n-1}) \to \tilde H_{k-1}(S^{n-1})$ to be an isomorphism for every $k$.

## Explanations

### L1 human

The homology of a space, of a subspace, and of the space relative to the subspace are tied together in one long chain of maps.
At each spot, what one map kills is exactly what the previous map produces.
So knowing two of the three kinds of groups often determines the third.

### L2 human

This is the exactness axiom of the Eilenberg–Steenrod axioms.
Combined with excision, it computes the homology of spheres by induction on dimension, and it gives the long exact sequences behind cellular homology.
The same algebra gives a long exact sequence for a triple $B \subseteq A \subseteq X$ and, dually, for singular cohomology with the arrows reversed.
