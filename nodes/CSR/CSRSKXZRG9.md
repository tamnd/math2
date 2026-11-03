---
tag: CSRSKXZRG9
kind: statement
role: theorem
name: Excision in algebraic K-theory
msc: [19A49, 19B99]
uses: [0B1261B5ED, 0VTH8KPCG2, 096Z9MP2ME, GYK9TGKG77, Q14JS2MA1C]
about: [GYK9TGKG77, Q14JS2MA1C]
sources:
  - url: https://en.wikipedia.org/wiki/Excision_theorem
---

## Statement

Let $f \colon R \to S$ be a [[ring homomorphism|0VTH8KPCG2]] of [[rings|0B1261B5ED]] with identity.
Let $I$ be an [[ideal|096Z9MP2ME]] of $R$ such that $f$ maps $I$ bijectively onto an ideal $f(I)$ of $S$.
Then $f$ induces an isomorphism of [[relative K-groups|GYK9TGKG77]]
$$K_0(R, I) \xrightarrow{\ \cong\ } K_0(S, f(I)).$$

## Remarks

Let $D(R, I) = \set{(a, b) \in R \times R : a - b \in I}$ be the double of $R$ along $I$.
Then $K_0(R, I)$ is the kernel of the map $K_0(D(R, I)) \to K_0(R)$ induced by the first projection, on the [[K0|Q14JS2MA1C]] groups.
The idea of the proof: $K_0(R, I)$ can be described by idempotent matrices over the ring $\Z \oplus I$ obtained by adjoining a unit to $I$.
So it depends only on $I$ as a ring without unit.
Example: for $R = k[t^2, t^3] \subseteq S = k[t]$ and $I = t^2 k[t]$, an ideal of both rings, it gives $K_0(R, I) \cong K_0(S, I)$.
The analogue for $K_1$ fails in general: the map $K_1(R, I) \to K_1(S, f(I))$ is surjective, but Swan gave examples where it is not injective.
This failure is why the Mayer–Vietoris sequence of a Milnor square stops at $K_1$.

## Explanations

### L1 human

Excision says that a relative invariant depends only on the part being cut out, not on the rest of the ring.
For $K_0$, the relative group of an ideal does not change when the ideal sits inside a different ring.
For $K_1$ this is no longer true, which is one of the first signs that higher algebraic K-theory is subtle.

### L2 human

In topology, excision for homology lets one compute relative groups locally.
In algebraic K-theory, $K_0$ and negative K-theory satisfy excision, while $K_1$ and higher groups do not in general.
The failure of excision for $K_1$ and $K_2$ is measured by obstruction groups, and Suslin and Wodzicki characterised the ideals for which rational excision holds.
Excision for $K_0$ gives the exactness of the $K_0$ part of the Mayer–Vietoris sequence for the square formed by $R \subseteq S$ and a common ideal $I$.
