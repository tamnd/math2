---
tag: Q630X0VHAE
kind: statement
role: theorem
name: Property P conjecture
msc: [57K10, 57K30]
uses: [QYEAZTYGPT, ZA405B0Z1S]
about: [QYEAZTYGPT, ZA405B0Z1S]
sources:
  - url: https://en.wikipedia.org/wiki/Property_P_conjecture
same_as:
  wikidata: Q7250222
  wikipedia: Property P conjecture
---

## Statement

Let $K \subset S^3$ be a tame [[knot|QYEAZTYGPT]] that is not the unknot.
Let $r = p/q \in \mathbb{Q}$ be a slope other than $\infty = 1/0$, and let $S^3_r(K)$ be the result of [[Dehn surgery|ZA405B0Z1S]] on $K$ with slope $r$.
Then $S^3_r(K)$ is not simply connected.

## Remarks

The homology of $S^3_{p/q}(K)$ is $\Z / p$, or $\Z$ when $p = 0$, so it is nontrivial unless $p = \pm 1$.
The content of the theorem is therefore about the slopes $r = \pm 1/q$.
Kronheimer and Mrowka proved it in 2004 using instanton Floer homology and work on taut foliations and contact structures.
With the Poincaré conjecture, proved by Perelman, it also follows from the Gordon–Luecke result that a nontrivial surgery on a nontrivial knot never gives $S^3$.
The hypothesis that $K$ is knotted is needed: $1/q$ surgery on the unknot gives $S^3$.
Example: $+1$ surgery on the right-handed trefoil gives the [[Poincaré homology sphere|NHERCK7C43]], up to orientation, which has the same homology as $S^3$ but a fundamental group of order $120$.

## Explanations

### L1 human

Dehn surgery cuts out a thickened knot from space and glues it back in a twisted way, making a new three-dimensional space.
For the unknot, some twists give back the $3$-sphere.
The theorem says that for a genuine knot, every twisted regluing gives a space with a loop that cannot be shrunk.
So surgery on a real knot always leaves a trace in the fundamental group.

### L2 human

By the [[Lickorish–Wallace theorem|1YP4RF1QXV]] every closed orientable $3$-manifold arises by surgery on a link, so it is natural to ask what surgery on a single knot can produce.
Property P says that, apart from the slope $\infty$ which gives back $S^3$, it never produces a fake or real $3$-sphere.
It implies the key step of the [[Gordon–Luecke theorem|EBASBW5TYS]], that nontrivial surgery on a nontrivial knot never gives $S^3$.
Conversely, that step together with the Poincaré conjecture implies Property P.
The proof by Kronheimer and Mrowka shows that the fundamental group of $S^3_{\pm 1/q}(K)$ has a nontrivial representation into $SU(2)$.
