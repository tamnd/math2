---
tag: 87VKHCKSDP
kind: example
name: The napkin ring problem by an extreme case
msc: ["00A35", "51M25"]
topics: [X1NSTVGDNQ]
audience: ug1
instance_of: [FTBJX4G51S]
uses: [FTBJX4G51S]
sources:
  - url: https://en.wikipedia.org/wiki/Napkin_ring_problem
    locator: lead section
---

## Example

A cylindrical hole is drilled straight through the center of a solid ball, and the ring that remains has height $6$ cm along the axis of the hole.
What is the volume of the ring?
The radius of the ball is not given.
We guess the answer by [[specialization|FTBJX4G51S]] to an extreme case, and then we check it.

1. We read the problem as a claim.
   Since the radius is not given, the problem claims that the volume does not depend on the radius.
2. We choose the extreme case.
   The smallest possible ball has radius $3$ cm, and then the hole has radius $0$, so the ring is the whole ball.
3. We solve the extreme case:
   $$V = \frac{4}{3}\pi \cdot 3^3 = 36\pi \text{ cm}^3.$$
4. We conjecture that the volume is $36\pi$ cm³ for every radius.

Step 1 trusts the wording of the problem, so we check the answer for a ball of any radius $R \ge 3$.

1. We center the ball at the origin with the hole along the $z$-axis, so the ring lies between the planes $z = -3$ and $z = 3$.
2. At $z = \pm 3$ the hole meets the sphere, so the radius $r$ of the hole satisfies $r^2 + 3^2 = R^2$, that is, $r^2 = R^2 - 9$.
3. At height $z$ with $|z| \le 3$, the cross-section is an annulus with outer radius $\sqrt{R^2 - z^2}$ and inner radius $r$, so its area is
   $$\pi\left(R^2 - z^2 - r^2\right) = \pi\left(9 - z^2\right).$$
4. The area does not contain $R$, and the volume is
   $$\int_{-3}^{3} \pi\left(9 - z^2\right) dz = \pi\left(54 - 18\right) = 36\pi \text{ cm}^3.$$

The extreme case gave the right answer.

## Remarks

The extreme case worked only because the answer does not depend on the radius, and we took that from the wording of the problem.
Without that knowledge a single extreme case is only a guess.
The computation shows why the independence holds: each cross-section of the ring has area $\pi(9 - z^2)$, the same as the cross-section of a ball of radius $3$ at the same height.

For a ring of height $h$ the same computation gives
$$\int_{-h/2}^{h/2} \pi\left(\frac{h^2}{4} - z^2\right) dz = \frac{\pi h^3}{6},$$
and $h = 6$ gives $36\pi$ again.

## Explanations

### L1 human

The problem does not say how big the ball is, so the answer cannot depend on the size of the ball.
Then we may pick the easiest ball: the smallest one, with a hole so thin that nothing is removed.
That ball has radius $3$ cm, and its volume is $36\pi$ cubic centimeters, about $113$.
A careful calculation for a ball of any size gives the same number.

### L2 human

We use the extreme-case idea on a second problem.
A square is inscribed in a circle and a second square is drawn around the same circle; what is the ratio of their areas?
Scaling the figure multiplies both areas by the same factor, so the ratio cannot depend on the size, and we take radius $1$.
The inscribed square has diagonal $2$, so its side is $\sqrt{2}$ and its area is $2$.
The outer square has side $2$ and area $4$, so the ratio is $1 : 2$.

This is the typical use: when the answer is known not to depend on a parameter, give the parameter its easiest value.
Watch out for where that knowledge comes from.
Here scaling proves it, but in the napkin ring we only read it from the problem, so the check was needed.
