---
tag: XNC3VQ11SH
kind: proof
name: Proof of the rank–nullity theorem by extending a basis of the kernel
msc: ["15A03", "15A04"]
topics: [9080WQTZ3M]
audience: ug1
proves: 0W4FSW1TVB
methods: [01XM7JEKHY, 0NTF6DMVAP]
uses: [0NRYHJPQG2, 0S23E6YE83, 0WSFKKT6FF, 0QW084460E, 0M4SXE5WW3, 0WK0Y8RH1M, 0KCQ9Y3QKA, 0CRMGPAH83, 03GSZ8RTZJ, ~46f99cf4, ~c10ad39e]
sources:
  - url: https://en.wikipedia.org/wiki/Rank–nullity_theorem
    locator: First proof
  - book: isbn:9783031410253
    locator: Chapter 3
---

## Proof

Let $n = \dim V$.
We extend a basis of the kernel to a basis of $V$, and we show that the new vectors map to a basis of the image.

1. By the [[lemma on the kernel|~46f99cf4]], $\ker T$ is a subspace of $V$.
2. By the [[dimension of a subspace|0QW084460E]], $\ker T$ is finite-dimensional. Let $k = \dim \ker T$.
3. Let $(v_1, \dots, v_k)$ be a [[basis|0KCQ9Y3QKA]] of $\ker T$. It is a [[linearly independent|0CRMGPAH83]] family in $V$.
4. By [[extension to a basis|0M4SXE5WW3]], there is a basis $(v_1, \dots, v_k, u_1, \dots, u_m)$ of $V$.
5. By the [[dimension theorem|0WK0Y8RH1M]], all bases of $V$ have $n$ elements. So $k + m = n$.
6. Spanning. Let $w \in \im T$, so $w = T(v)$ for some $v \in V$.
7. Write $v = \sum_{i=1}^k a_i v_i + \sum_{j=1}^m c_j u_j$ in the basis of step 4.
8. Each $T(v_i) = 0$. By the [[lemma on linear combinations|~c10ad39e]], $w = \sum_{j=1}^m c_j T(u_j)$.
9. So $T(u_1), \dots, T(u_m)$ span $\im T$.
10. Independence. Suppose $\sum_{j=1}^m c_j T(u_j) = 0$ with $c_j \in F$.
11. By linearity, $T\left(\sum_j c_j u_j\right) = 0$. So $\sum_j c_j u_j \in \ker T$.
12. The $v_i$ span $\ker T$, so $\sum_j c_j u_j = \sum_i a_i v_i$ for some $a_i \in F$.
13. Then $\sum_i a_i v_i - \sum_j c_j u_j = 0$. The basis of step 4 is independent, so all $c_j = 0$.
14. By steps 9 and 13, $(T(u_1), \dots, T(u_m))$ is a basis of $\im T$. So $\im T$ is finite-dimensional and $\dim \im T = m$.
15. By step 5, $\dim \im T + \dim \ker T = m + k = n = \dim V$.

## Idea

Split a basis of $V$ into a basis of the kernel and some extra vectors.
The kernel part is sent to $0$.
The extra vectors are sent to a basis of the image, because any relation among their images would put a combination of them into the kernel.

## Variants

- Infinite-dimensional form. The same steps work with index sets. Take a basis $(v_i)_{i \in I}$ of $\ker T$ and extend it to a basis $(v_i)_{i \in I} \cup (u_j)_{j \in J}$ of $V$, by the [[general extension theorem|0M4SXE5WW3]]. Steps 6 to 13 show that $(T(u_j))_{j \in J}$ is a basis of $\im T$. So $U = \operatorname{span}(u_j)$ satisfies $V = \ker T \oplus U$ and $T|_U \colon U \to \im T$ is an isomorphism. Hence $\dim V = \abs{I} + \abs{J} = \dim \ker T + \dim \im T$ as cardinals.
- The [[second proof|~982b537e]] uses the first isomorphism theorem and the dimension of a quotient space.
- For matrices, row reduction gives a third proof: the pivot columns give the rank, and the free variables give the nullity, and together they are the $n$ columns.
