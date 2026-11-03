---
tag: X58VGXJ2FJ
kind: statement
role: theorem
name: Lieb–Wu solution of the one-dimensional Hubbard model
msc: [82B23, 82B20, 82D03]
uses: [3B76W03AN7, S92G5M6X41]
about: [3B76W03AN7]
sources:
  - url: https://en.wikipedia.org/wiki/Hubbard_model
---

## Statement

Let $t > 0$ and $U \ge 0$, and let $H_L$ be the [[Hubbard model|3B76W03AN7]] on a ring of $L$ sites,
$$H_L = -t \sum_{j=1}^{L} \sum_{\sigma} \big(c_{j\sigma}^\dagger c_{j+1,\sigma} + c_{j+1,\sigma}^\dagger c_{j\sigma}\big) + U \sum_{j=1}^{L} n_{j\uparrow} n_{j\downarrow}.$$
Let $E_0(L)$ be its ground-state energy at half filling, with $L$ electrons and total magnetization $0$.
Then
$$\lim_{L \to \infty} \frac{E_0(L)}{L} = -4t \int_0^\infty \frac{J_0(\omega) J_1(\omega)}{\omega\big(1 + e^{\omega U/(2t)}\big)}\, d\omega,$$
where $J_0$ and $J_1$ are Bessel functions of the first kind.
Moreover, for every $U > 0$ the half-filled chain has a positive charge gap, so it is an insulator.
In particular there is no metal–insulator transition at a positive value of $U$.

## Remarks

Lieb and Wu (1968) diagonalized the model with the nested [[Bethe ansatz|S92G5M6X41]].
It reduces the ground state to a pair of coupled linear integral equations for the densities of charge and spin rapidities, and the formula above is their solution.
At $U = 0$ the formula gives $-2t\int_0^\infty J_0 J_1 \omega^{-1}\, d\omega = -4t/\pi$, the energy of free fermions at half filling.
For large $U$, expanding $1/(1 + e^{x}) = \sum_{n \ge 1} (-1)^{n+1} e^{-nx}$ and using $J_0(\omega)J_1(\omega) \approx \omega/2$ near $0$ gives $E_0/L \approx -(4t^2/U)\ln 2$, the energy of the Heisenberg chain with $J = 4t^2/U$ measured from $J/4$ per bond.
The charge gap opens exponentially slowly for small $U$ and is close to $U - 4t$ for large $U$.

## Explanations

### L1 human

In one dimension the Hubbard model can be solved exactly.
Lieb and Wu found a closed formula for the lowest energy of a long chain with one electron per site.
They also showed that any repulsion, however weak, turns the half-filled chain into an insulator.
This was an early exact demonstration of a Mott insulator.

### L2 human

The solution is a central example of a Bethe ansatz for particles with internal degrees of freedom, where spin and charge are described by separate sets of rapidities.
The excitations separate into spinons and holons, a form of spin–charge separation typical of one-dimensional systems.
At large $U$ the result matches the antiferromagnetic Heisenberg chain, which links it to Bethe's and Hulthén's solution.
Completeness of the Bethe ansatz states and the full thermodynamics were developed later by others.
