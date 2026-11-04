---
tag: 380M6VQXRT
kind: proof
name: Proof of Burnside's p^a q^b theorem
msc: [20D10]
proves: 0FMAQSB1SC
sources:
  - wikipedia: en:1912650@r1349836899
    locator: Burnside's theorem, section Proof
    note: adopted
    mention: wikipedia://en/1912650#PDC3
    sections: [Proof]
---

## Proof

The following proof — using more background than Burnside's — is by contradiction. Let $p^a q^b$ be the smallest product of two prime powers, such that there is a non-solvable group $G$ whose order is equal to this number.

- $G$ **is a [[simple group|0C093D1T4M]] with trivial [[center|0DZ93493VN]] and** $a$ **is not zero.**

If $G$ had a [[nontrivial|0BNPC9850Y]] proper [[normal subgroup|0CB0DX5BVV]] $H$, then (because of the minimality of *$G$*), $H$ and $G / H$ would be solvable, so $G$ as well, which would contradict our assumption. So $G$ is simple.

If $a$ were zero, $G$ would be a finite [[q-group|06QYRTX9KQ]], hence [[nilpotent|0DZPD2MG33]], and therefore solvable.

Similarly, $G$ cannot be abelian, otherwise it would be solvable. As $G$ is simple, its center must therefore be trivial.

- **There is an element $g$ of $G$ which has $q^d$ [[conjugates|0DEBXAJ5SA]], for some $d > 0$.**

By the first statement of Sylow's theorem, $G$ has a [[subgroup|0X1JXT47GA]] $S$ of order $p^a$. Because $S$ is a nontrivial $p$-group, its center $Z(S)$ is nontrivial. Fix a nontrivial element $g \in Z(S)$. The number of conjugates of $g$ is equal to the index of its centralizer $G_g$, which divides the [[index|0DTXBQPA2S]] $q^b$ of $S$ (because $S$ is a subgroup of $G_g$). Hence this number is of the form $q^d$. Moreover, the integer $d$ is strictly positive, since $g$ is nontrivial and therefore not central in $G$.

- **There exists a nontrivial irreducible representation $\rho$ with character $\chi$, such that its dimension $n$ is not divisible by $q$ and the [[complex number|09FTAET5Z4]] $\chi(g)$ is not zero.**

Let $(\chi_i)_{1 \leq i \leq h}$ be the family of irreducible characters of $G$ over $\mathbb{C}$ (here $\chi_1$ denotes the trivial character). Because $g$ is not in the same conjugacy class as 1, the orthogonality relation for the columns of the group's character table gives:

$$0=\sum_{i=1}^h \chi_i(1)\chi_i(g)= 1 + \sum_{i=2}^h \chi_i(1)\chi_i(g).$$

Now the $\chi_i(g)$ are algebraic integers, because they are sums of [[roots of unity|0S61N75H45]]. If all the nontrivial irreducible characters which don't vanish at $g$ take a value divisible by $q$ at 1, we deduce that

$$-\frac1q=\sum_{i\ge 2,~\chi_i(g)\ne 0}\frac{\chi_i(1)}q\chi_i(g)$$

is an algebraic integer (since it is a sum of integer multiples of algebraic integers), which is absurd. This proves the statement.

- **The complex number $q^d \chi(g) / n$ is an algebraic integer.**

The set of integer-valued class functions on $G$, $Z(\mathbb{Z}[G])$, is a [[commutative ring|0310REJJY8]], [[finitely generated|05QY1VEBYD]] over $\mathbb{Z}$. All of its elements are thus integral over $\mathbb{Z}$, in particular the mapping $u$ which takes the value 1 on the conjugacy class of $g$ and 0 elsewhere.

The mapping $A\colon Z(\mathbb{Z}[G]) \rightarrow \operatorname{End}(\mathbb{C}^n)$ which sends a class function $f$ to

$$\sum_{s\in G} f(s)\rho(s)$$

is a ring homomorphism. Because $\rho(s)^{-1} A(u) \rho(s) = A(u)$ for all $s$, Schur's lemma implies that $A(u)$ is a homothety $\lambda I_n$. Its [[trace|0XC1RDBY7A]] $n \lambda$ is equal to

$$\sum_{s\in G} f(s)\chi(s)=q^d\chi(g).$$

Because the homothety $\lambda I_n$ is the homomorphic image of an integral element, this proves that the complex number $\lambda = q^d \chi(g) / n$ is an algebraic integer.

- **The complex number $\chi(g) / n$ is an algebraic integer.**

Since $q$ is relatively prime to $n$, by [[Bézout's identity|0DQVHMYAGA]] there are two integers $x$ and $y$ such that:

$$xq^d + yn=1\quad\text{therefore}\quad \frac{\chi(g)}{n}=x\frac{q^d\chi(g)}{n} + y\chi(g).$$

Because a linear combination with integer coefficients of algebraic integers is again an algebraic integer, this proves the statement.

- **The image of $g$, under the representation $\rho$, is a homothety.**

Let $\zeta$ be the complex number $\chi(g) / n$. It is an algebraic integer, so its norm $N(\zeta)$ (i.e. the product of its conjugates, that is the roots of its [[minimal polynomial|0VX9EP2GS8]] over $\mathbb{Q}$) is a nonzero integer. Now $\zeta$ is the average of roots of unity (the eigenvalues of $\rho(g)$), hence so are its conjugates, so they all have an absolute value less than or equal to 1. Because the absolute value of their product $N(\zeta)$ is greater than or equal to 1, their absolute value must all be 1, in particular $\zeta$, which means that the eigenvalues of $\rho(g)$ are all equal, so $\rho(g)$ is a homothety.

- **Conclusion**

Let $N$ be the kernel of $\rho$. The homothety $\rho(g)$ is central in $\operatorname{Im}(\rho)$ (which is canonically isomorphic to $G / N$), whereas $g$ is not central in $G$. Consequently, the normal subgroup $N$ of the simple group $G$ is nontrivial, hence it is equal to $G$, which contradicts the fact that $\rho$ is a nontrivial representation.

This contradiction proves the theorem.
