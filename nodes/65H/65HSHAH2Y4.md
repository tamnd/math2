---
tag: 65HSHAH2Y4
kind: definition
name: Normed field
msc: [12J05, 12J10]
defines: ZFW9Q3WTAQ
uses: [0QA8CHH8MG, 08J2M1JYAG]
sources:
  - url: https://en.wikipedia.org/wiki/Absolute_value_(algebra)
---

## Definition

Let $K$ be a [[field|0QA8CHH8MG]].
An *absolute value* on $K$ is a map $\abs{\cdot} \colon K \to \R$ such that:

1. $\abs{x} \ge 0$ for all $x \in K$, and $\abs{x} = 0$ if and only if $x = 0$.
2. $\abs{xy} = \abs{x} \abs{y}$ for all $x, y \in K$.
3. $\abs{x + y} \le \abs{x} + \abs{y}$ for all $x, y \in K$.

A *normed field* is a field $K$ together with an absolute value on $K$.
It is a metric space with the distance $d(x, y) = \abs{x - y}$.

## Remarks

Example: $\C$ with the modulus $\abs{a + bi} = \sqrt{a^2 + b^2}$ is a normed field; clause 2 is $\abs{zw} = \abs{z}\abs{w}$, and clause 3 is the triangle inequality in the plane.
Example: $\Q$ with the [[p-adic absolute value|WGN82TCEF2]] for a prime $p$ is a normed field.
Example: every field with the trivial absolute value, $\abs{x} = 1$ for $x \ne 0$, is a normed field.
Non-example: on $\R$, the map $x \mapsto x^2$ satisfies clauses 1 and 2 but fails clause 3, since $(1 + 1)^2 = 4 > 2 = 1^2 + 1^2$.
Clauses 1 and 2 give $\abs{1} = 1$ and $\abs{-x} = \abs{x}$.
An absolute value that satisfies the stronger inequality $\abs{x + y} \le \max(\abs{x}, \abs{y})$ is a [[non-Archimedean absolute value|1H5F1BP6XS]].
A normed field is a [[topological field|D7YQW9RG24]] for the topology of its metric.
