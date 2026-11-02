---
tag: VZBYXH5995
kind: definition
name: Ehresmann connection
msc: [53C05]
defines: TD6VEP3SCE
uses: [CX4M8K61AB, WY6K3P4YCG, 6P9PXQDSEN]
sources:
  - url: https://en.wikipedia.org/wiki/Ehresmann_connection
---

## Definition

Let $\pi : E \to M$ be a smooth [[fibre bundle|CX4M8K61AB]], and let $TE$ be the [[tangent bundle|WY6K3P4YCG]] of $E$.
The *vertical bundle* is $V = \ker d\pi \subset TE$, where $d\pi$ is the [[differential|6P9PXQDSEN]] of $\pi$.
Its fibre $V_e$ is the tangent space at $e$ of the fibre through $e$.
An *Ehresmann connection* on $E$ is a smooth subbundle $H \subset TE$, the *horizontal bundle*, such that $T_eE = H_e \oplus V_e$ for every $e \in E$.

## Remarks

Since $d\pi_e$ is onto with kernel $V_e$, it restricts to an isomorphism $H_e \to T_{\pi(e)}M$.
So each tangent vector of $M$ has a unique horizontal lift at each point of the fibre above it.
Example: for the product bundle $E = M \times F$ with $\pi$ the first projection, $H_{(p, y)} = T_pM \times \set{0}$ is an Ehresmann connection; $V_{(p,y)} = \set{0} \times T_yF$, and the two are complementary.
Non-example: $H = TE$ fails the condition when the fibres have positive dimension, because $H_e \cap V_e = V_e \ne \set{0}$.
Equivalently, an Ehresmann connection is a smooth vector-valued $1$-form $\Phi$ on $E$ with $\Phi \circ \Phi = \Phi$ and image $V$; then $H = \ker \Phi$.
Horizontal lifts of curves exist locally; if the fibres are not compact they may fail to exist for all times.
On a vector bundle, the Ehresmann connections invariant under the scalings of the fibres and compatible with addition correspond to connections in the sense of covariant derivatives.
