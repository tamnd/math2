---
tag: 6HVZ30TS5F
kind: definition
name: Circle map
msc: ["37E10", "37E45"]
defines: N2SVK69S53
uses: [060W5CBZP6, 0KZZ70ZHXP, 0QT00PB5G2, 0YTCMFB4HC, 2Q1J7RZ4TK]
sources:
  - url: https://en.wikipedia.org/wiki/Arnold_tongue
---

## Definition

Let $\Omega \in \R$ and $K \ge 0$.
Let $F_{\Omega, K} \colon \R \to \R$ be the map
$$F_{\Omega, K}(x) = x + \Omega - \frac{K}{2\pi} \sin(2\pi x).$$
Since $F_{\Omega, K}(x + 1) = F_{\Omega, K}(x) + 1$, it induces a map $f_{\Omega, K}$ of the [[circle|060W5CBZP6]] $\R / \Z$, given by $f_{\Omega, K}(x + \Z) = F_{\Omega, K}(x) + \Z$.
The map $f_{\Omega, K}$ is the *(standard) circle map* with parameters $\Omega$ and $K$, and $F_{\Omega, K}$ is its lift.

## Remarks

Example: for $K = 0$ the circle map is the rotation $x \mapsto x + \Omega$; for irrational $\Omega$ it is an [[irrational rotation|2Q1J7RZ4TK]].

The derivative is $F'_{\Omega, K}(x) = 1 - K \cos(2\pi x)$.
For $0 \le K < 1$ it is positive everywhere, so $f_{\Omega, K}$ is a [[diffeomorphism|0KZZ70ZHXP]] of the circle.
For $K = 1$ the derivative vanishes at $x = 0$, so $f_{\Omega, 1}$ is a [[homeomorphism|0QT00PB5G2]] with a [[critical point|0YTCMFB4HC]], but not a diffeomorphism.

Non-example: for $K > 1$ the derivative takes negative values, so $F_{\Omega, K}$ is not monotone and $f_{\Omega, K}$ is not invertible.
The map is still defined, but it is not a homeomorphism.

The parameter $\Omega$ is often taken in $[0, 1)$, since $f_{\Omega + 1, K} = f_{\Omega, K}$.
