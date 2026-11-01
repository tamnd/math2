---
tag: 7HWZ06SRMF
kind: definition
name: Jacobson radical
msc: [13A15, 16N20]
defines: XA0DCNH7WY
uses: [0GYGHKX834, 09J6KGT65G, 019NFGFPR5]
sources:
  - url: https://en.wikipedia.org/wiki/Jacobson_radical
---

## Definition

Let $R$ be a [[commutative ring|0GYGHKX834]].
The *Jacobson radical* of $R$ is the intersection of all [[maximal ideals|09J6KGT65G]] of $R$:
$$J(R) = \bigcap_{M \text{ maximal}} M.$$

## Remarks

Equivalent form: $x \in J(R)$ if and only if $1 - xy$ is a [[unit|019NFGFPR5]] of $R$ for every $y \in R$.
Example: in $\Z/12\Z$ the maximal ideals are $2\Z/12\Z$ and $3\Z/12\Z$, so $J(\Z/12\Z) = 6\Z/12\Z = \set{0, 6}$; for $y \in \Z/12\Z$, $1 - 6y$ is $1$ or $7$, both units.
Non-example: $2 \notin J(\Z)$, since $2 \notin 3\Z$; with the equivalent form, $1 - 2 \cdot 2 = -3$ is not a unit of $\Z$.
The [[nilradical|QQDN6EYQNJ]] is contained in $J(R)$, since every maximal ideal is prime.
The inclusion can be strict: for $\Z_{(p)}$, the integers localized at a prime $p$, the nilradical is $0$ while $J = p\Z_{(p)}$.
$R$ is a [[local ring|MZ02BKPHJA]] exactly when $J(R)$ is a maximal ideal.
Other notations are $\operatorname{Jac}(R)$ and $\operatorname{rad}(R)$.
For an ideal $I$, the Jacobson radical of $I$ is the intersection of the maximal ideals that contain $I$.
