---
tag: VEFHHSP35P
kind: statement
role: theorem
name: Tellegen's theorem
msc: [94C05, 94C15]
uses: [0KFYGSHHF5, 9B0V41V2F8]
about: [9B0V41V2F8]
sources:
  - url: https://en.wikipedia.org/wiki/Tellegen%27s_theorem
same_as:
  wikidata: Q913327
  wikipedia: Tellegen's theorem
---

## Statement

Let $G = (V, E)$ be a finite [[directed graph|0KFYGSHHF5]] whose underlying graph is connected.
Let $(i_e)_{e \in E}$ be real numbers that satisfy the current law of [[Kirchhoff's circuit laws|9B0V41V2F8]] on $G$.
Let $(v_e)_{e \in E}$ be real numbers that satisfy the voltage law on $G$.
Then
$$\sum_{e \in E} v_e \, i_e = 0.$$

## Remarks

By the voltage law, $v_e = \varphi(\text{tail}(e)) - \varphi(\text{head}(e))$ for a potential $\varphi \colon V \to \R$.
Then $\sum_e v_e i_e = \sum_{x \in V} \varphi(x) \big( \sum_{e \text{ leaves } x} i_e - \sum_{e \text{ enters } x} i_e \big)$, and each inner sum vanishes by the current law.
The currents and the voltages need not come from the same circuit, nor from the same moment in time; only the graph must be the same.
Nothing is assumed about the elements in the branches, which may be nonlinear or time-varying.
When $v$ and $i$ belong to the same circuit, $v_e i_e$ is the power absorbed by branch $e$, so the theorem says that the total power is conserved.
Take a loop of a battery of voltage $E$ and a resistor $r$ with current $i = E / r$, and orient both branches along the current.
Then the battery branch has $v = -E$, the resistor branch has $v = E$, and $(-E) i + E i = 0$.

## Explanations

### L1 human

In any circuit, the power given out by the sources equals the power taken in by the other elements.
Tellegen's theorem says much more: this balance follows from Kirchhoff's two laws alone.
You can even take the currents from one circuit and the voltages from another circuit with the same wiring, and the sum of their products is still zero.

### L2 human

In linear-algebra terms, the allowed currents form the kernel of the incidence matrix $A$, and the allowed voltages form the image of $A^{T}$.
These are orthogonal complements in $\R^E$, and the theorem is the orthogonality.
The freedom to mix two circuits makes the theorem a source of reciprocity results and of sensitivity formulas in circuit theory.
