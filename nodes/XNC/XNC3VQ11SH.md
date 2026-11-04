---
tag: XNC3VQ11SH
kind: proof
name: Proof of the rank–nullity theorem by extending a basis of the kernel
msc: [15A03, 15A04]
proves: 0W4FSW1TVB
uses: [0NRYHJPQG2, 0S23E6YE83, 0WSFKKT6FF, 00YC1D652K, 0QW084460E, 0M4SXE5WW3, 0WK0Y8RH1M, 0KCQ9Y3QKA, 0CRMGPAH83, 088RYKAWK9, 03GSZ8RTZJ, 0ZZXSBTR4J, 0APCFW7639]
sources:
  - url: https://en.wikipedia.org/wiki/Rank–nullity_theorem
    locator: First proof
---

## Proof

Let $T$ be a [[linear map|0NRYHJPQG2]] as in the statement. We extend a basis of the kernel to a basis of $V$. Then we show that the new vectors map to a basis of the image.

1. Let $n = \dim V$. The [[kernel|0S23E6YE83]] $\ker T$ is a [[subspace|00YC1D652K]] of $V$. It contains $0$, since $T(0) = T(0 + 0) = 2T(0)$ gives $T(0) = 0$.
2. If $u, v \in \ker T$ and $a \in F$, then $T(u + v) = T(u) + T(v) = 0$ and $T(av) = a T(v) = 0$. So $\ker T$ is closed under both operations.
3. The [[image|0WSFKKT6FF]] $\im T$ is a subspace of $W$. It contains $T(0) = 0$, and $T(u) + T(v) = T(u + v)$ and $a T(v) = T(av)$ lie in $\im T$.
4. By the [[dimension of a subspace|0QW084460E]], $\ker T$ is finite-dimensional. Let $k = \dim \ker T$ and let $(v_1, \dots, v_k)$ be a [[basis|0KCQ9Y3QKA]] of $\ker T$.
5. This family is [[linearly independent|0CRMGPAH83]] in $V$. By [[extension to a basis|0M4SXE5WW3]] and the [[dimension theorem|0WK0Y8RH1M]], there is a basis $(v_1, \dots, v_k, u_1, \dots, u_{n-k})$ of $V$.
6. The vectors $T(u_1), \dots, T(u_{n-k})$ [[span|088RYKAWK9]] $\im T$. Let $w \in \im T$, say $w = T(v)$ with $v \in V$.
7. Write $v = \sum_{i=1}^k a_i v_i + \sum_{j=1}^{n-k} c_j u_j$. Since $T(v_i) = 0$, linearity gives $w = T(v) = \sum_{j=1}^{n-k} c_j T(u_j)$.
8. The vectors $T(u_1), \dots, T(u_{n-k})$ are linearly independent. Suppose $\sum_{j=1}^{n-k} c_j T(u_j) = 0$ with $c_j \in F$.
9. By linearity, $T\left(\sum_j c_j u_j\right) = 0$, so $\sum_j c_j u_j \in \ker T$. Since $(v_i)$ spans $\ker T$, $\sum_j c_j u_j = \sum_i a_i v_i$ for some $a_i \in F$.
10. Then $\sum_i a_i v_i - \sum_j c_j u_j = 0$. The basis of step 5 is linearly independent, so all $c_j = 0$.
11. By steps 6 to 10, $(T(u_1), \dots, T(u_{n-k}))$ is a basis of $\im T$. So $\dim \im T = n - k$, by the definition of [[dimension|03GSZ8RTZJ]].
12. Hence $\dim \im T + \dim \ker T = (n - k) + k = n = \dim V$. In other words, the [[rank|0ZZXSBTR4J]] plus the [[nullity|0APCFW7639]] of $T$ equals $\dim V$.

## Idea

Split a basis of $V$ into a basis of the kernel and some extra vectors. The kernel part is sent to $0$. The extra vectors are sent to a basis of the image, because any relation among their images would put a combination of them into the kernel.
