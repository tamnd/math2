---
tag: CJSGE7JSGH
kind: statement
role: theorem
name: K-theory of finite fields
msc: [19D50, 19D06]
uses: [0ZXZ82FTX2, 5GVFZWMWC8, 0KVGH0J5B3, BK3091CPGF, XFGZFM8PC6]
about: [5GVFZWMWC8, 0ZXZ82FTX2]
sources:
  - url: https://en.wikipedia.org/wiki/Algebraic_K-theory
---

## Statement

Let $q$ be a prime power and let $\F_q$ be the [[finite field|0ZXZ82FTX2]] with $q$ elements.
Then the [[algebraic K-groups|5GVFZWMWC8]] of $\F_q$ are $K_0(\F_q) \cong \Z$ and, for every integer $i \ge 1$,
$$K_{2i}(\F_q) = 0, \qquad K_{2i-1}(\F_q) \cong \Z/(q^i - 1),$$
a [[cyclic group|0KVGH0J5B3]] of order $q^i - 1$.

## Remarks

The theorem is due to Quillen.
He used Brauer lifting to build a map from $BGL(\F_q)$ to a space $F\Psi^q$.
This space is the homotopy fibre of the map $\psi^q - 1$ on the space $BU$ of topological K-theory, where $\psi^q$ is an Adams operation.
He computed the homology of the groups $GL_n(\F_q)$ and showed that this map induces an isomorphism in homology, so that $BGL(\F_q)^+ \simeq F\Psi^q$, the [[plus construction|XFGZFM8PC6]] of [[$BGL(\F_q)$|BK3091CPGF]].
The homotopy groups of $F\Psi^q$ come from the long exact sequence of the fibration and Bott periodicity: $\psi^q$ acts on $\pi_{2i}(BU) \cong \Z$ by multiplication by $q^i$.

Check in low degrees: $K_1(\F_q) = \F_q^\times$ is cyclic of order $q - 1$, as the formula says for $i = 1$.
Also $K_2(\F_q) = 0$, which agrees with the classical fact that every Steinberg symbol over a finite field is trivial.
For $q = 2$ the formula gives $K_3(\F_2) \cong \Z/3$.

## Explanations

### L1 human

Finite fields are the first rings whose higher K-groups were completely computed.
The answer is very regular: the even groups vanish and the odd group in degree $2i - 1$ is cyclic of order $q^i - 1$.
It was found by comparing invertible matrices over $\F_q$ with the topology of vector bundles.

### L2 human

The computation is a model for the whole subject: Quillen's plus construction turns a problem about the homology of the groups $GL_n(\F_q)$ into a homotopy computation.
It feeds into many later results, for example the localization sequence for rings of integers, whose terms include the K-groups of the residue fields.
It also gives the K-theory of the algebraic closure of $\F_p$, by passing to the colimit over the fields $\F_{p^m}$.
