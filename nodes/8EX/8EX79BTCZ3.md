---
tag: 8EX79BTCZ3
kind: proof
name: Proof that kernels and images of commuting maps are invariant
msc: ["15A04"]
topics: [Z6S6PWMJPH]
audience: ug1
proves: 8YNE1HTZEP
methods: [0NTF6DMVAP]
uses: [0EP59ESQ94, 0BNEXSKNRV, 02YFME3RGW]
sources:
  - url: https://en.wikipedia.org/wiki/Invariant_subspace
    locator: For a single operator
---

## Proof

We check the definition of an invariant subspace in each case, and we get part 2 from part 1 because polynomials in $T$ commute.

1. Let $ST = TS$ and let $v \in \ker S$.
   Then
$$S(T(v)) = T(S(v)) = T(0) = 0,$$
   so $T(v) \in \ker S$, and $\ker S$ is [[$T$-invariant|0EP59ESQ94]].
2. Let $w \in \operatorname{im} S$, so $w = S(u)$ for some $u \in V$.
   Then $T(w) = T(S(u)) = S(T(u))$, which is a value of $S$, so $\operatorname{im} S$ is $T$-invariant.
   Steps 1 and 2 prove part 1.
3. Let $p, q \in F[x]$.
   Evaluation at $T$ respects products, by the definition of the [[value at $T$|0BNEXSKNRV]], and $pq = qp$ in $F[x]$, so
$$p(T)\, q(T) = (pq)(T) = (qp)(T) = q(T)\, p(T).$$
4. By step 3, $S = p(T)$ commutes with $q(T)$.
   Steps 1 and 2, with $q(T)$ in the role of $T$, show that $\ker p(T)$ and $\operatorname{im} p(T)$ are $q(T)$-invariant.
   Taking $q = x$ gives $q(T) = T$, which proves part 2.
5. Let $U$ and $W$ be $T$-invariant, and let $v = u + w$ with $u \in U$ and $w \in W$.
   Then $T(v) = T(u) + T(w)$ with $T(u) \in U$ and $T(w) \in W$, so $T(v) \in U + W$.
6. Let $v \in U \cap W$.
   Then $T(v) \in U$ because $U$ is invariant, and $T(v) \in W$ because $W$ is invariant, so $T(v) \in U \cap W$.
   Steps 5 and 6 prove part 3.

## Idea

If $S$ commutes with $T$, then $T$ can be moved past $S$.
So $T$ cannot take a vector that $S$ kills to a vector that $S$ does not kill, and it cannot take a value of $S$ to something that is not a value of $S$.
Polynomials in $T$ commute with $T$, and that gives the main case without any further work.

## Variants

In module language, $p(T)$ is an endomorphism of the $F[x]$-module $V$ defined by $T$.
Kernels and images of module maps are submodules, and submodules are exactly the invariant subspaces, so the statement follows at once.
