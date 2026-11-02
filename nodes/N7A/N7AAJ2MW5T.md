---
tag: N7AAJ2MW5T
kind: statement
role: theorem
name: Brouwer fixed-point theorem
msc: [55M20, 54H25]
uses: [0Q0H13G8ZB, 0VGFHTM75Y, JQDHHFXBF3, 68PFSGP39B, Z6JR1GN2RE, 00KAFBR32E, 02AS45T3H9, G44NQXCWT9]
about: [JQDHHFXBF3]
sources:
  - url: https://en.wikipedia.org/wiki/Brouwer_fixed-point_theorem
same_as:
  wikidata: Q1144897
  wikipedia: Brouwer fixed-point theorem
---

## Statement

Let $n \ge 1$ and let $D^n = \set{x \in \R^n : \norm{x} \le 1}$ be the [[closed unit ball|0Q0H13G8ZB]].
Every [[continuous map|0VGFHTM75Y]] $f \colon D^n \to D^n$ has a fixed point: there is $x \in D^n$ with $f(x) = x$.

## Remarks

The idea of the proof: suppose $f(x) \neq x$ for all $x$.
Send $x$ to the point where the ray from $f(x)$ through $x$ leaves the ball; this is a continuous [[retraction|68PFSGP39B]] of $D^n$ onto the sphere $S^{n-1}$ that fixes $S^{n-1}$.
No such retraction exists by the [[no-retraction theorem|Z6JR1GN2RE]], because $H_{n-1}(S^{n-1}) \neq 0$ for $n \ge 2$ while $D^n$ is contractible; for $n = 1$ the [[intermediate value theorem|00KAFBR32E]] applied to $f(x) - x$ suffices.
The theorem is also the case of a closed ball in the [[Lefschetz fixed-point theorem|G44NQXCWT9]], since $L(f) = 1$ for every self-map of a contractible compact polyhedron.
In the language of the [[fixed-point property|JQDHHFXBF3]], it says that $D^n$ has this property.
So does every space homeomorphic to $D^n$, such as every compact [[convex set|02AS45T3H9]] of $\R^n$ with nonempty interior.
Each hypothesis matters: the translation $x \mapsto x + 1$ of the non-compact space $\R$ has no fixed point.
The rotation $z \mapsto -z$ of the circle $S^1$, which is compact but has a hole, has none either.

## Explanations

### L1 human

If you continuously deform a disk and put it back on top of itself, at least one point ends up exactly where it started.
Stirring a cup of coffee gently, without breaking the surface, always leaves some point of the surface in its original place.
The result says nothing about which point it is; it only guarantees that one exists.

### L2 human

The theorem is the basic existence tool behind many other fixed-point results.
Schauder's theorem extends it to compact convex sets in normed spaces, and Kakutani's theorem to set-valued maps, which is how Nash proved the existence of equilibria in games.
Its proofs connect several subjects: degree theory, homology, the no-retraction theorem, and combinatorial arguments through Sperner's lemma.
