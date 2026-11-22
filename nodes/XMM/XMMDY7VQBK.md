---
tag: XMMDY7VQBK
kind: example
name: Two bases of the plane with opposite orientations
msc: [15A04, 15A15]
topics: [DTBK11SR77]
audience: ug2
instance_of: [0QJJAQ6ZYZ]
uses: [0Q8BZXVT1Z]
sources:
  - url: https://en.wikipedia.org/wiki/Orientation_(vector_space)
---

## Example

In $\mathbb{R}^2$ with the standard basis $E = (e_1, e_2)$ and the standard [[orientation|0QJJAQ6ZYZ]], take the two ordered bases
$$B = ((1, 1), (-1, 1)), \qquad C = ((1, 2), (3, 4)).$$
We show that $B$ is positive and $C$ is negative.

1. The change of basis matrix from $E$ to $B$ has the vectors of $B$ as its columns, and its determinant is
$$\det \begin{pmatrix} 1 & -1 \\ 1 & 1 \end{pmatrix} = 1 \cdot 1 - (-1) \cdot 1 = 2 > 0.$$
So by the [[definition|0Q8BZXVT1Z]], $B$ has the standard orientation.
2. In the same way, the matrix for $C$ has determinant
$$\det \begin{pmatrix} 1 & 3 \\ 2 & 4 \end{pmatrix} = 1 \cdot 4 - 3 \cdot 2 = -2 < 0.$$
So $C$ has the opposite orientation.
3. We check $B$ with angles.
   The vector $(1, 1)$ has angle $45^\circ$ and $(-1, 1)$ has angle $135^\circ$, so the turn from the first to the second is $90^\circ$ counterclockwise, as for $e_1$ and $e_2$.
4. We check $C$ with angles.
   The vector $(1, 2)$ has angle about $63.4^\circ$ and $(3, 4)$ has angle about $53.1^\circ$, so the shorter turn from the first to the second is clockwise.
5. We check $B$ with a path.
   The family $B_t = ((1, t), (-t, 1))$ for $t \in [0, 1]$ has determinant $1 \cdot 1 - (-t) \cdot t = 1 + t^2 > 0$.
   So every $B_t$ is a basis, and the path joins $B_0 = E$ to $B_1 = B$.

## Remarks

The change of basis matrix from $B$ to $C$ has determinant equal to the quotient of the two determinants, $-2 / 2 = -1$.
Its sign is negative, which confirms that $B$ and $C$ lie in different classes.
No path of bases joins $E$ to $C$, since the determinant would have to change sign and so pass through $0$, where the vectors are dependent.

A small change of one vector can change the answer.
If we replace $(3, 4)$ by $(3, 6)$, the determinant becomes $1 \cdot 6 - 3 \cdot 2 = 0$, and $C$ is no longer a basis.
If we use $(3, 7)$, the determinant is $1 \cdot 7 - 3 \cdot 2 = 1 > 0$, and $C$ becomes positive.
Exchanging the two vectors of $C$ also makes it positive, since the determinant becomes $3 \cdot 2 - 1 \cdot 4 = 2$.

## Explanations

### L1 human

In the plane, a basis has the standard orientation when you turn counterclockwise, by less than half a turn, to get from the first arrow to the second.
The basis $B$ turns counterclockwise by a quarter turn.
The basis $C$ turns a little bit clockwise, so it has the other orientation.

### L2 human

The sign of one $2 \times 2$ determinant decides the orientation, and no angle needs to be measured.
Step 5 shows the other description of orientation: two bases with the same orientation can be joined by a path of bases.
Watch out: the angles must be measured from the first vector to the second, in this order, since the reversed pair has the other orientation.
