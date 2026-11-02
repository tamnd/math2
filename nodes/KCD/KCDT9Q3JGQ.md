---
tag: KCDT9Q3JGQ
kind: statement
role: theorem
name: Sphere eversion
msc: [57R42, 57R52]
uses: [T62369RFH6, 6RW68JGBHC, 0XPR1E85W0]
about: [6RW68JGBHC]
sources:
  - url: https://en.wikipedia.org/wiki/Sphere_eversion
same_as:
  wikidata: Q565198
  wikipedia: Sphere eversion
---

## Statement

Let $S^2 \subseteq \R^3$ be the unit [[sphere|T62369RFH6]], let $\iota \colon S^2 \to \R^3$ be the inclusion and let $\alpha \colon S^2 \to \R^3$ be the map $\alpha(x) = -x$.
Then there is a smooth map $H \colon S^2 \times [0, 1] \to \R^3$ such that each $H_t = H(\cdot, t)$ is an [[immersion|6RW68JGBHC]], $H_0 = \iota$ and $H_1 = \alpha$.

## Remarks

Such a family $H$ is a regular homotopy that turns the sphere inside out: the outward normal of $\iota$ corresponds to the inward normal of $\alpha$.
The surfaces $H_t$ may pass through themselves, but they may never develop a crease or a pinch.
Stephen Smale proved this as a consequence of his classification of immersions of spheres: regular homotopy classes of immersions $S^2 \to \R^3$ correspond to $\pi_2(SO(3))$, which is the trivial group.
The proof was not constructive; explicit eversions were later found, for example by Bernard Morin, and by William Thurston with the method of corrugations.
The analogue for circles fails: by the Whitney–Graustein theorem, immersions $S^1 \to \R^2$ are classified by the turning number, and the standard circle and its reversal have turning numbers $1$ and $-1$.

## Explanations

### L1 human

Imagine a sphere made of a material that can pass through itself but cannot be creased.
The theorem says that such a sphere can be turned inside out by a continuous motion.
The result is surprising, because the obvious attempt, pushing two opposite caps through each other, leaves a sharp ring that cannot be smoothed away.

### L2 human

Sphere eversion is the standard example of the power of the Smale–Hirsch theorem and of the homotopy principle.
It shows that a regular homotopy can connect immersions that look very different.
The only invariants of immersions $S^2 \to \R^3$ up to regular homotopy are homotopy-theoretic, and here they vanish.
Its failure for circles in the plane shows that the outcome depends on the dimensions through the relevant homotopy group.
