---
tag: QY29R8PF9Z
kind: example
name: Coding the square root of two as a real number in second-order arithmetic
msc: ["03F35", "03B30"]
topics: [BY8AAFN7C5]
audience: grad
instance_of: [DC60FYCSPM]
uses: [DC60FYCSPM, Y92NXGEQBD, 08J2M1JYAG]
sources:
  - url: https://en.wikipedia.org/wiki/Second-order_arithmetic
    locator: Coding mathematics
---

## Example

In [[second-order arithmetic|DC60FYCSPM]] a real number is a sequence $(q_k)_{k \in \mathbb{N}}$ of rationals with $\lvert q_k - q_l \rvert \le 2^{-k}$ for all $k < l$.
We build such a sequence for $\sqrt{2}$, and we check that $\Delta^0_1$ comprehension already proves that it exists.

For each $k$, let $m_k$ be the largest natural number with $m_k^2 \le 2 \cdot 4^k$, and put $q_k = m_k / 2^k$.

1. We compute the first terms.
   The bounds $2 \cdot 4^k$ for $k = 0, \dots, 5$ are $2, 8, 32, 128, 512, 2048$, and the largest squares below them are $1, 4, 25, 121, 484, 2025$.
   So the terms are the fractions below.
$$q_0 = 1, \quad q_1 = \tfrac{2}{2}, \quad q_2 = \tfrac{5}{4}, \quad q_3 = \tfrac{11}{8}, \quad q_4 = \tfrac{22}{16}, \quad q_5 = \tfrac{45}{32}.$$
2. Check $k = 5$: $45^2 = 2025 \le 2048$ and $46^2 = 2116 > 2048$, so $m_5 = 45$.
3. Each $q_k$ is within $2^{-k}$ below $\sqrt{2}$.
   By the choice of $m_k$ we have $m_k^2 \le 2 \cdot 4^k < (m_k + 1)^2$, and dividing by $4^k$ gives $q_k^2 \le 2 < (q_k + 2^{-k})^2$.
   So $q_k \le \sqrt{2} < q_k + 2^{-k}$.
4. The sequence increases.
   For $k < l$, the number $2^{l-k} m_k$ has square $4^{l-k} m_k^2 \le 2 \cdot 4^l$, so $m_l \ge 2^{l-k} m_k$, and $q_l \ge q_k$.
5. The sequence meets the condition of a real.
   For $k < l$, steps 3 and 4 give $q_k \le q_l \le \sqrt{2} < q_k + 2^{-k}$, so $0 \le q_l - q_k < 2^{-k}$.
6. The sequence is computable.
   The relation $m = m_k$ is the condition $m^2 \le 2 \cdot 4^k < (m + 1)^2$, and $4^k$ is a primitive recursive function of $k$, so the relation is decidable.
7. So the set of codes of the pairs $(k, q_k)$ is defined by a $\Delta^0_1$ formula, and $\Delta^0_1$ comprehension proves that it exists.

This set is a code of $\sqrt{2}$.

## Remarks

The code is not unique.
The shifted sequence $q'_k = q_{k+1}$ is a second code, and step 5 gives $\lvert q_k - q'_k \rvert < 2^{-k} \le 2^{-k+1}$.
So the two codes are equal in the sense of the coded equality of reals, which allows a difference of $2^{-k+1}$ at place $k$.

The fixed rate $2^{-k}$ matters.
With it, the order $x < y$ becomes the $\Sigma^0_1$ statement "for some $k$, $q_k + 2^{-k+1} < r_k$".
Without a fixed rate, a Cauchy sequence gives no bound on how far its tail can still move, and a statement such as $x > 0$ needs more quantifiers.

The same method codes every computable [[real number|08J2M1JYAG]], so all such codes exist in the base system $\mathsf{RCA}_0$.
A real such as $\sum_k 2^{-h(k)}$, where $h$ lists the halting set, has no computable code, and $\mathsf{RCA}_0$ does not prove that it exists.

## Explanations

### L1 human

The theory has no real numbers as objects, only whole numbers and sets of them.
So a real number is given by a list of better and better fractions.
For $\sqrt{2}$ the list is $1, 1, 5/4, 11/8, 22/16, 45/32, \ldots$, and the $k$-th fraction is less than $2^{-k}$ below the true value.
For example, $45/32 = 1.40625$, and $\sqrt{2} - 1.40625 \approx 0.008$, which is less than $1/32 \approx 0.031$.

### L2 human

The method is general.
If a real has a computable list of approximations with errors at most $2^{-k}$, then the list is defined by a $\Delta^0_1$ formula, and $\mathsf{RCA}_0$ proves that the code exists.
This is how $\mathsf{RCA}_0$ gets $\pi$, $e$ and every algebraic number.

Watch out: do not code a real by its binary expansion.
Adding two expansions is not computable from them, since one digit of the sum can depend on all later digits of the summands.
For example, if the inputs begin $0.0111$ and $0.1000$, the sum is close to $1$.
No finite part of the inputs decides whether the digit of the sum before the point is $0$ or $1$.
The Cauchy code with a fixed rate avoids this problem.
