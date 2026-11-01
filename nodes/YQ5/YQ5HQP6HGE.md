---
tag: YQ5HQP6HGE
kind: definition
name: Finitely presented module
msc: ["13E15", 13C05]
defines: 3EH4C3M5GV
uses: [0310REJJY8, 0NZ8JA25WK, 0DZ9DKAKZR, 05QY1VEBYD, JB7ZBFBA9C, 0670T59HGE]
sources:
  - url: https://en.wikipedia.org/wiki/Finitely_generated_module
---

## Definition

Let $R$ be a [[commutative ring|0310REJJY8]] and let $M$ be an [[$R$-module|0NZ8JA25WK]].
The module $M$ is *finitely presented* if there are integers $m, n \ge 0$ and an [[exact sequence|JB7ZBFBA9C]] of $R$-modules
$$R^m \xrightarrow{\ \varphi\ } R^n \xrightarrow{\ \pi\ } M \to 0.$$
Such a sequence is a *finite presentation* of $M$.

## Remarks

Equivalently, $M$ is [[finitely generated|05QY1VEBYD]] and the kernel of some surjection $R^n \to M$ is finitely generated.
By Schanuel's lemma, the kernel of every surjection $R^n \to M$ is then finitely generated.
The map $\varphi$ is given by an $n \times m$ matrix over $R$, so $M$ is the quotient of $R^n$ by the column span of a matrix.
Over a [[Noetherian ring|0670T59HGE]], every finitely generated module is finitely presented, since submodules of $R^n$ are finitely generated.

Example: over $R = \Z$, the module $\Z/6\Z$ is finitely presented.
The sequence $\Z \xrightarrow{6} \Z \to \Z/6\Z \to 0$, with the second map the reduction modulo $6$, is exact, because the image of multiplication by $6$ is $6\Z$, which is the kernel of the reduction.

Non-example: let $k$ be a field, $R = k[x_1, x_2, x_3, \ldots]$ the polynomial ring in infinitely many variables, and $M = R/(x_1, x_2, \ldots) \cong k$.
Then $M$ is finitely generated, by the class of $1$.
The kernel of $R \to M$ is the ideal $(x_1, x_2, \ldots)$, which is not finitely generated, so $M$ is not finitely presented.
