---
tag: X2RASNPXQ7
kind: definition
name: Fourier optics
msc: [78A10, 78A45, 42B10]
defines: 14BSX4E9BH
uses: [DPVM34ADZV, 2Z29JN3VES, WQ3PJ4NWAG, N111BHFQ2H]
sources:
  - url: https://en.wikipedia.org/wiki/Fourier_optics
---

## Definition

Consider a monochromatic scalar optical system of wavelength $\lambda$ and wavenumber $k = 2\pi/\lambda$.
*Fourier optics* is the model in which the field in each plane $z = \text{const}$ is a function $u(x, y)$ on $\R^2$.
The system acts by these linear operators:

1. free propagation over a distance $z$ multiplies the [[Fourier transform|DPVM34ADZV]] $\widehat u$ by the transfer function $H_z = e^{2\pi i \gamma z}$ of the [[angular spectrum method|WQ3PJ4NWAG]];
2. a thin optical element multiplies $u$ by its transmission function $t(x, y)$;
3. in particular, in the [[paraxial approximation|N111BHFQ2H]], a thin lens of focal length $f$ has $t(x, y) = e^{-i k (x^2 + y^2)/(2f)}$, restricted to the lens aperture.

## Remarks

Combining these rules in the paraxial approximation gives the Fourier transforming property of a lens.
Let $u_0$ be the field in the front focal plane, and let the lens aperture be large.
Then the field in the back focal plane is
$$u_f(x, y) = \frac{1}{i \lambda f} \, \widehat{u_0}\left( \frac{x}{\lambda f}, \frac{y}{\lambda f} \right),$$
up to a constant phase factor.
Example: a 4f system, two lenses of focal length $f$ separated by $2f$, maps $u_0(x, y)$ to $u_0(-x, -y)$.
A mask $M$ in the common focal plane turns it into a filter that multiplies the spectrum by $M(\lambda f f_x, \lambda f f_y)$.
In coherent imaging, the image is the [[convolution|2Z29JN3VES]] of the ideal image with the amplitude point spread function, whose Fourier transform is a scaled copy of the pupil function.
The model ignores polarisation and treats elements as infinitely thin; thick or strongly scattering elements fall outside it.

## Explanations

### L1 human

Fourier optics treats light in a plane like a signal, and lenses and empty space like filters acting on that signal.
Space between lenses acts on each spatial frequency by a phase, a lens acts by a quadratic phase, and together they perform Fourier transforms.
