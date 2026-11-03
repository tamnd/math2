---
tag: NMBY32JM60
kind: statement
role: theorem
name: Six-term exact sequence
msc: [46L80, 19K99]
uses: [BP86XQRZD2, 7NTVTHC7CG, XBVMWZJ5FF, 2VHFR8XFWK, JB7ZBFBA9C, KJKNJMGKZZ]
about: [BP86XQRZD2, 7NTVTHC7CG]
sources:
  - url: https://en.wikipedia.org/wiki/Operator_K-theory
---

## Statement

Let $0 \to I \xrightarrow{\iota} A \xrightarrow{\pi} B \to 0$ be a [[short exact sequence|KJKNJMGKZZ]] of C*-algebras and $*$-homomorphisms.
Let $\partial_1 \colon K_1(B) \to K_0(I)$ be the [[index map|XBVMWZJ5FF]].
Then there is a homomorphism $\partial_0 \colon K_0(B) \to K_1(I)$, the exponential map, such that the cyclic diagram
$$
\begin{array}{ccccc}
K_0(I) & \xrightarrow{\iota_*} & K_0(A) & \xrightarrow{\pi_*} & K_0(B) \\
\uparrow{\scriptstyle \partial_1} & & & & \downarrow{\scriptstyle \partial_0} \\
K_1(B) & \xleftarrow{\pi_*} & K_1(A) & \xleftarrow{\iota_*} & K_1(I)
\end{array}
$$
is [[exact|JB7ZBFBA9C]] at each of its six groups.
The maps $\partial_0$ and $\partial_1$ are natural with respect to morphisms of short exact sequences.

## Remarks

Half-exactness of $K_0$ and $K_1$ together with the index map give an exact sequence $K_1(I) \to K_1(A) \to K_1(B) \to K_0(I) \to K_0(A) \to K_0(B)$, which continues to the left with the groups $K_n = K_0 \circ S^n$ of suspensions.
[[Bott periodicity|2VHFR8XFWK]] identifies $K_{n+2}$ with $K_n$, and the long sequence folds into six terms; the exponential map is the index map of the suspended sequence composed with the Bott map.
Example: for $0 \to \mathcal{K} \to \mathcal{T} \to C(\mathbb{T}) \to 0$, the index map sends the generator $[z]$ of $K_1(C(\mathbb{T})) \cong \Z$ to a generator of $K_0(\mathcal{K}) \cong \Z$, and the sequence then gives $K_0(\mathcal{T}) \cong \Z$ and $K_1(\mathcal{T}) = 0$.
The sequence needs a genuine short exact sequence: exactness in the middle, $\ker \pi = \iota(I)$, is used to build the connecting maps.

## Explanations

### L1 human

When a C*-algebra $A$ is built from an ideal $I$ and a quotient $B$, the K-groups of the three algebras are tied together.
Six groups sit on a hexagon, and at each one the image of the incoming map is exactly the kernel of the outgoing map.
So if four of the groups and the maps are known, one can often compute the remaining two.

### L2 human

This is the main computational tool of operator K-theory, the analogue of the long exact sequence in homology for a pair of spaces.
For $A = C(X)$ and $I = C_0(X \setminus Y)$ with $Y$ a closed subset, it is the six-term sequence of topological K-theory for the pair $(X, Y)$.
The index map generalizes the Fredholm index.
The exponential map is named after its formula.
For unital $A$, let $p$ be a projection in $M_n(B)$ with self-adjoint lift $h \in M_n(A)$.
Then $e^{2 \pi i h}$ is a unitary over the unitization of $I$, and its class gives $\partial_0[p]$ up to a sign convention.
The Pimsner–Voiculescu sequence for crossed products by $\Z$ is derived from it.
