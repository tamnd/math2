---
tag: QSWSVYRCS1
kind: object
name: Mandelbrot set
msc: [37F46, 37F10]
uses: [WDZFV2ACXR, 5M4S7P04GR, SSNFTHZ6YJ, FDVAHRJKF3]
sources:
  - url: https://en.wikipedia.org/wiki/Mandelbrot_set
same_as:
  wikidata: Q257
  wikipedia: Mandelbrot set
---

## Description

For $c \in \C$ let $f_c(z) = z^2 + c$, the [[quadratic family|WDZFV2ACXR]].
The *Mandelbrot set* is
$$M = \set{c \in \C : \text{the sequence } f_c^n(0),\ n \ge 0, \text{ is bounded}}.$$
Here $0$ is the only critical point of $f_c$.
Check of a few points:

1. $c = 0$: the orbit of $0$ is $0, 0, 0, \ldots$, so $0 \in M$.
2. $c = -1$: the orbit is $0, -1, 0, -1, \ldots$, so $-1 \in M$.
3. $c = i$: the orbit is $0, i, -1 + i, -i, -1 + i, -i, \ldots$, so $i \in M$.
4. $c = 1$: the orbit is $0, 1, 2, 5, 26, \ldots$, which is unbounded, so $1 \notin M$.

If some $\abs{f_c^n(0)} > 2$, the orbit tends to $\infty$.
So $M$ is the set of $c$ with $\abs{f_c^n(0)} \le 2$ for all $n$, and $M$ is a compact subset of the disc $\abs{c} \le 2$.

## Remarks

A parameter $c$ lies in $M$ exactly when the [[Julia set|5M4S7P04GR]] of $f_c$ is connected.
For $c \notin M$ the Julia set is a Cantor set.
Douady and Hubbard proved that $M$ is connected.
Its intersection with the real line is the interval $[-2, 1/4]$.
Shishikura proved that the boundary of $M$ has [[Hausdorff dimension|SSNFTHZ6YJ]] $2$.
The main cardioid is the set of $c = \lambda/2 - \lambda^2/4$ with $\abs{\lambda} < 1$.
For these $c$, the map $f_c$ has a fixed point with multiplier $\lambda$, hence an attracting fixed point.
Whether $M$ is [[locally connected|FDVAHRJKF3]] is an open problem, known as the MLC conjecture.

## Explanations

### L1 human

For each complex number $c$, start at $0$ and apply $z \mapsto z^2 + c$ again and again.
Colour $c$ black if the numbers you get stay bounded, and leave it white if they run off to infinity.
The black region is the Mandelbrot set, a cardioid with discs and filaments attached, and with smaller copies of itself everywhere along its edge.
It is a map of the whole quadratic family: each point tells whether the Julia set of that map is one connected piece or dust.
