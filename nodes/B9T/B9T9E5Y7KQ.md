---
tag: B9T9E5Y7KQ
kind: proof
name: Proof that the real numbers are uncountable by nested intervals
msc: ["03E10"]
proves: 0518MM6BE1
uses: [0X55M9XET4, 0ZG61TFBES, 0PVG1CRAJN, 0TK8Y3J5RW, 0DSHAVH45F, MF56GK7QY2]
sources:
  - url: https://people.uwec.edu/daviscw/oldclasses/math316Spring2018/chapter1/lecture7/notes.pdf
    locator: Lemma 8 and Proposition 9
---

## Proof

We argue by contradiction, with nested closed intervals.

1. Suppose that $\R$ is [[countable|0ZG61TFBES]]. Then there is an [[injective function|0PVG1CRAJN]] $j \colon \R \to \N$.
2. Fix $n \in \N$. Since $j$ is injective, at most one real number $x$ satisfies $j(x) = n$.
3. Let $[a, b]$ be a closed [[interval|0TK8Y3J5RW]] with $a < b$, and put $d = (b - a)/3$. Let $L = [a, a + d]$ and $R = [b - d, b]$.
4. Since $a + d < b - d$, the intervals $L$ and $R$ are disjoint. By step 2, at least one of them contains no $x$ with $j(x) = n$.
5. Define $T(n, [a, b])$ to be $L$ if $L$ contains no $x$ with $j(x) = n$, and $R$ otherwise. By step 4, $T(n, [a, b])$ is a closed subinterval of $[a, b]$ of length $d > 0$ that contains no $x$ with $j(x) = n$.
6. By [[definition by recursion|0DSHAVH45F]], there are closed intervals $I_n = [a_n, b_n]$ with $I_0 = [0, 1]$ and $I_{n+1} = T(n, I_n)$ for each $n \in \N$. Each has $a_n < b_n$.
7. By step 5, $I_{n+1} \subseteq I_n$ for each $n$, and $I_{n+1}$ contains no real $x$ with $j(x) = n$.
8. By the [[nested intervals theorem|MF56GK7QY2]], applied to $I_1 \supseteq I_2 \supseteq \cdots$, there is a real number $y$ with $y \in I_n$ for all $n \ge 1$.
9. Let $m = j(y)$. Then $y \in I_{m+1}$ by step 8. But $I_{m+1}$ contains no $x$ with $j(x) = m$ by step 7. This is a contradiction.
10. Hence there is no injection $\R \to \N$, and $\R$ is [[uncountable|0X55M9XET4]].

## Idea

Each natural number $n$ labels at most one real number. At stage $n$ we shrink the interval to a third that avoids that real. The completeness of $\R$ gives a point in all the intervals, and this point has avoided its own label, which is absurd.
