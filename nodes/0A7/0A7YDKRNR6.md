---
tag: 0A7YDKRNR6
kind: definition
name: Complex sine and cosine
msc: [33B10]
defines: 00NZKRSWNX
uses: [054VXHMCA3]
sources:
  - url: https://en.wikipedia.org/wiki/Sine_and_cosine
    locator: Complex exponential function definitions
  - url: https://en.wikipedia.org/wiki/Sine_and_cosine
    locator: Complex arguments
---

## Definition

For $z \in \mathbb{C}$, the complex sine and the complex cosine of $z$ are
$$\sin z = \frac{e^{iz} - e^{-iz}}{2i}, \qquad \cos z = \frac{e^{iz} + e^{-iz}}{2},$$
where $e^w$ is the [[complex exponential|054VXHMCA3]] of $w$.

## Remarks

For real $z$, these are the usual sine and cosine, by [[Euler's formula|04R3CY41VJ]].
The functions $\sin$ and $\cos$ are [[entire|0419794R0T]], with $\sin' = \cos$ and $\cos' = -\sin$. The identity $\sin^2 z + \cos^2 z = 1$ holds for each $z \in \mathbb{C}$.
They are not bounded on $\mathbb{C}$. For real $y$, $\cos(iy) = \cosh y = \frac{e^y + e^{-y}}{2}$.
The [[power series of the cosine|0Z1G2F8DGY]] is the same as in the real case.

## Explanations

### L1 human

Euler's formula $e^{i\theta} = \cos \theta + i \sin \theta$ lets us solve for $\cos \theta$ and $\sin \theta$ in terms of exponentials.
These formulas make sense for every complex number, so we use them to define $\sin z$ and $\cos z$.
On the imaginary axis they grow very fast: $\cos(10 i)$ is more than $10000$.
