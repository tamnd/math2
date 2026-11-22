---
tag: DNE70E95DF
kind: proof
name: Proof of the Fitting decomposition of an endomorphism
msc: ["15A04", "15A21"]
topics: [Z6S6PWMJPH]
audience: grad
proves: 77SACA9CVQ
methods: [0NTF6DMVAP, MKHVRNW68H]
uses: [0W4FSW1TVB, P4JG9DJ2HH, 0912EEEVCT, 0WGAXEK99E, 8YNE1HTZEP, FSKECQK1GW]
sources:
  - book: isbn:9783031410253
    locator: Chapter 8
  - url: https://en.wikipedia.org/wiki/Fitting_lemma
---

## Proof

We show that the chains of kernels and images stop, then split $V$ with rank-nullity, and then prove uniqueness by comparing dimensions.

*Part 1.*

1. If $T^j v = 0$, then $T^{j+1} v = T(T^j v) = 0$, so $\ker T^j \subseteq \ker T^{j+1}$.
2. Every $T^{j+1} w$ equals $T^j (T w)$, so $\operatorname{im} T^{j+1} \subseteq \operatorname{im} T^j$.
3. By the [[rank-nullity theorem|0W4FSW1TVB]], $\dim \ker T^j + \dim \operatorname{im} T^j = n$ for each $j$.
4. By steps 1 to 3, $\ker T^j = \ker T^{j+1}$ holds exactly when the dimensions of the two kernels agree, which holds exactly when $\operatorname{im} T^j = \operatorname{im} T^{j+1}$.
5. Assume $\ker T^j = \ker T^{j+1}$, and let $T^{j+2} v = 0$.
   Then $T^{j+1}(T v) = 0$, so $T v \in \ker T^{j+1} = \ker T^j$, and $T^{j+1} v = T^j(T v) = 0$.
   With step 1 this gives $\ker T^{j+2} = \ker T^{j+1}$.
6. By induction on step 5, once two neighboring kernels in the chain are equal, all later kernels are equal.
7. Before that happens, each step of the chain adds at least one dimension, and the dimensions lie between $0$ and $n$.
   So there are at most $n$ strict steps, and the chain is constant from some $k \le n$ on.
8. By step 4, the images are constant from the same $k$ on, which proves part 1.

*Part 2.*

9. Let $K = \ker T^n$ and $I = \operatorname{im} T^n$.
   The map $T$ commutes with $T^n$, so $K$ and $I$ are $T$-invariant by the theorem that [[kernels and images of commuting maps are invariant|8YNE1HTZEP]].
10. Let $v \in K \cap I$, and write $v = T^n w$.
    Then $T^{2n} w = T^n v = 0$, so $w \in \ker T^{2n}$.
11. Since $n \ge k$, step 8 gives $\ker T^{2n} = \ker T^n$, so $v = T^n w = 0$, and $K \cap I = 0$.
12. By step 3, $\dim K + \dim I = n$, and with step 11 the [[dimension criterion for a direct sum|P4JG9DJ2HH]] gives $V = K \oplus I$.

*Part 3.*

13. By the definition of $K$, $(T|_K)^n = T^n|_K = 0$, so $T|_K$ is nilpotent.
14. The image of $T|_I$ is $T(\operatorname{im} T^n) = \operatorname{im} T^{n+1}$, which equals $\operatorname{im} T^n = I$ by step 8, so $T|_I \colon I \to I$ is onto.
15. An onto endomorphism of a finite-dimensional space is bijective, by the theorem on [[injective, surjective and bijective endomorphisms|0912EEEVCT]], so $T|_I$ is invertible.

*Part 4.*

16. Let $V = K' \oplus I'$ as in part 4, and let $d = \dim K' \le n$.
17. By the [[characterizations of nilpotent maps|FSKECQK1GW]], $(T|_{K'})^d = 0$, so $T^n$ is $0$ on $K'$, and $K' \subseteq K$.
18. The map $T|_{I'}$ is invertible, so $T^n|_{I'}$ is invertible, and $I' = T^n(I') \subseteq \operatorname{im} T^n = I$.
19. From $\dim K' + \dim I' = n = \dim K + \dim I$ and the two inclusions, $\dim K' = \dim K$ and $\dim I' = \dim I$.
20. A [[subspace of full dimension is the whole space|0WGAXEK99E]], applied inside $K$ and inside $I$, so $K' = K$ and $I' = I$.

## Idea

The kernels of the powers of $T$ grow, and once they stop growing for one step they never grow again.
So they are constant from $n$ on, and by rank-nullity the images are constant too.
A vector in both $\ker T^n$ and $\operatorname{im} T^n$ is $T^n w$ with $T^{2n} w = 0$, and since $\ker T^{2n} = \ker T^n$ it must be $0$.
Rank-nullity then says that the two pieces fill the space.
For uniqueness, any nilpotent piece lies in $\ker T^n$ and any invertible piece lies in $\operatorname{im} T^n$, and the dimensions leave no room for anything else.

## Variants

One can derive the theorem from the [[primary decomposition|49ZHBMYKVE]].
Write $m_T = t^e q$ with $q(0) \ne 0$, so that the [[kernels lemma|ACBNK1VFVG]] gives $V = \ker T^e \oplus \ker q(T)$, with $T$ nilpotent on the first piece and invertible on the second.
Then $\ker T^e = \ker T^n$, and $\ker q(T) = \operatorname{im} T^e = \operatorname{im} T^n$ follows from $q(T) T^e = 0$ and a count of dimensions.
For modules of finite length, step 7 is replaced by the ascending and descending chain conditions, as in [[Fitting's lemma|F52B2JMEHY]].
