---
tag: V93Y0XYPZD
kind: concept
name: Serre's twisting sheaf
msc: [14F06, 14C20]
sources:
  - url: https://en.wikipedia.org/wiki/Proj_construction
---

## Summary

Let $S$ be a graded ring.
Serre's twisting sheaf $\mathcal{O}(1)$ on $\operatorname{Proj} S$ is the sheaf attached to the graded module $S$ shifted by one degree.
On projective space $\mathbb{P}^n_k$ it is the line bundle whose global sections are the linear forms in the homogeneous coordinates.
Its powers $\mathcal{O}(m)$ turn graded modules into sheaves and sheaves back into graded modules, and they control embeddings into projective space.

## Explanations

### L1 human

A homogeneous polynomial of degree $m$ is not a function on projective space, since its value changes when one rescales the coordinates.
It is a section of a line bundle instead, and this line bundle is $\mathcal{O}(m)$.
For example, on the projective line, the linear forms $x_0$ and $x_1$ are sections of $\mathcal{O}(1)$, and $x_0^2 + x_1^2$ is a section of $\mathcal{O}(2)$.
The zeros of such a section are well defined, and they form a hypersurface of projective space.
