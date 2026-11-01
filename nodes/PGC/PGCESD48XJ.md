---
tag: PGCESD48XJ
kind: definition
name: Quasicircle
msc: [30C62]
defines: ADZAXRA6QT
uses: [A9J2KK4CEJ, 060W5CBZP6]
sources:
  - url: https://en.wikipedia.org/wiki/Quasicircle
---

## Definition

Let $K \ge 1$ and let $\mathbb{T} = \set{z \in \C : \abs{z} = 1}$ be the unit [[circle|060W5CBZP6]].
A subset $\Gamma$ of $\C$ is a *$K$-quasicircle* if $\Gamma = f(\mathbb{T})$ for some $K$-[[quasiconformal mapping|A9J2KK4CEJ]] $f \colon \C \to \C$.
It is a *quasicircle* if it is a $K$-quasicircle for some $K \ge 1$.

## Remarks

Every quasicircle is a bounded Jordan curve, since $f$ is a homeomorphism.
Example: an ellipse with semi-axes $a \ge b > 0$ is the image of $\mathbb{T}$ under the real-linear map $z \mapsto \frac{a+b}{2} z + \frac{a-b}{2}\bar z$, which is $K$-quasiconformal with $K = a/b$; so an ellipse is a quasicircle.
Ahlfors' three-point condition gives an equivalent form.
A bounded Jordan curve $\Gamma$ is a quasicircle if and only if there is a constant $C$ with the following property.
For any two points $z_1, z_2 \in \Gamma$, the arc of $\Gamma$ of smaller diameter between them has diameter at most $C \abs{z_1 - z_2}$.
Non-example: the cardioid $r = 1 - \cos\theta$ has a cusp at $0$.
Take the two points of the cardioid at angles $\pm\theta$ near the cusp.
Their distance is of order $\theta^3$, while the arc between them through the cusp has diameter of order $\theta^2$.
So the three-point condition fails, and the cardioid is not a quasicircle.
Every $C^1$ Jordan curve and the Koch snowflake are quasicircles.
