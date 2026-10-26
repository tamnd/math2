---
tag: 0XNZWJ96HK
kind: definition
name: Rotation
msc: [51F20]
defines: 0HFREYRSZP
uses: [0J1N3WTKM4, 0XW7V9ZZ05]
sources:
  - url: https://en.wikipedia.org/wiki/Euclidean_plane_isometry
    locator: Rotations
  - url: https://en.wikipedia.org/wiki/Rotation_(mathematics)
    locator: In Euclidean geometry
---

## Definition

Let $c$ be a point of $\mathbb{R}^n$, and let $A$ be an orthogonal $n \times n$ matrix with $\det A = 1$. The rotation about $c$ with the matrix $A$ is the map
$$R \colon \mathbb{R}^n \to \mathbb{R}^n, \qquad R(p) = c + A\,(p - c).$$
In the [[Euclidean plane|0XW7V9ZZ05]] $\mathbb{R}^2$, the rotation about $c$ through the angle $\theta \in \mathbb{R}$ is the case
$$A = \begin{pmatrix} \cos \theta & -\sin \theta \\ \sin \theta & \cos \theta \end{pmatrix}.$$

## Remarks

Each rotation is a direct [[Euclidean isometry|0J1N3WTKM4]] that fixes $c$. In the plane, each orthogonal matrix with determinant $1$ has this form, so each plane rotation has an angle.
In the plane, rotations about one centre commute, and their angles add modulo $2\pi$. Rotations about different centres do not commute in general.
In the plane, the composite of the reflections in two lines that meet at $c$ is a rotation about $c$.
Mathlib's `Orientation.rotation` is the rotation through an angle of an oriented Euclidean plane, as a linear map.

## Explanations

### L1 human

A plane rotation turns the whole plane about one fixed point through one angle. With $\theta > 0$, the turn is anticlockwise. The rotation about $(0, 0)$ through $\pi/2$ sends $(1, 0)$ to $(0, 1)$ and $(0, 1)$ to $(-1, 0)$.
