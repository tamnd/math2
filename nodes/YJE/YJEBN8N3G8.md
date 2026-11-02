---
tag: YJEBN8N3G8
kind: concept
name: WKB approximation
msc: ["34E20", "34E05"]
sources:
  - url: https://en.wikipedia.org/wiki/WKB_approximation
same_as:
  wikidata: Q907306
  wikipedia: WKB approximation
---

## Summary

The WKB approximation gives approximate solutions of linear differential equations whose highest derivative is multiplied by a small parameter, such as $\varepsilon^2 y'' = Q(x) y$.
It writes the solution as the exponential of a series in $\varepsilon$ and keeps the first terms.
It is also called the Liouville–Green method, and the name WKB refers to Wentzel, Kramers and Brillouin.
It is the basis of semiclassical approximations in quantum mechanics and of the asymptotics of special functions.

## Explanations

### L1 human

When a wave travels through a medium that changes slowly, it looks locally like a pure wave.
The WKB approximation lets the local wavelength and amplitude change slowly along the way.
For $\varepsilon^2 y'' = -k(x)^2 y$ with $k > 0$, the solutions are close to $k(x)^{-1/2} \cos\bigl(\frac{1}{\varepsilon} \int k(x) \, dx + c\bigr)$.
If $k$ is constant, this is exactly a cosine of frequency $k / \varepsilon$.
The approximation breaks down where $k$ vanishes, at turning points.
