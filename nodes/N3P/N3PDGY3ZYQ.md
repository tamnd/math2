---
tag: N3PDGY3ZYQ
kind: definition
name: Process function
msc: [80A05, 80A10]
defines: 10J7Y8HKGP
uses: [T8J5XRYBZZ, PVDWD7HGFG, S8H21RWQ86, CY4GJQGF06]
sources:
  - url: https://en.wikipedia.org/wiki/Process_function
---

## Definition

Let $\Sigma$ be a thermodynamic system.
A *process function* of $\Sigma$ is a quantity $X(\gamma)$ assigned to each process $\gamma$ of $\Sigma$, which may depend on the whole path of $\gamma$.
It is called a process function when it is not the change of a [[state function|T8J5XRYBZZ]].
That is, there is no state function $F$ with $X(\gamma) = F(B) - F(A)$ for every process $\gamma$ from $A$ to $B$.

## Remarks

The [[work|S8H21RWQ86]] done on a gas is a process function.
For a [[quasistatic process|PVDWD7HGFG]] $\gamma$ in the $(p, V)$ plane, the work done on the gas is $W(\gamma) = -\int_\gamma p \, dV$.
Take the states $A = (p_1, V_1)$ and $B = (p_2, V_2)$ with $p_1 < p_2$ and $V_1 < V_2$.
The path that first expands at pressure $p_1$ and then raises the pressure gives $W = -p_1 (V_2 - V_1)$.
The path that first raises the pressure and then expands gives $W = -p_2 (V_2 - V_1)$, which is different.
[[Heat|CY4GJQGF06]] is also a process function.
The change of internal energy is not a process function in this sense, because it equals $U(B) - U(A)$.
Infinitesimal process functions are written $\delta W$ and $\delta Q$ to show that they are inexact differentials.
