---
tag: B1021FRSPZ
kind: statement
role: theorem
name: Schwinger–Dyson equation
msc: [81T70, 81S40]
uses: [1NYTFT5NPE, HVGDXMPB29]
about: [1NYTFT5NPE]
sources:
  - url: https://en.wikipedia.org/wiki/Schwinger%E2%80%93Dyson_equation
same_as:
  wikidata: Q1269302
  wikipedia: Schwinger–Dyson equation
---

## Statement

Let $S \colon \R^N \to \R$ be a smooth function with $Z = \int_{\R^N} e^{-S(\phi)} \, d\phi$ finite and nonzero.
For a function $F$ on $\R^N$, write $\langle F \rangle = Z^{-1} \int_{\R^N} F(\phi) \, e^{-S(\phi)} \, d\phi$.
Let $F$ be smooth, and fix $i \in \set{1, \dots, N}$.
Assume that $F e^{-S}$, $(\partial_i F) e^{-S}$ and $F (\partial_i S) e^{-S}$ are integrable on $\R^N$.
Then
$$\left\langle \frac{\partial F}{\partial \phi_i} \right\rangle = \left\langle F \, \frac{\partial S}{\partial \phi_i} \right\rangle.$$

## Remarks

The proof is integration by parts in the variable $\phi_i$.
On almost every line parallel to the $i$-th axis, the function $g = F e^{-S}$ and its derivative $g' = (\partial_i F - F\,\partial_i S)e^{-S}$ are integrable.
So $g$ has limits at $\pm\infty$, these limits are $0$, and $\int g' = 0$.

In field theory, $\phi_i$ are the values of a lattice field, and the formal continuum form reads $\langle \delta F/\delta\phi(x) \rangle = \langle F \, \delta S/\delta\phi(x) \rangle$.
It expresses the invariance of the [[path integral|1NYTFT5NPE]] under a shift of the integration variable.

Example: take the Euclidean [[quartic interaction|HVGDXMPB29]], $S = \int \left(\tfrac12\abs{\nabla\phi}^2 + \tfrac12 m^2\phi^2 + \tfrac{\lambda}{4!}\phi^4\right)dx$, and $F = \phi(y)$.
The equation becomes
$$(-\Delta_x + m^2)\langle \phi(x)\phi(y) \rangle + \frac{\lambda}{3!}\langle \phi(x)^3\phi(y) \rangle = \delta(x - y).$$
For $\lambda = 0$ it says that the two-point function is the Green's function of $-\Delta + m^2$, the [[propagator|K9SR95P4NJ]].

## Explanations

### L1 human

The Schwinger–Dyson equations are the quantum version of the equations of motion.
Classically the field satisfies $\delta S/\delta\phi = 0$.
In the quantum theory this holds only inside averages, up to extra terms that appear when two fields sit at the same point.

### L2 human

The equations form an infinite system that links each correlation function to higher ones.
They hold beyond perturbation theory and are used to derive [[Ward–Takahashi identities|STN15FJ43Z]] when $F$ is replaced by the variation under a symmetry.
Truncating the system gives nonperturbative approximations, for example in studies of the quark propagator.
In random matrix theory, the same integration by parts gives the loop equations.
