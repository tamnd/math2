---
tag: 1GE6HRGS87
kind: statement
role: theorem
name: GHS inequality
msc: [82B20, 60K35]
uses: [R0KGM32QN6, 8HAEC947YG]
about: [R0KGM32QN6]
sources:
  - url: https://en.wikipedia.org/wiki/Griffiths_inequality
---

## Statement

Let $\Lambda$ be a finite set, let $J_{ij} = J_{ji} \ge 0$ for $i \ne j$ in $\Lambda$, and let $h_i \ge 0$ for $i \in \Lambda$.
Write $\langle F \rangle$ for the average of $F$ under the [[Ising model|R0KGM32QN6]] measure on $\set{-1, +1}^\Lambda$ proportional to
$$\exp\Big( \sum_{\set{i, j} \subseteq \Lambda} J_{ij} \sigma_i \sigma_j + \sum_{i \in \Lambda} h_i \sigma_i \Big).$$
Then for all $i, j, k \in \Lambda$,
$$\langle \sigma_i \sigma_j \sigma_k \rangle - \langle \sigma_i \rangle \langle \sigma_j \sigma_k \rangle - \langle \sigma_j \rangle \langle \sigma_i \sigma_k \rangle - \langle \sigma_k \rangle \langle \sigma_i \sigma_j \rangle + 2 \langle \sigma_i \rangle \langle \sigma_j \rangle \langle \sigma_k \rangle \le 0.$$

## Remarks

The left-hand side is the third cumulant (truncated three-point function), and it equals $\partial^2 \langle \sigma_i \rangle / \partial h_j \partial h_k$.
So the inequality says that each magnetization $\langle \sigma_i \rangle$ is concave along every direction with nonnegative components in the region $h \ge 0$.
In particular it is a concave function of a uniform field $h \ge 0$.
A standard proof takes four independent copies of the system and an orthogonal change of variables, and reduces to inequalities of [[Griffiths type|8HAEC947YG]] for the new variables.
The hypothesis $h_i \ge 0$ is needed: flipping all spins and fields changes the sign of the left-hand side, so for $h_i \le 0$ it is $\ge 0$ instead.
Unlike the Griffiths inequalities, the result is stated for pair interactions and fields, not for general multi-spin couplings.

Example: for one site with field $h \ge 0$, $\langle \sigma \rangle = \tanh h$, and $\frac{d^2}{dh^2} \tanh h = -2 \tanh h \, (1 - \tanh^2 h) \le 0$.

## Explanations

### L1 human

Turn up the magnetic field on a ferromagnet and its magnetization grows, but each further step of field helps a little less.
The GHS inequality makes this precise: magnetization is concave in a nonnegative field.
It was proved by Griffiths, Hurst and Sherman in 1970.

### L2 human

Concavity in the field means that the susceptibility $\partial \langle \sigma_i \rangle / \partial h$ decreases as $h \ge 0$ grows.
This is used to control the magnetization and the susceptibility near the critical point, and it leads to inequalities between critical exponents.
It sits next to the [[Griffiths inequalities|8HAEC947YG]], which give monotonicity, and the Lee–Yang theorem, from which it can also be derived.
