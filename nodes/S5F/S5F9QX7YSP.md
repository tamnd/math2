---
tag: S5F9QX7YSP
kind: example
name: Edwards–Anderson model
msc: [82B44, 82D30, 82B20]
instance_of: [EHPA4B5S5W]
uses: [R0KGM32QN6]
sources:
  - url: https://en.wikipedia.org/wiki/Spin_glass
---

## Example

Let $d \ge 1$ and $L \ge 2$ be integers, and let $\Lambda_L = \set{1, \dots, L}^d \subset \Z^d$.
Let $E_L$ be the set of pairs $\set{x, y}$ of points of $\Lambda_L$ at distance $1$.
Let $(J_{xy})_{\set{x,y} \in E_L}$ be independent random variables with a common law that is symmetric about $0$, for example standard Gaussian or uniform on $\set{-1, +1}$.
The *Edwards–Anderson model* is the random Hamiltonian
$$H_L(\sigma) = -\sum_{\set{x, y} \in E_L} J_{xy} \sigma_x \sigma_y, \qquad \sigma \in \set{-1, +1}^{\Lambda_L},$$
with the Gibbs measure proportional to $e^{-\beta H_L(\sigma)}$ for each sample of the couplings.

Check: the couplings are independent, and a symmetric law that is not concentrated at $0$ gives both signs with positive probability.
So the model is a [[spin glass|EHPA4B5S5W]], with couplings supported on the nearest-neighbour edges of $\Z^d$.

## Remarks

It is the [[Ising model|R0KGM32QN6]] on $\Z^d$ with each coupling replaced by an independent random sign or Gaussian.
Frustration is present: around a unit square of $\Z^2$, the product of the four couplings is negative with probability $1/2$, and then no configuration satisfies all four bonds.
Edwards and Anderson introduced the quantity $q = \lim \frac{1}{\abs{\Lambda_L}} \sum_x \langle \sigma_x \rangle^2$ as an order parameter for the frozen phase.
The nature of the low-temperature phase in finite dimension is still not settled mathematically.

## Explanations

### L1 human

Put a small magnet at each point of a square grid and connect each pair of neighbours by a bond.
Toss a coin for each bond: heads, the two magnets prefer to agree; tails, they prefer to disagree.
That is the Edwards–Anderson model.
It is the most realistic simple model of a spin glass, because each magnet only feels its neighbours, as in a real material.
