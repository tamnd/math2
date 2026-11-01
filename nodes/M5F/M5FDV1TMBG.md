---
tag: M5FDV1TMBG
kind: definition
name: Torsion group
msc: [20F50, 20K10]
defines: JZNQTTMG58
uses: [G5S1M9, 0WE2NHZJ7B, 0NCJ5WXN6Z, 0C4JS9RF5M, 0ZDW0H0VX4]
sources:
  - url: https://en.wikipedia.org/wiki/Torsion_group
---

## Definition

Let $G$ be a [[group|G5S1M9]].
$G$ is a *torsion group* (or *periodic group*) if every element of $G$ has finite [[order|0WE2NHZJ7B]].
That is, for every $g \in G$ there is an integer $n \ge 1$ with $g^n = e$.

## Remarks

Example: the group $\Q/\Z$, the [[rational numbers|0NCJ5WXN6Z]] modulo the [[integers|0C4JS9RF5M]] under addition.
If $x = \tfrac{a}{b} + \Z$ with $a, b \in \Z$ and $b \ge 1$, then $b x = a + \Z = 0$, so $x$ has finite order.
The Prüfer group is another infinite example.

Non-example: the group $\Z$ under addition.
For $n \ne 0$ and $k \ge 1$, $k n \ne 0$, so $n$ has infinite order.

A group of finite [[exponent|0ZDW0H0VX4]] is a torsion group, but $\Q/\Z$ is a torsion group of infinite exponent.
A finitely generated abelian torsion group is finite.
For nonabelian groups this fails: there are finitely generated infinite torsion groups, such as the Grigorchuk group; see the Burnside problem.
