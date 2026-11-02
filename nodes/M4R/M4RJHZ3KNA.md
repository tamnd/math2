---
tag: M4RJHZ3KNA
kind: example
name: Total variation denoising
msc: [94A08, 68U10, 49J45]
illustrates: [8QA5DEWNYD]
uses: [8QA5DEWNYD, SASP14MA1Z, 07Q7CNM5WF]
sources:
  - url: https://en.wikipedia.org/wiki/Total_variation_denoising
same_as:
  wikidata: Q7828156
  wikipedia: Total variation denoising
---

## Example

Let $\Omega \subseteq \R^n$ be a bounded open set, let $f \in L^2(\Omega)$ be a noisy image, and let $\lambda > 0$.
For $u \in L^2(\Omega)$ let
$$TV(u) = \sup \Big\{ \int_\Omega u \operatorname{div} \varphi \, dx : \varphi \in C^1_c(\Omega; \R^n), \ \abs{\varphi(x)} \le 1 \text{ for all } x \Big\},$$
the [[total variation|8QA5DEWNYD]] of $u$, which equals $\int_\Omega \abs{\nabla u} \, dx$ for smooth $u$.
*Total variation denoising*, in the model of Rudin, Osher and Fatemi, replaces $f$ by the minimizer of
$$E(u) = TV(u) + \frac{\lambda}{2} \int_\Omega (u - f)^2 \, dx, \qquad u \in L^2(\Omega).$$
The functional $E$ is lower semicontinuous, coercive and strictly [[convex|07Q7CNM5WF]] on the [[Lp space|SASP14MA1Z]] $L^2(\Omega)$, so it has exactly one minimizer.

A worked case on $\Omega = (0, 1)$: let $h > 0$ and $f = h$ on $(0, \tfrac12)$, $f = 0$ on $(\tfrac12, 1)$, a single edge of height $h$.
Assume $\lambda \ge 4/h$ and set $\delta = 2/\lambda$.
The minimizer is $u = h - \delta$ on $(0, \tfrac12)$ and $u = \delta$ on $(\tfrac12, 1)$.

Check: let $w(x) = 2x$ on $[0, \tfrac12]$ and $w(x) = 2 - 2x$ on $[\tfrac12, 1]$.
Then $\abs{w} \le 1$, $w(0) = w(1) = 0$, $w' = \lambda (f - u)$, and $\int_0^1 u w' \, dx = h - 2\delta = TV(u)$.
For every $v$ one has $TV(v) \ge \int_0^1 v w' \, dx$, and expanding the squares gives $E(v) - E(u) \ge \frac{\lambda}{2} \int_0^1 (v - u)^2 \, dx \ge 0$.

## Remarks

The edge survives at the same place, and its height drops from $h$ to $h - 4/\lambda$.
A quadratic penalty $\int \abs{\nabla u}^2$ instead of $TV(u)$ would smear the jump into a smooth ramp.
If $\lambda < 4/h$, the minimizer is the constant $h/2$, so a weak fidelity term erases small edges.

## Explanations

### L1 human

A noisy photo has many small random oscillations.
Total variation denoising looks for an image close to the photo whose total amount of up-and-down change is small.
Noise has a lot of such change and is removed.
A sharp edge costs only its height, not its steepness, so edges are kept, though with a little less contrast.
In the example, a step of height $h$ comes out as a step of height $h - 4/\lambda$.
