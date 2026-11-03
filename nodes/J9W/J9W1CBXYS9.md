---
tag: J9W1CBXYS9
kind: definition
name: Travel-time tomography
msc: [86A22, 86A15, 44A12]
defines: 3CW42MYP4Y
uses: [JRN1693EHB, RKX9XJ0RVW, HGMX1QGTAZ, VJNZJ352PC]
sources:
  - url: https://en.wikipedia.org/wiki/Seismic_tomography
---

## Definition

Let $v > 0$ be the wave speed on a region $\Omega$ and let $u = 1/v$ be the slowness.
For a source $s$ and a receiver $r$, the travel time is
$$t(s, r) = \int_{\gamma} u \, d\ell.$$
Here $d\ell$ is arc length, and $\gamma$ is the ray from $s$ to $r$, a path that makes the travel time stationary by [[Fermat's principle|RKX9XJ0RVW]].
*Travel-time tomography* is the [[seismic tomography|JRN1693EHB]] that estimates $u$ from the observed travel times $t_i$ of many source-receiver pairs.
In linearised form, for a reference slowness $u_0$ with rays $\gamma_i^0$, it solves the following equations for the slowness perturbation $\delta u = u - u_0$:
$$t_i - t_i^0 = \int_{\gamma_i^0} \delta u \, d\ell, \qquad i = 1, \dots, N.$$
Here $t_i^0$ are the travel times in $u_0$.

## Remarks

The linearisation keeps the reference rays, because by Fermat's principle the first-order change of the path does not change the time.
Example: two unit square cells side by side with slownesses $u_1, u_2$; a horizontal ray through both has time $u_1 + u_2$, and a vertical ray through cell $1$ has time $u_1$.
Times $t_1 = 1.2$ and $t_2 = 0.5$ give $u_1 = 0.5$ and $u_2 = 0.7$, so both cells are determined.
Non-example of a well-posed set-up: with only the horizontal ray, only the sum $u_1 + u_2$ is known, so the data do not determine the model.
For a constant reference speed the rays are straight lines, and the data are samples of the [[Radon transform|VJNZJ352PC]] (in two dimensions) of $\delta u$.
Travel times in a general medium solve the [[eikonal equation|HGMX1QGTAZ]] $\abs{\nabla t} = u$, which is used to compute rays and times.

## Explanations

### L1 human

The travel time of a wave adds up the slowness along its path.
Travel-time tomography collects many such sums along crossing paths and solves for the slowness in each part of the region.
