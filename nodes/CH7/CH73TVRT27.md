---
tag: CH73TVRT27
kind: conjecture
name: Brennan conjecture
msc: [30C35, 30C55]
uses: [02WHMEG5ZR, 0QW64ARSHB, 0YYT36R4YD]
about: [0YYT36R4YD]
sources:
  - url: https://en.wikipedia.org/wiki/Brennan_conjecture
same_as:
  wikidata: Q51757594
  wikipedia: Brennan conjecture
history:
  posed_by: "James E. Brennan"
  first_stated: "1978"
---

## Statement

Let $\Omega \subsetneq \C$ be a [[simply connected domain|0QW64ARSHB]], and let $\varphi \colon \Omega \to \mathbb{D}$ be a [[conformal map|0YYT36R4YD]] onto the unit disc $\mathbb{D} = \set{z \in \C : \abs{z} < 1}$.
Then for every real $p$ with $4/3 < p < 4$,
$$\int_\Omega \abs{\varphi'(z)}^p \, dA(z) < \infty,$$
where $dA$ is area measure.

## Remarks

Such a map $\varphi$ exists by the [[Riemann mapping theorem|02WHMEG5ZR]].
For $p = 2$ the integral is the area of $\mathbb{D}$, which is $\pi$.
The range is sharp at both ends.
Take the Koebe domain $\Omega = \C \setminus (-\infty, -1/4]$ and the inverse $\varphi$ of the [[Koebe function|EZQFWKF03Q]].
Then $\abs{\varphi'(z)}$ behaves like $\abs{z}^{-3/2}$ at infinity and like $\abs{z + 1/4}^{-1/2}$ near the tip of the slit.
So the integral diverges for $p \le 4/3$ and for $p \ge 4$.
The conjecture is known for $4/3 < p < 3 + \delta$ with some $\delta > 0$; Brennan proved this range.
The full conjecture is open.

## Explanations

### L1 human

The derivative of a Riemann map measures how much the map stretches the domain near each point.
Near a sharp inward corner or the tip of a slit, this stretching blows up.
The conjecture says that it never blows up too badly: a certain power of it always has finite total integral.
The slit plane is the worst case and shows that the claimed range of powers cannot be enlarged.
