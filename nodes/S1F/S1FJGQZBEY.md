---
tag: S1FJGQZBEY
kind: definition
name: Compartmental models in epidemiology
msc: [92D30, 34C60]
defines: BX5ZA16MM6
uses: [AKP63KCK02, 0P97V20RW7]
sources:
  - url: https://en.wikipedia.org/wiki/Compartmental_models_(epidemiology)
---

## Definition

Let $k \ge 1$, and let $x(t) = (x_1(t), \dots, x_k(t))$ give the number of hosts in each of $k$ compartments at time $t \ge 0$.
A *compartmental model* is an [[ordinary differential equation|0P97V20RW7]] $x'(t) = f(x(t))$ on $[0, \infty)^k$ of the following form.

1. For $i \ne j$ there is a flow rate $\phi_{ij}(x) \ge 0$ from compartment $i$ to compartment $j$, with $\phi_{ij}(x) = 0$ when $x_i = 0$.
2. Each compartment $i$ has an inflow from outside $b_i(x) \ge 0$ and an outflow to outside $d_i(x) \ge 0$, with $d_i(x) = 0$ when $x_i = 0$.
3. The equations are $x_i' = b_i(x) - d_i(x) + \sum_{j \ne i} \left( \phi_{ji}(x) - \phi_{ij}(x) \right)$ for $i = 1, \dots, k$.

In epidemiology the compartments are infection states, and the model is one kind of [[mathematical model of an infectious disease|AKP63KCK02]].

## Remarks

Clause 1 and the condition on $d_i$ ensure that solutions starting in $[0, \infty)^k$ stay there.
If all $b_i$ and $d_i$ are zero, the total $x_1 + \cdots + x_k$ is constant, since every flow leaves one compartment and enters another.

Example: the [[SIR model|J5FHBDJGJA]] has compartments $S, I, R$, flow $\phi_{SI} = \beta S I / N$ from $S$ to $I$, flow $\phi_{IR} = \gamma I$ from $I$ to $R$, and no other flows.
Both flows are nonnegative and vanish when their source compartment is empty.

Non-example: the equation $x_1' = -1$ with $k = 1$ fails clause 2.
Its outflow $d_1 = 1$ does not vanish at $x_1 = 0$, and the solution becomes negative.

Compartments are often written with letters: S susceptible, E exposed, I infectious, R removed or recovered, M with maternal immunity.
A model is named by the order of its compartments, as in SIR, SIS, SEIR or MSEIR.
