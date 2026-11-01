---
tag: B7CV5DZPRK
kind: definition
name: Multiplicity of a local ring
msc: [13H15, 13D40]
defines: JX20MNDDXT
uses: [MZ02BKPHJA, BNQVS83GZV, MVGBS3J1P7, TMTPWVETQK, 0670T59HGE]
sources:
  - url: https://en.wikipedia.org/wiki/Hilbert–Samuel_function
---

## Definition

Let $(R, \mathfrak m)$ be a [[Noetherian|0670T59HGE]] [[local ring|MZ02BKPHJA]] of [[Krull dimension|MVGBS3J1P7]] $d$, and let $I$ be an [[$\mathfrak m$-primary ideal|TMTPWVETQK]].
Let $P$ be the polynomial that agrees with the [[Hilbert–Samuel function|BNQVS83GZV]] $n \mapsto \ell(R/I^n)$ for all large $n$.
It has degree $d$, and its leading coefficient has the form $e/d!$ for a positive integer $e$.
The integer $e = e(I, R)$ is the *multiplicity* of $I$.
The *multiplicity of $R$* is $e(R) = e(\mathfrak m, R)$.

## Remarks

Example: let $R = k[x, y]_{(x, y)}/(y^2 - x^3)$, with $k$ a field.
For $n \ge 2$, $\ell(R/\mathfrak m^n) = 2n - 1$, since the monomials of degree $< n$ in $k[x, y]$ number $n(n+1)/2$ and those divisible by $y^2$ number $(n-2)(n-1)/2$.
So $d = 1$, the leading coefficient is $2 = e/1!$, and $e(R) = 2$.
Non-example: the function $n \mapsto \ell(R/I^n)$ for an ideal $I$ that is not $\mathfrak m$-primary, such as $I = (y)$ in $k[x, y]_{(x, y)}$, takes infinite values, so it has no multiplicity in this sense.
A regular local ring has multiplicity $1$, and an Artinian local ring $R$ has $e(R) = \ell(R)$.
