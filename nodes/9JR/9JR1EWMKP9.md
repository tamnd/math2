---
tag: 9JR1EWMKP9
kind: definition
name: Biochemical systems theory
msc: [92C42, 92C45, 34C60]
defines: 6R3FTQGV2V
uses: [0NT64JV96A, 04DXAFN2ES, 0N8NGKDZDZ]
sources:
  - url: https://en.wikipedia.org/wiki/Biochemical_systems_theory
---

## Definition

Let $X_1, \dots, X_n > 0$ be dependent concentrations and $X_{n+1}, \dots, X_{n+m} > 0$ independent (fixed) concentrations.
A *generalized mass action (GMA) system* is a system of [[ordinary differential equations|0NT64JV96A]]
$$\frac{dX_i}{dt} = \sum_{k=1}^{r} \gamma_{ik} \prod_{j=1}^{n+m} X_j^{f_{ikj}}, \qquad i = 1, \dots, n,$$
with real rate constants $\gamma_{ik}$ and real kinetic orders $f_{ikj}$.
An *S-system* is the special case with one production term and one degradation term per equation:
$$\frac{dX_i}{dt} = \alpha_i \prod_{j=1}^{n+m} X_j^{g_{ij}} - \beta_i \prod_{j=1}^{n+m} X_j^{h_{ij}}, \qquad \alpha_i, \beta_i \ge 0,\ g_{ij}, h_{ij} \in \R.$$

## Remarks

The kinetic order $f_{ikj}$ equals the logarithmic derivative $\partial \ln v_{ik} / \partial \ln X_j$ of the term $v_{ik}$, which is constant for a power law.
Example: if $\alpha_i, \beta_i > 0$, a positive [[equilibrium|0N8NGKDZDZ]] of an S-system satisfies $\alpha_i \prod_j X_j^{g_{ij}} = \beta_i \prod_j X_j^{h_{ij}}$.
Taking [[logarithms|04DXAFN2ES]] with $y_j = \ln X_j$ gives the linear system $\sum_j (g_{ij} - h_{ij})\, y_j = \ln(\beta_i / \alpha_i)$ for $i = 1, \dots, n$.
Non-example: the Michaelis–Menten rate $V s / (K + s)$ is not a power law in $s$, since its logarithmic derivative $K/(K + s)$ depends on $s$.
Biochemical systems theory approximates it by a power law near an operating point.
Mass-action kinetics is the special case of a GMA system with nonnegative integer kinetic orders.
