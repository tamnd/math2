---
tag: NRNWR47MF1
kind: proof
name: Proof that the order of a finite field is a prime power
msc: ["12E20"]
proves: 0H5WWC8RZX
uses: [08RTDHX1SK, 0P7CH1CND5, 00758QM6JJ, 0GGE0Z0JQ1, 0ZMYX7GMH0, 0VPFBAY7MW, 0GS74FGFEK, 0VTQTPQGAV]
sources:
  - url: https://en.wikipedia.org/wiki/Finite_field
    locator: Properties
---

## Proof

1. Let $F$ be a [[finite field|08RTDHX1SK]], with zero $0$ and identity $1$. For an integer $k$, write $k \cdot 1$ for the $k$-fold sum of $1$, and its negative when $k < 0$.
2. The map $\chi \colon \Z \to F$, $k \mapsto k \cdot 1$, is a [[ring homomorphism|0GGE0Z0JQ1]].
3. The set $\Z$ is infinite and $F$ is finite, so $\chi$ is not injective. So there are integers $j < k$ with $j \cdot 1 = k \cdot 1$, and then $(k - j) \cdot 1 = 0$ with $k - j > 0$.
4. So the [[characteristic|0P7CH1CND5]] of $F$ is a positive integer $p$. A field is an integral domain, so [[$p$ is a prime number|00758QM6JJ]].
5. The kernel of $\chi$ is the ideal of the integers $k$ with $k \cdot 1 = 0$. It contains $p$. If $k = sp + r$ with $0 \le r < p$ is in it, then $r \cdot 1 = 0$, so $r = 0$ by the minimality of $p$. So the kernel is $p\Z$.
6. By the [[first isomorphism theorem for rings|0ZMYX7GMH0]], the image $P = \chi(\Z)$ is a subring of $F$ isomorphic to $\Z/p\Z = \F_p$. So $P$ is a field with $p$ elements.
7. Every subfield of $F$ contains $1$, hence all the elements $k \cdot 1$, hence $P$. So $P$ is the [[prime subfield|0VPFBAY7MW]] of $F$, and we identify it with $\F_p$.
8. The field $F$ is a vector space over $P$. It is spanned by the finite set $F$, so it has a finite [[basis|0VTQTPQGAV]] $b_1, \dots, b_n$. Here $n = [F : \F_p]$ is the [[degree|0GS74FGFEK]].
9. Each element of $F$ is $c_1 b_1 + \dots + c_n b_n$ for exactly one tuple $(c_1, \dots, c_n) \in P^n$, because $b_1, \dots, b_n$ is a basis.
10. There are $p^n$ such tuples. So $\abs{F} = p^n$ with $n = [F : \F_p]$.

## Idea

A finite field cannot contain an infinite copy of $\Z$, so some multiple of $1$ is zero and the characteristic is a prime $p$. The multiples of $1$ form a copy of $\F_p$, and the whole field is a finite-dimensional vector space over it. Counting coordinates gives $p^n$ elements.
