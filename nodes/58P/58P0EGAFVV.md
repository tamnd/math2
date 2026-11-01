---
tag: 58P0EGAFVV
kind: statement
role: theorem
name: Artin–Schreier theorem
msc: ["12D15", 12J15]
uses: [0QA8CHH8MG, 0MCXX29HWY, 0GS74FGFEK, 778KFSM09P, 1ZB13N78XW, 0JP0W07Y9A, X32TSWJSYT]
about: [778KFSM09P, 0X6AB5P3G1]
sources:
  - url: https://en.wikipedia.org/wiki/Real_closed_field
---

## Statement

Let $F$ be a [[field|0QA8CHH8MG]] and let $C$ be an [[algebraic closure|0MCXX29HWY]] of $F$.
Suppose that the [[degree|0GS74FGFEK]] $[C : F]$ is finite and greater than $1$.
Then $[C : F] = 2$, the field $F$ has [[characteristic|1ZB13N78XW]] $0$, $F$ is [[real closed|778KFSM09P]], and $C = F(i)$ with $i^2 = -1$.

## Remarks

The proof uses Galois theory on the finite extension $C/F$.
One first shows that $C/F$ is separable, so that $C/F$ is a finite Galois extension.
In characteristic $p$ such an extension of degree greater than $1$ cannot exist, by an argument with the roots of $x^p - x - a$.
In characteristic $0$, one shows that $i \notin F$, that $C = F(i)$, and that $-1$ is not a sum of squares in $F$, by studying cyclic subextensions of prime degree.
Example: $F = \R$ and $C = \C$, where $[\C : \R] = 2$, as the [[fundamental theorem of algebra|0JP0W07Y9A]] says.
Without the finiteness hypothesis nothing of this kind holds: for $F = \Q$, the degree $[\overline{\Q} : \Q]$ is infinite.

## Explanations

### L1 human

The theorem says that the pair $\R \subset \C$ is the only kind of example where a field is a finite step away from being algebraically closed.
If finitely many new elements make a field algebraically closed, then one square root of $-1$ is enough, and the field behaves like the real numbers.

### L2 human

In terms of Galois groups: a field whose absolute Galois group is finite and nontrivial has absolute Galois group of order $2$, and it is real closed.
So the only nontrivial finite subgroups of absolute Galois groups have order $2$, and they come from orderings of the field.
The theorem is part of the theory of real closed fields developed by Artin and Schreier.
That theory also shows that a field can be ordered if and only if it is [[formally real|X32TSWJSYT]].
