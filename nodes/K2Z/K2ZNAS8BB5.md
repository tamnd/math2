---
tag: K2ZNAS8BB5
kind: proof
name: Proof of the module description of invariant subspaces and similarity
msc: ["15A21", "13C05"]
topics: [GEBYZKYV3D]
audience: grad
proves: R5X8SNHBGG
methods: [0NTF6DMVAP, 0ASJVEFA9J]
uses: [KGVTFBZX59, 0NZ8JA25WK, 0FCCDXH97W, 03NDVCSHSB, 0ACX5QT8TE, 0YQSGNYE3K, 0KCQ9Y3QKA, 027KDW2K72]
sources:
  - url: https://en.wikipedia.org/wiki/Structure_theorem_for_finitely_generated_modules_over_a_principal_ideal_domain
    locator: Corollaries
---

## Proof

1. The map $F[x] \to \operatorname{End}(V)$, $f \mapsto f(T)$, is a ring homomorphism, by the properties of the [[evaluation homomorphism|0FCCDXH97W]]: $(f + g)(T) = f(T) + g(T)$, $(fg)(T) = f(T) g(T)$ and $1(T) = \operatorname{id}$.
2. So $f \cdot v = f(T) v$ satisfies the [[module axioms|0NZ8JA25WK]]: $(f + g) \cdot v = f \cdot v + g \cdot v$, $(fg) \cdot v = f \cdot (g \cdot v)$, $f \cdot (v + w) = f \cdot v + f \cdot w$ and $1 \cdot v = v$.
3. An $F$-basis of $V$ generates $V_T$, since the constant polynomials act as scalars. So $V_T$ is finitely generated.
4. By the [[definition of the minimal polynomial|03NDVCSHSB]], $m_T(T) = 0$, so $m_T \cdot v = 0$ for every $v$, and $m_T \ne 0$. This proves part 1.
5. Let $U$ be a submodule. It is closed under addition and under multiplication by constants, so it is a subspace. It is closed under $x \cdot u = Tu$, so it is [[$T$-invariant|0ACX5QT8TE]].
6. Conversely, let $U$ be a $T$-invariant subspace. By induction on $k$, $T^k U \subseteq U$. So $f(T) U \subseteq U$ for every $f = \sum a_k x^k$, since $U$ is a subspace. So $U$ is a submodule. This proves part 2.
7. Let $\varphi$ be a module homomorphism. Taking $f$ constant in $\varphi(f \cdot v) = f \cdot \varphi(v)$ shows that $\varphi$ is $F$-linear. Taking $f = x$ gives $\varphi(Tv) = S \varphi(v)$.
8. Conversely, let $\varphi$ be linear with $\varphi T = S \varphi$. By induction on $k$, $\varphi T^k = S \varphi T^{k-1} = \cdots = S^k \varphi$. By linearity, $\varphi f(T) = f(S) \varphi$ for every $f$, so $\varphi$ is a module homomorphism.
9. A module isomorphism is a bijective homomorphism. If $\varphi$ is a bijective homomorphism, its inverse is linear and $\varphi^{-1} S = \varphi^{-1} S \varphi \varphi^{-1} = \varphi^{-1} \varphi T \varphi^{-1} = T \varphi^{-1}$, so by step 8 the inverse is a homomorphism too. This proves part 3.
10. Let $A, B \in M_n(F)$ with $B = P^{-1} A P$ for an invertible $P$. Then $\varphi(v) = Pv$ is a linear bijection with $\varphi B = PB = AP = A \varphi$. By part 3, $\varphi \colon F^n_B \to F^n_A$ is an isomorphism.
11. Conversely, let $\varphi \colon F^n_B \to F^n_A$ be an isomorphism. By part 3 it is a linear bijection, so $\varphi(v) = Pv$ for the invertible [[matrix of $\varphi$|0YQSGNYE3K]] $P$, and $PB = AP$. So $B = P^{-1} A P$, and $A$ and $B$ are [[similar|027KDW2K72]]. This proves part 4.
12. Let $M$ be an $F[x]$-module with $\dim_F M = n$. Let $L \colon M \to M$ be $L(m) = x \cdot m$. It is $F$-linear by the module axioms, since constants commute with $x$ in $F[x]$.
13. By induction on $k$, $x^k \cdot m = L^k(m)$. By the module axioms, $f \cdot m = f(L)(m)$ for every $f$. So $M = M_L$ as modules.
14. Choose a [[basis|0KCQ9Y3QKA]] $b_1, \dots, b_n$ of $M$, let $\kappa \colon M \to F^n$ be the coordinate map, and let $A$ be the matrix of $L$ in this basis. Then $\kappa$ is a linear bijection with $\kappa L = A \kappa$.
15. By part 3, $\kappa \colon M_L \to F^n_A$ is an isomorphism. This proves part 5.
16. By part 4, the class of $F^n_A$ depends only on the similarity class of $A$, and different classes give different modules. By part 5, every module of $F$-dimension $n$ arises. So the map of classes is a bijection.

## Idea

Every statement reduces to one remark: an $F[x]$-module structure on $V$ is the same as one linear map, the action of $x$.
A module map must commute with the action of $x$, so module isomorphisms are exactly changes of basis that carry one matrix to the other.

## Variants

The same proof works over any commutative ring $R$: $R[x]$-modules are $R$-modules with an endomorphism.
Some books state part 4 with $B = PAP^{-1}$; then the isomorphism goes from $F^n_A$ to $F^n_B$.
