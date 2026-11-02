---
tag: MCXT7ZW329
kind: definition
name: Iterated function
msc: [37B02, 26A18, 37-01]
defines: AYVTR2ES5B
uses: [0EPAT51DXQ, 0THBK9V825]
sources:
  - url: https://en.wikipedia.org/wiki/Iterated_function
    locator: Definition
---

## Definition

Let $X$ be a set and let $f \colon X \to X$ be a [[map|0EPAT51DXQ]].
The *iterates* of $f$ are the maps $f^n \colon X \to X$ for $n \in \N$, defined recursively by
$$f^0 = \id_X, \qquad f^{n+1} = f \circ f^n,$$
where $\circ$ is [[function composition|0THBK9V825]].
The map $f^n$ is the *$n$-th iterate* of $f$.

## Remarks

By induction, $f^m \circ f^n = f^{m + n}$ and $(f^m)^n = f^{mn}$ for all $m, n \in \N$.
If $f$ is a bijection, one also sets $f^{-n} = (f^{-1})^n$, and the rule $f^m \circ f^n = f^{m+n}$ then holds for all $m, n \in \Z$.

Example: for $f(x) = x^2$ on $\R$, one has $f^2(x) = (x^2)^2 = x^4$ and in general $f^n(x) = x^{2^n}$.
The check is the induction step $f^{n+1}(x) = f(x^{2^n}) = x^{2^{n+1}}$.

Non-example: for $g(x) = x + 1$ on $\R$, the pointwise square $x \mapsto g(x)^2 = (x+1)^2$ is not the second iterate, which is $g^2(x) = x + 2$.
The notation $f^n$ can mean either object, so texts state which one is meant; for example $\sin^2 x$ usually means $(\sin x)^2$.
