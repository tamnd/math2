---
tag: D3F3XAZA0M
kind: example
name: Determinants of rotations and reflections of the plane
msc: ["15A15"]
topics: [DTBK11SR77]
audience: ug1
instance_of: [00KDZRW4C0]
uses: [0ZN2J42SK7, 0B9QNFGTHM, 027MBSVPY3, 0QJJAQ6ZYZ]
sources:
  - url: https://en.wikipedia.org/wiki/Determinant
    locator: Orientation
---

## Example

Let $\theta \in \mathbb{R}$, and let
$$R_\theta = \begin{pmatrix} \cos\theta & -\sin\theta \\ \sin\theta & \cos\theta \end{pmatrix}, \qquad S_\theta = \begin{pmatrix} \cos 2\theta & \sin 2\theta \\ \sin 2\theta & -\cos 2\theta \end{pmatrix}.$$
Here $R_\theta$ is the [[rotation|0B9QNFGTHM]] by the angle $\theta$, and $S_\theta$ is the [[reflection|027MBSVPY3]] in the line through $0$ at angle $\theta$.

1. By the [[2 × 2 formula|0ZN2J42SK7]], $\det R_\theta = \cos\theta \cos\theta - (-\sin\theta)\sin\theta = \cos^2\theta + \sin^2\theta = 1$.
2. By the same formula, $\det S_\theta = -\cos^2 2\theta - \sin^2 2\theta = -1$.
3. Check with $\theta = \pi/2$: $R_{\pi/2} = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}$ has determinant $0 \cdot 0 - (-1) \cdot 1 = 1$.
4. Check with $\theta = 0$: $S_0 = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}$, the reflection in the $x$-axis, has determinant $-1$.

## Remarks

Rotations keep areas and the turning direction, so their determinant is $+1$.
Reflections keep areas but reverse the turning direction, so their determinant is $-1$; they change the [[orientation|0QJJAQ6ZYZ]].
The product $S_\theta S_0$ is a rotation, and its determinant is $(-1)(-1) = 1$, as multiplicativity predicts.
A scaled rotation $c R_\theta$ has determinant $c^2$.

## Explanations

### L1 human

Turning the plane does not change sizes or the direction of turning, and its determinant is $1$.
A mirror does not change sizes, but it swaps clockwise and counterclockwise, and its determinant is $-1$.

### L2 human

The orthogonal $2 \times 2$ matrices are exactly the rotations and the reflections, and the determinant separates the two kinds.
A trap: a determinant of $1$ does not imply a rotation; the shear $\begin{pmatrix} 1 & 1 \\ 0 & 1 \end{pmatrix}$ also has determinant $1$.
