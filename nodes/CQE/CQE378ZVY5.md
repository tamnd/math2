---
tag: CQE378ZVY5
kind: example
name: Newton fractal
msc: [37F10, 65H05]
instance_of: [5M4S7P04GR]
uses: [07EXVNF9VP, 5M4S7P04GR, C0N0XGC6GK, 0XDK9CGYKJ]
sources:
  - url: https://en.wikipedia.org/wiki/Newton_fractal
same_as:
  wikidata: Q1151001
  wikipedia: Newton fractal
---

## Example

Let $p(z) = z^3 - 1$, with roots $1$, $\omega = e^{2\pi i/3}$ and $\omega^2$.
[[Newton's method|07EXVNF9VP]] for $p$ iterates the [[rational function|0XDK9CGYKJ]]
$$N(z) = z - \frac{p(z)}{p'(z)} = \frac{2z^3 + 1}{3z^2}.$$
The *Newton fractal* of $p$ is the [[Julia set|5M4S7P04GR]] $J(N)$.
It is usually drawn with each point of the [[Fatou set|C0N0XGC6GK]] coloured by the root its orbit tends to.

Check of the main features:

1. Each root $r$ is a superattracting fixed point: $N(r) = r$ since $p(r) = 0$, and $N'(z) = p(z) p''(z) / p'(z)^2$ vanishes at $r$.
2. So each root has an open basin of attraction, contained in the Fatou set.
3. The map $N$ commutes with $z \mapsto \omega z$, so the picture has threefold rotational symmetry.
4. The Julia set is the common boundary of the three basins: every point of $J(N)$ lies in the closure of each basin.

## Remarks

Newton's method can therefore fail in a complicated way: arbitrarily close to the boundary of one basin there are starting points that converge to each of the other roots.
For a quadratic polynomial with two distinct roots, the Newton map is conjugate to $z \mapsto z^2$.
Then the Julia set is the perpendicular bisector of the two roots, a result going back to Cayley.

## Explanations

### L1 human

Newton's method guesses a root of a polynomial and improves the guess again and again.
Colour each starting point in the plane by the root that the guesses settle on.
For $z^3 - 1$ there are three colours, and the borders between them form an endlessly detailed fractal.
Near any border point all three colours appear, so a tiny change of the starting guess can change which root is found.
