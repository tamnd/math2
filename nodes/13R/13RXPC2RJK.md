---
tag: 13RXPC2RJK
kind: definition
name: Riemann domain over C^n
msc: [32D26]
defines: A15BF6QHDR
uses: [0MXB4CKHFW, 0V032VWTHD, MDH71ZZ8XX, 507C34W0ZT]
sources:
  - url: https://en.wikipedia.org/wiki/Function_of_several_complex_variables
---

## Definition

A *Riemann domain over $\C^n$* is a pair $(X, \pi)$ where $X$ is a [[connected|0V032VWTHD]] [[Hausdorff space|0MXB4CKHFW]] and $\pi \colon X \to \C^n$ is a [[local homeomorphism|MDH71ZZ8XX]].
Let $W \subseteq X$ be open and $f \colon W \to \C$ a function.
Then $f$ is *holomorphic* if $f \circ (\pi|_V)^{-1}$ is a [[holomorphic function|507C34W0ZT]] on $\pi(V)$ for every open set $V \subseteq W$ on which $\pi$ is injective.
The Riemann domain is *schlicht* if $\pi$ is injective.

## Remarks

The charts $\pi|_V$ make $X$ a complex manifold of dimension $n$ on which $\pi$ is locally biholomorphic.
A schlicht Riemann domain is the same as a domain in $\C^n$, through the identification of $X$ with $\pi(X)$.

Example: $X = \C^2$ with $\pi(w, z_2) = (e^w, z_2)$.
The space $X$ is connected and Hausdorff, and $\pi$ is a local homeomorphism because $w \mapsto e^w$ is a local homeomorphism of $\C$ onto $\C \setminus \set{0}$.
It is not schlicht, since $\pi(w + 2\pi i, z_2) = \pi(w, z_2)$.

Non-example: $X = \C^2$ with $\pi(w, z_2) = (w^2, z_2)$.
Here $\pi$ is not injective on any neighbourhood of a point $(0, z_2)$, because $(w, z_2)$ and $(-w, z_2)$ have the same image; so $\pi$ is not a local homeomorphism there.
