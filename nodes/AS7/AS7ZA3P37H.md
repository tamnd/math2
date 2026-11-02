---
tag: AS7ZA3P37H
kind: definition
name: Character space
msc: [46J05, 46J20]
defines: M7JVFJ3MMX
uses: [4A82S5FVRT, P6KHVSTPZV]
sources:
  - url: https://en.wikipedia.org/wiki/Gelfand_representation
---

## Definition

Let $A$ be a commutative complex Banach algebra.
A *character* of $A$ is a nonzero linear map $\varphi \colon A \to \C$ with $\varphi(ab) = \varphi(a) \varphi(b)$ for all $a, b \in A$.
The *character space* $\Delta(A)$ of $A$ is the set of characters of $A$.
Each character is continuous with $\norm{\varphi} \le 1$, so $\Delta(A)$ is a subset of the [[continuous dual space|4A82S5FVRT]] $A^*$.
The topology on $\Delta(A)$ is the relative weak-* topology, the [[weak topology|P6KHVSTPZV]] of the maps $\varphi \mapsto \varphi(a)$, $a \in A$.

## Remarks

Other names are the *maximal ideal space* and the *Gelfand spectrum*, written $\sigma(A)$ or $\mathfrak{M}(A)$.
The space $\Delta(A)$ is locally compact and Hausdorff.
If $A$ has a unit, then $\varphi(1) = 1$ for every character, $\Delta(A)$ is weak-* closed in the unit ball of $A^*$, and so it is compact by the [[Banach–Alaoglu theorem|1BXEJXQ2YT]].
For unital $A$, the map $\varphi \mapsto \ker \varphi$ is a bijection from $\Delta(A)$ onto the set of [[maximal ideals|0PV74TR5FP]] of $A$; the [[Gelfand–Mazur theorem|3D6XH41A3B]] shows that each quotient $A / \mathfrak{m}$ is $\C$.

Example: let $X$ be a compact Hausdorff space and $A = C(X)$ with the sup norm.
For $x \in X$, the evaluation $\varphi_x(f) = f(x)$ is linear and multiplicative, and $\varphi_x(1) = 1$, so it is a character.
Every character of $C(X)$ has this form, and $x \mapsto \varphi_x$ is a homeomorphism from $X$ onto $\Delta(A)$.

Non-example: on $C([0,1])$, the map $\varphi(f) = \int_0^1 f(t) \, dt$ is linear and nonzero but not multiplicative.
For $f(t) = t$ one has $\varphi(f^2) = 1/3$, while $\varphi(f)^2 = 1/4$.
