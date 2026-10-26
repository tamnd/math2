---
tag: 03YEM7JEDN
kind: statement
role: theorem
name: Open mapping theorem
aliases: [open-mapping-theorem-complex-analysis]
msc: [30A99]
uses: [0DG0Z72CQD, 097KNJFJ7V]
sources:
  - url: https://en.wikipedia.org/wiki/Open_mapping_theorem_(complex_analysis)
    locator: lead section
  - url: https://en.wikipedia.org/wiki/Open_mapping_theorem_(complex_analysis)
    locator: Proof
same_as:
  wikidata: Q967972
  wikipedia: Open mapping theorem (complex analysis)
---

## Statement

Let $D \subseteq \mathbb{C}$ be a [[domain|097KNJFJ7V]] and let $f : D \to \mathbb{C}$ be [[holomorphic|0DG0Z72CQD]] on $D$.
Assume that $f$ is not constant on $D$.
Then $f$ is an open map: for each open set $V \subseteq D$, the image $f(V)$ is an open subset of $\mathbb{C}$.

## Remarks

The [[maximum modulus principle|048F2P90WR]] follows. If $|f|$ had a local maximum at $z_0$, then $f$ would map a small disc around $z_0$ onto a set that contains no disc around $f(z_0)$.
The connectedness of $D$ matters only to exclude functions that are constant on one part of $D$.
There is no real analogue: $x \mapsto x^2$ maps $(-1, 1)$ onto $[0, 1)$, which is not open in $\mathbb{R}$. In contrast, $z \mapsto z^2$ maps the unit disc onto the unit disc.

## Explanations

### L1 human

A nonconstant holomorphic function never squeezes an open set into a curve or a point.
Around each point of the image, the image also contains a small disc.
