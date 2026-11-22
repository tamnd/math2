---
tag: SRN03D73AJ
kind: example
name: Two reflections of the plane compose to a rotation by twice the angle
msc: ["15B10", "51F15"]
topics: [AZS5BPF5H3]
audience: ug1
instance_of: [HNY4CPEEJA]
illustrates: [C97Z06HHB2]
uses: [025158VEYZ, 0QRBVFJ50X]
sources:
  - url: https://en.wikipedia.org/wiki/Orthogonal_matrix
    locator: Lower dimensions
---

## Example

Let $S(\alpha) = \begin{pmatrix} \cos 2\alpha & \sin 2\alpha \\ \sin 2\alpha & -\cos 2\alpha \end{pmatrix}$ be the [[reflection|025158VEYZ]] in the line through $0$ at the angle $\alpha$.
We take the mirror lines $y = x$, at the angle $\frac{\pi}{4}$, and $y = 0$, at the angle $0$, and we compose the two reflections in both orders.

1. Put $\alpha = \frac{\pi}{4}$ and $\alpha = 0$ into the formula:
$$S\left(\tfrac{\pi}{4}\right) = \begin{pmatrix} 0 & 1 \\ 1 & 0 \end{pmatrix}, \qquad S(0) = \begin{pmatrix} 1 & 0 \\ 0 & -1 \end{pmatrix}.$$
2. Multiply, first $S(0)$ and then $S(\pi/4)$:
$$S\left(\tfrac{\pi}{4}\right) S(0) = \begin{pmatrix} 0 \cdot 1 + 1 \cdot 0 & 0 \cdot 0 + 1 \cdot (-1) \\ 1 \cdot 1 + 0 \cdot 0 & 1 \cdot 0 + 0 \cdot (-1) \end{pmatrix} = \begin{pmatrix} 0 & -1 \\ 1 & 0 \end{pmatrix}.$$
3. This is the [[rotation matrix|HNY4CPEEJA]] $R(\pi/2)$. Its angle $\frac{\pi}{2} = 2\left(\frac{\pi}{4} - 0\right)$ is twice the angle between the lines.
4. Multiply in the other order:
$$S(0) S\left(\tfrac{\pi}{4}\right) = \begin{pmatrix} 1 \cdot 0 + 0 \cdot 1 & 1 \cdot 1 + 0 \cdot 0 \\ 0 \cdot 0 + (-1) \cdot 1 & 0 \cdot 1 + (-1) \cdot 0 \end{pmatrix} = \begin{pmatrix} 0 & 1 \\ -1 & 0 \end{pmatrix}.$$
5. This is $R(-\pi/2)$, the rotation by $2\left(0 - \frac{\pi}{4}\right)$.

Check on a point: $S(0)$ sends $(1, 0)$ to $(1, 0)$, and then $S(\pi/4)$ swaps the coordinates and gives $(0, 1)$.
So the first product turns $(1, 0)$ to $(0, 1)$, a quarter turn counterclockwise.

## Remarks

The example shows the rule $S(\alpha) S(\beta) = R(2(\alpha - \beta))$ of [[the classification of O(2)|C97Z06HHB2]].
Each reflection has determinant $-1$, so the product has determinant $(-1)(-1) = 1$, as a rotation must.

The two orders give opposite rotations, so these two reflections do not commute.
Reflections in two lines commute only when the lines are equal or perpendicular.
For perpendicular lines, such as $y = x$ and $y = -x$ at the angles $\frac{\pi}{4}$ and $-\frac{\pi}{4}$, both orders give $R(\pi) = -I_2$.
If we move the second mirror from $y = 0$ to the line at the angle $\frac{\pi}{12}$, the angle between the lines becomes $\frac{\pi}{6}$, and the product becomes the turn by $\frac{\pi}{3}$.

## Explanations

### L1 human

Put two mirrors through the origin, at an angle of $45$ degrees to each other.
Reflect a picture in the first mirror, and then reflect the result in the second mirror.
The picture is no longer reversed.
It is turned by $90$ degrees, which is twice the angle between the mirrors.

### L2 human

Here is the typical use: to build the turn by $\theta$ from reflections, take two mirror lines through the origin at the angle $\frac{\theta}{2}$, and reflect first in the line with the smaller angle.
For example, the turn by $\frac{\pi}{3}$ is $S(\pi/6) S(0)$.
Watch out: the angle of the turn is twice the angle between the mirrors, not equal to it, and the order of the two reflections decides the direction of the turn.
