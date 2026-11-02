---
tag: JCMXX84BWT
kind: definition
name: Relaxation oscillation
msc: [34C26, "34E15"]
defines: 2NHWCM0DK8
uses: [0AA97XA70K, 0V33BNKZ9S, 0673D85QKZ]
sources:
  - url: https://en.wikipedia.org/wiki/Relaxation_oscillator
---

## Definition

Let $f, g \colon \R^2 \to \R$ be [[smooth|0V33BNKZ9S]], and for $\varepsilon > 0$ consider the planar slow–fast [[autonomous system|0673D85QKZ]]
$$\varepsilon x' = f(x, y), \qquad y' = g(x, y).$$
Here $x$ is the fast variable and $y$ is the slow variable.
The *critical manifold* is the curve $S = \set{(x, y) : f(x, y) = 0}$.
Its points with $\partial f / \partial x < 0$ form the attracting part of $S$, and its points with $f = \partial f / \partial x = 0$ are the fold points.
A *relaxation oscillation* is a family of [[periodic orbits|0AA97XA70K]] $\Gamma_\varepsilon$, for small $\varepsilon > 0$, such that, as $\varepsilon \to 0$:

1. $\Gamma_\varepsilon$ converges, in the Hausdorff distance, to a closed curve $\Gamma_0$;
2. $\Gamma_0$ is a union of arcs of the attracting part of $S$, traversed in the direction of the slow flow $y' = g(x, y)$;
3. the other pieces of $\Gamma_0$ are horizontal segments $y = \text{const}$ that start at fold points;
4. $\Gamma_0$ contains at least one horizontal segment.

## Remarks

Along the arcs of $S$ the motion takes a time of order $1$, and along the horizontal segments, the jumps, it takes a time of order $\varepsilon$.

Example: the van der Pol equation $u'' - \mu(1 - u^2) u' + u = 0$ with large $\mu$.
With $F(x) = x^3/3 - x$, $\varepsilon = 1/\mu^2$ and a rescaled time, it becomes $\varepsilon x' = y - F(x)$, $y' = -x$.
The critical manifold is the cubic $y = F(x)$; its attracting part is $\abs{x} > 1$ and its fold points are $(\pm 1, \mp 2/3)$.
The limit curve $\Gamma_0$ runs down the right branch from $(2, 2/3)$ to $(1, -2/3)$, jumps to $(-2, -2/3)$, runs up the left branch to $(-1, 2/3)$, and jumps back to $(2, 2/3)$.
The period of the van der Pol oscillation is about $(3 - 2 \ln 2)\, \mu$ for large $\mu$.

Non-example: the harmonic oscillator $x' = y$, $y' = -x$ has periodic orbits, but no small parameter and no fast variable, so it is not of the slow–fast form.

Some authors use the term more loosely, for any oscillation with slow phases and fast jumps.
