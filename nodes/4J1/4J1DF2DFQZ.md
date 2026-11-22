---
tag: 4J1DF2DFQZ
kind: proof
name: Proof of the dimension formula for the centralizer of a matrix
msc: ["15A27"]
topics: [GEBYZKYV3D]
audience: grad
proves: GXZGWZSJ2J
uses: [R3Z20J19BR, 42MMQBTP0M, KGVTFBZX59, RK1QVMYW7H, 03NDVCSHSB, 0C8WYW4KYQ, 0VY3WPP9Y3, 8G3X8MPG7E]
sources:
  - url: https://en.wikipedia.org/wiki/Commuting_matrices
    locator: Characterizations and properties
---

## Proof

We view $F^n$ as a module over $F[x]$, split it into cyclic pieces, and count the module maps between each pair of pieces.

Let $V = F^n$ with the [[F[x]-module structure|KGVTFBZX59]] $f \cdot v = f(A) v$.
For a monic nonconstant $a \in F[x]$, write $\bar f$ for the class of $f$ in $F[x]/(a)$.

*Part 1.*

1. If $X$ and $Y$ commute with $A$, then so do $X + Y$ and $cX$ for $c \in F$, and so does $XY$, because $XYA = XAY = AXY$. The identity commutes with $A$, so $\mathcal{C}(A)$ is a subalgebra of $M_n(F)$. It contains $A$, hence every power $A^k$ and every $f(A)$.
2. The map $F[x] \to M_n(F)$, $f \mapsto f(A)$, is linear with image $F[A]$. By the definition of the [[minimal polynomial|03NDVCSHSB]], its kernel is the ideal $(\mu_A)$, so $F[A] \cong F[x]/(\mu_A)$ has dimension $\deg \mu_A$.
3. By the [[cyclic decomposition theorem|R3Z20J19BR]], $\mu_A = d_r$ and $\chi_A = d_1 \cdots d_r$. So $\dim F[A] = m_r$, which proves part 1.

*Part 2.*

