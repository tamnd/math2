---
tag: PV1H86FB4Y
kind: proof
name: Proof of the existence of finite fields of every prime power order
msc: ["12E20"]
proves: 0T8M3YC5RG
uses: [01441KDGBY, 02NZZ1J0FH, 0SHMC00RJV, 0AD4VS02H3, 067F8YVYMH, 03XVP8Q4GY, 0P7CH1CND5, 0GHDDVAH8P, 0396VGFA78, 07QY5RPFBR, 08RTDHX1SK]
sources:
  - url: https://en.wikipedia.org/wiki/Finite_field
    locator: Existence and uniqueness
---

## Proof

1. Let $p$ be prime, let $n \ge 1$ and let $q = p^n$. Let $f = x^q - x \in \F_p[x]$.
2. By the [[existence of splitting fields|01441KDGBY]], $f$ has a [[splitting field|02NZZ1J0FH]] $L$ over $\F_p$. So $f = (x - a_1) \cdots (x - a_q)$ with $a_i \in L$, since $f$ is monic of degree $q$ and [[splits|0SHMC00RJV]] over $L$.
3. The field $L$ contains $\F_p$, so $p \cdot 1 = 0$ in $L$, and the [[characteristic|0P7CH1CND5]] of $L$ is $p$.
4. The [[formal derivative|0AD4VS02H3]] of $f$ is $f' = q x^{q-1} - 1$. Since $q \cdot 1 = p^{n-1} (p \cdot 1) = 0$ in $L$, we get $f' = -1$.
5. Suppose that some root $c$ of $f$ in $L$ has [[multiplicity|03XVP8Q4GY]] at least $2$. Then $f'(c) = 0$ by the [[criterion for repeated roots|067F8YVYMH]]. This contradicts $f'(c) = -1 \neq 0$.
6. So every root of $f$ has multiplicity $1$, and $a_1, \dots, a_q$ are distinct. Let $R = \set{a_1, \dots, a_q}$, so $\abs{R} = q$ and $R = \set{a \in L : a^q = a}$.
7. The [[Frobenius endomorphism|0GHDDVAH8P]] $\varphi(a) = a^p$ of $L$ is a ring homomorphism, by the [[freshman's dream|0396VGFA78]]. So $\psi = \varphi^n$, $\psi(a) = a^{q}$, is a ring homomorphism $L \to L$.
8. So $R = \set{a \in L : \psi(a) = a}$ contains $0$ and $1$. For $a, b \in R$, we get $\psi(a - b) = \psi(a) - \psi(b) = a - b$ and $\psi(ab) = \psi(a)\psi(b) = ab$.
9. For $a \in R$ with $a \neq 0$, we get $\psi(a^{-1}) = \psi(a)^{-1} = a^{-1}$, since $\psi(a)\psi(a^{-1}) = \psi(1) = 1$.
10. By steps 8 and 9, $R$ is a [[subfield|07QY5RPFBR]] of $L$. By step 6 it has $q = p^n$ elements, so it is a [[finite field|08RTDHX1SK]] of order $p^n$.

## Idea

Build a field in which $x^q - x$ splits, and look at its roots. The derivative is the constant $-1$, so the roots are distinct and there are exactly $q$ of them. The map $a \mapsto a^q$ is a ring homomorphism in characteristic $p$, so its fixed points form a field.
