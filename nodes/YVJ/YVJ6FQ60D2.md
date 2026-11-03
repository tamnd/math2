---
tag: YVJ6FQ60D2
kind: example
name: Worm-like chain
msc: [82D60]
illustrates: [GYNMZ9201M]
uses: [GYNMZ9201M, M5WZKH7ZDV]
sources:
  - url: https://en.wikipedia.org/wiki/Worm-like_chain
same_as:
  wikidata: Q503490
  wikipedia: Worm-like chain
---

## Example

The *worm-like chain*, or Kratky–Porod model, describes a semiflexible polymer as a continuous curve $r \colon [0, L] \to \R^3$ parametrized by arc length.
Its unit tangent is $t(s) = r'(s)$, with $\abs{t(s)} = 1$.
The bending energy of a shape is
$$E = \frac{\kappa}{2} \int_0^L \abs{t'(s)}^2 \, ds,$$
where $\kappa > 0$ is the bending stiffness.
At temperature $T$ the shapes are weighted by the [[Boltzmann distribution|GYNMZ9201M]] $e^{-E/(k_B T)}$.
The *persistence length* is $P = \kappa / (k_B T)$.
For this ensemble, tangent correlations decay exponentially, $\langle t(s) \cdot t(s') \rangle = e^{-\abs{s - s'}/P}$.
Check of the mean square end-to-end distance: since $R = r(L) - r(0) = \int_0^L t(s) \, ds$,
$$\langle \abs{R}^2 \rangle = \int_0^L \int_0^L e^{-\abs{s - s'}/P} \, ds \, ds' = 2 P L - 2 P^2 \big(1 - e^{-L/P}\big).$$

## Remarks

For $L \ll P$, expanding the exponential gives $\langle \abs{R}^2 \rangle \approx L^2$: the chain is a stiff rod.
For $L \gg P$, it gives $\langle \abs{R}^2 \rangle \approx 2 P L$: the chain is like an [[ideal chain|M5WZKH7ZDV]] with $N = L / (2P)$ segments of length $b = 2P$, the Kuhn length.
Double-stranded DNA is the standard example, with a persistence length of about $50$ nm under physiological conditions.

## Explanations

### L1 human

A worm-like chain is a smooth bendable rod, like a long piece of cooked spaghetti, that is shaken by heat.
Bending costs energy, so short pieces are almost straight.
Over long distances the small bends add up and the chain forgets its direction.
The persistence length is the distance over which it keeps its direction.
A chain much shorter than it looks like a rod; a chain much longer than it looks like a random walk.
