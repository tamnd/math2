---
tag: BJYDT498FX
kind: statement
role: theorem
name: Luttinger's theorem
msc: [82D35, 81V74]
uses: [GK3SVTXXKX, FW27X1KB37, 663MJA8NAC]
about: [GK3SVTXXKX]
sources:
  - url: https://en.wikipedia.org/wiki/Luttinger%27s_theorem
same_as:
  wikidata: Q6705975
  wikipedia: Luttinger's theorem
---

## Statement

Consider a translation-invariant system of interacting spin-$1/2$ fermions in $\R^d$ at zero temperature, with density $n$ and chemical potential $\mu$, and units where $\hbar = 1$.
Let $G(k, \omega)$ be its single-particle Green's function, written as $G(k, \omega) = 1/(\omega + \mu - \varepsilon_k - \Sigma(k, \omega))$ with self-energy $\Sigma$.
Assume that the system is connected to the non-interacting system by perturbation theory in the interaction, as in a [[Fermi liquid|FW27X1KB37]].
Then
$$n = 2 \int_{\set{k \,:\, G(k, 0) > 0}} \frac{d^d k}{(2\pi)^d}.$$
In words, the volume enclosed by the interacting [[Fermi surface|GK3SVTXXKX]] equals the volume of the free Fermi sea at the same density.
Here the interacting Fermi surface is where $G(k, 0)$ changes sign.

## Remarks

Joaquin Luttinger derived it in 1960, using a functional introduced in joint work with John Ward.
The proof writes the density as a frequency integral of $G$, and shows to all orders of perturbation theory that the extra term coming from $\Sigma$ is zero.
The argument is perturbative, so the theorem is not established for systems that are not adiabatically connected to free fermions.

Example: for free fermions in $\R^3$, $\Sigma = 0$ and $G(k, 0) > 0$ exactly when $\varepsilon_k < \mu$, which is the Fermi ball of radius $k_F$, and the formula gives $n = k_F^3 / 3\pi^2$.
For an interacting Fermi liquid the shape of the Fermi surface can change, but the volume it encloses stays fixed by $n$.

## Explanations

### L1 human

Interactions change many things about electrons in a metal: their mass, their lifetime, the shape of the Fermi surface.
Luttinger's theorem says one thing does not change: the volume inside the Fermi surface.
That volume is fixed by counting electrons, just as for free electrons.

### L2 human

The theorem is the reason one can read the electron density off measured Fermi surfaces, for instance from quantum oscillations.
In crystals the integral runs over the Brillouin zone, and it counts electrons modulo filled bands.
Its proof uses the Luttinger–Ward functional of many-body perturbation theory.
Apparent violations in strongly correlated systems are a sign of physics that is not perturbatively connected to a free [[Fermi gas|663MJA8NAC]].
