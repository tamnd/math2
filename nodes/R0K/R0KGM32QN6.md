---
tag: R0KGM32QN6
kind: example
name: Ising model
msc: [82B20, 60K35, 82B26]
instance_of: [059TJN0NZ1]
sources:
  - url: https://en.wikipedia.org/wiki/Ising_model
same_as:
  wikidata: Q1076349
  wikipedia: Ising model
---

## Example

Let $G = (V, E)$ be a finite [[graph|00C0BR7D7H]], and let $J > 0$, $h \in \R$ and $\beta \ge 0$ be real numbers.
A spin configuration is a map $\sigma \colon V \to \set{-1, +1}$.
Its energy is
$$H(\sigma) = -J \sum_{\set{u, v} \in E} \sigma(u) \sigma(v) - h \sum_{v \in V} \sigma(v).$$
The *Ising model* on $G$ at inverse temperature $\beta$ is the [[probability measure|059TJN0NZ1]] on $\set{-1, +1}^V$ given by
$$\mu_\beta(\sigma) = \frac{e^{-\beta H(\sigma)}}{Z_\beta}, \qquad Z_\beta = \sum_{\tau \in \set{-1, +1}^V} e^{-\beta H(\tau)}.$$
Check: each weight $e^{-\beta H(\sigma)}$ is positive and there are finitely many configurations.
So $Z_\beta > 0$, and the values of $\mu_\beta$ are positive and sum to $1$.

## Remarks

With $J > 0$, neighbouring spins prefer to agree, and the measure favours aligned configurations more strongly as $\beta$ grows.
At $\beta = 0$ the spins are independent and uniform.
On the infinite lattice $\Z^d$, limits of these measures as $G$ grows are Gibbs measures.
For $h = 0$ and $d \ge 2$ there is a phase transition: there is more than one Gibbs measure for large $\beta$ and only one for small $\beta$.
For $d = 1$ there is no phase transition.
For $d = 2$ and $h = 0$, Onsager's solution gives the critical value $\beta_c$ by $\sinh(2 \beta_c J) = 1$, that is $\beta_c = \frac{\ln(1 + \sqrt 2)}{2J}$.
Its Glauber dynamics, in which single spins flip at random, is an [[interacting particle system|GR49AM3PSZ]] with $\mu_\beta$ as invariant measure.

## Explanations

### L1 human

Picture a magnet as a grid of tiny arrows, each pointing up or down.
Neighbouring arrows like to point the same way, and heat shakes them at random.
At high temperature the arrows are disordered; at low temperature, in two or more dimensions, most of them line up and the material is magnetised.
For two spins joined by one edge with $h = 0$, the aligned configurations each get weight $e^{\beta J}$ and the opposite ones $e^{-\beta J}$.
