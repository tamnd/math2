---
tag: 0NTM3J5MFE
kind: statement
role: lemma
name: Discrete Grönwall inequality
msc: [26D15, 39A22]
uses: [07EJHQYR9A]
sources:
  - url: https://www.ceremade.dauphine.fr/~mischler/Enseignements/M2evol2018/chap0.pdf
    locator: Lemma 5.1 and (5.4)
    note: S. Mischler, lecture notes "Chapter 0, on the Gronwall lemma", Section 5. Lemma 5.1 is the product form of the remark. With 1 + c <= e^c it gives the statement, and (5.4) is the case of a constant c_k.
  - url: https://en.wikipedia.org/wiki/Gr%C3%B6nwall%27s_inequality
    locator: lead section
---

## Statement

Let $(u_k)_{k \ge 0}$ be a sequence of real numbers with $u_0 \ge 0$, and let $(b_k)_{k \ge 0}$ and $(c_k)_{k \ge 0}$ be sequences of non-negative real numbers.
Assume that $u_{k+1} \le (1 + c_k)\, u_k + b_k$ for each $k \ge 0$.
Then for each $n \ge 0$,
$$u_n \le \left( u_0 + \sum_{k=0}^{n-1} b_k \right) \exp\left( \sum_{k=0}^{n-1} c_k \right).$$

## Remarks

Proof idea: by induction, $u_n \le u_0 \prod_{k<n} (1 + c_k) + \sum_{k<n} b_k \prod_{k<j<n} (1 + c_j)$. Then use $1 + c \le e^{c}$.
It is the discrete analogue of [[Grönwall's inequality|07EJHQYR9A]], with sums in place of integrals.
It bounds the growth of errors in numerical methods such as the [[Euler method|0JARTXX4XP]].

## Explanations

### L1 human

At each step, the quantity grows at most by a factor $1 + c_k$ and an extra amount $b_k$.
The inequality says that the total growth is at most exponential in the sum of the rates.
