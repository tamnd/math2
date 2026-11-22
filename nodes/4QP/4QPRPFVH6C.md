---
tag: 4QPRPFVH6C
kind: example
name: The principal angle between a line and a plane in R3
msc: [15A18]
topics: [8GQVME4SZZ]
audience: grad
instance_of: [YHVD3773AW]
illustrates: [VC8KCEGAZA]
uses: [0Q8HZTJC7G, 0ZEHZY85E6, JT8Q204E4R]
sources:
  - url: https://en.wikipedia.org/wiki/Angles_between_flats
---

## Example

Let $U = \R(1, 1, 1)$ and let $W$ be the plane $z = 0$ in $\R^3$, so $p = 1$ and $q = 2$.
There is exactly one [[principal angle|YHVD3773AW]], and we compute it in three ways.

1. A unit vector of $U$ is $u = \frac{1}{\sqrt 3}(1, 1, 1)$.
2. The [[orthogonal projection|0Q8HZTJC7G]] onto $W$ sets the last coordinate to $0$, so $P_W u = \frac{1}{\sqrt 3}(1, 1, 0)$.
3. For a line, the [[singular value characterization|VC8KCEGAZA]] gives the cosine of the angle as the length of this projection:
$$\cos \theta_1 = \norm{P_W u} = \frac{\sqrt 2}{\sqrt 3} = \sqrt{\tfrac{2}{3}} \approx 0.8165.$$
4. So $\theta_1 = \arccos \sqrt{2/3} \approx 35.26^\circ$.
5. The same with matrices: $Q_1 = u$, and $Q_2$ has the columns $(1, 0, 0)$ and $(0, 1, 0)$.
6. Then $M = Q_1^{\mathsf{T}} Q_2 = \frac{1}{\sqrt 3}(1 \ 1)$ is a $1 \times 2$ matrix, and its only singular value is its length $\sqrt{1/3 + 1/3} = \sqrt{2/3}$.
7. The principal vectors are $u_1 = u$ and $w_1 = P_W u / \norm{P_W u} = \frac{1}{\sqrt 2}(1, 1, 0)$, and indeed
$$u_1 \cdot w_1 = \frac{1 + 1 + 0}{\sqrt 3 \cdot \sqrt 2} = \frac{2}{\sqrt 6} = \sqrt{\tfrac{2}{3}}.$$
8. Check with the normal $n = (0, 0, 1)$ of $W$: the [[angle|0ZEHZY85E6]] between $u$ and $n$ has cosine $\frac{1}{\sqrt 3}$, so it is about $54.74^\circ$, and $90^\circ - 54.74^\circ = 35.26^\circ$.
9. The distance formula of the theorem gives $\norm{P_U - P_W}_F^2 = 1 + 2 - 2 \cdot \frac{2}{3} = \frac{5}{3}$.
10. Directly, $P_U = u u^{\mathsf{T}}$ has every entry $\frac{1}{3}$ and $P_W = \operatorname{diag}(1, 1, 0)$, so $P_U - P_W$ has diagonal $-\frac{2}{3}, -\frac{2}{3}, \frac{1}{3}$ and six entries $\frac{1}{3}$ off the diagonal.
11. The sum of the squares of these entries is $\frac{4 + 4 + 1 + 6}{9} = \frac{15}{9} = \frac{5}{3}$, in agreement with step 9.

## Remarks

In school geometry, the angle between a line and a plane is the angle between the line and its orthogonal projection onto the plane.
Step 7 shows that this is exactly the principal angle, with $w_1$ along the projection.
Its sine is the length $\frac{1}{\sqrt 3}$ of the part of $u$ along the normal, and $\sin^2 \theta_1 + \cos^2 \theta_1 = \frac{1}{3} + \frac{2}{3} = 1$ confirms this.

What changes when the line tilts?
For the line $\R(1, 1, t)$ the projection of a unit vector has length $\sqrt{2} / \sqrt{2 + t^2}$.
At $t = 0$ the line lies in the plane and the angle is $0$, and as $t$ grows the angle tends to $\pi/2$, the case of the normal line.
For a line and a plane no singular value decomposition is needed, since $M$ has only one row.

## Explanations

### L1 human

The line rises out of the floor at a slant.
Shine a light from straight above, and the line casts a shadow on the floor.
The principal angle is the angle between the line and its shadow.
Here the line goes one step east, one step north and one step up, and the angle is about $35$ degrees.

### L2 human

For a line and a subspace, the cosine of the angle is the length of the projection of a unit vector of the line.
Here the unit vector $\frac{1}{\sqrt 3}(1, 1, 1)$ loses its last coordinate under the projection, and what is left has length $\sqrt{2/3}$.
The typical use is to find the angle between a direction and a plane, for example the slope of a ray against a surface.
Watch out: if you compute the angle with the normal, about $54.74^\circ$ here, you must subtract it from $90^\circ$.
