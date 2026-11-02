---
tag: B416H6DQDA
kind: example
name: Butterfly catastrophe
msc: [58K35, 58K05]
illustrates: [6FKJ6SXP3G, 23RVD8K8RB]
uses: [6FKJ6SXP3G, JV45S0KQE6, 0YTCMFB4HC]
sources:
  - url: https://en.wikipedia.org/wiki/Catastrophe_theory
---

## Example

The *butterfly catastrophe* is the family of functions of one variable $x \in \R$
$$V(x; a, b, c, d) = x^6 + a x^4 + b x^3 + c x^2 + d x,$$
with four control parameters $(a, b, c, d) \in \R^4$.
For $a = b = c = d = 0$ the function is $x^6$, whose [[critical point|0YTCMFB4HC]] at $0$ is degenerate: the first five derivatives vanish there.

The derivative $V'(x) = 6x^5 + 4a x^3 + 3b x^2 + 2c x + d$ has degree $5$, so $V$ has at most five critical points.
Since $V(x) \to +\infty$ as $x \to \pm\infty$, nondegenerate critical points alternate minimum, maximum, minimum, maximum, minimum.
So $V$ can have three local minima, which the fold, cusp and swallowtail cannot.

Check with $a = -15/2$, $b = 0$, $c = 12$, $d = 0$.
Then $V(x) = x^6 - \tfrac{15}{2} x^4 + 12 x^2$ and
$$V'(x) = 6x^5 - 30x^3 + 24x = 6x(x^2 - 1)(x^2 - 4).$$
The critical points are $-2, -1, 0, 1, 2$.
The sign of $V'$ is negative on $(-\infty, -2)$ and changes at each of the five simple roots.
So $-2, 0, 2$ are local minima and $-1, 1$ are local maxima.
The region of parameters with three minima is the "pocket" of the butterfly, bounded by the [[bifurcation set|JV45S0KQE6]].

## Explanations

### L1 human

The butterfly is the elementary catastrophe of one state variable with four control knobs.
Its potential $x^6 + \cdots$ can have up to three valleys at once.
For the settings in the example, the valleys sit at $x = -2$, $0$ and $2$, with hills at $\pm 1$ between them.
A system that rests in the middle valley can be pushed into either side valley as the knobs move.
That extra middle state is what the butterfly adds to the simpler cusp.
