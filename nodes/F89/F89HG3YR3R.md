---
tag: F89HG3YR3R
kind: example
name: Plummer model
msc: [85A05, 85A15]
instance_of: [9YTGKNPMCP]
uses: [DWK5N5SKTK, ANRZZMH2Q0, 3XQ8W7ZKMB]
sources:
  - url: https://en.wikipedia.org/wiki/Plummer_model
same_as:
  wikidata: Q2099709
  wikipedia: Plummer model
---

## Example

Let $M > 0$ be a total mass, $a > 0$ a scale length and $G$ the gravitational constant.
Let $r$ be the distance from the centre.
The *Plummer model* has density and potential
$$\rho(r) = \frac{3M}{4\pi a^3} \left( 1 + \frac{r^2}{a^2} \right)^{-5/2}, \qquad \Phi(r) = -\frac{G M}{\sqrt{r^2 + a^2}}.$$

Check of [[Poisson's equation|DWK5N5SKTK]] $\Delta \Phi = 4\pi G \rho$: here $r^2 \Phi'(r) = G M r^3 (r^2 + a^2)^{-3/2}$, whose derivative is $3 G M a^2 r^2 (r^2 + a^2)^{-5/2}$.
Dividing by $r^2$ gives $\Delta \Phi = 3 G M a^2 (r^2 + a^2)^{-5/2} = 4 \pi G \rho$.
The mass inside radius $r$ is $M(r) = M r^3 / (r^2 + a^2)^{3/2}$, which tends to $M$ as $r \to \infty$.

It is a [[polytrope|9YTGKNPMCP]] of index $5$: $\rho \propto (-\Phi)^5$, and $\theta(\xi) = (1 + \xi^2/3)^{-1/2}$ solves the [[Lane–Emden equation|ANRZZMH2Q0]] of index $5$.

## Remarks

By [[Jeans's theorem|3XQ8W7ZKMB]], the distribution function $f(E) \propto (-E)^{7/2}$ for $E < 0$, and $f = 0$ otherwise, where $E = \frac{1}{2} v^2 + \Phi$, is a steady isotropic stellar system whose density is the Plummer density.
The half-mass radius solves $r^3/(r^2 + a^2)^{3/2} = 1/2$, which gives $r_h = a / \sqrt{2^{2/3} - 1} \approx 1.305 \, a$.
Plummer introduced the model to fit the light of globular clusters, and it is the standard initial condition in simulations of star clusters.

## Explanations

### L1 human

The Plummer model is a ball of stars that is dense in the middle and thins out smoothly, with no sharp edge but a finite total mass.
Its formulas are simple enough to check by hand, which makes it the first example in most courses on star clusters.
Its gravity near the centre is like that of a uniform ball, and far away like that of a point of mass $M$.
