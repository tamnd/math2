---
tag: DGJEC8MTMQ
kind: definition
name: Conformal radius
msc: [30C35, 31A15]
defines: GYEX4BH5WM
uses: [02WHMEG5ZR, 0QW64ARSHB, 0YYT36R4YD, WX0HMW4GT7, 0MB48XDBY3, M36SD56MWQ]
sources:
  - url: https://en.wikipedia.org/wiki/Conformal_radius
---

## Definition

Let $\Omega \subsetneq \C$ be a [[simply connected domain|0QW64ARSHB]] and let $a \in \Omega$.
Let $\mathbb{D}$ be the unit disc.
By the [[Riemann mapping theorem|02WHMEG5ZR]] there is a unique [[conformal map|0YYT36R4YD]] $f \colon \mathbb{D} \to \Omega$ onto $\Omega$ with $f(0) = a$ and $f'(0) > 0$.
The *conformal radius* of $\Omega$ at $a$ is the number $\operatorname{rad}(a, \Omega) = f'(0)$.

## Remarks

Equivalently, $\operatorname{rad}(a, \Omega) = 1/\abs{\varphi'(a)}$ for any conformal map $\varphi$ of $\Omega$ onto $\mathbb{D}$ with $\varphi(a) = 0$.
Example: let $\Omega = \mathbb{D}$ and $a \in \mathbb{D}$.
The map $f(w) = (w + a)/(1 + \bar a w)$ sends $\mathbb{D}$ onto $\mathbb{D}$ with $f(0) = a$ and $f'(0) = 1 - \abs{a}^2 > 0$, so $\operatorname{rad}(a, \mathbb{D}) = 1 - \abs{a}^2$.
Non-example: $\Omega = \C$ is simply connected, but no conformal map of $\mathbb{D}$ onto $\C$ exists, so the definition does not apply.
With $d = \operatorname{dist}(a, \partial\Omega)$ one has $d \le \operatorname{rad}(a, \Omega) \le 4d$.
The lower bound follows from the [[Schwarz lemma|0MB48XDBY3]] applied to $f^{-1}$ on the disc of centre $a$ and radius $d$; the upper bound is the [[Koebe quarter theorem|WX0HMW4GT7]].
The [[Green's function|M36SD56MWQ]] of $\Omega$ satisfies $g(z, a) = -\log\abs{z - a} + \log \operatorname{rad}(a, \Omega) + o(1)$ as $z \to a$.
Under a conformal map $F$ of $\Omega$ onto $\Omega'$, $\operatorname{rad}(F(a), \Omega') = \abs{F'(a)} \operatorname{rad}(a, \Omega)$.
