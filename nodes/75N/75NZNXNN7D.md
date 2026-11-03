---
tag: 75NZNXNN7D
kind: statement
role: theorem
name: Fluctuation theorem
msc: [82C05, 82C35]
uses: [STR73R5MX4, 0DVDCMA2DK, 0WQNRCNY3M]
about: [STR73R5MX4]
sources:
  - url: https://en.wikipedia.org/wiki/Fluctuation_theorem
same_as:
  wikidata: Q900831
  wikipedia: Fluctuation theorem
---

## Statement

Let a classical system have phase space $\R^{2N}$ and a deterministic flow $\Gamma \mapsto \Gamma(t)$ with phase space compression factor $\Lambda(\Gamma) = \nabla_\Gamma \cdot \dot\Gamma$.
Assume the dynamics is time-reversible: there is an involution $M$ of phase space with $M(\Gamma(t)) = (M\Gamma)(-t)$.
Let the initial [[probability density|0DVDCMA2DK]] $f$ be positive everywhere and even under time reversal, $f(M\Gamma) = f(\Gamma)$.
For $t > 0$ define the dissipation function
$$\Omega_t(\Gamma) = \ln \frac{f(\Gamma)}{f(\Gamma(t))} - \int_0^t \Lambda(\Gamma(s))\, ds.$$
Let $p_t$ be the probability density of the random variable $\Omega_t$ when $\Gamma$ has density $f$.
Then, for every real $A$,
$$\frac{p_t(A)}{p_t(-A)} = e^{A}.$$

## Remarks

The proof pairs each trajectory segment with its time reverse $M\Gamma(t)$, which has dissipation $-\Omega_t$.
The ratio of the probabilities of the two segments is $e^{\Omega_t}$, by the change of variables formula along the flow, whose Jacobian is $\exp \int_0^t \Lambda\, ds$.
This form is the transient fluctuation theorem of Evans and Searles; the steady-state form of Gallavotti and Cohen holds as $t \to \infty$ under extra chaoticity hypotheses.
It implies the integral form $\mathbb{E}[e^{-\Omega_t}] = 1$ and, by Jensen's inequality, the second-law inequality $\mathbb{E}[\Omega_t] \ge 0$, where $\mathbb{E}$ is the [[expected value|0WQNRCNY3M]].
Example: let a system start in the canonical distribution at temperature $T$ and then be driven by a field.
Then $\Omega_t$ is the dissipative work done by the field divided by $k_B T$, and negative values have exponentially small probability.

## Explanations

### L1 human

The second law says that entropy grows on average, but in a very small system it can briefly shrink.
The fluctuation theorem says exactly how rare this is: a decrease by $A$ is $e^{A}$ times less likely than an increase by $A$.
For large systems or long times, $A$ is large, and decreases are practically never seen.

### L2 human

The theorem gives the second law as a statement about probabilities, valid far from equilibrium and for small systems.
It has been tested in experiments with colloidal particles in optical traps.
The [[entropy production|STR73R5MX4]] measured in units of $k_B$ plays the role of $\Omega_t$ in many models.
The Jarzynski equality and the Crooks fluctuation theorem are relatives for the work done on a system driven between two equilibrium states.
