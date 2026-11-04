---
tag: WC9M3CNP02
kind: proof
name: Proof of the boundedness theorem by Bolzano–Weierstrass
msc: [26A15]
proves: 0ATVXC3NCC
uses: [0P27W9RW0G, 0KDJD249DT, 05FQ3VGAR9, 0R8J3ZQMJS, 0N32V0E3XJ, 0PAQM3H57X, 0MVDQEAB60, 0S4JF619V7, 0A74SX55QP]
sources:
  - url: https://en.wikipedia.org/wiki/Extreme_value_theorem
    locator: Proof of the boundedness theorem
---

## Proof

We argue by contradiction.

1. Let $a \le b$ and let $f \colon [a, b] \to \R$ be [[continuous|0P27W9RW0G]]. Suppose that $f$ is not bounded.
2. Then for each natural number $n$, the number $n$ is not a bound. So there is $x_n \in [a, b]$ with $\abs{f(x_n)} > n$.
3. The sequence $(x_n)$ satisfies $a \le x_n \le b$, so it is [[bounded|05FQ3VGAR9]]. By the [[Bolzano–Weierstrass theorem|0KDJD249DT]], it has a [[subsequence|0R8J3ZQMJS]] $(x_{n_k})$ that converges to some real $c$.
4. Since $a \le x_{n_k} \le b$ for all $k$, [[limits preserve non-strict inequalities|0N32V0E3XJ]], with constant sequences, gives $a \le c \le b$.
5. The function $f$ is continuous, so it is [[sequentially continuous|0MVDQEAB60]] by the [[equivalence|0PAQM3H57X]]. Hence $f(x_{n_k}) \to f(c)$.
6. The convergent sequence $(f(x_{n_k}))$ is [[bounded|0S4JF619V7]]: there is $K$ with $\abs{f(x_{n_k})} \le K$ for all $k$.
7. The indices satisfy $n_0 < n_1 < \cdots$. By induction on $k$, $n_k \ge k$ for all $k$.
8. By the [[Archimedean property|0A74SX55QP]], there is a natural number $k$ with $k > K$.
9. For this $k$, steps 2 and 7 give $\abs{f(x_{n_k})} > n_k \ge k > K$. This contradicts step 6.
10. So $f$ is bounded: there is $K$ with $\abs{f(x)} \le K$ for all $x \in [a, b]$.

## Idea

If $f$ were unbounded, we could pick points where $\abs{f}$ exceeds $1, 2, 3, \dots$. These points have a convergent subsequence, and its limit stays in the closed interval. Continuity at that limit would force the values to converge, hence stay bounded, which they do not.
