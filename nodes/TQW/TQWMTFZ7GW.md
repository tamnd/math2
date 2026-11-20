---
tag: TQWMTFZ7GW
kind: proof
name: Proof that the open elements of an interior algebra form a Heyting algebra
msc: ["06E25", "06D20"]
topics: [QYA4H5Y7VR]
audience: research
proves: KCDVRED7B2
uses: [7X1HGZ6FK0, BND6A96S3D, 0XADJKM699, 0HM0HQCK6N]
methods: [0NTF6DMVAP, TFQ1845T84, S3QADD13E9]
sources:
  - url: https://en.wikipedia.org/wiki/Interior_algebra
    locator: Open and closed elements
  - url: https://en.wikipedia.org/wiki/Heyting_algebra
    locator: Formal definition
---

## Proof

Let $(B, I)$ be an [[interior algebra|7X1HGZ6FK0]], with axioms (I1) $I1 = 1$, (I2) $Ix \le x$, (I3) $IIx = Ix$, (I4) $I(x \land y) = Ix \land Iy$.

**Part A: $I$ is monotone and $I0 = 0$.**

1. Let $x \le y$. Then $x = x \land y$.
2. So $Ix = I(x \land y) = Ix \land Iy$ by (I4), and therefore $Ix \le Iy$.
3. By (I2), $I0 \le 0$, so $I0 = 0$.

**Part B: $B^\circ$ is a bounded sublattice.**

4. $1 \in B^\circ$ by (I1), and $0 \in B^\circ$ by step 3.
5. Let $x, y \in B^\circ$. By (I4), $I(x \land y) = Ix \land Iy = x \land y$, so $x \land y \in B^\circ$.
6. Also $x \le x \lor y$, so $x = Ix \le I(x \lor y)$ by step 2; in the same way $y \le I(x \lor y)$.
7. So $x \lor y \le I(x \lor y)$, and $I(x \lor y) \le x \lor y$ by (I2).
8. So $I(x \lor y) = x \lor y$, and $x \lor y \in B^\circ$.
9. Hence $B^\circ$ is a sublattice of $B$ with $0$ and $1$, and it is [[distributive|0HM0HQCK6N]], because $B$ is.

**Part C: residuation in $B$.**

10. Claim: for all $z, x, y \in B$, $z \land x \le y$ iff $z \le \neg x \lor y$.
11. If $z \land x \le y$, then $z = (z \land x) \lor (z \land \neg x) \le y \lor \neg x$, by distributivity and $x \lor \neg x = 1$.
12. If $z \le \neg x \lor y$, then $z \land x \le (\neg x \land x) \lor (y \land x) = y \land x \le y$.

**Part D: the implication of $B^\circ$.**

13. Let $x, y \in B^\circ$, and put $x \Rightarrow y = I(\neg x \lor y)$.
14. By (I3), $I(x \Rightarrow y) = x \Rightarrow y$, so $x \Rightarrow y \in B^\circ$.
15. Let $z \in B^\circ$ with $z \land x \le y$. By step 10, $z \le \neg x \lor y$.
16. By step 2, $z = Iz \le I(\neg x \lor y) = x \Rightarrow y$.
17. Conversely, let $z \le x \Rightarrow y$. By (I2), $z \le \neg x \lor y$.
18. By step 10, $z \land x \le y$.
19. So for all $z, x, y \in B^\circ$: $z \le x \Rightarrow y$ iff $z \land x \le y$.
20. By steps 9 and 19 and the [[definition of a Heyting algebra|BND6A96S3D]], $B^\circ$ is a Heyting algebra.
21. Its pseudocomplement is $x \Rightarrow 0 = I(\neg x \lor 0) = I \neg x$. $\blacksquare$

## Idea

Open elements are closed under finite meets by (I4), and under finite joins because $I$ is monotone and decreasing.
In $B$ the Boolean element $\neg x \lor y$ is the largest $z$ with $z \land x \le y$.
Its interior is the largest open such $z$, and (I3) makes it open.

## Variants

1. Topological form: in a space $X$, the open sets are closed under finite intersections and arbitrary unions, and $U \Rightarrow V$ is the union of all open $W$ with $W \cap U \subseteq V$.
   This is the interior of $(X \setminus U) \cup V$, by the same argument.
2. Lattice form: a complete lattice in which finite meets distribute over arbitrary joins is a Heyting algebra, and $B^\circ$ of a complete interior algebra is such a lattice.
