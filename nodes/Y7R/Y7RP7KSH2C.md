---
tag: Y7RP7KSH2C
kind: definition
name: Canonical height
msc: [37P30, 11G50]
defines: C55ST3TH02
uses: [F1FF505PWH, ZT9A6JK8QF, MWBDFS2KJ5, BE4X0QG8XW]
sources:
  - url: https://en.wikipedia.org/wiki/Néron–Tate_height
---

## Definition

Let $\overline{\Q}$ be an algebraic closure of $\Q$, let $N \ge 1$ and let $h \colon \mathbb{P}^N(\overline{\Q}) \to \R$ be the absolute logarithmic [[height|F1FF505PWH]] on [[projective space|ZT9A6JK8QF]].
Let $\phi \colon \mathbb{P}^N \to \mathbb{P}^N$ be a morphism of degree $d \ge 2$ defined over $\overline{\Q}$, and write $\phi^n$ for its $n$-fold composition.
The *canonical height* of $\phi$ is the function $\hat{h}_\phi \colon \mathbb{P}^N(\overline{\Q}) \to \R$ given by
$$\hat{h}_\phi(P) = \lim_{n \to \infty} \frac{h(\phi^n(P))}{d^n}.$$

## Remarks

The limit exists because $h(\phi(Q)) = d \, h(Q) + O(1)$ uniformly in $Q$, so the sequence $d^{-n} h(\phi^n(P))$ is Cauchy, by a telescoping argument.
It has these properties, due to Call and Silverman:

1. $\hat{h}_\phi(\phi(P)) = d \, \hat{h}_\phi(P)$;
2. $\hat{h}_\phi - h$ is bounded on $\mathbb{P}^N(\overline{\Q})$;
3. $\hat{h}_\phi(P) \ge 0$, with equality exactly when $P$ is preperiodic for $\phi$.

Property 3 uses Northcott's theorem: a point of canonical height $0$ has an orbit of bounded height inside a fixed [[number field|MWBDFS2KJ5]], and such an orbit is finite.

Example: for $\phi(z) = z^2$ on $\mathbb{P}^1$, $h(\phi(P)) = 2 h(P)$ exactly, so $\hat{h}_\phi = h$.
Its zeros are $0$, $\infty$ and the roots of unity, which are exactly the preperiodic points of $z \mapsto z^2$.

Non-example: for $\psi(z) = z^2 + 1$ the naive height $h$ is not the canonical height of $\psi$.
It fails property 1: $h(1) = 0$, but $h(\psi(1)) = h(2) = \log 2 \ne 2 h(1)$.

For an elliptic curve $E$ over a number field, the [[Lattès map|9PK608W8MS]] that describes doubling on $x$-coordinates has degree $4$.
Its canonical height, up to a normalizing factor, is the Néron–Tate height of $E$.
