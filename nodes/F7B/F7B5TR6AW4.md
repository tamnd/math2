---
tag: F7B5TR6AW4
kind: definition
name: Bel–Robinson tensor
msc: ["83C05", "83C40", "53B30"]
defines: WB1FW655PG
uses: [D1SYF8F8RQ, WD15XKXW46, 1Y4WX4XQWJ]
sources:
  - url: https://en.wikipedia.org/wiki/Bel%E2%80%93Robinson_tensor
---

## Definition

Let $(M, g)$ be a four-dimensional oriented [[Lorentzian manifold|D1SYF8F8RQ]] with volume form $\epsilon_{abcd}$, and let $C_{abcd}$ be its [[Weyl tensor|WD15XKXW46]].
Let ${}^*C_{abcd} = \tfrac12 \epsilon_{abef} C^{ef}{}_{cd}$ be the [[Hodge dual|1Y4WX4XQWJ]] of $C$ on its first pair of indices.
The *Bel–Robinson tensor* of $(M, g)$ is the tensor field
$$T_{abcd} = C_{aecf} \, C_b{}^e{}_d{}^f + {}^*C_{aecf} \, {}^*C_b{}^e{}_d{}^f.$$

## Remarks

The tensor $T_{abcd}$ is totally symmetric and trace-free in every pair of indices.
If the Ricci tensor of $g$ vanishes, then the Bianchi identities give $\nabla^a T_{abcd} = 0$.
For future-pointing causal vectors $u, v, w, x$ one has $T_{abcd} u^a v^b w^c x^d \ge 0$.
Example: for the Schwarzschild metric the Weyl tensor is nonzero outside the singularity, so $T_{abcd} u^a u^b u^c u^d > 0$ for a static observer with four-velocity $u$.
By contrast, in Minkowski space $C_{abcd} = 0$, so $T_{abcd} = 0$.
In a vacuum the Weyl tensor equals the Riemann tensor, and then $T_{abcd}$ is often written with $R_{abcd}$ in place of $C_{abcd}$.

## Explanations

### L1 human

The Bel–Robinson tensor is the square of the Weyl curvature, arranged so that it behaves like an energy density.
