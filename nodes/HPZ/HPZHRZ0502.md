---
tag: HPZHRZ0502
kind: statement
role: theorem
name: Plancherel theorem
msc: [42B10, 42A38]
uses: [DPVM34ADZV, SASP14MA1Z, MM0EJ2GDE4, HM2HHE3J51]
about: [DPVM34ADZV]
sources:
  - url: https://en.wikipedia.org/wiki/Plancherel_theorem
same_as:
  wikidata: Q2096184
  wikipedia: Plancherel theorem
---

## Statement

Let $n \ge 1$, and let $L^p(\R^n)$ denote the [[Lebesgue spaces|SASP14MA1Z]] with respect to Lebesgue measure.
For $f \in L^1(\R^n)$ let $\hat f(\xi) = \int_{\R^n} f(x) e^{-2\pi i x \cdot \xi} \, dx$ be its [[Fourier transform|DPVM34ADZV]].

1. If $f \in L^1(\R^n) \cap L^2(\R^n)$, then $\hat f \in L^2(\R^n)$ and
$$\int_{\R^n} \abs{\hat f(\xi)}^2 \, d\xi = \int_{\R^n} \abs{f(x)}^2 \, dx.$$
2. The map $f \mapsto \hat f$ on $L^1(\R^n) \cap L^2(\R^n)$ extends uniquely to a [[unitary operator|MM0EJ2GDE4]] $\mathcal F$ of the [[Hilbert space|HM2HHE3J51]] $L^2(\R^n)$ onto itself.

## Remarks

Proof idea: for Schwartz functions the identity follows from the multiplication formula $\int \hat f \, \overline{\hat g} = \int f \, \overline{g}$ and Fourier inversion.
Schwartz functions are dense in $L^1 \cap L^2$ for the norm $\norm{f}_1 + \norm{f}_2$, which gives part 1.
Since $L^1 \cap L^2$ is dense in $L^2$, the isometry extends uniquely to $L^2$.
The extension is onto because its range is closed and contains the Schwartz space.

For $f \in L^2$ the transform is computed as the $L^2$ limit $\mathcal F f = \lim_{R \to \infty} \int_{\abs{x} \le R} f(x) e^{-2\pi i x \cdot \xi} \, dx$, because the integral itself may diverge.
The inner product is also preserved: $\int \mathcal F f \, \overline{\mathcal F g} = \int f \, \overline{g}$ for $f, g \in L^2(\R^n)$.

Example: for $f = \mathbf{1}_{[-1/2, 1/2]}$ on $\R$, $\hat f(\xi) = \frac{\sin \pi \xi}{\pi \xi}$ and $\int \abs{f}^2 = 1$.
So the theorem gives $\int_\R \left( \frac{\sin \pi \xi}{\pi \xi} \right)^2 d\xi = 1$.

The analogue for Fourier series is [[Parseval's identity|047RFCNVSK]].
The theorem generalizes to [[locally compact abelian groups|V9K9TG0K3J]] and, with representations in place of characters, to [[more general groups|DH3PYQJXH0]].

## Explanations

### L1 human

The energy of a signal, the integral of its squared size, is the same whether one computes it from the signal or from its frequency content.
So the Fourier transform preserves lengths and angles, like a rotation in infinite dimensions.
This lets one define the Fourier transform of every square-integrable function, even when the defining integral does not converge.

### L2 human

Plancherel's theorem makes $L^2$ the natural home of the Fourier transform.
It is the starting point of the $L^p$ theory, through interpolation with the trivial bound from $L^1$ to $L^\infty$.
In quantum mechanics it says that the position and momentum representations of a wave function carry the same total probability.
It also underlies the definition of Sobolev spaces $H^s$ by weights on the Fourier side.
