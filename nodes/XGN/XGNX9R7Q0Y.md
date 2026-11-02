---
tag: XGNX9R7Q0Y
kind: statement
role: theorem
name: Stability conjecture
msc: [37C20, 37D20]
uses: [KQX43WB57R, S31RTTJPDC, EY2W34JZA4, EWVATW6EYZ, E1Z444F6TV]
about: [D4MGFAHVMT, Z26Z4XZFVA]
sources:
  - url: https://en.wikipedia.org/wiki/Structural_stability
---

## Statement

Let $M$ be a compact smooth manifold without boundary and let $f \colon M \to M$ be a $C^1$ diffeomorphism, with [[non-wandering set|EY2W34JZA4]] $\Omega(f)$.
Say that $f$ satisfies the strong transversality condition if, for all $x, y \in \Omega(f)$, the stable manifold $W^s(x)$ and the unstable manifold $W^u(y)$ intersect [[transversally|EWVATW6EYZ]].
Then $f$ is [[structurally stable|KQX43WB57R]] in the $C^1$ topology if and only if $f$ satisfies [[Axiom A|S31RTTJPDC]] and the strong transversality condition.

## Remarks

The statement was conjectured by Palis and Smale and is now a theorem.
The direction from Axiom A and strong transversality to structural stability was proved by Robbin for $C^2$ diffeomorphisms and by Robinson in the $C^1$ case.
The converse direction, that $C^1$ structural stability forces Axiom A and strong transversality, was proved by Mañé.
Its proof uses closing-lemma techniques, in particular Mañé's ergodic version of the [[closing lemma|E1Z444F6TV]], and a delicate perturbation argument to obtain hyperbolicity from robustness.
Example: hyperbolic toral automorphisms such as [[Arnold's cat map|BSCZN8Y1AN]] satisfy both conditions, so they are structurally stable.
An irrational rotation of the circle is not structurally stable, as nearby rational rotations have periodic orbits.
Accordingly it does not satisfy Axiom A.
The analogous statement for flows was proved by Hayashi.

## Explanations

### L1 human

A system is structurally stable if small changes of the rule do not change the pattern of its orbits.
The theorem says exactly which systems have this property.
They are the systems that stretch and squeeze uniformly on their recurrent part, and whose stable and unstable directions cross cleanly.
So robustness and hyperbolicity turn out to be the same thing.

### L2 human

The theorem closes a programme started by Smale in the 1960s: to describe the structurally stable systems.
The easy half shows that hyperbolic systems are robust, using the persistence of hyperbolic sets under perturbation.
The hard half shows that robustness forces hyperbolicity; it relies on perturbation tools such as the [[closing lemma|E1Z444F6TV]].
A related result is the $\Omega$-stability theorem, which characterises the stability of the dynamics on $\Omega(f)$ by Axiom A and the absence of cycles.
In the $C^r$ topology with $r \ge 2$ the necessity direction is still open.
