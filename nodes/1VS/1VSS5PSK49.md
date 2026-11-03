---
tag: 1VSS5PSK49
kind: definition
name: Impulse response
msc: [93C05, 94A12]
defines: 3X3SYVM7R5
uses: [6J9MPVHSMF, 2Z29JN3VES, 0KPHENZ5S7, 020M04FN1H]
sources:
  - url: https://en.wikipedia.org/wiki/Impulse_response
---

## Definition

Discrete time: let $\delta$ be the unit impulse, given by $\delta[0] = 1$ and $\delta[n] = 0$ for $n \ne 0$.
Let $H$ be a [[linear time-invariant system|6J9MPVHSMF]] on sequences $\Z \to \C$ whose domain contains $\delta$.
The *impulse response* of $H$ is the sequence $h = H\delta$.

Continuous time: let $H$ be a linear time-invariant system on functions $\R \to \C$.
A locally integrable function $h \colon \R \to \C$ is the *impulse response* of $H$ if
$$(Hu)(t) = \int_{-\infty}^{\infty} h(t - s) \, u(s) \, ds$$
for every continuous input $u$ with compact support and every $t \in \R$.

## Remarks

In discrete time, $Hu = h * u$ for every finitely supported input $u$, by linearity and time invariance.
In continuous time, $h$ is formally the output for the input [[Dirac delta|0KPHENZ5S7]] $\delta$, since $h * \delta = h$; this can be made precise with distributions.
Example: take $x' = Ax + bu$, $y = cx$ with a real $n \times n$ matrix $A$, a column $b$, a row $c$ and zero state in the far past.
The variation of constants formula gives $h(t) = c \, e^{At} b$ for $t \ge 0$ and $h(t) = 0$ for $t < 0$, with the [[matrix exponential|020M04FN1H]] $e^{At}$.
Non-example: the system $(Hu)(t) = t \, u(t)$ has no impulse response, since it is not time-invariant.
Its response to an impulse at time $s$ is not a shift of its response to an impulse at time $0$.
Some systems, such as the identity $Hu = u$, have no impulse response that is a function; their impulse response is the distribution $\delta$.
