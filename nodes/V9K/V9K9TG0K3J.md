---
tag: V9K9TG0K3J
kind: statement
role: theorem
name: Plancherel theorem for abelian groups
msc: [43A25, 22B05]
uses: [ZR09S9R3AW, VY0HXD3GC4, FMW57WNPDB, VHN5VW5Q92, HM2HHE3J51]
about: [VHN5VW5Q92]
sources:
  - url: https://en.wikipedia.org/wiki/Plancherel_theorem
---

## Statement

Let $G$ be a [[locally compact abelian group|ZR09S9R3AW]] with a [[Haar measure|VY0HXD3GC4]] $\mu$, and let $\widehat{G}$ be its [[Pontryagin dual|FMW57WNPDB]].
For $f \in L^1(G)$ let $\widehat{f}$ be its [[Fourier transform|VHN5VW5Q92]].
Then there is a unique Haar measure $\nu$ on $\widehat{G}$ such that:

1. for every $f \in L^1(G) \cap L^2(G)$, the function $\widehat{f}$ lies in $L^2(\widehat{G}, \nu)$ and $\norm{\widehat{f}}_{L^2(\nu)} = \norm{f}_{L^2(\mu)}$;
2. the map $f \mapsto \widehat{f}$ on $L^1(G) \cap L^2(G)$ extends uniquely to a unitary isomorphism of [[Hilbert spaces|HM2HHE3J51]] $L^2(G, \mu) \to L^2(\widehat{G}, \nu)$.

## Remarks

The measure $\nu$ is called the dual measure of $\mu$; scaling $\mu$ by $c > 0$ scales $\nu$ by $1/c$.
One proof applies [[Bochner's theorem|ZRHAG4NXHC]] to functions $f * \tilde{f}$, where $\tilde{f}(x) = \overline{f(-x)}$, whose transform is $\abs{\widehat{f}}^2$.
This yields a Haar measure on $\widehat{G}$ for which the inversion formula holds for such functions.
Evaluating $f * \tilde{f}$ at $0$ then gives the isometry, and density of $L^1 \cap L^2$ in $L^2$ gives the extension.
Example: for $G = \mathbb{T}$ with normalised arc length, $\widehat{G} = \Z$, $\nu$ is counting measure, and the theorem is Parseval's identity $\frac{1}{2\pi}\int_0^{2\pi} \abs{f(\theta)}^2 \, d\theta = \sum_{n \in \Z} \abs{\widehat{f}(n)}^2$.
For $G = \R$ with Lebesgue measure and characters $x \mapsto e^{2\pi i \xi x}$, the dual measure is again Lebesgue measure.
The general [[Plancherel theorem for groups|DH3PYQJXH0]] extends the result to some non-abelian groups, where the dual is the unitary dual and $\nu$ becomes the Plancherel measure.

## Explanations

### L1 human

The energy of a function, the integral of its squared size, is the same as the total energy of its Fourier transform.
No energy is lost or created when a function is split into waves.
On the circle this is the familiar fact that the mean square of a periodic function is the sum of the squares of its Fourier coefficients.

### L2 human

The theorem makes the Fourier transform a unitary operator on $L^2$, so one can transform any square-integrable function, not only integrable ones.
It fixes a normalisation of the Haar measure on the dual group, which is the one used in the Fourier inversion formula.
Together with [[Pontryagin duality|QTVC6F2P9D]] it shows that $L^2(G)$ is diagonalised by the characters: translation operators become multiplication operators on $L^2(\widehat{G})$.
