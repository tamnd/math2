---
tag: 9RVKQJQ5JJ
kind: example
name: Contact process
msc: [60K35, 82C22, 92D30]
instance_of: [GR49AM3PSZ]
sources:
  - url: https://en.wikipedia.org/wiki/Contact_process_(mathematics)
same_as:
  wikidata: Q5164846
  wikipedia: Contact process (mathematics)
---

## Example

Let $d \ge 1$ and $\lambda > 0$.
For $x \in \Z^d$ and $\eta \in \set{0, 1}^{\Z^d}$, let
$$c(x, \eta) = \begin{cases} 1 & \text{if } \eta(x) = 1, \\ \lambda \, \#\set{y \in \Z^d : \abs{y - x} = 1, \ \eta(y) = 1} & \text{if } \eta(x) = 0. \end{cases}$$
The *contact process* on $\Z^d$ with infection rate $\lambda$ is the spin system on $\set{0, 1}^{\Z^d}$ with these flip rates.
Here $\eta(x) = 1$ means that site $x$ is infected.
An infected site recovers at rate $1$, and a healthy site is infected at rate $\lambda$ times its number of infected neighbours.
The rates are bounded by $\max(1, 2d\lambda)$ and each depends on $2d + 1$ sites, so it is an [[interacting particle system|GR49AM3PSZ]].

## Remarks

The configuration with no infected site is absorbing.
There is a critical value $\lambda_c \in (0, \infty)$: started from one infected site, the infection dies out almost surely for $\lambda < \lambda_c$ and survives forever with positive probability for $\lambda > \lambda_c$.
A lower bound is $\lambda_c \ge 1/(2d)$.
Indeed, the number of infected sites is dominated by a branching process in which each individual dies at rate $1$ and gives birth at rate $2d\lambda$.
This branching process dies out almost surely when $2d\lambda \le 1$.

## Explanations

### L1 human

It is a model of an epidemic on a grid.
Sick people heal at a fixed rate and pass the illness to healthy neighbours at rate $\lambda$ each.
If $\lambda$ is small the epidemic dies out; if $\lambda$ is large it may last forever.
