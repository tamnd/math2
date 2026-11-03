---
tag: 9PAYP81JKP
kind: example
name: Veselago medium
msc: [78A48, 78A40]
illustrates: [8EW2R66GXS]
uses: [F768YN0P2V, 5MJQ5J5H8Z, NM024G378A, 9VGK0SP6EQ, P3PK0Q02CZ]
sources:
  - url: https://en.wikipedia.org/wiki/Negative-index_metamaterial
---

## Example

A *Veselago medium* is a homogeneous, isotropic, lossless medium whose relative [[permittivity|F768YN0P2V]] $\varepsilon$ and relative [[permeability|5MJQ5J5H8Z]] $\mu$ are both negative at the frequency considered.
It is named after Victor Veselago, who studied the theory of such media in the 1960s.

Check that it carries waves and that it refracts negatively.
Take a [[plane wave|NM024G378A]] $E = E_0 e^{i(k \cdot x - \omega t)}$, $H = H_0 e^{i(k \cdot x - \omega t)}$ with real vectors $k$, $E_0$, $H_0$ and $k \cdot E_0 = 0$.
Maxwell's equations give $k \times E_0 = \omega \mu \mu_0 H_0$ and $k \times H_0 = -\omega \varepsilon \varepsilon_0 E_0$.
They have nonzero solutions when $\abs{k}^2 = \varepsilon \mu \, \omega^2 / c^2$, and $\varepsilon \mu > 0$, so plane waves propagate.
Since $\mu < 0$, the vector $H_0$ points opposite to $k \times E_0$, so $(E_0, H_0, k)$ is a left-handed triple.
The time-averaged [[Poynting vector|P3PK0Q02CZ]] is
$$\tfrac12 E_0 \times H_0 = \frac{E_0 \times (k \times E_0)}{2 \omega \mu \mu_0} = \frac{\abs{E_0}^2}{2 \omega \mu \mu_0} \, k,$$
which points opposite to $k$.
So energy flows against the phase velocity.
Since energy must flow away from a source, the [[refractive index|9VGK0SP6EQ]] is $n = -\sqrt{\varepsilon \mu}$.
At an interface with vacuum, Snell's law $\sin \theta_1 = n \sin \theta_2$ then puts the refracted ray on the same side of the normal as the incident ray.
This is [[negative refraction|8EW2R66GXS]].

## Explanations

### L1 human

In ordinary materials the wave crests move in the same direction as the energy.
In a Veselago medium they move backwards, towards the source, while the energy moves forward.
A beam entering it bends the "wrong" way, to the same side of the normal.
No natural material behaves like this, but metamaterials can approximate it in a range of frequencies.
