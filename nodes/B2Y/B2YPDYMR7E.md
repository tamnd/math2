---
tag: B2YPDYMR7E
kind: definition
name: Differentially closed field
msc: [12H05, 03C60]
defines: KPCN3KHG50
uses: [GA5PTQGC6G, 3J89REV9WQ, 0PF6TM8TWT]
sources:
  - url: https://en.wikipedia.org/wiki/Differentially_closed_field
---

## Definition

Let $(K, \partial)$ be a [[differential field|GA5PTQGC6G]] of characteristic $0$ with one [[derivation|3J89REV9WQ]] $\partial$.
Let $K\{y\}$ be the ring of differential polynomials over $K$.
It is the polynomial ring $K[y, y', y'', \dots]$ in the variables $y^{(k)}$, $k \ge 0$, with $\partial$ extended by $\partial(y^{(k)}) = y^{(k+1)}$.
The *order* of $f \in K\{y\}$ is the largest $k$ such that $y^{(k)}$ occurs in $f$; a nonzero element of $K$ has order $-1$.
For $a \in K$, $f(a)$ is the element obtained by replacing each $y^{(k)}$ by $\partial^k a$.
Let $f, g \in K\{y\}$ be nonzero, with the order of $g$ less than the order of $f$.
The field $K$ is *differentially closed* if, for all such $f$ and $g$, there is $a \in K$ with $f(a) = 0$ and $g(a) \ne 0$.

## Remarks

Taking $f$ of order $0$, that is $f \in K[y]$ nonconstant, and $g = 1$ shows that a differentially closed field is [[algebraically closed|0PF6TM8TWT]].
Its field of constants $\set{c \in K : \partial c = 0}$ is also algebraically closed.
Every differential field of characteristic $0$ is contained in a differentially closed field, and it has a differential closure, which is unique up to isomorphism over it.
The theory $\mathrm{DCF}_0$ of differentially closed fields of characteristic $0$ is complete, has elimination of quantifiers and is $\omega$-stable.

Example: by the existence result above, the differential closure of $(\Q, 0)$ is a differentially closed field.
Differentially closed fields are known through such existence results rather than by explicit construction.

Non-example: $\C(x)$ with $\partial = d/dx$ is not differentially closed.
Take $f = x y' - 1$, of order $1$, and $g = 1$, of order $-1$.
A solution would be $a \in \C(x)$ with $a' = 1/x$, and no rational function has this derivative.

Non-example: a field with the zero derivation is not differentially closed, since $f = y' - 1$ has no zero in it.
