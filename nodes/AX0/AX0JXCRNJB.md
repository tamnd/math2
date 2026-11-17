---
tag: AX0JXCRNJB
kind: example
name: Rotations of the plane about the origin commute
msc: [08A02]
topics: [BAZT8JJ70S]
audience: school
instance_of: [099E72KTF8]
uses: [0HFREYRSZP, 0THBK9V825, 08J2M1JYAG]
sources:
  - url: https://en.wikipedia.org/wiki/Rotation_matrix
    locator: In two dimensions
---

## Example

For a real number $\alpha$, let $R_\alpha \colon \mathbb{R}^2 \to \mathbb{R}^2$ be the [[rotation|0HFREYRSZP]] about the origin by the angle $\alpha$, given by
$$R_\alpha(x, y) = (x\cos\alpha - y\sin\alpha,\ x\sin\alpha + y\cos\alpha).$$
We check that [[composition|0THBK9V825]] of these rotations is [[commutative|099E72KTF8]].
Let $\alpha, \beta \in \mathbb{R}$ and $(x, y) \in \mathbb{R}^2$.

1. Put $(x', y') = R_\beta(x, y)$, so $x' = x\cos\beta - y\sin\beta$ and $y' = x\sin\beta + y\cos\beta$.
2. The first coordinate of $R_\alpha(x', y')$ is $x'\cos\alpha - y'\sin\alpha = x(\cos\alpha\cos\beta - \sin\alpha\sin\beta) - y(\sin\alpha\cos\beta + \cos\alpha\sin\beta)$.
3. By the addition formulas for cosine and sine, this is $x\cos(\alpha + \beta) - y\sin(\alpha + \beta)$.
4. The second coordinate of $R_\alpha(x', y')$ is $x'\sin\alpha + y'\cos\alpha = x(\sin\alpha\cos\beta + \cos\alpha\sin\beta) + y(\cos\alpha\cos\beta - \sin\alpha\sin\beta)$.
5. By the same formulas, this is $x\sin(\alpha + \beta) + y\cos(\alpha + \beta)$.
6. By steps 3 and 5, $R_\alpha \circ R_\beta = R_{\alpha + \beta}$.
7. In the same way, $R_\beta \circ R_\alpha = R_{\beta + \alpha}$. Since $\alpha + \beta = \beta + \alpha$, the two compositions are equal.

A check on the point $(1, 0)$ with the angles $90^\circ$ and $180^\circ$:

8. $R_{180^\circ}(1, 0) = (-1, 0)$, and $R_{90^\circ}(-1, 0) = (0, -1)$.
9. $R_{90^\circ}(1, 0) = (0, 1)$, and $R_{180^\circ}(0, 1) = (0, -1)$.

## Remarks

Composition of functions is not commutative in general, so this is a property of this special set of functions.
The rotations of the plane about the origin form the group [[SO(2)|0CGYNDCWRR]], and the example shows that this group is abelian.
With complex numbers, $R_\alpha$ is multiplication by $\cos\alpha + i\sin\alpha$, and the example follows from the [[commutativity of complex multiplication|G96XHQM1H6]].
Rotations of space do not commute in general.
For example, a rotation by $90^\circ$ about the $x$-axis and a rotation by $90^\circ$ about the $z$-axis give different results in the two orders.

## Explanations

### L1 human

Turn a picture by $30^\circ$, and then by $50^\circ$.
The picture has turned by $80^\circ$.
If we turn by $50^\circ$ first and then by $30^\circ$, the picture has also turned by $80^\circ$.
So the order of two turns about the same centre does not matter.

### L2 human

The key step is the rule $R_\alpha \circ R_\beta = R_{\alpha + \beta}$.
It changes a question about composition, which is not commutative in general, into a question about addition of angles, which is commutative.
The typical use is to show that a group of rotations, such as the rotations of a regular polygon, is abelian.
A trap is to extend the result to rotations of space, or to rotations about different centres in the plane.
