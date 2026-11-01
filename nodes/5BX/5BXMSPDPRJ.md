---
tag: 5BXMSPDPRJ
kind: definition
name: Elliptic function
msc: ["33E05", 30D30]
defines: FF9ZPCZ59K
uses: [0NSD1TPHR0, 089KWVYD69]
sources:
  - url: https://en.wikipedia.org/wiki/Elliptic_function
---

## Definition

Let $\omega_1, \omega_2 \in \C$ be linearly independent over $\R$, and let $\Lambda = \set{m\omega_1 + n\omega_2 : m, n \in \Z}$ be the lattice they span.
An *elliptic function* for $\Lambda$ is a [[meromorphic function|0NSD1TPHR0]] $f$ on $\C$ such that
$$f(z + \omega_1) = f(z) \quad \text{and} \quad f(z + \omega_2) = f(z)$$
for all $z \in \C$ that are not poles of $f$.
A function is *elliptic* if it is elliptic with respect to some such lattice.

## Remarks

Then $f(z + \omega) = f(z)$ for every $\omega \in \Lambda$, so $f$ is [[periodic|089KWVYD69]] with each lattice vector as a period.
A *fundamental parallelogram* is a set $\set{a + s\omega_1 + t\omega_2 : 0 \le s, t < 1}$ with $a \in \C$; an elliptic function is determined by its values there.
Example: the [[Weierstrass elliptic function|361NAK68QK]] $\wp$ of $\Lambda$ is elliptic with respect to $\Lambda$, and so is its derivative $\wp'$.
Constant functions are elliptic for every lattice.
Non-example: $e^z$ is meromorphic and periodic, but its periods are exactly the numbers $2\pi i k$ with $k \in \Z$.
They all lie on one line through $0$, so there is no second period independent over $\R$.
Equivalently, the elliptic functions for $\Lambda$ are the meromorphic functions on the compact Riemann surface $\C / \Lambda$.
