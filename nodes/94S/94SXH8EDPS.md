---
tag: 94SXH8EDPS
kind: definition
name: Cartan matrix of an algebra
msc: [16G10, 20C20]
defines: ZBQ4KRC98K
uses: [3CTW1P4HBP, BFFA03GE3V, E2P29GCD9T, G00C22AEDH, 0PHTC93M58, XA0DCNH7WY]
sources:
  - url: https://en.wikipedia.org/wiki/Cartan_matrix
---

## Definition

Let $K$ be a field and let $A$ be a finite-dimensional [[associative algebra|3CTW1P4HBP]] over $K$.
Let $P_1, \dots, P_n$ be representatives of the isomorphism classes of [[indecomposable|E2P29GCD9T]] [[projective|BFFA03GE3V]] left $A$-modules.
Let $S_i = P_i / JP_i$, where $J$ is the [[Jacobson radical|XA0DCNH7WY]] of $A$; then $S_1, \dots, S_n$ represent the isomorphism classes of [[simple|G00C22AEDH]] left $A$-modules.
The *Cartan matrix* of $A$ is the $n \times n$ integer matrix $C = (c_{ij})$.
Here $c_{ij}$ is the number of times $S_j$ occurs among the [[composition factors|0PHTC93M58]] of $P_i$.

## Remarks

Example: $A = K[x]/(x^2)$ has the single indecomposable projective $P_1 = A$, with composition series $0 \subset (x) \subset A$.
Both factors are the simple module $K$, so $C = (2)$.
Example: for the algebra $T_2(K)$ of upper triangular $2 \times 2$ matrices, $P_1 = K E_{11}$ is simple and $P_2 = K E_{12} + K E_{22}$ has the factors $S_2$ on top and $S_1$ below, so $C = \begin{pmatrix} 1 & 0 \\ 1 & 1 \end{pmatrix}$.
Non-example: the polynomial ring $K[x]$ is not finite-dimensional, and its projective module $K[x]$ has no composition series, so it has no Cartan matrix in this sense.
Some authors use the transpose of $C$.
If $K$ is a splitting field for $A$, for example algebraically closed, then $c_{ij} = \dim_K \Hom_A(P_j, P_i)$.
For the group algebra $KG$ of a finite group over a splitting field of characteristic $p$, Brauer showed that $C = D^{T} D$, where $D$ is the decomposition matrix, so $C$ is symmetric.
