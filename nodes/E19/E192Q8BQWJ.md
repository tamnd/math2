---
tag: E192Q8BQWJ
kind: example
name: Fold catastrophe
msc: [58K35, 37G10]
illustrates: [23RVD8K8RB, KSAFWZVB8K]
uses: [0YTCMFB4HC, KSAFWZVB8K, MAP5J6HK0T]
sources:
  - url: https://en.wikipedia.org/wiki/Catastrophe_theory
---

## Example

The *fold catastrophe* is the one-parameter family of functions
$$V_a(x) = x^3 + a x, \qquad x, a \in \R.$$
Its [[critical points|0YTCMFB4HC]] solve $V_a'(x) = 3x^2 + a = 0$.

1. For $a < 0$ there are two critical points $x = \pm \sqrt{-a/3}$; since $V_a''(x) = 6x$, the point $-\sqrt{-a/3}$ is a local maximum and $\sqrt{-a/3}$ is a local minimum.
2. For $a = 0$ there is one critical point, $x = 0$, and it is degenerate, since $V_0''(0) = 0$.
3. For $a > 0$ there are no critical points.

So as $a$ increases through $0$, the minimum and the maximum approach each other, merge at $x = 0$ and disappear.
The bifurcation set, the set of parameters where a degenerate critical point occurs, is the single point $a = 0$.
The family is the [[universal unfolding|KSAFWZVB8K]] of the germ $x^3$.
Indeed, the derivative of $V_a$ in $a$ is $x$, and $1$ and $x$ span $\mathcal{E}_1$ modulo the ideal $(x^2)$.

## Explanations

### L1 human

Picture a ball resting in a dip of a curve that has a dip next to a hump.
As the parameter $a$ grows, the dip and the hump become shallower and slide toward each other.
At $a = 0$ they merge into a flat inflection, and after that the dip is gone, so the ball suddenly rolls away.
This sudden loss of a resting state is the fold catastrophe, and in dynamics it appears as the [[saddle-node bifurcation|MAP5J6HK0T]].
