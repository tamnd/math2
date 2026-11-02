---
tag: 73SAQBFWKQ
kind: definition
name: Elliptic surface
msc: [14J27]
defines: VSC3F53DX4
uses: [KFTECAATKG, XJM2MT4S3Y, 6W8TDV9VVN, CDS1VWB7A3]
sources:
  - url: https://en.wikipedia.org/wiki/Elliptic_surface
---

## Definition

Let $X$ be a smooth projective [[algebraic surface|KFTECAATKG]] over an algebraically closed field.
An *elliptic fibration* on $X$ is a surjective [[morphism|CDS1VWB7A3]] $f \colon X \to C$ onto a smooth projective [[curve|XJM2MT4S3Y]] $C$ such that:

1. every fibre of $f$ is connected, and
2. the fibre $f^{-1}(c)$ is a smooth curve of [[genus|6W8TDV9VVN]] $1$ for all but finitely many $c \in C$.

An *elliptic surface* is a surface $X$ together with an elliptic fibration on it.

## Remarks

Many authors also require that $f$ be relatively minimal, meaning that no fibre contains a smooth rational curve of self-intersection $-1$, and some require a section of $f$.
Example: for an elliptic curve $E$ and a smooth projective curve $C$, the projection $E \times C \to C$ has every fibre isomorphic to $E$, so it is an elliptic fibration.
Example: blowing up $\mathbb{P}^2$ at the nine base points of a general pencil of plane cubics gives a rational elliptic surface, whose fibres are the cubics of the pencil.
Non-example: the projection $\mathbb{P}^1 \times \mathbb{P}^1 \to \mathbb{P}^1$ has all fibres of genus $0$, so it fails clause 2.
In characteristics $2$ and $3$ one also meets quasi-elliptic fibrations, whose general fibre is a cuspidal rational curve.
