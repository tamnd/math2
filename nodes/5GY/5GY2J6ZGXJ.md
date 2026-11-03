---
tag: 5GY2J6ZGXJ
kind: example
name: Potts model
msc: [82B20, 60K35, 82B26]
instance_of: [PAEME5EQRM]
uses: [PAEME5EQRM, R0KGM32QN6, 00C0BR7D7H]
sources:
  - url: https://en.wikipedia.org/wiki/Potts_model
same_as:
  wikidata: Q7235385
  wikipedia: Potts model
---

## Example

Let $q \ge 2$ be an integer, let $G = (V, E)$ be a finite [[graph|00C0BR7D7H]], and let $J \in \R$ and $\beta \ge 0$.
A configuration is a map $\sigma \colon V \to \set{1, \ldots, q}$, and its energy is
$$H(\sigma) = -J \sum_{\set{u, v} \in E} \delta(\sigma(u), \sigma(v)),$$
where $\delta(a, b)$ is $1$ if $a = b$ and $0$ otherwise.
The *$q$-state Potts model* is the probability measure on $\set{1, \ldots, q}^V$ proportional to $e^{-\beta H(\sigma)}$; it is ferromagnetic when $J > 0$.
It is a [[lattice model|PAEME5EQRM]] with $S = \set{1, \ldots, q}$ and pair interaction $\Phi_{\set{u,v}} = -J\delta(\sigma(u), \sigma(v))$.

Check for $q = 2$: write the two states as $s = \pm 1$; then $\delta(\sigma(u), \sigma(v)) = \frac12 (1 + s_u s_v)$.
So $H = -\frac{J}{2} \abs{E} - \frac{J}{2} \sum_{\set{u,v} \in E} s_u s_v$, which is the [[Ising model|R0KGM32QN6]] with coupling $J/2$ up to an additive constant that does not change the measure.

## Remarks

On the square lattice $\Z^2$ with $J > 0$, the critical point is given by $e^{\beta_c J} = 1 + \sqrt q$, the self-dual point of Kramers–Wannier duality.
Beffara and Duminil-Copin proved this for all $q \ge 1$ in the random cluster representation.
For $q = 2$ this gives $\sinh(\beta_c J) = 1$, the Onsager value for an Ising coupling $J/2$.
On $\Z^2$ the transition is continuous for $q \le 4$ and discontinuous for $q > 4$.
The model is closely tied to the [[Fortuin–Kasteleyn random cluster model|VCTMYPDXPX]], and as $\beta \to \infty$ with $J < 0$ it counts proper $q$-colourings of $G$.

## Explanations

### L1 human

The Potts model is the Ising model with $q$ colours instead of two.
Each vertex of a graph gets a colour, and each edge whose two ends share a colour lowers the energy by $J$.
At low temperature large regions of one colour form; at high temperature the colours are mixed.
How the change happens depends on $q$: for few colours the regions grow gradually, for many colours they appear abruptly.
