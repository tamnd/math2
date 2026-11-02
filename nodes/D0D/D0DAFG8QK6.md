---
tag: D0DAFG8QK6
kind: concept
name: Relative CW complex
msc: [57Q05, 55U10]
sources:
  - url: https://en.wikipedia.org/wiki/CW_complex
---

## Summary

A relative CW complex is a pair $(X, A)$ of spaces in which $X$ is built from $A$ by attaching cells of increasing dimension.
When $A$ is empty, it is the same as a [[CW complex|5W95QFHXPR]].
The inclusion $A \to X$ of a relative CW complex has the homotopy extension property, so it is a cofibration.

## Explanations

### L1 human

Start with any space $A$, not necessarily a CW complex.
Glue points to it, then intervals along their ends, then disks along their boundary circles, and so on.
The result $X$ is a relative CW complex over $A$.
For example, the closed disk $D^2$ is obtained from its boundary circle $S^1$ by gluing one $2$-cell, so $(D^2, S^1)$ is a relative CW complex.
