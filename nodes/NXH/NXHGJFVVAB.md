---
tag: NXHGJFVVAB
kind: definition
name: Carathéodory metric
msc: [32F45]
defines: SYNST4W3FR
uses: [JSGWAN2RJV, 3MQTWKBBBT, 85MM2EA0TK, 0A3HJX3KTF, V1QYA9RW73, DY8QQ5GTTX]
sources:
  - url: https://en.wikipedia.org/wiki/Carath%C3%A9odory_metric
---

## Definition

Let $\mathbb{D} = \set{\zeta \in \C : \abs{\zeta} < 1}$ and let $\rho(a, b) = \tanh^{-1} \abs{(a - b)/(1 - \bar a b)}$ be the Poincaré distance on $\mathbb{D}$.
Let $X$ be a [[complex manifold|JSGWAN2RJV]] and $p, q \in X$.
The *Carathéodory pseudodistance* of $X$ is
$$c_X(p, q) = \sup\set{\rho(f(p), f(q)) : f \colon X \to \mathbb{D} \text{ holomorphic}} .$$
The *Carathéodory–Reiffen pseudometric* is $\gamma_X(p, v) = \sup\set{\abs{df_p(v)} : f \colon X \to \mathbb{D} \text{ holomorphic},\ f(p) = 0}$ for $v$ tangent to $X$ at $p$.

## Remarks

$c_X$ is a [[pseudodistance|0A3HJX3KTF]], as a supremum of pseudodistances $(p, q) \mapsto \rho(f(p), f(q))$.
If $g \colon X \to Y$ is a [[holomorphic map|3MQTWKBBBT]], then $c_Y(g(p), g(q)) \le c_X(p, q)$, since $f \circ g$ is admissible for $X$ whenever $f$ is admissible for $Y$.
Example: $c_{\mathbb{D}} = \rho$; the identity gives $c_{\mathbb{D}} \ge \rho$, and the [[Schwarz–Pick theorem|V1QYA9RW73]] gives $\rho(f(a), f(b)) \le \rho(a, b)$ for every $f$.
Example: if $X$ is a bounded domain in $\C^n$, then $c_X$ is a distance, since a suitable linear function, rescaled, maps $X$ into $\mathbb{D}$ and separates any two given points.
Non-example: $c_{\C^n} \equiv 0$, since every bounded holomorphic function on $\C^n$ is constant.
For every connected $X$, $c_X \le k_X$, where $k_X$ is the [[Kobayashi pseudodistance|DY8QQ5GTTX]].
