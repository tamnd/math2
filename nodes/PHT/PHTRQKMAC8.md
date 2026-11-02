---
tag: PHTRQKMAC8
kind: definition
name: Electrical network
msc: [31C20, 94C05, 05C81]
defines: T7KRE7J3B4
uses: [00C0BR7D7H, WRY0M7SW59]
sources:
  - url: https://en.wikipedia.org/wiki/Electrical_network
---

## Definition

An *electrical network* is a pair $(G, c)$ of a connected [[graph|00C0BR7D7H]] $G = (V, E)$, in which every vertex has finitely many neighbours, and a function $c \colon E \to (0, \infty)$.
The number $c(e)$ is the *conductance* of the edge $e$, and $r(e) = 1/c(e)$ is its *resistance*.
For $x, y \in V$, write $c(x, y) = c(\set{x, y})$ if $\set{x, y} \in E$ and $c(x, y) = 0$ otherwise.
A *voltage* is a function $v \colon V \to \R$.
The *current* of $v$ is the function on ordered pairs of neighbours given by Ohm's law: $i(x, y) = c(x, y)\big(v(x) - v(y)\big)$.

## Remarks

The current is antisymmetric: $i(y, x) = -i(x, y)$.
The net current out of $x$ is $\sum_y i(x, y) = \sum_y c(x, y)\big(v(x) - v(y)\big)$.
Kirchhoff's node law at $x$ says that this net current is $0$, which holds exactly when $v$ is [[harmonic|WRY0M7SW59]] at $x$.
Example: the path $a - m - b$ with two edges of conductance $1$ is a network.
The voltage with $v(a) = 1$, $v(m) = \tfrac12$, $v(b) = 0$ is harmonic at $m$, and it sends the current $\tfrac12$ along each edge from $a$ to $b$.
Non-example: giving an edge conductance $0$ is not allowed; such an edge carries no current and should be removed from the graph instead.
Kirchhoff's cycle law, that voltage drops add to $0$ around each cycle, is automatic here because the current comes from a voltage.
