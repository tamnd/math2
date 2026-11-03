---
tag: JCE30PVPWM
kind: definition
name: Rate equation
msc: [80A30, "92E20"]
defines: TTH05RV6SW
uses: [0NT64JV96A]
sources:
  - url: https://en.wikipedia.org/wiki/Rate_equation
---

## Definition

Consider a reaction $a\,A + b\,B \to p\,P + q\,Q$ in a well-mixed volume, with stoichiometric coefficients $a, b, p, q > 0$.
Write $[X](t)$ for the concentration of the species $X$ at time $t$.
The *rate* of the reaction is
$$r = -\frac{1}{a} \frac{d[A]}{dt} = -\frac{1}{b} \frac{d[B]}{dt} = \frac{1}{p} \frac{d[P]}{dt} = \frac{1}{q} \frac{d[Q]}{dt}.$$
A *rate equation* for the reaction is a relation
$$r = k\,[A]^m [B]^n.$$
Here the *rate constant* $k > 0$ depends on the temperature but not on the concentrations.
The real numbers $m, n$ are the *partial orders* in $A$ and $B$.
The sum $m + n$ is the *overall order* of the reaction.

## Remarks

Example: for the step $2\,\mathrm{NO_2} \to 2\,\mathrm{NO} + \mathrm{O_2}$ with rate $r = k[\mathrm{NO_2}]^2$, the order is $2$.
Then $d[\mathrm{NO_2}]/dt = -2k[\mathrm{NO_2}]^2$, whose solution is $1/[\mathrm{NO_2}](t) = 1/[\mathrm{NO_2}](0) + 2kt$, as one checks by differentiation.
For an elementary reaction, the orders equal the stoichiometric coefficients of the reactants; this is mass-action kinetics.
For a composite reaction, the orders need not equal the coefficients and may be fractional.
Non-example: the enzyme rate $r = V[S]/(K + [S])$ of Michaelis–Menten kinetics, with constants $V, K > 0$, is not of power-law form.
Indeed it behaves like $[S]$ for small $[S]$ and tends to the constant $V$ for large $[S]$, while $k[S]^m$ has one exponent $m$ at all scales.
The integrated forms of the rate equations of order $0$, $1$ and $2$ are standard tools to find the order from data.
