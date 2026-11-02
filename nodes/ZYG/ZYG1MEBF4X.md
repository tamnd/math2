---
tag: ZYG1MEBF4X
kind: definition
name: Levitzki radical
msc: [16N40]
defines: 9DD8M9R868
uses: [0894J980RK, 0DDA6CY7GJ]
sources:
  - url: https://en.wikipedia.org/wiki/Radical_of_a_ring
---

## Definition

Let $R$ be a [[ring|0894J980RK]].
A subset $S$ of $R$ is *locally nilpotent* if the following holds for every finite subset $F \subseteq S$.
There is an integer $n \ge 1$ such that every product $f_1 f_2 \cdots f_n$ of $n$ elements of $F$ is $0$.
The *Levitzki radical* $\operatorname{L}(R)$ of $R$ is the sum of all locally nilpotent [[two-sided ideals|0DDA6CY7GJ]] of $R$.

## Remarks

The sum of all locally nilpotent ideals is again locally nilpotent, so $\operatorname{L}(R)$ is the largest locally nilpotent ideal of $R$.
Example: let $R$ be the ring of upper triangular $2 \times 2$ matrices over a field $k$ and $N$ its strictly upper triangular matrices.
$N$ is locally nilpotent since $N^2 = 0$, and $R/N \cong k \times k$ has no nonzero nilpotent elements, so $\operatorname{L}(R) = N$.
Non-example: in $M_2(\Q)$ the set $\set{e_{12}, e_{21}}$ consists of nilpotent elements but is not locally nilpotent, since $(e_{12} e_{21})^m = e_{11} \ne 0$ for all $m$.
Every nilpotent ideal is locally nilpotent and every locally nilpotent ideal is nil, which gives $\operatorname{Nil}_*(R) \subseteq \operatorname{L}(R) \subseteq \operatorname{Nil}^*(R)$ with the [[prime radical|WF117EJ2HF]] and the [[upper nilradical|3G2JQEYBEK]].
