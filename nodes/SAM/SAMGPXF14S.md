---
tag: SAMGPXF14S
kind: proof
name: Proof that a finite field of order q is the splitting field of x^q - x
msc: ["12E20"]
proves: 0CDAHW576M
uses: [08RTDHX1SK, 0H5WWC8RZX, 0VPFBAY7MW, 0QWR8WTZEW, 0SHMC00RJV, 0MA5B744K3, 02NZZ1J0FH]
sources:
  - url: https://en.wikipedia.org/wiki/Finite_field
    locator: Existence and uniqueness
---

## Proof

1. Let $F$ be a [[finite field|08RTDHX1SK]] of order $q = p^n$, with $p$ prime. By the [[prime power theorem|0H5WWC8RZX]], $q = p'^{n'}$, where $p'$ is the characteristic of $F$. By unique factorisation of $q$, $p' = p$.
2. Let $P$ be the [[prime subfield|0VPFBAY7MW]] of $F$. It is the copy $\F_p$ of the multiples of $1$, as in that theorem.
3. The polynomial $f = x^q - x$ has coefficients $1$, $-1$ and $0$, so $f \in P[x]$, and $F/P$ is a field extension.
4. By the [[factorisation of $x^q - x$|0QWR8WTZEW]], $f = \prod_{a \in F} (x - a)$ in $F[x]$. So $f$ [[splits|0SHMC00RJV]] over $F$, and its roots are exactly the elements of $F$.
5. The [[field generated|0MA5B744K3]] over $P$ by the roots of $f$ is $P(F)$. This is the smallest subfield of $F$ that contains $F$, so it is $F$.
6. By steps 4 and 5, $F$ satisfies both conditions of a [[splitting field|02NZZ1J0FH]] of $x^q - x$ over $\F_p$.

## Idea

Every element of $F$ is a root of $x^q - x$, and this polynomial has no other roots. So it splits over $F$, and its roots already make up the whole field.
