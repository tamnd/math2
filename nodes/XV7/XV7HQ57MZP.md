---
tag: XV7HQ57MZP
kind: example
name: Wess–Zumino model
msc: [81T60, 81T10]
illustrates: [S847N922FY]
uses: [VZ9ZJNWN73, W3GY719S7X]
sources:
  - url: https://en.wikipedia.org/wiki/Wess–Zumino_model
same_as:
  wikidata: Q3859871
  wikipedia: Wess–Zumino model
---

## Example

The *Wess–Zumino model* is the simplest four-dimensional field theory with $N = 1$ [[supersymmetry|VZ9ZJNWN73]].
Work on Minkowski space $\R^{1,3}$ with signature $(+,-,-,-)$.
The fields form a chiral multiplet: a complex scalar field $\phi$ and a left-handed [[Weyl spinor field|W3GY719S7X]] $\psi_\alpha$ with anticommuting components.
Choose a polynomial $W$, the superpotential, usually $W(\phi) = \frac{m}{2}\phi^2 + \frac{g}{3}\phi^3$ with $m > 0$ and $g \in \C$.
After eliminating an auxiliary field, the Lagrangian density in two-component notation is
$$\mathcal{L} = \partial_\mu\bar\phi \, \partial^\mu\phi + i \bar\psi \bar\sigma^\mu \partial_\mu \psi - \abs{W'(\phi)}^2 - \frac{1}{2}\left( W''(\phi) \, \psi\psi + \overline{W''(\phi)} \, \bar\psi\bar\psi \right).$$

Check of the equal masses predicted by supersymmetry, at $\phi = 0$: the potential is $\abs{W'(\phi)}^2 = \abs{m\phi + g\phi^2}^2$, whose quadratic part $m^2\abs{\phi}^2$ gives the scalar the mass $m$.
The fermion term is $-\frac{1}{2}(m\psi\psi + m\bar\psi\bar\psi)$ at quadratic order, a Majorana mass term of mass $m$.
So the two bosonic and the two fermionic degrees of freedom all have mass $m$.
The potential $\abs{W'}^2$ is non-negative, as supersymmetry requires.
It vanishes exactly at the critical points of $W$, here $\phi = 0$ and $\phi = -m/g$ when $g \ne 0$, which are the supersymmetric vacua.

## Remarks

Julius Wess and Bruno Zumino introduced the model in 1974.
Supersymmetry acts by $\delta\phi = \sqrt2 \, \epsilon\psi$ and a corresponding rule for $\psi$, with a constant anticommuting spinor $\epsilon$, up to conventions.
The model is renormalizable, and the superpotential is not renormalized in perturbation theory, an early example of non-renormalization theorems.

## Explanations

### L1 human

The Wess–Zumino model is a small theory with one boson and one fermion, tied together by supersymmetry.
All of their interactions come from a single polynomial, the superpotential.
Because of the symmetry, the boson and the fermion have exactly the same mass, and quantum corrections that would normally spoil the theory cancel between them.
It is the standard first example in every course on supersymmetry.
