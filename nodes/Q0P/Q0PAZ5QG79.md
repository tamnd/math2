---
tag: Q0PAZ5QG79
kind: definition
name: Pointed space
msc: [55P99, 55Q05]
defines: T9DG8DDE75
uses: [0CQHFPGJ45, 0VGFHTM75Y]
sources:
  - url: https://en.wikipedia.org/wiki/Pointed_space
---

## Definition

A *pointed space* is a pair $(X, x_0)$ where $X$ is a [[topological space|0CQHFPGJ45]] and $x_0 \in X$.
The point $x_0$ is the *base point*.
A *pointed map* $f \colon (X, x_0) \to (Y, y_0)$ is a [[continuous map|0VGFHTM75Y]] $f \colon X \to Y$ with $f(x_0) = y_0$.

## Remarks

Pointed spaces and pointed maps form a category, often written $\mathbf{Top}_*$.
A pointed homotopy between pointed maps is a homotopy relative to the base point, and $[X, Y]_*$ denotes the set of pointed homotopy classes.
Example: $(S^n, e_1)$ with $e_1 = (1, 0, \ldots, 0)$ is a pointed space.
Non-example: the empty space has no point, so it carries no structure of a pointed space.
Every space $X$ gives a pointed space $X_+ = X \sqcup \set{*}$ with a new base point $*$.
