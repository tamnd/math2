---
tag: MRJ2FHX6K1
kind: example
name: Hypernetted-chain equation
msc: [82D15, 82B21, 45G10]
instance_of: [BSCYBP6AS6]
sources:
  - url: https://en.wikipedia.org/wiki/Hypernetted-chain_equation
same_as:
  wikidata: Q5958347
  wikipedia: Hypernetted-chain equation
---

## Example

Consider a classical fluid in $\R^3$ with number density $\rho$, inverse temperature $\beta$ and pair potential $u(r)$.
Let $g$ be the radial distribution function, $h = g - 1$, and $c$ the direct correlation function of the [[Ornstein–Zernike equation|29T4NC87AR]].
The hypernetted-chain closure is
$$g(r) = \exp\big(-\beta u(r) + h(r) - c(r)\big), \quad \text{equivalently} \quad c(r) = h(r) - \ln g(r) - \beta u(r).$$
Together with the Ornstein–Zernike equation
$$h(r_{12}) = c(r_{12}) + \rho \int_{\R^3} c(r_{13}) \, h(r_{23}) \, dx_3,$$
where $r_{ij} = \abs{x_i - x_j}$, it forms a closed [[nonlinear integral equation|BSCYBP6AS6]] for $h$: substitute $c = h - \ln(1 + h) - \beta u$.

Check at low density: as $\rho \to 0$ the Ornstein–Zernike equation gives $c = h$ to leading order.
Then the closure gives $g = e^{-\beta u}$, the exact low-density limit of the radial distribution function.

## Remarks

The closure is usually solved numerically by iteration, with the convolution done by the fast Fourier transform.
The [[Percus–Yevick approximation|K3E536PSRJ]] is usually more accurate for hard spheres, while the hypernetted-chain equation is usually preferred for long-range potentials such as the Coulomb potential.

## Explanations

### L1 human

The equation describes how particles in a liquid arrange around each other.
It combines the exact Ornstein–Zernike relation with an approximate rule that leaves out a certain class of terms, the so-called bridge diagrams, in an expansion of the correlations.
The resulting equation is nonlinear because the rule involves a logarithm.
