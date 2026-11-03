---
tag: 7DZV6MYEAC
kind: definition
name: Olami–Feder–Christensen model
msc: [86A15, 82C22, 37B15]
defines: 129CMCWCAG
uses: [5QXNC6NTVN, N33S3095R5]
sources:
  - url: https://en.wikipedia.org/wiki/Olami%E2%80%93Feder%E2%80%93Christensen_model
---

## Definition

Fix an integer $L \ge 2$, a threshold $F_{\mathrm{th}} > 0$ and a transfer parameter $\alpha$ with $0 < \alpha \le 1/4$.
A state is a function $F$ from the square lattice $\set{1, \dots, L}^2$ to $[0, F_{\mathrm{th}})$, where $F(i)$ is the force on site $i$.
The *Olami–Feder–Christensen model* evolves a state by the following rules.

1. Driving: all values $F(i)$ increase by the same amount until the largest value equals $F_{\mathrm{th}}$.
2. Toppling: every site $i$ with $F(i) \ge F_{\mathrm{th}}$ is reset to $0$.
Each nearest neighbour $j$ of $i$ inside the lattice gets $F(j) \mapsto F(j) + \alpha F(i)$, with $F(i)$ taken before the reset.
3. Relaxation: rule 2 is repeated until all sites are below $F_{\mathrm{th}}$; then rule 1 starts again.

The set of topplings caused by one driving step is an *avalanche*, and the number of topplings is its size.
Force passed across the boundary of the lattice is lost.

## Remarks

Example: with $\alpha = 0.2$, a site with $F(i) = F_{\mathrm{th}}$ in the interior topples, its value becomes $0$, and its four neighbours gain $0.2 F_{\mathrm{th}}$ each.
The total force drops by $(1 - 4\alpha) F_{\mathrm{th}} = 0.2 F_{\mathrm{th}}$, so the bulk dynamics is dissipative.
For $\alpha = 1/4$ the bulk dynamics conserves the total force, and loss happens only at the boundary.
Non-example: the [[abelian sandpile model|N33S3095R5]] of Bak, Tang and Wiesenfeld adds integer grains at random single sites.
It moves a fixed number of grains in each toppling, so it fails rule 1 and the proportional transfer of rule 2.
The model is a deterministic cellular automaton with real values, apart from the random initial state.

## Explanations

### L1 human

The grid holds numbers that all grow together until one reaches the threshold.
That site then empties and hands a fixed fraction of its value to each neighbour.
Chains of such events are the model earthquakes.
