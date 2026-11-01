---
tag: N3XH42KVV3
kind: statement
role: theorem
name: Cohen structure theorem
msc: [13J10, 13H05]
uses: [G9Q61B8A7C, NJ3APQ8BHH, 3E8ZG3NJYZ, 63XXTF6B5M, MGM3CNJW9V, MVGBS3J1P7, 0F6ES3BRYP, 6N3X2QX4W9]
about: [G9Q61B8A7C]
sources:
  - url: https://en.wikipedia.org/wiki/Cohen_structure_theorem
same_as:
  wikidata: Q5141331
  wikipedia: Cohen structure theorem
---

## Statement

Let $(R, \mathfrak m)$ be a [[complete Noetherian local ring|G9Q61B8A7C]] with [[residue field|NJ3APQ8BHH]] $k = R/\mathfrak m$.

1. Suppose that $R$ contains a field. Then $R$ contains a coefficient field, a subfield $K$ such that $K \to R \to k$ is an isomorphism. Moreover $R \cong k[\![X_1, \dots, X_n]\!]/J$, a quotient of a [[formal power series ring|3E8ZG3NJYZ]], for some $n$ and some ideal $J$.
2. If $R$ contains a field and $R$ is a [[regular local ring|63XXTF6B5M]] of [[Krull dimension|MVGBS3J1P7]] $d$, then $R \cong k[\![X_1, \dots, X_d]\!]$.
3. In general, let $C = k$ if $k$ has [[characteristic|0F6ES3BRYP]] $0$. If $k$ has characteristic $p > 0$, let $C$ be a complete [[discrete valuation ring|MGM3CNJW9V]] of characteristic $0$ with maximal ideal $pC$ and residue field $k$. Such a ring exists. Then $R$ is isomorphic to a quotient $C[\![X_1, \dots, X_n]\!]/J$ for some $n$ and some ideal $J$.

## Remarks

The hard part is the existence of a coefficient field, or of a coefficient ring in the general case.
Once it exists, choose generators $x_1, \dots, x_n$ of $\mathfrak m$ and send $X_i$ to $x_i$.
This map from the power series ring is surjective because $R$ is complete and $\mathfrak m$ is finitely generated.
In clause 2 the number of generators can be taken equal to $d$.
Then the kernel is $0$, since a proper quotient of the domain $k[\![X_1, \dots, X_d]\!]$ has dimension less than $d$.
A complete local ring $R$ contains a field if and only if $R$ and $k$ have the same characteristic.
When $k$ is perfect of characteristic $p > 0$, the ring $C$ can be taken to be the ring of [[Witt vectors|6N3X2QX4W9]] $W(k)$; for $k = \F_p$ this is $\Z_p$.
Example: the completion of $k[x, y]_{(x, y)}/(y^2 - x^3)$ at its maximal ideal is $k[\![X, Y]\!]/(Y^2 - X^3)$.

## Explanations

### L1 human

Complete local rings look complicated in general, but the theorem says that each one is a quotient of a power series ring.
So, up to taking a quotient, the only complete local rings are rings of power series in several variables over a field or over a ring like the $p$-adic integers.
For example, the completed local ring at a smooth point of a $d$-dimensional variety over a field $k$ is the power series ring $k[\![X_1, \dots, X_d]\!]$.

### L2 human

Together with the faithful flatness of [[completion|NPF42DJMBX]], the theorem lets one reduce questions about Noetherian local rings to quotients of power series rings, where explicit computation is possible.
It implies, for example, that complete Noetherian local rings are excellent and that they are quotients of regular local rings.
