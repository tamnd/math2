---
tag: GGDJN5KXN4
kind: definition
name: Iterative functional equation
msc: [39B12, 26A18]
defines: BCGBQ3HK26
uses: [SRAN4EKWS0, AYVTR2ES5B, 0EPAT51DXQ]
sources:
  - url: https://en.wikipedia.org/wiki/Iterated_function
---

## Definition

Let $X$ and $Y$ be sets.
An *iterative functional equation* for an unknown [[function|0EPAT51DXQ]] $\varphi \colon X \to Y$ is a [[functional equation|SRAN4EKWS0]] in one variable $x \in X$ of the following kind.
In it, $\varphi$ is evaluated at $x$ and at images of $x$ under given maps $f_1, \dots, f_k \colon X \to X$ or under [[iterates|AYVTR2ES5B]] of $\varphi$ itself.
The basic linear form, for $Y = \R$ and given $f \colon X \to X$ and $g, h \colon X \to \R$, is
$$\varphi(f(x)) = g(x)\, \varphi(x) + h(x) \quad \text{for all } x \in X.$$

## Remarks

Example: $\varphi(2x) = \varphi(x) + 1$ on $X = (0, \infty)$ is of the basic linear form with $f(x) = 2x$, $g = 1$, $h = 1$, and $\varphi = \log_2$ solves it.
Non-example: Cauchy's equation $\varphi(x + y) = \varphi(x) + \varphi(y)$ is not iterative, since it involves two independent variables.
The case $g = 1$, $h = 1$ is the [[Abel equation|68SHB7Z721]], and the case $g = s$ constant, $h = 0$ is [[Schröder's equation|VTJV7JVJEA]].
Equations with iterates of the unknown, such as $\varphi(\varphi(x)) = f(x)$, ask for [[iterative roots|27C6J3YNZY]] of $f$.
