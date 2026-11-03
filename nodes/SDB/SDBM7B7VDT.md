---
tag: SDBM7B7VDT
kind: definition
name: Perfectly matched layer
msc: [78A40, 65N99, 65M99]
defines: GFKAG6BAXX
uses: [MNXKTXJ35G, 9BWWD4QK8Y, NM024G378A]
sources:
  - url: https://en.wikipedia.org/wiki/Perfectly_matched_layer
---

## Definition

Consider time-harmonic waves with time factor $e^{-i\omega t}$, $\omega > 0$, governed by the [[Helmholtz equation|MNXKTXJ35G]] or by the [[Maxwell equations|9BWWD4QK8Y]] in a homogeneous medium.
Let the physical domain be the half-space $x < L$, and let the layer be $L < x < L + \delta$ with $\delta > 0$.
Let $\sigma \colon \R \to [0, \infty)$ be continuous, with $\sigma = 0$ for $x \le L$ and $\sigma > 0$ in the layer.
The complex stretched coordinate is
$$\tilde{x}(x) = x + \frac{i}{\omega} \int_L^x \sigma(s) \, ds.$$
A *perfectly matched layer* in the direction $x$ is the layer $L < x < L + \delta$ in which every derivative $\partial_x$ in the equations is replaced by $\partial_{\tilde{x}} = \frac{1}{1 + i \sigma(x)/\omega} \partial_x$.
The layer is closed at $x = L + \delta$ by a simple boundary condition, such as a zero field.

## Remarks

Check that a [[plane wave|NM024G378A]] passes into the layer without reflection.
Let $u = e^{i(k_x x + k_y y + k_z z)}$ solve the equation for $x < L$, with $k_x > 0$, so that it travels towards the layer.
The function $e^{i(k_x \tilde{x} + k_y y + k_z z)}$ solves the stretched equation, and it equals $u$ for $x \le L$.
For $x > L$ it equals $u \exp\big(-\frac{k_x}{\omega} \int_L^x \sigma(s) \, ds\big)$, which decays.
So the incoming wave continues into the layer without any reflected wave, whatever $k_y$, $k_z$ and $\omega$ are.

After the wave reflects at the end of the layer and comes back, its amplitude is multiplied by $R = \exp\big(-\frac{2 k_x}{\omega} \int_L^{L+\delta} \sigma(s) \, ds\big)$.
In vacuum, with $k_x = (\omega / c) \cos \theta$ at incidence angle $\theta$, this is $R = \exp\big(-\frac{2 \cos \theta}{c} \int_L^{L+\delta} \sigma \, ds\big)$, which is small except near grazing incidence.

Non-example: adding a real conductivity to the material in the layer, without the matching magnetic loss, is not a PML.
Its wave impedance differs from that of the domain, so part of the wave reflects at $x = L$.

After discretization the layer is no longer exactly reflectionless, so $\sigma$ is made to grow gradually, for example as a power of $x - L$.

## Explanations

### L1 human

The trick is to let the coordinate $x$ become complex inside the layer.
An outgoing wave $e^{ikx}$ then turns into a decaying exponential, while its form at the entrance stays unchanged.
Because nothing changes at the entrance, nothing reflects there.
