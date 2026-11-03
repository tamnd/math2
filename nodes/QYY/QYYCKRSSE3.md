---
tag: QYYCKRSSE3
kind: proof
name: Proof of the Bolzano–Weierstrass theorem by a monotone subsequence
msc: [40A05]
proves: 0KDJD249DT
uses: [05FQ3VGAR9, 0R8J3ZQMJS, 0MHGJRZMTM, 0KN22AAW5R, 0FM6N4R0VB, 02V2GYAC8P]
sources:
  - url: https://en.wikipedia.org/wiki/Bolzano–Weierstrass_theorem
    locator: Proof
---

## Proof

1. Since $(a_n)$ is [[bounded|05FQ3VGAR9]], there is $K \ge 0$ with $-K \le a_n \le K$ for all $n$.
2. [[Every sequence has a monotone subsequence|0MHGJRZMTM]]. Let $(a_{n_k})$ be a [[subsequence|0R8J3ZQMJS]] of $(a_n)$ that is [[monotone|0KN22AAW5R]].
3. Each term $a_{n_k}$ is a term of $(a_n)$. So $-K \le a_{n_k} \le K$ for all $k$.
4. If $(a_{n_k})$ is increasing, it is bounded above by $K$. By the [[monotone convergence theorem|0FM6N4R0VB]], it converges to a real number.
5. If $(a_{n_k})$ is decreasing, it is bounded below by $-K$. Since a [[decreasing sequence bounded below converges|02V2GYAC8P]], it converges to a real number.
6. In both cases, $(a_n)$ has a subsequence that converges to a real number.

## Idea

Each sequence has a monotone subsequence. If the sequence is bounded, this subsequence is bounded too. The completeness of $\mathbb{R}$, in the form of the monotone convergence theorem, then makes it converge.
