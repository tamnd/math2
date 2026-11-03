---
tag: KXJ5AGAFH8
kind: definition
name: Scalar–tensor theory
msc: [83D05]
defines: MWX9XPYEYY
uses: [384JFR3K6X, BY4QYYS788, ZHX2VYQDZ3, JPE3A1SN7V, SANYJGZ311]
sources:
  - url: https://en.wikipedia.org/wiki/Scalar%E2%80%93tensor_theory
---

## Definition

Work in units with $c = 1$, and let $G$ be a constant with the dimension of the gravitational constant.
Let $g$ be a [[Lorentzian metric|BY4QYYS788]] on a four-dimensional manifold, $\phi$ a real scalar field and $\psi$ the matter fields.
A *scalar–tensor theory* (in the Jordan frame) is an [[alternative to general relativity|384JFR3K6X]] with action
$$S = \frac{1}{16 \pi G} \int \left[ F(\phi) R - Z(\phi) \, g^{ab} \partial_a \phi \, \partial_b \phi - 2 U(\phi) \right] \sqrt{-g} \, d^4 x + S_m[g, \psi].$$
Here $R$ is the [[scalar curvature|ZHX2VYQDZ3]] of $g$, and $F > 0$, $Z$ and $U$ are smooth functions.
The matter action $S_m$ depends on $g$ and $\psi$ but not on $\phi$.

## Remarks

Example: $F = 1$, $Z = 0$ and $U = \Lambda$ give the [[Einstein–Hilbert action|JPE3A1SN7V]] with cosmological constant $\Lambda$, together with a scalar field that has no dynamics; so general relativity is a degenerate case.
Example: $F(\phi) = \phi$, $Z(\phi) = \omega/\phi$ with a constant $\omega$, and $U = 0$ give Brans–Dicke theory.
Non-example: a theory in which $\phi$ appears in $S_m$, so that different kinds of matter may feel different metrics, is not of this form.
The condition that matter couples only to $g$ makes the theory a metric theory.
A conformal change $\tilde g = F(\phi) g$ rewrites the gravitational part as the Einstein–Hilbert action of $\tilde g$ plus a scalar field.
This is the *Einstein frame*, in which matter couples to $\phi$.
The most general scalar–tensor theory in four dimensions with second-order field equations is Horndeski's theory, which allows further terms with second derivatives of $\phi$.

## Explanations

### L1 human

A scalar–tensor theory is general relativity with one extra field mixed into the gravitational part of the [[Lagrangian|SANYJGZ311]].
The function $F(\phi)$ in front of $R$ plays the role of $1/G$, so where $\phi$ changes, the effective strength of gravity changes.
