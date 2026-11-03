---
tag: 6KMKXSX99V
kind: statement
role: proposition
name: Michaelis–Menten kinetics
msc: [92C45, 80A30]
uses: [TTH05RV6SW, X7YR27X88B]
about: [TTH05RV6SW]
sources:
  - url: https://en.wikipedia.org/wiki/Michaelis%E2%80%93Menten_kinetics
same_as:
  wikidata: Q613955
  wikipedia: Michaelis–Menten kinetics
---

## Statement

Consider the enzyme reaction $E + S \rightleftharpoons C \to E + P$ with [[mass-action rate equations|TTH05RV6SW]] and rate constants $k_1$ (binding), $k_{-1}$ (unbinding) and $k_2$ (catalysis), all positive.
Let $s$, $c$ and $e$ be the concentrations of substrate, complex and free enzyme, and let $e_0 = e + c$ be the total enzyme concentration, which is constant.
If the complex is at quasi-steady state, $dc/dt = 0$, then
$$c = \frac{e_0\, s}{K_M + s}, \qquad v = \frac{dp}{dt} = \frac{V_{\max}\, s}{K_M + s},$$
where $V_{\max} = k_2 e_0$ is the maximal rate and $K_M = (k_{-1} + k_2)/k_1$ is the *Michaelis constant*.

## Remarks

Mass action gives $dc/dt = k_1 e s - (k_{-1} + k_2) c$, and substituting $e = e_0 - c$ and setting it to zero gives $k_1 (e_0 - c) s = (k_{-1} + k_2) c$, which solves to the formula for $c$; then $v = k_2 c$.
The [[quasi-steady-state approximation|X7YR27X88B]] makes the hypothesis $dc/dt = 0$ precise as a limit when $e_0$ is small compared with $s_0$.
The rate is half of $V_{\max}$ exactly when $s = K_M$, it is about $(V_{\max}/K_M)\, s$ for $s \ll K_M$, and it saturates at $V_{\max}$ for $s \gg K_M$.
The double reciprocal form $1/v = 1/V_{\max} + (K_M / V_{\max})(1/s)$ is the Lineweaver–Burk plot, a straight line in $1/s$.
If instead the binding step is assumed to be at equilibrium (the assumption of Michaelis and Menten in 1913), the same formula holds with $K_M$ replaced by $k_{-1}/k_1$.

## Explanations

### L1 human

An enzyme can handle only one substrate molecule at a time, like a cashier serving one customer.
With few customers the service rate grows in proportion to the number of customers; with very many, the cashier is always busy and the rate levels off.
The Michaelis–Menten formula is the curve that joins these two regimes, with the half-way point at the substrate level $K_M$.

### L2 human

The formula is the standard rate law in enzyme kinetics, and the two numbers $V_{\max}$ and $K_M$ are what experiments report for an enzyme.
The same saturating shape reappears as the Monod law for microbial growth and as the Holling type II functional response in ecology.
With cooperative binding at several sites it is replaced by the Hill equation.
