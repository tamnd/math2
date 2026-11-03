---
tag: 5T0WAFVWTN
kind: definition
name: Ambient noise seismic interferometry
msc: [86A15, 86A22, 60G10]
defines: S4DMN0NS7Y
uses: [SH6JY9RN2E, DT0QXJE705, 5EHD2XBQDG]
sources:
  - url: https://en.wikipedia.org/wiki/Seismic_interferometry
---

## Definition

Let $u_A(t)$ and $u_B(t)$ be the ground motion recorded at stations $A$ and $B$, modelled as jointly [[stationary random processes|DT0QXJE705]].
Their cross-correlation is
$$C_{AB}(\tau) = \lim_{T \to \infty} \frac{1}{T} \int_0^T u_A(t)\, u_B(t + \tau)\, dt.$$
*Ambient noise seismic interferometry* is the method that computes $C_{AB}$ from long records of ambient noise.
It uses $C_{AB}$ as an estimate of the wave propagation between $A$ and $B$.
Let $G$ be the [[Green's function|SH6JY9RN2E]] of the [[wave equation|5EHD2XBQDG]] of the medium.
The method rests on a fact about diffuse noise fields excited by uncorrelated sources with a white spectrum.
For them, $\frac{d}{d\tau} C_{AB}(\tau)$ is proportional to $G(B, A, \tau) - G(B, A, -\tau)$.
For other source spectra the same relation holds after filtering by the spectrum.
So in all cases $C_{AB}$ has arrivals at $\pm$ the travel time between the stations.

## Remarks

Example: a one-dimensional homogeneous medium of speed $c$, with noise $u(x, t) = f(t - x/c) + g(t + x/c)$ made of two independent white noises $f$ and $g$ of equal power $S$, travelling right and left.
With $A$ at $x = 0$ and $B$ at $x = L$, only $f$ correlates with $f$ and $g$ with $g$, and $E[f(t) f(t + s)] = S\, \delta(s)$, so
$$C_{AB}(\tau) = S\, \delta(\tau - L/c) + S\, \delta(\tau + L/c).$$
The peaks lie at $\pm L/c$, the travel time between $A$ and $B$.
Non-example: if all noise travels to the left ($f = 0$), only the peak at $\tau = -L/c$ remains.
Then the cross-correlation is one-sided and does not give the full Green's function; the method needs noise from all directions.
In practice the records are cut into windows, normalised in time and frequency to reduce earthquakes and spectral peaks, correlated and stacked over months.

## Explanations

### L1 human

Correlate the noise at two stations and average for a long time.
If noise comes from everywhere, the result looks like the signal one station would record if the other one were a source.
