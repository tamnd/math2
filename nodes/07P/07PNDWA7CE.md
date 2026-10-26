---
tag: 07PNDWA7CE
kind: definition
name: Generalised eigenspace
msc: [15A18]
defines: 0AJ035ZTZE
uses: [0SAAHC36J9]
sources:
  - url: https://en.wikipedia.org/wiki/Generalized_eigenvector
    locator: Overview and definition
---

## Definition

Let $F$ be a field, let $V$ be a vector space over $F$, let $T \colon V \to V$ be an endomorphism, and let $\lambda \in F$.
The *generalised eigenspace* of $T$ for $\lambda$ is
$$V_\lambda = \{v \in V : (T - \lambda \id_V)^k (v) = 0 \text{ for some } k \ge 1\}.$$

## Remarks

It is a $T$-invariant subspace that contains the eigenspace $E_\lambda$.
If $\dim V = n$ is finite, then $V_\lambda = \ker (T - \lambda \id_V)^n$.
Its dimension is the [[algebraic multiplicity|0FY42N02DV]] of $\lambda$, in finite dimensions.
Its nonzero elements are the [[generalised eigenvectors|01H6QKWGDH]] for $\lambda$.

## Explanations

### L1 human

The generalised eigenspace is a larger version of the eigenspace.
It contains the vectors that become zero after we apply $T - \lambda \id$ several times.
These spaces always fill the space over $\C$, even when the eigenspaces do not.
