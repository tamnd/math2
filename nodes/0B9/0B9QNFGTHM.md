---
tag: 0B9QNFGTHM
kind: example
name: Rotation matrix
msc: [15B10]
instance_of: [0CGYNDCWRR]
uses: [0QRBVFJ50X, 0CGYNDCWRR]
sources:
  - url: https://en.wikipedia.org/wiki/Rotation_matrix
    locator: In two dimensions
same_as:
  wikidata: Q1256564
  wikipedia: Rotation matrix
---

## Example

Let $\theta \in \R$.
The *rotation matrix* of angle $\theta$ is
$$R(\theta) = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}.$$
The map $x \mapsto R(\theta) x$ rotates the plane $\R^2$ about the origin by the angle $\theta$, counterclockwise.
It is an [[orthogonal matrix|0W02QESPJQ]] with determinant $\cos^2\theta + \sin^2\theta = 1$, so it is an element of $SO(2)$.

## Remarks

Rotations add their angles: $R(\alpha) R(\beta) = R(\alpha + \beta)$.
So $R(\theta)^{-1} = R(-\theta) = R(\theta)^T$.
For $\theta$ not a multiple of $\pi$, $R(\theta)$ has no real eigenvalue; its complex eigenvalues are $e^{\pm i\theta}$.
Every element of $SO(2)$ is $R(\theta)$ for some $\theta$.

## Explanations

### L1 human

The rotation matrix sends $(1, 0)$ to $(\cos\theta, \sin\theta)$ and $(0, 1)$ to $(-\sin\theta, \cos\theta)$.
These are the first and the second column.
For $\theta = 90$ degrees, it is $\begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$.
