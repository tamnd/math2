---
tag: TS9TBY8ES1
kind: statement
role: lemma
name: Lindelöf's maximum principle
msc: [31A05, 30C80]
uses: [Z1MHMGFNFW, 0Q4CBD3HX0, 9XJ5FBQD7M, FYR6V2NH6C, XBM7J5R1VQ, C95QJ7YH5T]
about: [Z1MHMGFNFW]
sources:
  - url: https://en.wikipedia.org/wiki/Phragm%C3%A9n%E2%80%93Lindel%C3%B6f_principle
---

## Statement

Let $\Omega \subset \C$ be a bounded [[domain|0Q4CBD3HX0]] and let $F \subset \partial\Omega$ be a finite set.
Let $u$ be a [[subharmonic function|Z1MHMGFNFW]] on $\Omega$ that is bounded above.
Assume that $\limsup_{z \to \zeta} u(z) \le 0$ for every $\zeta \in \partial\Omega \setminus F$.
Then $u \le 0$ on $\Omega$.

## Remarks

Proof idea: let $d$ be the diameter of $\Omega$ and let $\varepsilon > 0$.
The function $v = u + \varepsilon \sum_{p \in F} \log(\abs{z - p}/d)$ is subharmonic, and $v \le u$ on $\Omega$ because each logarithm is negative there.
At each $p \in F$, $v \to -\infty$ since $u$ is bounded above; so $\limsup v \le 0$ at every boundary point.
The [[maximum principle for subharmonic functions|9XJ5FBQD7M]] gives $v \le 0$, and letting $\varepsilon \to 0$ gives $u \le 0$.
The bound from above is needed.
On the punctured disc $\Omega = \set{0 < \abs{z} < 1}$ with $F = \set{0}$, the function $u(z) = -\log\abs{z}$ is harmonic, tends to $0$ on the unit circle, and is positive on $\Omega$.
The finite set $F$ may be replaced by any [[polar set|C95QJ7YH5T]] in $\partial\Omega$, with the same conclusion.

## Explanations

### L1 human

The ordinary maximum principle needs control at every boundary point.
This version says that finitely many bad boundary points do not matter, provided the function cannot blow up there.

### L2 human

The lemma is the bounded form of the [[Phragmén–Lindelöf principle|FYR6V2NH6C]]: a growth condition lets one ignore a small part of the boundary.
Applied to $\log\abs{f}$ for a bounded holomorphic $f$, it shows that $\abs{f} \le 1$ on $\Omega$ when $\limsup \abs{f} \le 1$ at all but finitely many boundary points.
A related result for holomorphic functions on a half-strip is [[Lindelöf's theorem|XBM7J5R1VQ]].
In the study of harmonic measure the lemma shows that finite sets of boundary points carry no mass.
