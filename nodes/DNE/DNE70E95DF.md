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

We show that the chains stop, then split $V$ with rank-nullity, and then prove uniqueness by comparing dimensions.

1. If $T^j v = 0$, then $T^{j+1} v = 0$. So $\ker T^j \subseteq \ker T^{j+1}$.
2. $T^{j+1} w = T^j (T w)$. So $\operatorname{im} T^{j+1} \subseteq \operatorname{im} T^j$.
3. By the [[rank-nullity theorem|0W4FSW1TVB]], $\dim \ker T^j + \dim \operatorname{im} T^j = n$ for each $j$.
4. So by steps 1 to 3, $\ker T^j = \ker T^{j+1}$ exactly when $\operatorname{im} T^j = \operatorname{im} T^{j+1}$.
5. Assume $\ker T^j = \ker T^{j+1}$, and let $T^{j+2} v = 0$. Then $T v \in \ker T^{j+1} = \ker T^j$.
6. So $T^{j+1} v = T^j (T v) = 0$. This gives $\ker T^{j+2} = \ker T^{j+1}$, with step 1.
7. By induction with step 6, once two kernels in the chain are equal, all later kernels are equal.
8. Before that index, each step adds at least one dimension. The dimensions lie between $0$ and $n$. So the chain is constant from some $k \le n$ on.
9. By step 4, the images are constant from the same $k$ on. This proves part 1.
10. Let $K = \ker T^n$ and $I = \operatorname{im} T^n$. $T$ commutes with $T^n$, so $K$ is $T$-invariant, by [[kernels of commuting maps|8YNE1HTZEP]].
11. $T (T^n w) = T^n (T w)$, so $T(I) \subseteq I$, and $I$ is $T$-invariant.
12. Let $v \in K \cap I$. Write $v = T^n w$. Then $T^{2n} w = T^n v = 0$, so $w \in \ker T^{2n}$.
13. By step 9, $\ker T^{2n} = \ker T^n$. So $v = T^n w = 0$, and $K \cap I = 0$.
14. By step 3, $\dim K + \dim I = n$. With step 13, the [[dimension criterion|P4JG9DJ2HH]] gives $V = K \oplus I$. This proves part 2.
15. $(T|_K)^n = T^n|_K = 0$, by the definition of $K$. So $T|_K$ is nilpotent.
16. $T(I) = \operatorname{im} T^{n+1}$, and this equals $\operatorname{im} T^n = I$, by step 9. So $T|_I \colon I \to I$ is surjective.
17. $I$ has finite dimension. So $T|_I$ is bijective, by the [[endomorphism criterion|0912EEEVCT]]. This proves part 3.
18. For part 4, let $V = K' \oplus I'$ as in the statement, and let $d = \dim K' \le n$.
19. By the [[characterizations of nilpotent maps|FSKECQK1GW]], $(T|_{K'})^d = 0$. So $T^n$ kills $K'$, and $K' \subseteq K$.
20. $T|_{I'}$ is invertible, so $T^n|_{I'}$ is invertible, and $I' = T^n(I') \subseteq I$.
21. $\dim K' + \dim I' = n = \dim K + \dim I$. With steps 19 and 20, $\dim K' = \dim K$ and $\dim I' = \dim I$.
22. A [[subspace of full dimension|0WGAXEK99E]] is the whole space, applied inside $K$ and inside $I$. So $K' = K$ and $I' = I$. This proves part 4.

## Idea

The kernels of the powers of $T$ grow, and once they stop growing they never grow again.
So they are constant from $n$ on, and the images are constant too.
A vector in both $\ker T^n$ and $\operatorname{im} T^n$ would lie in $\ker T^{2n} = \ker T^n$, which forces it to be $0$.
Rank-nullity then fills the space.

## Variants

One can derive the theorem from the [[primary decomposition|49ZHBMYKVE]] applied to $m_T = t^e q$ with $q(0) \ne 0$.
Then $\ker T^e$ is the nilpotent part, and $\ker q(T)$, which equals $\operatorname{im} T^e$ by the [[kernels lemma|ACBNK1VFVG]], is the invertible part.
For modules of finite length, step 8 is replaced by the ascending and descending chain conditions, as in [[Fitting's lemma|F52B2JMEHY]].
