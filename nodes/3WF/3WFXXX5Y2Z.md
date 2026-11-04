---
tag: 3WFXXX5Y2Z
kind: proof
name: Proof of the second isomorphism theorem
msc: [20A05]
proves: 0PPP2J2DJV
uses: [0TXWV1JGG1, 0W77CVBCHQ, 0N0PXCTYA7, 0ZTGMDNVTB, 0YYWCNTPWR, 05FD317V2W, 0HV9Y7WG5R, 0Z424HK8CQ, 0CXXJNG5B6]
sources:
  - url: https://proofwiki.org/wiki/Second_Isomorphism_Theorem/Groups
---

## Proof

We apply the first isomorphism theorem to the map $S \to SN/N$, $s \mapsto sN$.

1. Let $G$ be a group with identity $e$, let $S$ be a subgroup of $G$, and let $N$ be a [[normal subgroup|0W77CVBCHQ]] of $G$.
2. By the [[product of a subgroup and a normal subgroup is a subgroup|0TXWV1JGG1]], $SN$ is a subgroup of $G$.
3. Each $n \in N$ equals $en$ with $e \in S$, so $N \subseteq SN$. Thus $N$ is a [[subgroup|0N0PXCTYA7]] of $SN$.
4. For $x \in SN$ and $n \in N$, $xnx^{-1} \in N$ because $N$ is normal in $G$. So $N$ is normal in $SN$, and the [[quotient group|0YYWCNTPWR]] $SN/N$ exists.
5. By [[the intersection of subgroups is a subgroup|0ZTGMDNVTB]], $S \cap N$ is a subgroup of $G$. It lies in $S$, so it is a subgroup of $S$.
6. Let $s \in S$ and $x \in S \cap N$. Then $sxs^{-1} \in S$, since $S$ is a subgroup, and $sxs^{-1} \in N$, since $N$ is normal. So $S \cap N$ is normal in $S$.
7. We record a fact on [[left cosets|05FD317V2W]]: for $a \in SN$, $aN = N$ holds exactly when $a \in N$.
8. Proof of step 7. If $aN = N$, then $a = ae \in aN = N$. If $a \in N$, then $aN \subseteq N$ by closure, and each $m \in N$ equals $a(a^{-1}m) \in aN$.
9. Define $f \colon S \to SN/N$ by $f(s) = sN$. This makes sense because $s = se \in SN$.
10. For $s, t \in S$, $f(st) = (st)N = (sN)(tN) = f(s) f(t)$ by the operation of $SN/N$. So $f$ is a [[group homomorphism|0HV9Y7WG5R]].
11. Let $xN \in SN/N$, with $x = sn$, $s \in S$ and $n \in N$. By step 8, $nN = N$, the identity of $SN/N$. So $xN = (sN)(nN) = sN = f(s)$, and $f$ is surjective.
12. For $s \in S$, $f(s)$ is the identity $N$ exactly when $sN = N$, that is, when $s \in N$ by step 7. So the [[kernel|0Z424HK8CQ]] of $f$ is $S \cap N$.
13. By the [[first isomorphism theorem|0CXXJNG5B6]] and steps 11 and 12, the map $s(S \cap N) \mapsto f(s) = sN$ is an isomorphism from $S/(S \cap N)$ onto $\operatorname{im} f = SN/N$.
14. Steps 2, 4, 6 and 13 give all the claims of the statement.

## Idea

Every coset of $N$ inside $SN$ already has a representative in $S$, because the factor from $N$ can be absorbed into the coset. So $s \mapsto sN$ maps $S$ onto $SN/N$. It forgets exactly the elements of $S$ that lie in $N$, and the first isomorphism theorem turns this into the isomorphism.
