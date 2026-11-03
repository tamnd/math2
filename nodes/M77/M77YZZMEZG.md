---
tag: M77YZZMEZG
kind: definition
name: Propagator
msc: [81T18, 81Q30]
defines: K9SR95P4NJ
uses: [SH6JY9RN2E, AYCCDQWCJF, DPVM34ADZV, AES2T5JPFP]
sources:
  - url: https://en.wikipedia.org/wiki/Propagator
---

## Definition

Let $m > 0$ and use Minkowski space $\R^{1,3}$ with metric of signature $(+,-,-,-)$, so $p^2 = p_0^2 - \abs{\mathbf{p}}^2$.
The *Feynman propagator* of the free real scalar field of mass $m$ is the [[tempered distribution|AES2T5JPFP]]
$$\Delta_F(x) = \lim_{\varepsilon \to 0^+} \int_{\R^4} \frac{d^4p}{(2\pi)^4} \, \frac{i\, e^{-ip \cdot x}}{p^2 - m^2 + i\varepsilon}.$$
For the free field $\phi$ with vacuum $\lvert 0 \rangle$, it satisfies $\Delta_F(x - y) = \langle 0 \rvert T\{\phi(x)\phi(y)\} \lvert 0 \rangle$, where $T$ orders the fields by decreasing time.
More generally, a *propagator* of a free field is a [[Green's function|SH6JY9RN2E]] of its field equation, or a two-point function of the free field.

## Remarks

Check that $\Delta_F$ is a Green's function of the [[Klein–Gordon equation|AYCCDQWCJF]].
With $\square = \partial_t^2 - \nabla^2$, one has $(\square + m^2) e^{-ip\cdot x} = (m^2 - p^2) e^{-ip \cdot x}$.
So $(\square + m^2)\Delta_F(x) = -i \int \frac{d^4p}{(2\pi)^4} e^{-ip\cdot x} = -i\,\delta^4(x)$.

The $i\varepsilon$ selects the Feynman boundary condition: positive frequencies travel forward in time and negative frequencies backward.
Other choices of contour give the retarded and advanced propagators, which are also Green's functions but vanish before, or after, the source.

Non-example: the Wightman function $W(x - y) = \langle 0 \rvert \phi(x)\phi(y) \lvert 0 \rangle$ is a two-point function but not a Green's function.
It solves the homogeneous equation $(\square + m^2) W = 0$.

In Euclidean space $\R^d$ the propagator is $G(x) = \int \frac{d^dp}{(2\pi)^d} \frac{e^{ip\cdot x}}{\abs{p}^2 + m^2}$, which solves $(-\Delta + m^2) G = \delta$.
It is the [[Fourier transform|DPVM34ADZV]] of $1/(\abs{p}^2 + m^2)$, and the Wick rotation $p_0 \to i p_4$ relates it to $\Delta_F$.
