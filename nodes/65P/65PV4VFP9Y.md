---
tag: 65PV4VFP9Y
kind: conjecture
name: Schanuel's conjecture
msc: [11J81, 11J85]
uses: [07GJV36896, 0CRMGPAH83, 0VTQXTCR2G]
about: [0VTQXTCR2G, 07GJV36896]
sources:
  - url: https://en.wikipedia.org/wiki/Schanuel%27s_conjecture
same_as:
  wikidata: Q1579982
  wikipedia: Schanuel's conjecture
history:
  posed_by: "Stephen Schanuel"
---

## Statement

Let $z_1, \dots, z_n$ be complex numbers that are [[linearly independent|0CRMGPAH83]] over $\Q$.
Then the field $\Q(z_1, \dots, z_n, e^{z_1}, \dots, e^{z_n})$ has transcendence degree at least $n$ over $\Q$.
Here $e^{z}$ is the [[complex exponential|07GJV36896]].
The transcendence degree of a field $K \supseteq \Q$ is the largest number of elements of $K$ that are algebraically independent over $\Q$.

## Remarks

The conjecture is open.
The case $n = 1$ is known: if $z \ne 0$, then $z$ or $e^z$ is [[transcendental|0VTQXTCR2G]], which is the Hermite–Lindemann theorem.
If $z_1, \dots, z_n$ are algebraic, the conjecture gives the [[Lindemann–Weierstrass theorem|0JNCBFMPXR]], which is proved.
With $z_1 = 1$ and $z_2 = i\pi$, it would imply that $e$ and $\pi$ are algebraically independent; it is not even known whether $e + \pi$ is irrational.
It would also imply the [[Gelfond–Schneider theorem|RN58Z2NWAC]] and [[Baker's theorem|WMBJSNG57F]], and even that $\Q$-linearly independent logarithms of algebraic numbers are algebraically independent.

## Explanations

### L1 human

Take numbers $z_1, \dots, z_n$ with no rational linear relation among them, together with their exponentials.
The conjecture says that among these $2n$ numbers, at least $n$ are transcendental and free of any polynomial relation.
It is a single statement that would contain most known transcendence results and many famous open ones.
