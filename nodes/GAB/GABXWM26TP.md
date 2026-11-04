---
tag: GABXWM26TP
kind: proof
name: Proof that the integers are a Euclidean domain
msc: [11A05]
proves: 000JFQGDXG
uses: [0JHM6JK7FD, 09S3PFBEPM, 0GJ2HRG95T, 01BX15HSRR]
sources:
  - url: https://en.wikipedia.org/wiki/Euclidean_division
    locator: Proof, Existence
---

## Proof

We use the well-ordering principle. Let $\Z$ be the [[ring of integers|0JHM6JK7FD]].

1. The ring $\Z$ is commutative and $1 \neq 0$. If $a \neq 0$ and $b \neq 0$, then $\abs{a b} = \abs{a} \abs{b} \ge 1$, so $a b \neq 0$. So $\Z$ is an [[integral domain|09S3PFBEPM]].
2. For $n \neq 0$, $\delta(n) = \abs{n}$ is a natural number. So $\delta$ is a function $\Z \setminus \set{0} \to \N$.
3. Let $a, b \in \Z$ with $b \neq 0$. Let $S = \set{a - b q : q \in \Z} \cap \N$, where $\N$ contains $0$.
4. Let $q_0 = -\abs{a}$ if $b > 0$ and $q_0 = \abs{a}$ if $b < 0$. In both cases $b q_0 = -\abs{a} \abs{b}$.
5. Then $a - b q_0 = a + \abs{a} \abs{b} \ge a + \abs{a} \ge 0$, because $\abs{b} \ge 1$. So $a - b q_0 \in S$, and $S$ is nonempty.
6. By the [[well-ordering principle|01BX15HSRR]], $S$ has a least element $r$. Write $r = a - b q$ with $q \in \Z$, so $a = b q + r$ and $r \ge 0$.
7. Suppose that $r \ge \abs{b}$. Let $e = 1$ if $b > 0$ and $e = -1$ if $b < 0$, so that $b e = \abs{b}$.
8. Then $a - b (q + e) = r - \abs{b} \ge 0$, so $r - \abs{b} \in S$. But $r - \abs{b} < r$, because $\abs{b} \ge 1$. This contradicts the choice of $r$.
9. Hence $0 \le r < \abs{b}$. This proves the division with remainder in the statement.
10. If $r \neq 0$, then $\delta(r) = r < \abs{b} = \delta(b)$. So $r = 0$ or $\delta(r) < \delta(b)$.
11. By steps 1, 2 and 10, $\Z$ is a [[Euclidean domain|0GJ2HRG95T]] with Euclidean function $\delta(n) = \abs{n}$.

## Idea

Among all the nonnegative numbers $a - b q$, take the smallest one. If it were at least $\abs{b}$, we could subtract $\abs{b}$ once more and stay nonnegative, which would give a smaller one. So the smallest one is less than $\abs{b}$.
