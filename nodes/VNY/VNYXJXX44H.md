---
tag: VNYXJXX44H
kind: definition
name: Reinhardt domain
msc: [32Q02, 32A05]
defines: WA0SE56FVH
uses: [BH57D2FBNR, 02BH3MCBQB, 0V032VWTHD]
sources:
  - url: https://en.wikipedia.org/wiki/Function_of_several_complex_variables
---

## Definition

A *domain* in $\C^n$ is a nonempty [[open|02BH3MCBQB]] and [[connected|0V032VWTHD]] subset of $\C^n$.
A domain $D \subseteq \C^n$ is a *Reinhardt domain* (with centre $0$) if for every $z \in D$ and every $\theta = (\theta_1, \dots, \theta_n) \in \R^n$ the point
$$(e^{i\theta_1} z_1, \dots, e^{i\theta_n} z_n)$$
lies in $D$.
A Reinhardt domain $D$ is *complete* if for every $z \in D$ and every $w \in \C^n$ with $\abs{w_j} \le \abs{z_j}$ for $j = 1, \dots, n$, the point $w$ lies in $D$.

## Remarks

Example: the unit polydisc $\set{\abs{z_1} < 1, \abs{z_2} < 1}$ is a complete Reinhardt domain, since both conditions only involve $\abs{z_1}$ and $\abs{z_2}$ and stay true when these decrease.
The annulus product $\set{1 < \abs{z_1} < 2, \ 1 < \abs{z_2} < 2}$ is a Reinhardt domain that is not complete: it contains $(3/2, 3/2)$ but not $(0, 3/2)$.
Non-example: the ball $\set{z \in \C^2 : \abs{z_1 - 1/2}^2 + \abs{z_2}^2 < 1}$ contains $(7/5, 0)$, but its rotation $(-7/5, 0)$ is at distance $19/10 > 1$ from the centre, so it is not Reinhardt.
A Reinhardt domain with centre $a$ is a set $a + D$ with $D$ a Reinhardt domain with centre $0$.
A Reinhardt domain is determined by its image under $z \mapsto (\abs{z_1}, \dots, \abs{z_n})$.
