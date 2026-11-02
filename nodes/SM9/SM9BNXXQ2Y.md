---
tag: SM9BNXXQ2Y
kind: definition
name: Siciak extremal function
msc: [32U35, 32U15]
defines: QBJ9R06GYE
uses: [X4ZHQG9995, FF2P7ER3QT]
sources:
  - url: https://en.wikipedia.org/wiki/Pluripolar_set
---

## Definition

Let $E \subseteq \C^n$ be a nonempty set and let $\mathcal{L}$ be the [[Lelong class|X4ZHQG9995]] of $\C^n$.
The *Siciak extremal function* of $E$ is the function $V_E \colon \C^n \to [0, +\infty]$ given by
$$V_E(z) = \sup\set{u(z) : u \in \mathcal{L},\ u \le 0 \text{ on } E} .$$
Its upper semicontinuous regularisation is $V_E^*(z) = \limsup_{w \to z} V_E(w)$.

## Remarks

The value is at least $0$, since $u = 0$ is admissible.
For compact $E$, Siciak's theorem gives the polynomial formula
$$V_E(z) = \sup\set{\tfrac{1}{\deg p} \log\abs{p(z)} : p \text{ a polynomial},\ \deg p \ge 1,\ \sup_E \abs{p} \le 1} .$$
Example: for the closed unit ball $E = \set{\abs{z} \le 1}$, $V_E(z) = \max(\log\abs{z}, 0)$.
Check: this function lies in $\mathcal{L}$ and vanishes on $E$, so $V_E \ge \max(\log\abs{z}, 0)$.
Conversely, let $u \in \mathcal{L}$ with $u \le 0$ on $E$, and let $w$ be a unit vector.
The function $\lambda \mapsto u(\lambda w) - \log\abs{\lambda}$ is subharmonic and bounded above on $\abs{\lambda} > 1$, so it extends across $\infty$.
It is at most $0$ on $\abs{\lambda} = 1$, so by the maximum principle $u(\lambda w) \le \log\abs{\lambda}$ for $\abs{\lambda} > 1$.
Non-example: if $E$ is [[pluripolar|N0MAGPW8AP]], then $V_E^* \equiv +\infty$, so $V_E^*$ is not in $\mathcal{L}$; for compact $E$ the converse holds as well, and $V_E^* \in \mathcal{L}^+$ when $E$ is compact and not pluripolar.
For $n = 1$ and compact $E$ of positive logarithmic capacity, $V_E^*$ is the Green function of the unbounded component of $\C \setminus E$ with pole at infinity, extended by $0$.
When $V_E$ is continuous, $E$ is called $L$-regular.
