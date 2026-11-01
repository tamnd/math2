---
tag: WX0HMW4GT7
kind: statement
role: theorem
name: Koebe quarter theorem
msc: [30C25, 30C55]
uses: [R91E83SDBD, 8G5ABXRK85, EZQFWKF03Q, BYZDAZNHP4]
about: [R91E83SDBD]
sources:
  - url: https://en.wikipedia.org/wiki/Koebe_quarter_theorem
same_as:
  wikidata: Q588218
  wikipedia: Koebe quarter theorem
---

## Statement

Let $\mathbb{D}$ be the [[unit disc|8G5ABXRK85]], and let $f \colon \mathbb{D} \to \C$ be a [[univalent function|R91E83SDBD]].
Then the image $f(\mathbb{D})$ contains the open disc with centre $f(0)$ and radius $\abs{f'(0)}/4$.

## Remarks

After replacing $f$ by $(f - f(0))/f'(0)$, one may assume $f(z) = z + a_2 z^2 + \cdots$ is in the class $S$.
If $w \notin f(\mathbb{D})$, then $g = wf/(w - f)$ is again in $S$, and its second coefficient is $a_2 + 1/w$.
Bieberbach's inequality $\abs{a_2} \le 2$ for functions in $S$, which follows from the [[Grönwall area theorem|BYZDAZNHP4]], gives $\abs{a_2 + 1/w} \le 2$ and $\abs{a_2} \le 2$, hence $\abs{1/w} \le 4$, that is, $\abs{w} \ge 1/4$.
The constant $1/4$ is sharp: the [[Koebe function|EZQFWKF03Q]] $k(z) = z/(1-z)^2$ is in $S$ and omits the value $-1/4$.
Injectivity is necessary: $f(z) = (e^{Nz} - 1)/N$ has $f(0) = 0$ and $f'(0) = 1$, but omits the value $-1/N$, which is close to $0$ for large $N$.

## Explanations

### L1 human

A univalent function on the unit disc cannot squeeze its image too much near the image of the centre.
After normalising so that $f(0) = 0$ and $f'(0) = 1$, the image always contains the disc of radius $1/4$ around $0$.
The Koebe function shows that a quarter is the best one can say.

### L2 human

The theorem is the basic covering theorem of univalent function theory.
It gives the distance estimate $\frac{1}{4}\abs{f'(z)}(1 - \abs{z}^2) \le \operatorname{dist}(f(z), \partial f(\mathbb{D})) \le \abs{f'(z)}(1 - \abs{z}^2)$ for univalent $f$, where the upper bound comes from the Schwarz lemma.
This compares the hyperbolic metric of a simply connected domain with the reciprocal of the distance to its boundary, up to a factor $4$.
Together with the Koebe distortion theorem, it gives the compactness of the class $S$ in the topology of locally uniform convergence.
For maps that need not be injective, [[Bloch's theorem|KW31KDX7TB]] gives a much weaker covering result.
