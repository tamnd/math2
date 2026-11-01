---
tag: AA943HVK6Z
kind: definition
name: Class field theory
msc: [11R37]
defines: BEKCEYHCHX
uses: [MWBDFS2KJ5, YB4JTB4WJN, B7KNZCBFYT, 0QMZAQ6QQ4, 082GHNPJ53, NN77VYSGXR, 0X1JXT47GA]
sources:
  - url: https://en.wikipedia.org/wiki/Class_field_theory
---

## Definition

Let $K$ be an [[algebraic number field|MWBDFS2KJ5]] with ring of integers $\mathcal{O}_K$.
A *modulus* of $K$ is a formal product $\mathfrak{m} = \mathfrak{m}_0 \mathfrak{m}_\infty$ of a nonzero ideal $\mathfrak{m}_0$ of $\mathcal{O}_K$ and a set $\mathfrak{m}_\infty$ of real embeddings of $K$.
Let $I_K^{\mathfrak{m}}$ be the group of [[fractional ideals|YB4JTB4WJN]] of $K$ coprime to $\mathfrak{m}_0$.
Let $P_K^{\mathfrak{m}}$ be its [[subgroup|0X1JXT47GA]] of principal ideals $(\alpha)$ with $\alpha \in K^\times$ such that $v_{\mathfrak{p}}(\alpha - 1) \ge v_{\mathfrak{p}}(\mathfrak{m}_0)$ for every prime $\mathfrak{p} \mid \mathfrak{m}_0$ and $\sigma(\alpha) > 0$ for every $\sigma \in \mathfrak{m}_\infty$.
A *congruence subgroup* modulo $\mathfrak{m}$ is a subgroup $H$ with $P_K^{\mathfrak{m}} \subseteq H \subseteq I_K^{\mathfrak{m}}$; the quotient $I_K^{\mathfrak{m}}/P_K^{\mathfrak{m}}$ is the *ray class group* modulo $\mathfrak{m}$.
Let $L/K$ be a finite [[Galois extension|0QMZAQ6QQ4]].
It is the *class field* of $H$ if the following holds for every nonzero prime ideal $\mathfrak{p}$ of $\mathcal{O}_K$ coprime to $\mathfrak{m}_0$.
The prime $\mathfrak{p}$ [[splits completely|B7KNZCBFYT]] in $L$ if and only if $\mathfrak{p} \in H$.
Class field theory is the theory of class fields of congruence subgroups.

## Remarks

The main theorems are as follows.
Each congruence subgroup $H$ has a class field $L$, unique inside a fixed algebraic closure.
This $L/K$ is [[abelian|082GHNPJ53]] and unramified at the places not dividing $\mathfrak{m}$.
The [[Artin map|7938EKMMVR]] gives $\Gal(L/K) \cong I_K^{\mathfrak{m}}/H$.
Every finite abelian extension of $K$ is the class field of some congruence subgroup.
The ray class group is finite, and its order is a multiple of the class number.

Example: $K = \Q$, $\mathfrak{m} = n\infty$ with $n \ge 3$, and $H = P_{\Q}^{\mathfrak{m}}$.
For a prime $p \nmid n$, the ideal $(p)$ has the unique positive generator $p$, so $(p) \in H$ if and only if $p \equiv 1 \pmod n$.
This is exactly the condition for $p$ to split completely in the [[cyclotomic field|NN77VYSGXR]] $\Q(\zeta_n)$, so $\Q(\zeta_n)$ is the class field of $H$.

Non-example: for $\mathfrak{m} = 5$ without the infinite place, $(p) = (-p)$ lies in $P_{\Q}^{\mathfrak{m}}$ when $p \equiv \pm 1 \pmod 5$.
So $\Q(\zeta_5)$ is not the class field of $P_{\Q}^{\mathfrak{m}}$: the prime $19 \equiv -1 \pmod 5$ gives $(19) \in P_{\Q}^{\mathfrak{m}}$, but $19$ does not split completely in $\Q(\zeta_5)$.
The class field of this group is the real subfield $\Q(\zeta_5 + \zeta_5^{-1}) = \Q(\sqrt{5})$.
