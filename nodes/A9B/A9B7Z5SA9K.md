---
tag: A9B7Z5SA9K
kind: example
name: Rectangular function
msc: ["42A38", "94A12"]
illustrates: [DPVM34ADZV]
uses: [DPVM34ADZV, QY8ETVDA1Z, P3T104G564]
sources:
  - url: https://en.wikipedia.org/wiki/Rectangular_function
same_as:
  wikidata: Q946860
  wikipedia: Rectangular function
---

## Example

The *rectangular function* is $\operatorname{rect} \colon \R \to \R$ with $\operatorname{rect}(x) = 1$ for $\abs{x} < \frac12$, $\operatorname{rect}(x) = \frac12$ for $\abs{x} = \frac12$, and $\operatorname{rect}(x) = 0$ for $\abs{x} > \frac12$.
It is integrable, so its [[Fourier transform|DPVM34ADZV]] is defined by the integral.
For $\xi \ne 0$,
$$\widehat{\operatorname{rect}}(\xi) = \int_{-1/2}^{1/2} e^{-2\pi i x \xi}\, dx = \frac{e^{\pi i \xi} - e^{-\pi i \xi}}{2\pi i \xi} = \frac{\sin(\pi \xi)}{\pi \xi},$$
and $\widehat{\operatorname{rect}}(0) = 1$.
This function is the normalized sinc function, $\operatorname{sinc}(\xi) = \sin(\pi\xi)/(\pi\xi)$.

## Remarks

The transform is continuous and tends to $0$ at infinity, as for every integrable function.
It decays only like $1/\abs{\xi}$ and is not integrable, which reflects the jumps of $\operatorname{rect}$.
So the inversion formula does not hold as an absolutely convergent integral.
It holds in $L^2(\R)$.
As a symmetric improper integral it gives $\frac12$ at $x = \pm\frac12$, the average of the two one-sided limits, which is why the value $\frac12$ is used there.

By the [[convolution theorem|QY8ETVDA1Z]], the triangle function $\operatorname{rect} * \operatorname{rect}(x) = \max(1 - \abs{x}, 0)$ has transform $\operatorname{sinc}^2$, which is integrable.
Read in the other direction, $\operatorname{sinc}$ is a [[band-limited function|P3T104G564]] whose transform is $\operatorname{rect}$.

## Explanations

### L1 human

The rectangular function is a box: it switches on at $-\frac12$ and off at $\frac12$.
Its frequency content is the sinc wave $\sin(\pi\xi)/(\pi\xi)$, a central peak with slowly shrinking ripples.
Sharp edges in time need many high frequencies, which is why the ripples die out so slowly.
