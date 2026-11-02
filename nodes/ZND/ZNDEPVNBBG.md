---
tag: ZNDEPVNBBG
kind: example
name: Hilbert transform of sinusoids
msc: [44A15, 42A50]
illustrates: [NSCEBXM7ZM]
uses: [NSCEBXM7ZM, 0SYR10HD4R]
sources:
  - url: https://en.wikipedia.org/wiki/Hilbert_transform
---

## Example

Let $\omega > 0$, and define the [[Hilbert transform|NSCEBXM7ZM]] of a bounded continuous function $f$ by the [[principal value|0SYR10HD4R]] at $0$ and at $\infty$
$$Hf(x) = \frac{1}{\pi} \lim_{\varepsilon \to 0^+,\, R \to \infty} \int_{\varepsilon < \abs{u} < R} \frac{f(x - u)}{u}\, du.$$
Then
$$H[\cos(\omega \cdot)](x) = \sin(\omega x), \qquad H[\sin(\omega \cdot)](x) = -\cos(\omega x).$$
Check for the cosine: $\cos(\omega(x - u)) = \cos(\omega x) \cos(\omega u) + \sin(\omega x) \sin(\omega u)$.
On the symmetric set $\varepsilon < \abs{u} < R$, the odd function $\cos(\omega u)/u$ integrates to $0$.
The even function $\sin(\omega u)/u$ integrates to $2 \int_{\varepsilon}^{R} \frac{\sin(\omega u)}{u}\, du$, which tends to $2 \cdot \frac{\pi}{2} = \pi$.
So $H[\cos(\omega \cdot)](x) = \frac{1}{\pi} \cdot \pi \sin(\omega x) = \sin(\omega x)$.
The same computation with $\sin(\omega(x - u)) = \sin(\omega x)\cos(\omega u) - \cos(\omega x)\sin(\omega u)$ gives $-\cos(\omega x)$.
For $\omega < 0$ the signs change, since $\int_0^\infty \frac{\sin(\omega u)}{u}\, du = -\frac{\pi}{2}$.

## Remarks

The result agrees with the Fourier multiplier $-i \sgn(\omega)$ of the Hilbert transform: $H[e^{i\omega x}] = -i \sgn(\omega)\, e^{i\omega x}$.
Applying $H$ twice gives $H^2 \cos = -\cos$, an instance of $H^2 = -\id$.
The function $\cos(\omega x) + i \sin(\omega x) = e^{i\omega x}$ is the analytic signal of $\cos(\omega x)$.

## Explanations

### L1 human

The Hilbert transform shifts every wave by a quarter of a period.
A cosine becomes a sine, and a sine becomes minus a cosine.
This is the property that makes it useful in signal processing, where it turns a real oscillation into its complex partner.
