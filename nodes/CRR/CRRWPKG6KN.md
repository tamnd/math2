---
tag: CRRWPKG6KN
kind: proof
name: Proof of the number of functions between finite sets
msc: [05A05]
proves: 08QQH9F7G0
uses: [05099E1NMJ, 0XHDTE5YMZ, 0D2MXBV21T, 0SNQEF7Z53, 0VPK4X73Q0, 0GV2573FP4, 01FPXMTBX1, 07EH4R3RVQ]
methods: [0ASJVEFA9J]
sources:
  - url: https://proofwiki.org/wiki/Cardinality_of_Set_of_All_Mappings
---

## Proof

Fix $B$ with $|B| = n$. We argue by induction on $m = |A|$ that $B^A$ is finite with $n^m$ elements.

1. Let $m = 0$. Then $A = \varnothing$. A [[function|0XHDTE5YMZ]] from $\varnothing$ to $B$ has the empty graph, so there is exactly one. Thus $|B^A| = 1 = n^0$.
2. Suppose the claim holds for all sets with $m$ elements. Let $|A| = m + 1$, with a [[bijection|0SNQEF7Z53]] $f : \set{1, \dots, m+1} \to A$.
3. Put $a = f(m+1)$ and $A' = A \setminus \set{a}$. The restriction of $f$ to $\set{1, \dots, m}$ is a bijection onto $A'$. So $|A'| = m$.
4. Define $\Phi : B^A \to B^{A'} \times B$ by $\Phi(\varphi) = (\varphi|_{A'}, \varphi(a))$, where $\varphi|_{A'}$ is the [[restriction|0D2MXBV21T]] of $\varphi$ to $A'$.
5. Define $\Psi : B^{A'} \times B \to B^A$ as follows. For $\psi : A' \to B$ and $b \in B$, let $\Psi(\psi, b)$ send each $x \in A'$ to $\psi(x)$ and send $a$ to $b$.
6. This defines a function on $A$, because each element of $A$ is either in $A'$ or equal to $a$, and not both.
7. The maps are mutually inverse. Indeed, $\Psi(\Phi(\varphi))$ agrees with $\varphi$ on $A'$ and at $a$, and $\Phi(\Psi(\psi, b)) = (\psi, b)$.
8. By the induction hypothesis, $|B^{A'}| = n^m$. By the [[rule of product|0VPK4X73Q0]], $B^{A'} \times B$ is finite with $n^m \cdot n = n^{m+1}$ elements.
9. The map $\Psi$ is a bijection onto $B^A$. Composing it with a numbering of $B^{A'} \times B$ gives a bijection from $\set{1, \dots, n^{m+1}}$ to $B^A$.
10. A composite of bijections is a bijection, since [[injections compose|01FPXMTBX1]] and [[surjections compose|07EH4R3RVQ]]. So $|B^A| = n^{m+1}$, as the [[bijection principle|0GV2573FP4]] also states. This completes the induction.

## Idea

A function on $A$ is the same as a function on $A$ minus one point, together with the value at that point.
So adding one point to the domain multiplies the count by $n$, the number of possible values.
Starting from the single empty function, we get $n^m$.
