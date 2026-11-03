---
tag: ZSWNS5BRS1
kind: statement
role: fact
name: Glen's flow law
msc: [86A40, 76A05]
uses: [P1KWMQG4NZ, KG2XWEMJ30, NM5Q4845Z4, 8DT9MB9V6R, C6RVY7R8S6]
about: [8DT9MB9V6R]
sources:
  - url: https://en.wikipedia.org/wiki/Glen%E2%80%93Nye_flow_law
same_as:
  wikidata: Q124485902
  wikipedia: Glen–Nye flow law
---

## Statement

Let $\sigma_{ij}$ be the [[Cauchy stress tensor|KG2XWEMJ30]] in glacier ice, and let $\tau_{ij} = \sigma_{ij} - \tfrac13 \sigma_{kk} \delta_{ij}$ be its deviatoric part.
Let $\dot\varepsilon_{ij}$ be the [[strain rate tensor|P1KWMQG4NZ]].
Define the effective stress $\tau_e$ by $\tau_e^2 = \tfrac12 \tau_{ij}\tau_{ij}$, summed over $i$ and $j$.
Glen's flow law states that polycrystalline ice deforms according to
$$\dot\varepsilon_{ij} = A\, \tau_e^{\,n-1}\, \tau_{ij}.$$
Here the rate factor $A > 0$ depends on temperature and on properties of the ice.
The exponent $n$ is close to $3$.

## Remarks

It is an empirical constitutive law, fitted to laboratory creep experiments of Glen and put into tensor form by Nye.
With the effective strain rate $\dot\varepsilon_e$ defined by $\dot\varepsilon_e^2 = \tfrac12 \dot\varepsilon_{ij}\dot\varepsilon_{ij}$, the law gives $\dot\varepsilon_e = A \tau_e^n$.
Writing $\tau_{ij} = 2\eta\, \dot\varepsilon_{ij}$ gives the effective [[viscosity|NM5Q4845Z4]] $\eta = 1/(2A\tau_e^{\,n-1})$, which decreases as stress increases, so ice is a shear-thinning [[non-Newtonian fluid|8DT9MB9V6R]] of [[power-law|C6RVY7R8S6]] type; $n = 1$ would give a Newtonian fluid.
Example: in a slab of ice of thickness $H$ on a plane of slope $\alpha$, the shear stress at height $z$ above the bed is $\tau_{xz} = \rho g (H - z)\sin\alpha$.
Integrating $du/dz = 2A\tau_{xz}^n$ shows that the surface speed exceeds the basal speed by $\frac{2A}{n+1}(\rho g \sin\alpha)^n H^{n+1}$.
So the surface speed grows like $H^4$ for $n = 3$, which explains why thick glaciers flow much faster than thin ones.

## Explanations

### L1 human

Ice looks solid, but under its own weight it slowly flows like a very thick liquid.
Glen's law says how fast it deforms when pushed: doubling the stress makes it deform about eight times faster, because of the power $3$.
Warm ice deforms faster than cold ice, which is captured by the factor $A$.

### L2 human

Glen's law is the constitutive relation used in almost all models of glaciers and ice sheets, combined with the Stokes equations for slow viscous flow.
Its nonlinearity is what makes ice-flow equations nonlinear, for example in the shallow ice approximation, where ice flux grows like a high power of thickness and surface slope.
The rate factor is usually taken to follow an Arrhenius law in temperature.
