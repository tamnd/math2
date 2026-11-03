---
tag: JVQZC6KYAV
kind: example
name: Chiral Potts model
msc: [82B20, 82B23]
instance_of: [PAEME5EQRM]
uses: [5GY2J6ZGXJ]
sources:
  - url: https://en.wikipedia.org/wiki/Chiral_Potts_model
same_as:
  wikidata: Q17004982
  wikipedia: Chiral Potts model
---

## Example

Let $N \ge 2$ be an integer, and let $G = (V, E)$ be a finite piece of the square lattice whose edges are oriented to the right and upward.
A configuration is a map $\sigma \colon V \to \Z/N\Z$.
Let $W, \overline{W} \colon \Z/N\Z \to (0, \infty)$ be Boltzmann weights for horizontal and vertical edges.
The *chiral Potts model* is the probability measure on configurations with weight proportional to
$$\prod_{(x, y) \text{ horizontal}} W(\sigma_x - \sigma_y) \prod_{(x, y) \text{ vertical}} \overline{W}(\sigma_x - \sigma_y).$$
The products run over oriented edges $(x, y)$, and in general $W(k) \ne W(-k)$.
The weights are thus invariant under the cyclic shift $\sigma \mapsto \sigma + 1$ but not under $\sigma \mapsto -\sigma$; this lack of mirror symmetry is the chirality.

## Remarks

If $W(k) = W(-k)$ and $W$ takes one value at $k = 0$ and another for all $k \ne 0$, the model is the $N$-state [[Potts model|5GY2J6ZGXJ]].
For $N = 2$ there is no room for chirality, since $-k = k$ in $\Z/2\Z$, and the model is the [[Ising model|R0KGM32QN6]].
In the late 1980s an integrable family of chiral Potts models was found whose weights satisfy the star–triangle relation.
Unlike earlier solvable models, its weights are parametrized by points of an algebraic curve of genus greater than one when $N \ge 3$, not by elliptic or trigonometric functions.

## Explanations

### L1 human

Each site carries a clock hand with $N$ positions.
Neighbouring hands interact through their difference, but turning one step clockwise and one step anticlockwise can cost different energies.
This handedness models physical systems with a preferred direction of twist, and its solvable version needs new algebraic geometry.
