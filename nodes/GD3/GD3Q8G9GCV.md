---
tag: GD3Q8G9GCV
kind: definition
name: Free probability
msc: [46L54, 46L53]
defines: 11KYREAH1J
uses: [0KTW26C80J, TM7QS7P7X9, 0NFPJVJJHX]
sources:
  - url: https://en.wikipedia.org/wiki/Free_probability
---

## Definition

A *noncommutative probability space* is a pair $(A, \varphi)$ where $A$ is a unital [[algebra|1SENAHZW5A]] over $\C$ and $\varphi \colon A \to \C$ is a linear functional with $\varphi(1) = 1$.
Elements of $A$ are called noncommutative random variables.
Let $(A_i)_{i \in I}$ be a family of unital subalgebras of $A$.
They are *freely independent*, or *free*, if the following holds.
Whenever $n \ge 1$, $a_j \in A_{i(j)}$ and $\varphi(a_j) = 0$ for all $j$, and consecutive indices differ, $i(1) \ne i(2) \ne \cdots \ne i(n)$, then
$$\varphi(a_1 a_2 \cdots a_n) = 0.$$
Elements of $A$ are free if the unital subalgebras they generate are free.
*Free probability* is the study of noncommutative probability spaces and of free independence.

## Remarks

Example: let $F_2$ be the [[free group|0KTW26C80J]] on generators $a$ and $b$, let $A = \C[F_2]$ be its group algebra, and let $\varphi(\sum_g c_g g) = c_e$, the coefficient of the identity.
Then the subalgebras $A_1 = \C[\langle a \rangle]$ and $A_2 = \C[\langle b \rangle]$ are free.
An element of $A_1$ with $\varphi = 0$ is a combination of powers $a^k$ with $k \ne 0$, and likewise for $A_2$.
A product of such elements with alternating indices is a combination of alternating words $a^{k_1} b^{l_1} a^{k_2} \cdots$ with nonzero exponents.
These are reduced words, hence not the identity, so $\varphi$ of the product is $0$.
The same argument works for any [[free product|TM7QS7P7X9]] of groups.

Non-example: classically independent variables are not free.
Let $A = L^\infty(\Omega, P)$ for a [[probability space|0NFPJVJJHX]] $(\Omega, P)$, $\varphi$ the expectation, and $x, y$ independent with mean $0$ and nonzero variance.
Then $\varphi(xyxy) = \varphi(x^2)\varphi(y^2) \ne 0$, although the indices alternate, so the defining condition fails.

Often $A$ is a C*-algebra or a von Neumann algebra and $\varphi$ is a state, frequently a faithful trace.
Freeness determines all mixed moments of free variables from their separate moments, as independence does classically.