4. A linear map $X \colon V \to V$ is $F[x]$-linear exactly when $X(Av) = A(Xv)$ for all $v$, that is, when $XA = AX$. So $\mathcal{C}(A)$ is the space of $F[x]$-module endomorphisms of $V$.
5. By the cyclic decomposition theorem, $V = Z_1 \oplus \cdots \oplus Z_r$, where $Z_i$ is the [[cyclic subspace|42MMQBTP0M]] of a vector $v_i$ whose annihilator is $d_i$. The map $F[x] \to Z_i$, $f \mapsto f(A) v_i$, is $F[x]$-linear and onto with kernel $(d_i)$, so $Z_i \cong F[x]/(d_i)$.
6. Let $\iota_j \colon Z_j \to V$ be the inclusions and $\pi_i \colon V \to Z_i$ the projections of the direct sum. They are $F[x]$-linear because each $Z_i$ is invariant under $A$. So $X \mapsto (\pi_i X \iota_j)_{i, j}$ is a linear bijection from $\mathcal{C}(A)$ onto $\bigoplus_{i, j} \operatorname{Hom}_{F[x]}(Z_j, Z_i)$, with inverse $(\varphi_{ij}) \mapsto \sum_{i, j} \iota_i \varphi_{ij} \pi_j$.
7. Now we count one Hom space. Let $a, b \in F[x]$ be monic and nonconstant, and let $g = \gcd(a, b)$. A module map $\varphi \colon F[x]/(a) \to F[x]/(b)$ is fixed by $c = \varphi(\bar 1)$, because $\varphi(\bar f) = f \cdot \varphi(\bar 1)$.
8. Since $a \cdot \bar 1 = 0$ in $F[x]/(a)$, the class $c$ satisfies $a c = 0$ in $F[x]/(b)$. Conversely, if $c = \bar h$ with $b \mid a h$, the rule $\bar f \mapsto \overline{f h}$ is well defined, because $f \equiv f' \pmod a$ gives $f h - f' h \in (a h) \subseteq (b)$.
9. So $\varphi \mapsto \varphi(\bar 1)$ is a linear bijection onto $K = \{ \bar h \in F[x]/(b) : b \mid a h \}$.
10. Write $a = g a'$ and $b = g b'$. Then the [[greatest common divisor|0C8WYW4KYQ]] of $a'$ and $b'$ is $1$, and $b \mid a h$ holds exactly when $b' \mid a' h$.
11. If $b' \mid a' h$, take $u, w$ with $u a' + w b' = 1$ by [[Bézout's identity|0VY3WPP9Y3]]. Then $h = u a' h + w b' h$, and $b'$ divides both terms, so $b' \mid h$. The converse holds because $b' \mid h$ gives $b' \mid a' h$, so $K = \{ \overline{b' s} : s \in F[x] \}$.
12. The linear map $F[x] \to K$, $s \mapsto \overline{b' s}$, is onto. Its kernel is the set of $s$ with $g b' \mid b' s$, that is, with $g \mid s$, so $K \cong F[x]/(g)$ and the Hom space has dimension $\deg g$.
13. Apply step 12 with $a = d_j$ and $b = d_i$, using step 5. Since $d_1 \mid \cdots \mid d_r$, we have $\gcd(d_i, d_j) = d_{\min(i, j)}$, of degree $m_{\min(i, j)}$. With step 6 this gives the first formula of part 2.
14. For a fixed $k$, the ordered pairs $(i, j)$ with $\min(i, j) = k$ are the pairs in $\{k, \dots, r\}^2$ that are not in $\{k + 1, \dots, r\}^2$. There are $(r - k + 1)^2 - (r - k)^2 = 2r - 2k + 1$ of them, which gives the second formula.

*Parts 3 and 4.*

15. Since $n \ge 1$, we have $r \ge 1$, and part 2 gives
$$\dim \mathcal{C}(A) - n = \sum_{i=1}^{r} (2r - 2i + 1) m_i - \sum_{i=1}^{r} m_i = \sum_{i=1}^{r} (2r - 2i)\, m_i \ge 0.$$
16. Each $m_i \ge 1$, so equality holds exactly when $r - i = 0$ for every $i$, that is, when $r = 1$.
17. By step 3, $r = 1$ holds exactly when $\mu_A = d_1 = \chi_A$. By the [[cyclicity criterion|RK1QVMYW7H]], this holds exactly when $A$ is cyclic, which proves part 3.
18. If $A$ is cyclic, then $r = 1$ and $m_1 = n$. So $F[A]$ has dimension $m_r = n$ by part 1, and $\mathcal{C}(A)$ has dimension $n$ by part 3. Since $F[A] \subseteq \mathcal{C}(A)$, the two are equal.
19. If $\mathcal{C}(A) = F[A]$, then $n \le \dim \mathcal{C}(A) = m_r \le n$ by part 3 and part 1. So $\dim \mathcal{C}(A) = n$, and $A$ is cyclic by part 3. This proves part 4.

## Idea

The [[matrices that commute with A|8G3X8MPG7E]] are exactly the module maps of $F^n$ to itself, once $x$ acts as $A$.
Split the module into cyclic pieces $F[x]/(d_i)$, and a commuting matrix becomes a block matrix of module maps between pieces.
A map out of $F[x]/(a)$ is fixed by where it sends $\bar 1$, and the allowed images form a copy of $F[x]/(\gcd(a, b))$.
So the dimension is a sum of degrees of gcds, and the divisibility chain turns each gcd into the smaller invariant factor.

## Variants

For a cyclic $A$ there is a short direct proof of part 4.
Let $v$ be a cyclic vector, so that $v, Av, \dots, A^{n-1} v$ is a basis of $F^n$, and let $X$ commute with $A$.
Write $Xv = f(A) v$ for some $f \in F[x]$, which is possible because these vectors span.
Then $X A^k v = A^k X v = f(A) A^k v$ for every $k$, so $X$ and $f(A)$ agree on a basis, and $X = f(A)$.

A second route to part 2, when $\chi_A$ splits, goes through the Jordan form.
For each ordered pair of Jordan blocks $J_k(\lambda)$ and $J_l(\lambda)$, one solves $J_k(\lambda) Y = Y J_l(\lambda)$ for a $k \times l$ matrix $Y$ directly, and the solutions form a space of dimension $\min(k, l)$.
Blocks with different eigenvalues contribute only $Y = 0$, and the sum of $\min(k, l)$ over all ordered pairs of blocks with the same eigenvalue gives the same number.
