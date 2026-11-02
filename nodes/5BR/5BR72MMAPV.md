---
tag: 5BR72MMAPV
kind: statement
role: theorem
name: Parseval formula for the Mellin transform
msc: [44A15, 42A38]
uses: [N5PVGRJE1T, SGZZ4Y0D36, X7GTF3D98F]
about: [N5PVGRJE1T]
sources:
  - url: https://en.wikipedia.org/wiki/Mellin_transform
---

## Statement

Let $\sigma \in \R$ and let $f, g \colon (0, \infty) \to \C$ be measurable.
Write $\mathcal{M}$ for the [[Mellin transform|N5PVGRJE1T]].

1. Assume that $x^{\sigma - 1} f(x)$ is [[integrable|X7GTF3D98F]] on $(0, \infty)$ and that $\int_0^\infty x^{2\sigma - 1} \abs{f(x)}^2 \, dx < \infty$. Then
$$\int_0^\infty x^{2\sigma - 1} \abs{f(x)}^2 \, dx = \frac{1}{2\pi} \int_{-\infty}^{\infty} \abs{\mathcal{M}f(\sigma + i\tau)}^2 \, d\tau.$$
2. Assume moreover that $x^{-\sigma} g(x)$ is integrable on $(0, \infty)$ and that $\int_0^\infty x^{1 - 2\sigma} \abs{g(x)}^2 \, dx < \infty$. Then
$$\int_0^\infty f(x) g(x) \, dx = \frac{1}{2\pi} \int_{-\infty}^{\infty} \mathcal{M}f(\sigma + i\tau) \, \mathcal{M}g(1 - \sigma - i\tau) \, d\tau.$$

## Remarks

The integrability hypotheses say that $f$ is [[Mellin convergent|SGZZ4Y0D36]] at $\sigma$ and $g$ at $1 - \sigma$, so the transforms on the right are defined pointwise.
Put $h_f(u) = e^{\sigma u} f(e^{u})$ and $h_g(u) = e^{(1 - \sigma) u} g(e^{u})$.
The substitution $x = e^{u}$ turns the hypotheses into $h_f, h_g \in L^1(\R) \cap L^2(\R)$ and the left sides into $\int \abs{h_f}^2 \, du$ and $\int h_f h_g \, du$.
It also turns $\mathcal{M}f(\sigma + i\tau)$ and $\mathcal{M}g(1 - \sigma - i\tau)$ into Fourier transforms of $h_f$ and $h_g$ at $\mp \tau / 2\pi$.
The [[Plancherel theorem|HPZHRZ0502]] for the Fourier transform on $\R$ then gives both formulas.
Example: $f(x) = e^{-x}$ and $\sigma = 1/2$ give $\int_0^\infty e^{-2x} \, dx = \frac{1}{2} = \frac{1}{2\pi} \int_{\R} \abs{\Gamma(\tfrac12 + i\tau)}^2 \, d\tau$; since $\abs{\Gamma(\tfrac12 + i\tau)}^2 = \pi / \cosh(\pi \tau)$, the right side is $\frac12 \int_{\R} \frac{d\tau}{\cosh \pi \tau} = \frac12$.
By density, part 1 extends $\mathcal{M}$ to a unitary map, up to the factor $2\pi$, from $L^2((0, \infty), x^{2\sigma - 1} dx)$ onto $L^2(\R)$.

## Explanations

### L1 human

The total energy of a function, measured with the weight $x^{2\sigma - 1}$, equals the total energy of its Mellin transform along the line $\operatorname{Re} s = \sigma$.
The second formula is the same fact for products of two functions.
It is the Mellin version of the Plancherel and Parseval identities for Fourier series and integrals.

### L2 human

The formula is used to evaluate integrals of products: one knows $\mathcal{M}f$ and $\mathcal{M}g$, and computes $\int_0^\infty f g \, dx$ by a single integral on a vertical line, often by residues.
Part 2 can also be read as the convolution rule for the Mellin convolution of $f$ and $x \mapsto g(1/x)/x$, combined with Mellin inversion at the point $x = 1$.
On the critical line $\sigma = 1/2$ the weight disappears, and part 1 says that $f \mapsto \mathcal{M}f(\tfrac12 + i\tau) / \sqrt{2\pi}$ preserves the norm of $L^2(0, \infty)$.
