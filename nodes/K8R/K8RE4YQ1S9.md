---
tag: K8RE4YQ1S9
kind: definition
name: Finitary operation
msc: [08A62, 08A02]
defines: EJ8YJVM9BW
uses: [MSXX2P86CY, 0EPAT51DXQ, 09CEDJYBKP]
sources:
  - url: https://en.wikipedia.org/wiki/Operation_(mathematics)
---

## Definition

Let $A$ be a set and let $n \ge 0$ be an integer.
Write $A^n$ for the [[Cartesian product|09CEDJYBKP]] of $n$ copies of $A$, with $A^0 = \set{()}$ the one-element set whose element is the empty tuple.
An *$n$-ary operation* on $A$ is a [[function|0EPAT51DXQ]] $f \colon A^n \to A$.
A *finitary operation* on $A$ is an $n$-ary operation on $A$ for some integer $n \ge 0$, called its [[arity|MSXX2P86CY]].

## Remarks

Example: the map $f \colon \Z^3 \to \Z$, $f(x, y, z) = x - y + z$, is a finitary operation of arity $3$ on $\Z$, because $x - y + z$ is an integer for all integers $x, y, z$.

Non-example: division $(x, y) \mapsto x / y$ is not a binary operation on $\Q$, because it is not defined when $y = 0$, so it is not a function on all of $\Q^2$.
On $\Q \setminus \set{0}$ it is a binary operation.

The requirement that the values lie in $A$ is often called closure of $A$ under $f$.
Some authors use the word operation only for finitary operations.
