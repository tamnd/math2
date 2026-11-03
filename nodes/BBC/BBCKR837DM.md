---
tag: BBCKR837DM
kind: statement
role: theorem
name: Einstein relation for diffusion
msc: [82C31, 82C70, 60J60]
uses: [ZW2RBS9VTR, FVQWR7NS00, GYNMZ9201M]
about: [ZW2RBS9VTR]
sources:
  - url: https://en.wikipedia.org/wiki/Einstein_relation_(kinetic_theory)
same_as:
  wikidata: Q900855
  wikipedia: Einstein relation (kinetic theory)
---

## Statement

Let $D > 0$ be a diffusion coefficient, let $\mu > 0$ be a mobility, and let $k_B T > 0$ be the thermal energy.
For a smooth potential $V \colon \R \to \R$, consider the overdamped [[Langevin equation|ZW2RBS9VTR]]
$$dX_t = -\mu V'(X_t)\, dt + \sqrt{2D}\, dW_t,$$
where $W$ is a standard Wiener process.
Assume that $e^{-\mu V / D}$ and $e^{-V/(k_B T)}$ are integrable on $\R$.
Then the stationary density of $X$ is proportional to $e^{-\mu V(x)/D}$.
It equals the [[Boltzmann density|GYNMZ9201M]] proportional to $e^{-V(x)/(k_B T)}$ for every such $V$ if and only if
$$D = \mu k_B T.$$

## Remarks

The [[Fokker–Planck equation|FVQWR7NS00]] of the process is $\partial_t p = \partial_x\big(\mu V' p + D\, \partial_x p\big)$.
A stationary density with zero probability current solves $\mu V' p + D p' = 0$, so $p \propto e^{-\mu V/D}$.
Comparing the exponent with $-V/(k_B T)$ for a non-constant $V$ forces $\mu/D = 1/(k_B T)$.
For a sphere of radius $r$ in a fluid of viscosity $\eta$, Stokes drag gives $\mu = 1/(6\pi\eta r)$, and the relation becomes the Stokes–Einstein formula $D = k_B T/(6\pi\eta r)$.
For a charged particle of charge $q$, the electrical mobility $q\mu$ gives the form $D = \mu_q k_B T / q$ with $\mu_q = q\mu$.

## Explanations

### L1 human

A small particle in a fluid is kicked around at random, and it also drifts when a force pulls it.
The relation says that the strength of the random spreading and the ease of drifting are not independent.
Their ratio is fixed by the temperature alone.
So by measuring how fast a particle spreads, one can tell how easily it moves under a force, and the other way round.

### L2 human

The relation is the simplest instance of the fluctuation–dissipation principle: the friction that damps motion and the noise that drives it come from the same collisions.
In the Langevin model it is exactly the condition under which the equilibrium state is the Boltzmann distribution.
Einstein used it in 1905 to connect Brownian motion with the size of molecules, and Perrin's measurements of $D$ then gave a value of Avogadro's number.
The Green–Kubo formula generalises the diffusion coefficient side, and linear response theory generalises the mobility side.
