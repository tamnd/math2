---
tag: EKFNRMFDVQ
kind: definition
name: Seismic ray theory
msc: [86A15, 74J05, 78A05]
defines: AZFGJKMKTP
uses: [6W00ZECYT0, 80737NDZ4V, HGMX1QGTAZ, RKX9XJ0RVW, EEPJJHC5JZ, GZ7E9GHQYB]
sources:
  - url: https://en.wikipedia.org/wiki/Seismic_wave
---

## Definition

Let an isotropic [[linearly elastic|6W00ZECYT0]] medium in a region of $\R^3$ have density $\rho(x) > 0$ and [[Lamé parameters|80737NDZ4V]] $\lambda(x)$, $\mu(x)$, all smooth.
Its P-speed and S-speed are $\alpha = \sqrt{(\lambda + 2\mu)/\rho}$ and $\beta = \sqrt{\mu/\rho}$.
*Seismic ray theory* is the asymptotic approximation of time-harmonic solutions of the elastic wave equation, as the angular frequency $\omega \to \infty$, by a ray series
$$u(x, t) = e^{i\omega (t - T(x))} \sum_{k \ge 0} \frac{A_k(x)}{(i\omega)^k}.$$
At leading order:

1. The travel time $T$ satisfies the [[eikonal equation|HGMX1QGTAZ]] $\abs{\nabla T}^2 = 1/v^2$, with $v = \alpha$ for a [[P-wave|EEPJJHC5JZ]] and $v = \beta$ for an [[S-wave|GZ7E9GHQYB]].
2. The amplitude $A_0$ is parallel to $\nabla T$ for a P-wave and orthogonal to $\nabla T$ for an S-wave.
3. The *rays* are the curves $x(s)$, with $s$ the arc length, such that $dx/ds = v \nabla T$; they satisfy
$$\frac{d}{ds}\Big(\frac{1}{v} \frac{dx}{ds}\Big) = \nabla \frac{1}{v}.$$

## Remarks

The higher terms $A_k$ solve transport equations along the rays and give the amplitudes; conservation of energy in a ray tube is their leading form.
Example: if $v$ is constant, $T(x) = \abs{x - x_0}/v$ solves the eikonal equation away from $x_0$, since $\abs{\nabla T} = 1/v$, and the rays are straight lines from the source $x_0$.
Non-example: suppose the medium changes over a distance shorter than a wavelength, for instance at a thin layer.
Then the ray series does not approximate the true wave field, and ray theory does not apply.
The ray equation in clause 3 is the Euler–Lagrange equation of the travel time $\int ds/v$, which is [[Fermat's principle|RKX9XJ0RVW]] for seismic rays.
At a sharp interface rays are joined by Snell's law, and each interface creates reflected and transmitted P- and S-rays.
