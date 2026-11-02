---
tag: W57F9ENPMV
kind: definition
name: Split exact sequence
msc: [18G35, "18E10"]
defines: 1ZPMDE4ARK
uses: [KJKNJMGKZZ, Y9CZ3MTNF1, BZEJKTQ76T]
sources:
  - url: https://en.wikipedia.org/wiki/Split_exact_sequence
---

## Definition

Let $\mathcal{A}$ be an [[abelian category|Y9CZ3MTNF1]] and let $0 \to A \xrightarrow{f} B \xrightarrow{g} C \to 0$ be a [[short exact sequence|KJKNJMGKZZ]] in $\mathcal{A}$.
Let $A \oplus C$ be the [[biproduct|BZEJKTQ76T]] of $A$ and $C$, with inclusion $i_A \colon A \to A \oplus C$ and projection $p_C \colon A \oplus C \to C$.
The sequence is *split* if there is an isomorphism $h \colon B \to A \oplus C$ with $h \circ f = i_A$ and $p_C \circ h = g$.

## Remarks

Equivalently, there is a morphism $t \colon B \to A$ with $t \circ f = 1_A$, or there is a morphism $u \colon C \to B$ with $g \circ u = 1_C$.
Every additive functor sends a split exact sequence to a split exact sequence.

Example: $0 \to \Z \xrightarrow{i} \Z \oplus \Z/2\Z \xrightarrow{p} \Z/2\Z \to 0$, with $i(n) = (n, 0)$ and $p(n, a) = a$, is split.
Take $h$ to be the identity of $\Z \oplus \Z/2\Z$; then $h \circ i = i_A$ and $p_C \circ h = p$.

Non-example: $0 \to \Z \xrightarrow{2} \Z \to \Z/2\Z \to 0$ is short exact but not split.
A split sequence would give an isomorphism $\Z \cong \Z \oplus \Z/2\Z$, but $\Z$ has no nonzero element of finite order.
