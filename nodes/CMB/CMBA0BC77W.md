---
tag: CMBA0BC77W
kind: example
name: Maxwell's fish-eye lens
msc: [78A05, 53A04]
instance_of: [C9TV3FZEM4]
uses: [MQ5ZJ7VADG, AXDKKVD18N, NSYMQMHPDN, 060W5CBZP6]
sources:
  - url: https://en.wikipedia.org/wiki/Gradient-index_optics
---

## Example

Fix constants $n_0 > 0$ and $a > 0$.
*Maxwell's fish-eye* is the medium on all of $\R^3$ with refractive index
$$n(x) = \frac{n_0}{1 + \abs{x}^2 / a^2}.$$
Since $n$ is smooth, positive and not constant, it is a [[gradient-index medium|C9TV3FZEM4]].
Its rays are the [[geodesics|NSYMQMHPDN]] of the metric $n(x)^2 \abs{dx}^2$.
Under [[stereographic projection|AXDKKVD18N]] from the round $3$-sphere of radius $a$ in $\R^4$ onto its equatorial space $\R^3$, the round metric pulls back to $\left(2 / (1 + \abs{x}^2/a^2)\right)^2 \abs{dx}^2$.
So $n^2 \abs{dx}^2$ is a constant multiple of the round metric, and the rays are the images of great circles.
Stereographic projection sends great circles to [[circles|060W5CBZP6]] and to lines through the origin, so every ray is a circle or a line through the centre.
All great circles through a point of the $3$-sphere also pass through its antipode, which projects to $x^* = -a^2 x / \abs{x}^2$.
Hence all rays from a point $x \ne 0$ meet again at $x^*$: the fish-eye images every point perfectly.

## Explanations

### L1 human

In Maxwell's fish-eye the index is highest at the centre and falls off with distance.
Every light ray travels along a circle, and all the rays that leave one point gather again at a single point on the other side of the centre.
The trick is that the medium is a flat picture of a sphere, where light runs along great circles.
