---
tag: 6JGAG0KN98
kind: definition
name: Plancherel measure
msc: ["43A30", "22D10"]
defines: QESEAKKABM
uses: [AHV05ZBCYW, CXG6JZGMCK, VY0HXD3GC4, 95Q8WZMN0W, BWPNB8CF6V, N8E0GVVWG1, W3BX66Y47G]
sources:
  - url: https://en.wikipedia.org/wiki/Plancherel_measure
---

## Definition

Let $G$ be a second countable [[unimodular|CXG6JZGMCK]] [[locally compact group|AHV05ZBCYW]] of [[type I|BWPNB8CF6V]], with a fixed [[Haar measure|VY0HXD3GC4]] $dg$.
Let $\widehat{G}$ be its [[unitary dual|95Q8WZMN0W]] with its Borel structure, and let $\hat f(\pi)$ be the [[Fourier transform|N8E0GVVWG1]] of $f$ at $\pi \in \widehat{G}$.
A *Plancherel measure* for $G$ is a positive Borel measure $\mu$ on $\widehat{G}$ with the following property.
For every $f \in L^1(G) \cap L^2(G)$, the operator $\hat f(\pi)$ is [[Hilbert–Schmidt|W3BX66Y47G]] for $\mu$-almost every $\pi$, and
$$\int_G \abs{f(g)}^2 \, dg = \int_{\widehat{G}} \norm{\hat f(\pi)}_{\mathrm{HS}}^2 \, d\mu(\pi).$$

## Remarks

The [[Plancherel theorem for groups|DH3PYQJXH0]] says that a Plancherel measure exists and is unique.
It depends on the choice of $dg$: replacing $dg$ by $c \, dg$ with $c > 0$ replaces $\mu$ by $c^{-1} \mu$.

Example: let $G = \R$ with Lebesgue measure, and identify $\widehat{G}$ with $\R$ through $\xi \mapsto (x \mapsto e^{2\pi i \xi x})$.
Then $\hat f(\xi) = \int_\R f(x) e^{-2\pi i \xi x} \, dx$, and the classical Plancherel identity $\int \abs{f}^2 \, dx = \int \abs{\hat f}^2 \, d\xi$ shows that Lebesgue measure on $\R$ is the Plancherel measure.

Example: let $G$ be a compact group with Haar measure of total mass $1$.
Then $\widehat{G}$ is discrete and the Plancherel measure is $\mu(\set{\pi}) = d_\pi$, the dimension of $\pi$; this is the [[Plancherel theorem for compact groups|56TSJ9Q92R]].

Non-example: for $G = \R$, counting measure on $\widehat{G} = \R$ is not a Plancherel measure.
For $f \in L^1 \cap L^2$ the function $\hat f$ is continuous, and the sum $\sum_{\xi \in \R} \abs{\hat f(\xi)}^2$ is infinite as soon as $\hat f$ is nonzero, since $\hat f$ is then nonzero on an interval.
