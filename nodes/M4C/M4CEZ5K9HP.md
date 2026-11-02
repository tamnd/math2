---
tag: M4CEZ5K9HP
kind: concept
name: Sobolev space
msc: ["46E35", 35D30]
sources:
  - url: https://en.wikipedia.org/wiki/Sobolev_space
same_as:
  wikidata: Q1501536
  wikipedia: Sobolev space
---

## Summary

A Sobolev space $W^{k,p}(U)$ consists of the functions in the [[Lp space|SASP14MA1Z]] $L^p(U)$ whose [[weak derivatives|C3EC148VZD]] up to order $k$ also lie in $L^p(U)$.
With the sum of the $L^p$ norms of the derivatives it is a [[Banach space|06GZ956657]], and for $p = 2$ it is a [[Hilbert space|HM2HHE3J51]], written $H^k(U)$.
Sobolev spaces are the main setting of the modern theory of partial differential equations, because weak solutions are found in them by functional analysis.
Embedding theorems then translate the integrability of derivatives into integrability or continuity of the function itself.

## Explanations

### L1 human

A Sobolev space measures a function together with its derivatives, but in an averaged sense rather than point by point.
A function belongs to $W^{1,2}$ when the function and its slope have finite energy $\int u^2 + \abs{\nabla u}^2$.
Corners are allowed, but jumps are not.
For example, $\abs{x}$ on $(-1, 1)$ lies in $W^{1,p}$ for every $p$, while the sign function on $(-1, 1)$ lies in no $W^{1,p}$.
