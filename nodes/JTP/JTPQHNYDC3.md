---
tag: JTPQHNYDC3
kind: statement
role: proposition
name: Thin lens equation
msc: [78A05]
uses: [N111BHFQ2H, 9WFT4VY2R7]
about: [N111BHFQ2H]
sources:
  - url: https://en.wikipedia.org/wiki/Thin_lens
---

## Statement

Let a thin lens of focal length $f \ne 0$ be surrounded by the same medium on both sides, and work in the [[paraxial approximation|N111BHFQ2H]].
Let an object point lie at distance $s_o$ in front of the lens and let its image lie at distance $s_i$ behind the lens.
Distances are positive for a real object in front and a real image behind.
Then
$$\frac{1}{s_o} + \frac{1}{s_i} = \frac{1}{f},$$
and the lateral magnification of the image is $m = -\dfrac{s_i}{s_o}$.

## Remarks

A proof uses [[ray transfer matrices|9WFT4VY2R7]].
The matrix from the object plane to the image plane is
$$\begin{pmatrix} 1 & s_i \\ 0 & 1 \end{pmatrix}\begin{pmatrix} 1 & 0 \\ -1/f & 1 \end{pmatrix}\begin{pmatrix} 1 & s_o \\ 0 & 1 \end{pmatrix} = \begin{pmatrix} 1 - s_i/f & s_o + s_i - s_o s_i / f \\ -1/f & 1 - s_o/f \end{pmatrix}.$$
The image plane is where all rays from one object point meet, that is, where the entry $B$ vanishes, which is the equation above.
The entry $A = 1 - s_i/f$ is then the magnification, and it equals $-s_i/s_o$.

Example: an object $30$ cm in front of a lens with $f = 10$ cm has $1/s_i = 1/10 - 1/30 = 1/15$, so $s_i = 15$ cm and $m = -1/2$: a real, inverted image half the size.
For $s_o = f$ the equation gives $1/s_i = 0$: the rays leave parallel and the image is at infinity.
For $0 < s_o < f$ with $f > 0$, $s_i < 0$: the image is virtual, as in a magnifying glass.

Other sign conventions write $\frac{1}{s_i} - \frac{1}{s_o} = \frac{1}{f}$ with signed coordinates along the axis.

## Explanations

### L1 human

The equation tells where a lens forms an image.
Put a candle at distance $s_o$ in front of a lens and a screen at distance $s_i$ behind it.
The flame is sharp on the screen when the two reciprocals add up to the reciprocal of the focal length.
Far objects give images near the focal point, and objects near the focal point give images far away.

### L2 human

The thin lens equation is the simplest case of first-order imaging.
For a thick lens or a system of lenses it keeps its form when the distances are measured from the principal planes, which are among the cardinal points.
The Newtonian form $x_o x_i = f^2$, with distances measured from the focal points, is equivalent.
