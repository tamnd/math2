---
tag: J5Z3FNCVTS
kind: definition
name: Conditionally negative definite function
msc: [43A35, 22D55]
defines: 4ZZX6Q8AGZ
uses: [G5S1M9, SCMS389SBG, 3PRZ02APFA, GTFZ277047]
sources:
  - url: https://en.wikipedia.org/wiki/Positive-definite_kernel
---

## Definition

Let $X$ be a nonempty set.
A function $\Psi \colon X \times X \to \R$ is a *conditionally negative definite kernel* if:

1. $\Psi(x, x) = 0$ for all $x \in X$;
2. $\Psi(x, y) = \Psi(y, x)$ for all $x, y \in X$;
3. $\sum_{i, j = 1}^{n} c_i c_j \Psi(x_i, x_j) \le 0$ for all $n \ge 1$, all $x_1, \dots, x_n \in X$ and all $c_1, \dots, c_n \in \R$ with $c_1 + \dots + c_n = 0$.

Let $G$ be a [[group|G5S1M9]] with identity $e$.
A function $\psi \colon G \to \R$ is *conditionally negative definite* if the kernel $\Psi(g, h) = \psi(h^{-1} g)$ on $G$ is conditionally negative definite.
This means $\psi(e) = 0$, $\psi(g^{-1}) = \psi(g)$, and $\sum_{i,j} c_i c_j \psi(g_j^{-1} g_i) \le 0$ when the real numbers $c_i$ add up to $0$.

## Remarks

Example: $\psi(x) = \abs{x}^2$ on $\R^n$.
Clauses 1 and 2 are clear.
For 3, write $\abs{x_i - x_j}^2 = \abs{x_i}^2 + \abs{x_j}^2 - 2\ip{x_i}{x_j}$.
When $\sum_i c_i = 0$, the first two terms contribute $0$, and the sum equals $-2\abs{\sum_i c_i x_i}^2 \le 0$.

Non-example: $\psi(x) = -\abs{x}^2$ on $\R^n$ fails clause 3.
With two points $x_1 \neq x_2$ and $c_1 = 1$, $c_2 = -1$, the sum is $-2\psi(x_1 - x_2) = 2\abs{x_1 - x_2}^2 > 0$.

If $\varphi$ is a real [[positive-definite function|3PRZ02APFA]] on $G$, then $\psi = \varphi(e) - \varphi$ is conditionally negative definite.
Some authors call these functions "of conditionally negative type" or simply "negative definite", and some drop the conditions $\psi(e) = 0$ or allow complex values.
A σ-compact locally compact group has [[property (T)|GTFZ277047]] if and only if every continuous conditionally negative definite function on it is bounded; this is the Delorme–Guichardet theorem.
