---
tag: 8BPMHA5MT4
kind: statement
role: theorem
name: Thomson's principle
msc: [31C20, 94C05]
uses: [T7KRE7J3B4, XAE5YJ3H68]
about: [XAE5YJ3H68]
sources:
  - url: https://en.wikipedia.org/wiki/Electrical_network
---

## Statement

Let $(G, c)$ be a finite [[electrical network|T7KRE7J3B4]] with vertex set $V$ and resistances $r = 1/c$, and let $a, b \in V$ with $a \ne b$.
A *unit flow* from $a$ to $b$ is a function $\theta$ on ordered pairs of neighbours with $\theta(y, x) = -\theta(x, y)$ such that:
1. $\sum_y \theta(x, y) = 0$ for every $x \notin \set{a, b}$;
2. $\sum_y \theta(a, y) = 1$.

Its energy is $\mathcal{E}(\theta) = \sum_{\set{x, y} \in E} r(x, y)\, \theta(x, y)^2$.
Then
$$R_{\mathrm{eff}}(a, b) = \min \set{\mathcal{E}(\theta) : \theta \text{ a unit flow from } a \text{ to } b},$$
where $R_{\mathrm{eff}}$ is the [[effective resistance|XAE5YJ3H68]].
The minimum is attained exactly at the unit current flow.
This is the current of strength $1$ from $a$ to $b$ given by a voltage that is harmonic off $\set{a, b}$.

## Remarks

Let $i$ be the unit current flow, with voltage $v$, so that $r(x, y)\, i(x, y) = v(x) - v(y)$.
For any unit flow $\theta$, the difference $\theta - i$ has net flow $0$ at every vertex.
Summing by parts gives $\sum_{\set{x, y} \in E} r(x, y)\, i(x, y)\big(\theta - i\big)(x, y) = \sum_x v(x) \sum_y (\theta - i)(x, y) = 0$.
Hence $\mathcal{E}(\theta) = \mathcal{E}(i) + \mathcal{E}(\theta - i)$, which is at least $\mathcal{E}(i)$ with equality only for $\theta = i$.
Finally $\mathcal{E}(i) = \sum_x v(x) \sum_y i(x, y) = v(a) - v(b) = R_{\mathrm{eff}}(a, b)$.
Example: let the network consist of two paths from $a$ to $b$ that share only their endpoints, with total resistances $r_1$ and $r_2$.
A unit flow carries a constant amount $t$ along the first path and $1 - t$ along the second, so its energy is $r_1 t^2 + r_2 (1 - t)^2$.
Minimizing over $t$ gives $r_1 r_2/(r_1 + r_2)$, the parallel law.
The dual statement, Dirichlet's principle, says that $1/R_{\mathrm{eff}}(a, b)$ is the minimum of $\sum_{\set{x, y} \in E} c(x, y)\big(f(x) - f(y)\big)^2$ over all $f$ with $f(a) = 1$ and $f(b) = 0$.

## Explanations

### L1 human

Send one unit of current through a network from $a$ to $b$.
There are many ways to split the current among the wires, and each way wastes some energy as heat.
The way that nature chooses, given by Ohm's law, wastes the least energy.
That least energy equals the effective resistance between $a$ and $b$.

### L2 human

The principle turns effective resistance into a minimum, so any unit flow gives an upper bound on $R_{\mathrm{eff}}(a, b)$.
Dually, any test function in Dirichlet's principle gives a lower bound.
The Rayleigh monotonicity law follows at once, since raising resistances raises the energy of every flow.
On infinite graphs, a unit flow of finite energy to infinity exists exactly when the random walk is transient.
This gives a proof of the transience of $\Z^3$ by exhibiting such a flow.
