---
tag: C1JFRZEPWR
kind: definition
name: Fraunhofer diffraction
msc: [78A45]
defines: D7YGBADRV9
uses: [4JZ84R10NJ, VYZJKBBKKR, DPVM34ADZV]
sources:
  - url: https://en.wikipedia.org/wiki/Fraunhofer_diffraction
---

## Definition

Let $u_0(\xi, \eta)$ be the complex amplitude of a monochromatic field in the plane $z = 0$, with wavelength $\lambda$ and wavenumber $k = 2\pi/\lambda$.
Assume $u_0$ is supported in the disk $\xi^2 + \eta^2 \le a^2$.
Assume the observation distance satisfies $z \gg k a^2 / 2$, so that the [[Fresnel number|VYZJKBBKKR]] $a^2/(\lambda z)$ is much smaller than $1$.
Then the factor $e^{i k (\xi^2 + \eta^2)/(2z)}$ in the [[Fresnel diffraction integral|4JZ84R10NJ]] is close to $1$, and the field is
$$u(x, y, z) = \frac{e^{i k z} \, e^{i k (x^2 + y^2)/(2z)}}{i \lambda z} \, \widehat{u_0}\left( \frac{x}{\lambda z}, \frac{y}{\lambda z} \right),$$
where $\widehat{u_0}(f_x, f_y) = \iint u_0(\xi, \eta) e^{-2\pi i (f_x \xi + f_y \eta)} d\xi \, d\eta$ is the [[Fourier transform|DPVM34ADZV]].
*Fraunhofer diffraction* is the diffraction pattern in this regime; its intensity is $\abs{\widehat{u_0}(x/(\lambda z), y/(\lambda z))}^2 / (\lambda z)^2$.

## Remarks

Example: a slit of width $a$, with $u_0 = 1$ for $\abs{\xi} \le a/2$ (in one transverse variable), gives $\widehat{u_0}(f) = a \, \frac{\sin(\pi a f)}{\pi a f}$.
So the intensity is proportional to $\left(\frac{\sin \beta}{\beta}\right)^2$ with $\beta = \pi a x / (\lambda z)$, and the dark fringes lie at $x = m \lambda z / a$ for nonzero integers $m$.
Non-example: for $a = 1$ cm, $\lambda = 500$ nm and $z = 1$ m, one has $k a^2 / 2 \approx 600$ m, so the condition fails and the pattern on the screen is a Fresnel pattern.
A converging lens of focal length $f$ produces the Fraunhofer pattern in its focal plane, with $z$ replaced by $f$.

## Explanations

### L1 human

Far enough from the aperture, the waves from different points of the aperture arrive almost parallel.
Their phase differences then depend linearly on the position in the aperture, and adding them up is exactly a Fourier transform.
