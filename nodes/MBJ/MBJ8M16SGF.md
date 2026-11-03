---
tag: MBJ8M16SGF
kind: definition
name: Phase-field model
msc: [74N20, 74N15, 35K55]
defines: 8M441PD0GX
uses: [7S813PEV69, DKN15NVKSB]
sources:
  - url: https://en.wikipedia.org/wiki/Phase-field_model
---

## Definition

Let $\Omega \subset \R^n$ be a bounded domain.
A *phase-field model* on $\Omega$ consists of the following data.

1. An *order parameter*, or phase field, $\phi \colon \Omega \times [0, T) \to \R$.
   Its distinct preferred values label the phases.
2. A free energy functional
$$F[\phi] = \int_\Omega \left( f(\phi) + \frac{\varepsilon^2}{2} \abs{\nabla \phi}^2 \right) dx,$$
where $f$ is a bulk energy density with a local minimum at each preferred value.
The small parameter $\varepsilon > 0$ sets the width of the interfaces.
3. An evolution law that is a gradient flow of $F$.
It is either non-conserved,
$$\partial_t \phi = -M \frac{\delta F}{\delta \phi} = M\left(\varepsilon^2 \Delta \phi - f'(\phi)\right),$$
or conserved,
$$\partial_t \phi = \nabla \cdot \left( M \nabla \frac{\delta F}{\delta \phi} \right).$$
Here $M > 0$ is a mobility, and $\delta F / \delta \phi = f'(\phi) - \varepsilon^2 \Delta \phi$ is the variational derivative.

## Remarks

Example: the double-well density $f(\phi) = \tfrac14 (\phi^2 - 1)^2$ has minima at $\phi = \pm 1$.
With the non-conserved law it gives the [[Allen–Cahn equation|7S813PEV69]] $\partial_t \phi = M(\varepsilon^2 \Delta \phi - \phi^3 + \phi)$.
With the conserved law it gives the [[Cahn–Hilliard equation|DKN15NVKSB]].
In one dimension the profile $\phi(x) = \tanh\left(x / (\sqrt{2}\,\varepsilon)\right)$ is a stationary interface of width of order $\varepsilon$: it satisfies $\varepsilon^2 \phi'' = \phi^3 - \phi$.

Non-example: an evolution $\partial_t \phi = +M \, \delta F / \delta \phi$ is not a phase-field model, because it increases $F$ instead of decreasing it.

In solid mechanics the free energy often also contains an elastic energy that depends on $\phi$.
The order parameter may then be a vector, for instance with one component per martensite variant.
