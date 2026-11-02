---
tag: 57DPMSN7H8
kind: definition
name: Effective resistance
msc: [31C20, 05C12, 94C05]
defines: XAE5YJ3H68
uses: [T7KRE7J3B4, WRY0M7SW59, YKETR75ZYW, TN6M6DVZRP]
sources:
  - url: https://en.wikipedia.org/wiki/Resistance_distance
---

## Definition

Let $(G, c)$ be a finite [[electrical network|T7KRE7J3B4]] with vertex set $V$, and let $a, b \in V$ with $a \ne b$.
Let $v \colon V \to \R$ be the unique function with $v(a) = 1$ and $v(b) = 0$ that is [[harmonic|WRY0M7SW59]] on $V \setminus \set{a, b}$.
This is the solution of a [[discrete Dirichlet problem|YKETR75ZYW]] with boundary $\set{a, b}$.
Let $I = \sum_{y} c(a, y)\big(1 - v(y)\big)$ be the net current that leaves $a$.
The *effective resistance* between $a$ and $b$ is $R_{\mathrm{eff}}(a, b) = 1/I$.
The number $C_{\mathrm{eff}}(a, b) = I$ is the *effective conductance*.

## Remarks

The current $I$ is positive: $0 \le v \le 1$ by the maximum principle, and $v(y) < 1$ for some neighbour $y$ of $a$ since $G$ is connected.
Scaling $v$ shows that $R_{\mathrm{eff}}(a, b)$ is the voltage difference between $a$ and $b$ when a current of strength $1$ enters at $a$ and leaves at $b$.
Example: for the path $a - m - b$ with unit conductances, $v(m) = \tfrac12$, so $I = \tfrac12$ and $R_{\mathrm{eff}}(a, b) = 2$, the sum of the two resistances in series.
If an edge of conductance $1$ is added between $a$ and $b$, the current becomes $\tfrac12 + 1$, so $R_{\mathrm{eff}}(a, b) = \tfrac23$, as for resistors in parallel.
Non-example: if $a$ and $b$ lie in different components of a disconnected graph, no current can flow between them.
Then the effective resistance is not a finite number, which is why connectedness is part of the definition of a network.
With $L$ the weighted [[graph Laplacian|TN6M6DVZRP]] and $L^{+}$ its Moore–Penrose pseudoinverse, $R_{\mathrm{eff}}(a, b) = (e_a - e_b)^{T} L^{+} (e_a - e_b)$, where $e_x$ is the indicator vector of $x$.
The function $(a, b) \mapsto R_{\mathrm{eff}}(a, b)$, extended by $0$ on the diagonal, is a metric on $V$, the resistance distance.
