---
tag: AE979FBMPD
kind: statement
role: theorem
name: Jordan–von Neumann–Wigner classification
msc: [17C20, 17C55, 17C90]
uses: [WYE4E80T43, ZDZ6FAAGAF, 1MSMVDRAVD, 0P17NGQQMQ, 0GE4DVQKR8, 1HRMT3DSX2]
about: [WYE4E80T43]
sources:
  - url: https://en.wikipedia.org/wiki/Jordan_algebra
---

## Statement

Let $J$ be a finite-dimensional [[formally real Jordan algebra|WYE4E80T43]] over $\R$.
Then $J$ is a direct sum of simple ideals, and this decomposition is unique up to order.
For $\mathbb{K} = \R, \C, \mathbb{H}$, let $H_n(\mathbb{K})$ be the [[Hermitian|0P17NGQQMQ]] $n \times n$ matrices over $\mathbb{K}$ with $X \circ Y = \frac{1}{2}(XY + YX)$, where $\mathbb{H}$ is the [[quaternions|0GE4DVQKR8]].
Each simple ideal of $J$ is isomorphic to exactly one of the following algebras:

1. the real numbers $\R$;
2. the [[spin factor|ZDZ6FAAGAF]] $\R \oplus \R^n$ for some $n \ge 2$;
3. $H_n(\R)$, $H_n(\C)$ or $H_n(\mathbb{H})$ for some $n \ge 3$;
4. the [[Albert algebra|1MSMVDRAVD]] $H_3(\mathbb{O})$ of Hermitian $3 \times 3$ matrices over the [[octonions|1HRMT3DSX2]].

## Remarks

Proof idea: a finite-dimensional formally real Jordan algebra has a unit and a positive definite trace form, so ideals have orthogonal complements that are again ideals.
This gives the decomposition into simple ideals.
A simple algebra is then studied through a complete system of orthogonal primitive idempotents and the Peirce decomposition it induces.
With two idempotents one gets a spin factor.
With at least three idempotents the off-diagonal spaces carry a composition algebra, which is $\R$, $\C$, $\mathbb{H}$ or $\mathbb{O}$ by Hurwitz's theorem.
The octonions occur only with exactly three idempotents, because they are not associative.

Example: the Hermitian $2 \times 2$ complex matrices form a simple formally real Jordan algebra of dimension $4$.
In the list it appears as the spin factor $\R \oplus \R^3$, with the Pauli matrices as an orthonormal basis of $\R^3$.
Similarly $H_2(\R)$, $H_2(\C)$ and $H_2(\mathbb{H})$ are the spin factors with $n = 2, 3, 5$, which is why item 3 starts at $n = 3$.

## Explanations

### L1 human

Jordan, von Neumann and Wigner looked for algebras that could describe the observables of quantum mechanics without using non-observable matrix products.
They found that, in finite dimension, every such algebra is built from a short list of pieces.
The pieces are Hermitian matrices over the real numbers, complex numbers or quaternions, the spin factors, and one exceptional $27$-dimensional algebra.
So, apart from the exceptional piece, these algebras come from ordinary matrices.

### L2 human

The theorem is the Jordan analogue of the classification of compact simple Lie groups, and the two are linked.
The automorphism groups of the simple pieces are compact Lie groups, for example $F_4$ for the Albert algebra.
Through the [[Koecher–Vinberg theorem|PXXEWA9V2S]], the list also classifies the irreducible symmetric cones, such as the cone of positive definite matrices and the Lorentz cone.
The same list of simple pieces classifies the simple Euclidean Jordan algebras, since these are the same as the simple formally real ones.
