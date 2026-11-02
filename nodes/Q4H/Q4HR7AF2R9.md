---
tag: Q4HR7AF2R9
kind: definition
name: Sine and cosine transforms
msc: ["42A38", "44A15"]
defines: C07WNRSW52
uses: [X7GTF3D98F, DPVM34ADZV]
sources:
  - url: https://en.wikipedia.org/wiki/Sine_and_cosine_transforms
---

## Definition

Let $f \colon [0, \infty) \to \C$ be a Lebesgue [[integrable function|X7GTF3D98F]].
The *cosine transform* of $f$ is the function on $[0, \infty)$ given by
$$\mathcal{F}_c f(\xi) = \int_0^\infty f(x) \cos(2\pi x \xi)\, dx.$$
The *sine transform* of $f$ is the function on $[0, \infty)$ given by
$$\mathcal{F}_s f(\xi) = \int_0^\infty f(x) \sin(2\pi x \xi)\, dx.$$

## Remarks

Both integrals converge absolutely because $\abs{\cos}$ and $\abs{\sin}$ are at most $1$.
Example: for $f(x) = e^{-x}$, two integrations by parts give $\mathcal{F}_c f(\xi) = \frac{1}{1 + a^2}$ and $\mathcal{F}_s f(\xi) = \frac{a}{1 + a^2}$ with $a = 2\pi \xi$.
Non-example: the constant function $f = 1$ is not integrable on $[0, \infty)$, and $\int_0^\infty \cos(2\pi x \xi)\, dx$ diverges for every $\xi$.

Let $f_e$ and $f_o$ be the even and the odd extensions of $f$ to $\R$, and let $\hat g$ denote the [[Fourier transform|DPVM34ADZV]] $\int_\R g(x) e^{-2\pi i x \xi}\, dx$.
Then $\hat f_e(\xi) = 2 \mathcal{F}_c f(\xi)$ and $\hat f_o(\xi) = -2i\, \mathcal{F}_s f(\xi)$.
Consequently, if $f$ is continuous and $\mathcal{F}_c f$ is integrable, then $f(x) = 4 \int_0^\infty \mathcal{F}_c f(\xi) \cos(2\pi x \xi)\, d\xi$ for $x \ge 0$.

Other conventions use $\cos(x \xi)$ and $\sin(x \xi)$, often with a factor $\sqrt{2/\pi}$ that makes the transforms their own inverses on $L^2(0, \infty)$.
