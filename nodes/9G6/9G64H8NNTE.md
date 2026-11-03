---
tag: 9G64H8NNTE
kind: definition
name: Landau–de Gennes theory
msc: [76A15, 82B26]
defines: 971G1WN0QX
uses: [XJ4NRM74W6, XSA203109Z, 0VR671PHE5, 07PTPSZPME, BYWG3ADRF3]
sources:
  - url: https://en.wikipedia.org/wiki/Landau%E2%80%93de_Gennes_theory
---

## Definition

Let $\Omega \subset \R^3$ be a bounded open set filled with a liquid crystal at temperature $T$.
A *Q-tensor* is a real [[symmetric matrix|0VR671PHE5]] $Q$ of size $3 \times 3$ with [[trace|07PTPSZPME]] $\tr Q = 0$.
The *Landau–de Gennes bulk energy density* is
$$f_B(Q) = \frac{a}{2} \tr(Q^2) - \frac{b}{3} \tr(Q^3) + \frac{c}{4} \big(\tr(Q^2)\big)^2,$$
where $a = a_0 (T - T^*)$ with constants $a_0, b, c > 0$ and a temperature $T^*$.
The *Landau–de Gennes energy* of a field $Q \colon \Omega \to \set{\text{Q-tensors}}$ is
$$\mathcal{F}(Q) = \int_\Omega \Big( f_B(Q) + \frac{L}{2} \abs{\nabla Q}^2 \Big) dx,$$
with an elastic constant $L > 0$ and $\abs{\nabla Q}^2 = \sum_{i,j,k} (\partial_k Q_{ij})^2$.

## Remarks

A Q-tensor is *uniaxial* if two eigenvalues coincide; then $Q = s \big(n \otimes n - \frac13 I\big)$ for a unit vector $n$ and a scalar order parameter $s$.
Example: for uniaxial $Q$ the eigenvalues are $2s/3, -s/3, -s/3$, so $\tr(Q^2) = 2s^2/3$ and $\tr(Q^3) = 2s^3/9$, and
$$f_B = \frac{a}{3} s^2 - \frac{2b}{27} s^3 + \frac{c}{9} s^4.$$
The isotropic state $s = 0$ and a nematic state $s > 0$ have equal energy when the bracket in $f_B = s^2 \big(\frac{a}{3} - \frac{2b}{27} s + \frac{c}{9} s^2\big)$ has a double root, that is, at $a = b^2/(27c)$, with $s = b/(3c)$.
So $s$ jumps from $0$ to $b/(3c)$: the isotropic–nematic transition is first order, at a temperature above $T^*$.
Non-example: the matrix $\mathrm{diag}(1, 0, 0)$ is symmetric but has trace $1$, so it is not a Q-tensor.
For uniaxial $Q$ with constant $s$, the elastic term reduces to the one-constant [[Oseen–Frank energy|BYWG3ADRF3]] with $K = 2 L s^2$.

## Explanations

### L1 human

The bulk term decides the phase, and the gradient term penalizes changes of $Q$ in space.
The minus sign of the cubic term favours alignment with $s > 0$, which is what makes the transition jump.
