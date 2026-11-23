---
tag: C9YTHB7TGH
kind: example
name: The integral of the square of the sine by symmetry
msc: ["00A35", "26A42"]
topics: [MEKKHHQTKB]
audience: school
instance_of: [H840D9TM2X]
uses: [H840D9TM2X, 0D37QFPEZE, 03H7WZ4T3K, 04TMP0XGMJ]
sources:
  - url: https://en.wikipedia.org/wiki/Integration_by_substitution
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Symmetry_in_mathematics
    locator: lead section
---

## Example

We compute
$$I = \int_0^{\pi/2} \sin^2 x \, dx$$
by a [[symmetry argument|H840D9TM2X]], with no antiderivative of $\sin^2$.
Let $J = \int_0^{\pi/2} \cos^2 x \, dx$.

1. The map $x \mapsto \tfrac{\pi}{2} - x$ maps $[0, \tfrac{\pi}{2}]$ onto itself and exchanges the endpoints.
2. Since $\sin(\tfrac{\pi}{2} - x) = \cos x$, the map turns $\sin^2$ into $\cos^2$.
3. Substitute $x = \tfrac{\pi}{2} - u$, with $dx = -du$, by [[integration by substitution|0D37QFPEZE]]:
   $$I = \int_{\pi/2}^{0} \sin^2\!\left(\tfrac{\pi}{2} - u\right) (-du) = \int_0^{\pi/2} \cos^2 u \, du = J.$$
4. By the [[Pythagorean identity|03H7WZ4T3K]], $\sin^2 x + \cos^2 x = 1$, so $I + J = \int_0^{\pi/2} 1 \, dx = \tfrac{\pi}{2}$.
5. Steps 3 and 4 give $2I = \tfrac{\pi}{2}$, so $I = \tfrac{\pi}{4}$.

Check: $\sin^2 x = \tfrac12 (1 - \cos 2x)$ has the antiderivative $\tfrac{x}{2} - \tfrac{\sin 2x}{4}$, which is $\tfrac{\pi}{4}$ at $\tfrac{\pi}{2}$ and $0$ at $0$.

## Remarks

The symmetry gives $I = J$ without computing either integral, and the Pythagorean identity gives $I + J$; together they give each one.
The same works on each interval $[\tfrac{k\pi}{2}, \tfrac{(k + 1)\pi}{2}]$ with $k$ an integer.
The reflection $x \mapsto \tfrac{(2k + 1)\pi}{2} - x$ maps this interval onto itself, and $\sin(k\pi + \tfrac{\pi}{2} - x) = \pm \cos x$, so it turns $\sin^2$ into $\cos^2$.
With $k = 0$ and $k = 1$, the integral of $\sin^2$ over $[0, \pi]$ is $\tfrac{\pi}{2}$.

On $[0, \tfrac{\pi}{3}]$ the method fails.
The reflection $x \mapsto \tfrac{\pi}{3} - x$ maps the interval onto itself but does not turn $\sin^2$ into $\cos^2$.
Indeed $\int_0^{\pi/3} \sin^2 x \, dx = \tfrac{\pi}{6} - \tfrac{\sqrt 3}{8}$, while $\int_0^{\pi/3} \cos^2 x \, dx = \tfrac{\pi}{6} + \tfrac{\sqrt 3}{8}$.

The same idea gives $\int_0^{\pi/2} \frac{\sin x}{\sin x + \cos x} \, dx = \tfrac{\pi}{4}$: the reflection exchanges the integrand with $\frac{\cos x}{\cos x + \sin x}$, and the two add up to $1$.

## Explanations

### L1 human

Draw the graphs of $\sin^2$ and $\cos^2$ between $0$ and a quarter turn.
One graph is the mirror image of the other, so the areas under them are equal.
At each point the two heights add up to $1$, so the two areas together fill a rectangle of height $1$ and width $\tfrac{\pi}{2}$.
Each area is half of the rectangle, which is $\tfrac{\pi}{4}$.

### L2 human

We check the interval $[0, \tfrac{\pi}{3}]$, where the symmetry is missing.

1. With the antiderivative $\tfrac{x}{2} - \tfrac{\sin 2x}{4}$, the integral of $\sin^2$ over $[0, \tfrac{\pi}{3}]$ is $\tfrac{\pi}{6} - \tfrac{\sin(2\pi/3)}{4} = \tfrac{\pi}{6} - \tfrac{\sqrt 3}{8}$.
2. The integral of $\cos^2 = 1 - \sin^2$ over the same interval is $\tfrac{\pi}{3} - (\tfrac{\pi}{6} - \tfrac{\sqrt 3}{8}) = \tfrac{\pi}{6} + \tfrac{\sqrt 3}{8}$.
3. The two values differ by $\tfrac{\sqrt 3}{4} \neq 0$, so the integrals are not equal there.

The method fits an integral over an interval whose reflection exchanges two integrands with a simple sum.
Watch out: the reflection must both map the interval onto itself and exchange the two integrands, and on $[0, \tfrac{\pi}{3}]$ only the first holds.
