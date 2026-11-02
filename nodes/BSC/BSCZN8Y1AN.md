---
tag: BSCZN8Y1AN
kind: example
name: Arnold's cat map
msc: [37D20, 37A25]
instance_of: [RCQH8P6DPQ]
uses: [03NM7DZXXC, 0ZND7NQ970, 2Z2QVWZ262]
sources:
  - url: https://en.wikipedia.org/wiki/Arnold%27s_cat_map
same_as:
  wikidata: Q2961488
  wikipedia: Arnold's cat map
---

## Example

Let $\mathbb{T}^2 = \R^2/\Z^2$ be the [[torus|03NM7DZXXC]] and let $A = \begin{pmatrix} 2 & 1 \\ 1 & 1 \end{pmatrix}$.
Arnold's cat map is $f(x, y) = (2x + y, \; x + y) \bmod 1$.
It is well defined because $A$ maps $\Z^2$ to $\Z^2$, and it is a diffeomorphism because $\det A = 1$, so $A^{-1}$ also has integer entries.

Check that it is an [[Anosov diffeomorphism|RCQH8P6DPQ]].
The derivative of $f$ is $A$ at every point.
The characteristic polynomial is $t^2 - 3t + 1$, so the [[eigenvalues|0ZND7NQ970]] are $\lambda_\pm = (3 \pm \sqrt5)/2$, with $\lambda_+ \approx 2.618$ and $\lambda_- = 1/\lambda_+ \approx 0.382$.
Let $E^u$ and $E^s$ be the eigenlines for $\lambda_+$ and $\lambda_-$; since $A$ is symmetric they are orthogonal.
Then $\norm{A^n v} = \lambda_-^n \norm{v}$ on $E^s$ and $\norm{A^{-n} v} = \lambda_+^{-n}\norm{v}$ on $E^u$, which is the required hyperbolicity with $C = 1$.

## Remarks

The map preserves [[Lebesgue measure|2Z2QVWZ262]], since $\abs{\det A} = 1$, and it is mixing for this measure.
Its periodic points are exactly the points with rational coordinates, so they are dense.
The number of fixed points of $f^n$ is $\abs{\det(A^n - I)} = \lambda_+^n + \lambda_+^{-n} - 2$; for $n = 1$ this is $1$, the origin.
Its topological entropy is $\log \lambda_+$.

## Explanations

### L1 human

Draw a picture on a square whose opposite sides are glued, so that it is really a torus.
Shear and stretch the picture by the matrix, then cut the pieces that stick out and shift them back into the square.
After a few steps the picture looks like random noise, because nearby points are pulled apart by a factor of about $2.6$ each time.
Yet the map is exactly invertible, and every point with rational coordinates returns to where it started.
