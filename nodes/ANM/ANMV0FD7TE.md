---
tag: ANMV0FD7TE
kind: proof
name: Proof of the discrete Grönwall inequality
msc: [26D15, 39A22]
proves: 0NTM3J5MFE
uses: [012C7GFF20, 0KN2V7840E]
sources:
  - url: https://www.ceremade.dauphine.fr/~mischler/Enseignements/M2evol2018/chap0.pdf
    locator: Lemma 5.1
---

## Proof

We argue by induction on $n$.

1. For $n \ge 0$ let $S_n = u_0 + \sum_{k=0}^{n-1} b_k$ and $E_n = \exp\left( \sum_{k=0}^{n-1} c_k \right)$. The claim is $u_n \le S_n E_n$.
2. Since $u_0 \ge 0$ and each $b_k \ge 0$, we have $S_n \ge 0$ and $S_{n+1} = S_n + b_n$.
3. Since each $c_k \ge 0$, the exponent of $E_n$ is non-negative. So $E_n \ge 1$, because [[the exponential function is increasing|0KN2V7840E]]. Also $E_{n+1} = e^{c_n} E_n$.
4. Base case: $S_0 = u_0$ and $E_0 = e^0 = 1$, so $u_0 \le S_0 E_0$ holds with equality.
5. Induction step: assume $u_n \le S_n E_n$ for some $n \ge 0$.
6. Since $1 + c_n \ge 1 > 0$, multiplying gives $(1 + c_n) u_n \le (1 + c_n) S_n E_n$.
7. By [[the inequality 1 + x ≤ exp x|012C7GFF20]], $1 + c_n \le e^{c_n}$. Since $S_n E_n \ge 0$ by steps 2 and 3, $(1 + c_n) S_n E_n \le e^{c_n} S_n E_n = S_n E_{n+1}$.
8. Since $b_n \ge 0$ and $E_{n+1} \ge 1$, we have $b_n \le b_n E_{n+1}$.
9. By the hypothesis and steps 6 to 8, $u_{n+1} \le (1 + c_n) u_n + b_n \le S_n E_{n+1} + b_n E_{n+1} = S_{n+1} E_{n+1}$.
10. By induction, $u_n \le S_n E_n$ for each $n \ge 0$. This is the stated inequality.

## Idea

At each step the bound is multiplied by at most $1 + c_k \le e^{c_k}$, and the new term $b_k$ is added. Since the exponential factor is at least $1$, the added terms can be put inside the same factor, so the whole bound is a sum times one exponential.
