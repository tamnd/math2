---
tag: DE8R41FXZD
kind: definition
name: Osculating orbit
msc: [70F15, 70M20]
defines: KAJTW4B41Q
uses: [BXFSBB8Q46, K6KNWEVRY4]
sources:
  - url: https://en.wikipedia.org/wiki/Osculating_orbit
---

## Definition

Let $\mu > 0$ and let $r \colon I \to \R^3 \setminus \set{0}$ be a twice differentiable motion that solves
$$r'' = -\frac{\mu\, r}{\norm{r}^3} + f(t, r, r')$$
for a perturbing acceleration $f$.
The *osculating orbit* at time $t_1 \in I$ is the [[Kepler orbit|BXFSBB8Q46]] with parameter $\mu$ of the solution $s$ of $s'' = -\mu\, s / \norm{s}^3$ with $s(t_1) = r(t_1)$ and $s'(t_1) = r'(t_1)$.
Its [[orbital elements|K6KNWEVRY4]] are the *osculating elements* of the motion at time $t_1$.

## Remarks

Example: if $f = 0$, then $r$ itself solves the Kepler problem, so the osculating orbit is the same at every time and the osculating elements are constant.

Non-example: the Kepler orbit through $r(t_1)$ with velocity $r'(t_1) + w$ for some $w \ne 0$ is not the osculating orbit at $t_1$, because its velocity at $t_1$ differs from that of the motion.

The osculating orbit depends on the choice of $\mu$, that is, on which body is taken as the centre and which forces count as perturbations.
