---
tag: EXD1197NPH
kind: definition
name: Geometric morphism
msc: [18F10, 18B25]
defines: N5R1WAEPFB
uses: [6837RS7N82, TZHF6ZM92S, H4MY8JN8W4]
sources:
  - url: https://en.wikipedia.org/wiki/Topos
---

## Definition

Let $\mathcal{E}$ and $\mathcal{F}$ be [[toposes|6837RS7N82]].
A *geometric morphism* $f \colon \mathcal{E} \to \mathcal{F}$ is a pair of functors $f_* \colon \mathcal{E} \to \mathcal{F}$ and $f^* \colon \mathcal{F} \to \mathcal{E}$ such that:

1. $f^*$ is [[left adjoint|TZHF6ZM92S]] to $f_*$;
2. $f^*$ [[preserves finite limits|H4MY8JN8W4]].

The functor $f_*$ is the *direct image* and $f^*$ is the *inverse image* of $f$.

## Remarks

Example: let $g \colon X \to Y$ be a continuous map of topological spaces.
The direct image $g_* F(V) = F(g^{-1}(V))$ and the inverse image $g^*$ of sheaves form a geometric morphism $\mathrm{Sh}(X) \to \mathrm{Sh}(Y)$.
The inverse image preserves finite limits, because stalks of $g^*G$ are stalks of $G$ and finite limits of sheaves are computed stalkwise.
Non-example: on $\mathbf{Set}$, take $f^* = - \times A$ and $f_* = (-)^A$ for a set $A$ with two elements.
Then $f^* \dashv f_*$, but $f^*$ sends the terminal set $1$ to $A$, which is not terminal, so clause 2 fails.
For a topos $\mathcal{E}$, a *point* of $\mathcal{E}$ is a geometric morphism $\mathbf{Set} \to \mathcal{E}$.
Every Grothendieck topos has, up to isomorphism, exactly one geometric morphism to $\mathbf{Set}$.
