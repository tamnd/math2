---
tag: XSZ9C68SPG
kind: definition
name: System of parameters
msc: [13C15, 13H05]
defines: 95QTEPMDA4
uses: [MZ02BKPHJA, MVGBS3J1P7, TMTPWVETQK, CZSCNZH8VY, 0670T59HGE]
sources:
  - url: https://en.wikipedia.org/wiki/System_of_parameters
---

## Definition

Let $(R, \mathfrak m)$ be a [[Noetherian|0670T59HGE]] [[local ring|MZ02BKPHJA]] of [[Krull dimension|MVGBS3J1P7]] $d$.
Elements $x_1, \dots, x_d$ of $\mathfrak m$ form a *system of parameters* of $R$ if the ideal $(x_1, \dots, x_d)$ is [[$\mathfrak m$-primary|TMTPWVETQK]].

## Remarks

The ideal $(x_1, \dots, x_d)$ is $\mathfrak m$-primary if and only if $\mathfrak m^n \subseteq (x_1, \dots, x_d)$ for some $n \ge 1$, and if and only if $R/(x_1, \dots, x_d)$ has finite [[length|CZSCNZH8VY]].
Example: in $R = k[x, y]_{(x, y)}$, with $k$ a field, the elements $x^2, y^3$ form a system of parameters, because $\dim R = 2$ and $\mathfrak m^4 \subseteq (x^2, y^3)$: each monomial $x^a y^b$ with $a + b = 4$ has $a \ge 2$ or $b \ge 3$.
Non-example: in the same ring, $x, x + x^2$ is not a system of parameters, because it generates the ideal $(x)$, and no power of $y$ lies in $(x)$.
If $x_1, \dots, x_d$ generate $\mathfrak m$ itself, then $R$ is a [[regular local ring|63XXTF6B5M]] and the list is called a regular system of parameters.
