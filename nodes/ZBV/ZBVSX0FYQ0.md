---
tag: ZBVSX0FYQ0
kind: example
name: K2 of the integers
msc: [19C99, 11R70]
instance_of: [W7T56A6YF8]
uses: [590VZSQ83X, HRYG5D46EQ, WFG4YMBYVQ]
sources:
  - url: https://en.wikipedia.org/wiki/Steinberg_group_(K-theory)
---

## Example

Milnor showed that $K_2(\Z) \cong \Z/2\Z$.
The nonzero element is the Steinberg symbol $\set{-1, -1}$.
In the [[Steinberg group|590VZSQ83X]] $St(\Z)$ it is the element $w^4$, where $w = x_{12}(1) \, x_{21}(-1) \, x_{12}(1)$.

Check that $w^4$ lies in $K_2(\Z)$.
The image of $w$ in $GL(\Z)$ is
$$\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} \begin{pmatrix} 1 & 0 \\ -1 & 1 \end{pmatrix} \begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix},$$
and this matrix has order $4$, so $w^4$ maps to the identity.

Check that $\set{-1, -1}$ is not trivial: the inclusion $\Z \to \R$ induces $K_2(\Z) \to K_2(\R)$, which sends $\set{-1, -1}$ to $\set{-1, -1}$.
The real [[Hilbert symbol|WFG4YMBYVQ]] is a [[Steinberg symbol|HRYG5D46EQ]] with value $-1$ on $(-1, -1)$, so this image is not trivial.

The upper bound, that $K_2(\Z)$ has at most two elements, uses the Euclidean algorithm to reduce words in the Steinberg group.

## Explanations

### L1 human

In integer matrices, the rotation by a quarter turn can be written with three row operations, and four quarter turns give the identity.
In the Steinberg group, which only knows the basic rules of row operations, the fourth power of that product is not trivial.
This is the only hidden relation for integer matrices, so $K_2(\Z)$ has exactly two elements.
