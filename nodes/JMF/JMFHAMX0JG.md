---
tag: JMFHAMX0JG
kind: definition
name: Tarski's axioms
msc: [51M05, 03B30, 03B25]
defines: 14DWEDXWCC
uses: [CE8GX6ADZS, 92SWXST1ZM, 655K8Y7VS8, DDY3Q3PJ6W]
sources:
  - url: https://en.wikipedia.org/wiki/Tarski%27s_axioms
---

## Definition

The language has variables for points and two relations.
The ternary relation $B(x, y, z)$ reads "$y$ lies [[between|CE8GX6ADZS]] $x$ and $z$".
The quaternary relation $xy \equiv zw$ reads "the segment $xy$ is congruent to the segment $zw$".
*Tarski's axioms* are the following first-order sentences, each universally closed.

1. Reflexivity of congruence: $xy \equiv yx$.
2. Identity of congruence: if $xy \equiv zz$, then $x = y$.
3. Transitivity of congruence: if $xy \equiv zu$ and $xy \equiv vw$, then $zu \equiv vw$.
4. Identity of betweenness: if $B(x, y, x)$, then $x = y$.
5. Pasch: if $B(x, u, z)$ and $B(y, v, z)$, then there is $a$ with $B(u, a, y)$ and $B(v, a, x)$.
6. Continuity, a schema: let $\varphi(x)$ and $\psi(y)$ be formulas in which $a$ and $b$ are not free. If some $a$ has $B(a, x, y)$ whenever $\varphi(x)$ and $\psi(y)$, then some $b$ has $B(x, b, y)$ whenever $\varphi(x)$ and $\psi(y)$.
7. Lower dimension: there are $a, b, c$ such that none of $B(a, b, c)$, $B(b, c, a)$, $B(c, a, b)$ holds.
8. Upper dimension: if $xu \equiv xv$, $yu \equiv yv$, $zu \equiv zv$ and $u \ne v$, then $B(x, y, z)$ or $B(y, z, x)$ or $B(z, x, y)$.
9. Euclid: if $B(x, u, t)$, $B(y, u, z)$ and $x \ne u$, then there are $v, w$ with $B(x, y, v)$, $B(x, z, w)$ and $B(v, t, w)$.
10. Five segments: if $x \ne y$, $B(x, y, z)$, $B(x', y', z')$, $xy \equiv x'y'$, $yz \equiv y'z'$, $xu \equiv x'u'$ and $yu \equiv y'u'$, then $zu \equiv z'u'$.
11. Segment construction: for all $x, y, a, b$ there is $z$ with $B(x, y, z)$ and $yz \equiv ab$.

## Remarks

Example: the plane $\R^2$, with $B(x, y, z)$ meaning that $y$ is on the closed segment $[x, z]$ and $xy \equiv zw$ meaning $\abs{x - y} = \abs{z - w}$, satisfies all eleven axioms.
Non-example: the line $\R$ with the same relations fails the lower dimension axiom, since of any three reals one lies between the other two.
The models are exactly the planes $K^2$ over [[real closed fields|DDY3Q3PJ6W]] $K$, with the relations defined as in $\R^2$.
The [[theory|92SWXST1ZM]] they define is [[complete|655K8Y7VS8]] and decidable.
Axiom 9 is a form of the parallel postulate; without it one gets an axiom system for absolute geometry.
