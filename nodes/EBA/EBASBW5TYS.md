---
tag: EBASBW5TYS
kind: statement
role: theorem
name: Gordon–Luecke theorem
msc: [57K10, 57K30]
uses: [QYEAZTYGPT, 0QT00PB5G2]
about: [QYEAZTYGPT]
sources:
  - url: https://en.wikipedia.org/wiki/Gordon%E2%80%93Luecke_theorem
same_as:
  wikidata: Q5586065
  wikipedia: Gordon–Luecke theorem
---

## Statement

Let $K$ and $K'$ be tame [[knots|QYEAZTYGPT]] in $S^3$.
Suppose that there is a [[homeomorphism|0QT00PB5G2]] $S^3 \setminus K \to S^3 \setminus K'$.
Then there is a homeomorphism $h \colon S^3 \to S^3$ with $h(K) = K'$.

## Remarks

The proof reduces the theorem to a statement about [[Dehn surgery|ZA405B0Z1S]].
A homeomorphism of complements that does not carry meridian to meridian would give a nontrivial surgery on $K'$ that yields $S^3$.
Gordon and Luecke showed that a nontrivial Dehn surgery on a nontrivial knot never gives $S^3$, using a careful study of the graphs formed by intersecting planar surfaces.
The homeomorphism $h$ may reverse orientation, so a knot and its mirror image have homeomorphic complements and count as equivalent here.
The analogue for links fails: twisting a link along an unknotted component changes the link but not the homeomorphism type of its complement.
The [[knot group|AQVHM3FP0D]] alone does not determine the knot: the square knot and the granny knot have isomorphic groups but are different knots.

## Explanations

### L1 human

Remove a knot from space and keep the space that is left.
The theorem says that this leftover space remembers the knot completely.
If two knots leave behind the same space, up to stretching, then the knots themselves are the same, up to mirror image.
So questions about knots can be turned into questions about $3$-manifolds.

### L2 human

The theorem justifies studying a knot through its complement, for instance through the hyperbolic structure of the complement of a [[hyperbolic knot|K47G2Q24DT]].
Combined with Mostow–Prasad rigidity, it shows that a hyperbolic knot is determined by the isometry type of its complement.
It is close to the Property P question: both are about which surgeries on a knot can give simple manifolds.
For links, and for knots in other $3$-manifolds, the complement can lose information.
