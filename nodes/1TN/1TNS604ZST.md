---
tag: 1TNS604ZST
kind: conjecture
name: Hochster's homological conjectures
msc: [13D22, 13H05]
uses: [0670T59HGE, MZ02BKPHJA, 63XXTF6B5M, 95QTEPMDA4, 69R5R2FCS5]
about: [63XXTF6B5M, 95QTEPMDA4]
sources:
  - url: https://en.wikipedia.org/wiki/Homological_conjectures_in_commutative_algebra
history:
  posed_by: "Melvin Hochster"
---

## Statement

Let $(R, \mathfrak{m})$ be a commutative [[Noetherian|0670T59HGE]] [[local ring|MZ02BKPHJA]] of dimension $d$.

1. Direct summand conjecture: let $R$ be a [[regular local ring|63XXTF6B5M]] and $R \subseteq S$ a ring extension with $S$ a finitely generated $R$-module. Then $R$ is a direct summand of $S$ as an $R$-module.
2. Monomial conjecture: if $x_1, \ldots, x_d$ is a [[system of parameters|95QTEPMDA4]] of $R$, then $(x_1 x_2 \cdots x_d)^t \notin (x_1^{t+1}, \ldots, x_d^{t+1})$ for every integer $t \ge 0$.
3. Big Cohen–Macaulay module conjecture: there is an $R$-module $B$ such that some system of parameters of $R$ is a [[regular sequence|69R5R2FCS5]] on $B$. The module $B$ need not be finitely generated.

## Remarks

These are three of the homological conjectures studied and organized by Hochster; there are others, such as the intersection conjectures.
Hochster proved all three when $R$ contains a field, using reduction to positive characteristic and the Frobenius map.
The monomial conjecture and the direct summand conjecture are known to be equivalent.
In mixed characteristic, André proved the direct summand conjecture and the existence of big Cohen–Macaulay algebras, using perfectoid methods; so the three statements are now theorems.
The [[direct summand conjecture|CQJ1FPKKHT]] has its own node.

## Explanations

### L1 human

These conjectures predict that some properties of polynomial rings over a field remain true for all Noetherian local rings.
For decades they were known only for rings that contain a field, and the case of rings like the $p$-adic integers resisted.
They were settled in that case only recently, with new tools from arithmetic geometry.
