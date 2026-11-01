---
tag: 8XDYNK6TV0
kind: definition
name: Non-Archimedean absolute value
msc: [12J25, 12J10]
defines: 1H5F1BP6XS
uses: [0QA8CHH8MG, 08J2M1JYAG, ZFW9Q3WTAQ]
sources:
  - url: https://en.wikipedia.org/wiki/Absolute_value_(algebra)
---

## Definition

Let $K$ be a [[field|0QA8CHH8MG]].
A *non-Archimedean absolute value* on $K$ is a map $\abs{\cdot} \colon K \to \R$ such that:

1. $\abs{x} \ge 0$ for all $x \in K$, and $\abs{x} = 0$ if and only if $x = 0$.
2. $\abs{xy} = \abs{x} \abs{y}$ for all $x, y \in K$.
3. $\abs{x + y} \le \max(\abs{x}, \abs{y})$ for all $x, y \in K$.

Clause 3 is the *strong triangle inequality*.

## Remarks

Clause 3 implies the triangle inequality, so a non-Archimedean absolute value is an absolute value, and $(K, \abs{\cdot})$ is a [[normed field|ZFW9Q3WTAQ]].
Example: for a prime $p$, the [[p-adic absolute value|WGN82TCEF2]] on $\Q$, given by $\abs{x}_p = p^{-v_p(x)}$ and $\abs{0}_p = 0$, is non-Archimedean.
Clause 2 is $p^{-v_p(xy)} = p^{-v_p(x)} p^{-v_p(y)}$, and clause 3 follows from $v_p(x + y) \ge \min(v_p(x), v_p(y))$.
Non-example: the usual absolute value on $\Q$ satisfies clauses 1 and 2 but fails clause 3, since $\abs{1 + 1} = 2 > 1 = \max(\abs{1}, \abs{1})$.
An absolute value on $K$ is non-Archimedean if and only if $\abs{n \cdot 1} \le 1$ for all integers $n$.
If $\abs{x} \ne \abs{y}$, then $\abs{x + y} = \max(\abs{x}, \abs{y})$.
For $0 < c < 1$, the rule $\abs{x} = c^{v(x)}$ turns a [[valuation|B85T5VKR3M]] $v$ with values in $\R$ into a non-Archimedean absolute value, and every non-Archimedean absolute value arises this way.
