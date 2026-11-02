---
tag: V6XSDT5C21
kind: statement
role: theorem
name: Josefson's theorem
msc: [32U15, 32U05]
uses: [N0MAGPW8AP, FF2P7ER3QT, X4ZHQG9995, QBJ9R06GYE]
about: [N0MAGPW8AP]
sources:
  - url: https://en.wikipedia.org/wiki/Pluripolar_set
---

## Statement

Let $E \subseteq \C^n$ be a [[pluripolar set|N0MAGPW8AP]], that is, locally contained in the $-\infty$ set of a [[plurisubharmonic function|FF2P7ER3QT]].
Then there is a plurisubharmonic function $u$ on $\C^n$, not identically $-\infty$, such that
$$E \subseteq \set{z \in \C^n : u(z) = -\infty}.$$

## Remarks

The theorem was proved by Bo Josefson in 1978.
Proofs build $u$ as a convergent series $\sum_j \varepsilon_j u_j$ of functions of the [[Lelong class|X4ZHQG9995]], with growth estimates that come from the [[Siciak extremal function|QBJ9R06GYE]] of compact pieces of $E$.
A consequence is that a countable union of pluripolar sets is pluripolar, since a suitable series of global functions works for the union.
For example, if $E$ is the union of the lines $\set{z_1 = 1/k}$, $k \ge 1$, in $\C^2$, then each line is pluripolar, and the theorem gives one global function for the whole union.
For $n = 1$ the statement is the classical fact that a locally polar set in $\C$ is polar.

## Explanations

### L1 human

A set is pluripolar if near each of its points it is hidden in the $-\infty$ set of some plurisubharmonic function.
The theorem says that one can then hide the whole set at once in the $-\infty$ set of a single plurisubharmonic function on all of $\C^n$.
So "small locally" and "small globally" mean the same thing.

### L2 human

Without the theorem, one would need two notions of pluripolarity, local and global, and many arguments in pluripotential theory would have to track which one is meant.
The global function $u$ may be chosen of logarithmic growth, $u(z) \le \log(1 + \abs{z}) + C$, which connects pluripolar sets with polynomial approximation through the Siciak extremal function.
Bedford and Taylor proved that pluripolar sets are exactly the sets of zero Monge–Ampère capacity.
Together with Josefson's theorem, this gives a complete description of the negligible sets of the theory.
