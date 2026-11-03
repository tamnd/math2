---
tag: Z4ECWDNHFN
kind: definition
name: Thermodynamic cycle
msc: [80A10, 80A05]
defines: AGRGCDWQF8
uses: [GYNNJBMTCP, TD4C13V3J6, T8J5XRYBZZ, CY4GJQGF06, S8H21RWQ86, V14W2V4JSR, F6JVQ12X43, PVDWD7HGFG, C9MM7GFRWN]
sources:
  - url: https://en.wikipedia.org/wiki/Thermodynamic_cycle
---

## Definition

Let $S$ be a [[thermodynamic system|GYNNJBMTCP]], called the working substance.
A *thermodynamic cycle* of $S$ is a finite sequence of processes that take $S$ through successive [[states|TD4C13V3J6]].
The final state of the last process must be the initial state of the first.

## Remarks

Every [[state function|T8J5XRYBZZ]] takes the same value at the end as at the start; in particular the change of [[internal energy|F6JVQ12X43]] over the cycle is $0$.
By the [[first law of thermodynamics|V14W2V4JSR]], the net [[heat|CY4GJQGF06]] $Q$ absorbed over the cycle equals the net [[work|S8H21RWQ86]] $W$ done by $S$.
For a closed simple system whose processes are all [[quasistatic|PVDWD7HGFG]], $W = \oint p\, dV$, the area enclosed by the loop in the $(V, p)$ plane, counted positive for a clockwise loop.
Example: expand an ideal gas isothermally from $V_1$ to $V_2$ at temperature $T_1$, then cool it at constant volume to $T_2 < T_1$.
Then compress it isothermally back to $V_1$ at $T_2$, and heat it at constant volume back to $T_1$.
The gas returns to its initial state $(T_1, V_1)$, so this is a cycle.
A non-example: the [[isothermal expansion|C9MM7GFRWN]] from $V_1$ to $V_2$ alone is not a cycle, because it ends in a state with a different volume.
