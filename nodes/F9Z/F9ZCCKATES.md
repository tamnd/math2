---
tag: F9ZCCKATES
kind: definition
name: Arithmetic dynamics
msc: [37P05, 37P15]
defines: BE4X0QG8XW
uses: [0XDK9CGYKJ, MWBDFS2KJ5, ZT9A6JK8QF, T75CZ5H47N]
sources:
  - url: https://en.wikipedia.org/wiki/Arithmetic_dynamics
---

## Definition

Let $K$ be a field, let $N \ge 1$, and let $\phi \colon \mathbb{P}^N \to \mathbb{P}^N$ be a morphism of [[projective space|ZT9A6JK8QF]] defined over $K$.
For $N = 1$ such a morphism is given by a [[rational function|0XDK9CGYKJ]] $\phi \in K(z)$.
Write $\phi^n$ for the $n$-fold composition of $\phi$ with itself and $\phi^0 = \id$.
For a point $P \in \mathbb{P}^N(K)$:

1. the *forward orbit* of $P$ is $\mathcal{O}_\phi(P) = \set{\phi^n(P) : n \ge 0}$;
2. $P$ is *periodic* if $\phi^n(P) = P$ for some $n \ge 1$;
3. $P$ is *preperiodic* if $\phi^m(P)$ is periodic for some $m \ge 0$, equivalently if $\mathcal{O}_\phi(P)$ is finite.

*Arithmetic dynamics* is the study of these orbits when $K$ is a field of arithmetic interest.
Examples of such fields are an [[algebraic number field|MWBDFS2KJ5]], a $p$-adic field or a finite field.

## Remarks

The set of preperiodic points of $\phi$ in $\mathbb{P}^N(K)$ is written $\operatorname{PrePer}(\phi, K)$.

Example: let $K = \Q$ and $\phi(z) = z^2 - 1$.
Then $0 \mapsto -1 \mapsto 0$, so $0$ and $-1$ are [[periodic|T75CZ5H47N]] of period $2$.
Also $1 \mapsto 0$, so $1$ is preperiodic but not periodic, since $\phi^n(1) \in \set{0, -1}$ for all $n \ge 1$.

Non-example: for the same $\phi$, the point $2$ is not preperiodic.
Its orbit is $2, 3, 8, 63, \ldots$, and $\phi(z) > z \ge 2$ for $z \ge 2$, so the orbit is strictly increasing and infinite.

When $K$ is a number field and $\phi$ has degree at least $2$, Northcott's theorem on [[heights|F1FF505PWH]] implies that $\operatorname{PrePer}(\phi, K)$ is finite.
