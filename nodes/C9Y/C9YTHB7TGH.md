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

1. The map $x \mapsto \tfrac{\pi}{2} - x$ maps the interval $[0, \tfrac{\pi}{2}]$ onto itself, and it exchanges the endpoints $0$ and $\tfrac{\pi}{2}$.
2. For each $x$, $\sin(\tfrac{\pi}{2} - x) = \cos x$. So the map turns $\sin^2$ into $\cos^2$.
3. We substitute $x = \tfrac{\pi}{2} - u$, with $dx = -du$, by [[integration by substitution|0D37QFPEZE]]. When $x = 0$, $u = \tfrac{\pi}{2}$, and when $x = \tfrac{\pi}{2}$, $u = 0$.
4. So $I = \int_{\pi/2}^{0} \sin^2(\tfrac{\pi}{2} - u) \, (-du) = \int_0^{\pi/2} \cos^2 u \, du = J$.
5. By the [[Pythagorean identity|03H7WZ4T3K]], $\sin^2 x + \cos^2 x = 1$ for each $x$. So $I + J = \int_0^{\pi/2} 1 \, dx = \tfrac{\pi}{2}$.
6. Steps 4 and 5 give $2I = \tfrac{\pi}{2}$, so $I = \tfrac{\pi}{4}$.

A check by an antiderivative: $\sin^2 x = \tfrac12 (1 - \cos 2x)$, so an antiderivative is $\tfrac{x}{2} - \tfrac{\sin 2x}{4}$.
Its value at $\tfrac{\pi}{2}$ is $\tfrac{\pi}{4} - 0$, and its value at $0$ is $0$, so $I = \tfrac{\pi}{4}$.

## Remarks

1. The symmetry gives $I = J$ without computing either integral. The Pythagorean identity gives $I + J$. Together they give each integral.
2. The method works on each interval $[\tfrac{k\pi}{2}, \tfrac{(k + 1)\pi}{2}]$ with an integer $k$. The reflection $x \mapsto \tfrac{(2k + 1)\pi}{2} - x$ maps this interval onto itself, and $\sin(k\pi + \tfrac{\pi}{2} - x) = \pm \cos x$, so it turns $\sin^2$ into $\cos^2$. With $k = 0$ and $k = 1$, the integral of $\sin^2$ over $[0, \pi]$ is $\tfrac{\pi}{2}$.
3. On $[0, \tfrac{\pi}{3}]$ the method fails: the reflection $x \mapsto \tfrac{\pi}{3} - x$ does not turn $\sin^2$ into $\cos^2$, and indeed $\int_0^{\pi/3} \sin^2 x \, dx = \tfrac{\pi}{6} - \tfrac{\sqrt 3}{8}$ differs from $\int_0^{\pi/3} \cos^2 x \, dx = \tfrac{\pi}{6} + \tfrac{\sqrt 3}{8}$.
4. The same idea computes $\int_0^{\pi/2} \frac{\sin x}{\sin x + \cos x} \, dx = \tfrac{\pi}{4}$: the reflection exchanges the integrand with $\frac{\cos x}{\cos x + \sin x}$, and the two integrands add up to $1$.

## Explanations

### L1 human

Draw the graphs of $\sin^2$ and $\cos^2$ between $0$ and a quarter turn.
One graph is the mirror image of the other, so the areas under them are equal.
At each point the two heights add up to $1$, so the two areas together make a rectangle of height $1$ and width $\tfrac{\pi}{2}$.
Each area is half of the rectangle, which is $\tfrac{\pi}{4}$.

### L2 human

We check Remark 3, where the symmetry is missing.

1. With the antiderivative $\tfrac{x}{2} - \tfrac{\sin 2x}{4}$, the integral of $\sin^2$ over $[0, \tfrac{\pi}{3}]$ is $\tfrac{\pi}{6} - \tfrac{\sin(2\pi/3)}{4} = \tfrac{\pi}{6} - \tfrac{\sqrt 3}{8}$.
2. The integral of $\cos^2 = 1 - \sin^2$ over the same interval is $\tfrac{\pi}{3} - (\tfrac{\pi}{6} - \tfrac{\sqrt 3}{8}) = \tfrac{\pi}{6} + \tfrac{\sqrt 3}{8}$.
3. The two values differ by $\tfrac{\sqrt 3}{4} \neq 0$, so the two integrals are not equal on this interval.

The typical use of the method is an integral over an interval whose reflection exchanges two related integrands with a simple sum.
A trap is to use the symmetry on an interval that the reflection does not map onto itself in the right way, as in step 3.
