---
tag: 6KYGXABK4Y
kind: proof
name: Proof that a nontrivial finite p-group has nontrivial centre by the class equation
msc: [20D15]
proves: 0RZCTT30H5
uses: [06DAH3VS6M, 0JM7PA288B, 051VYKA1EX, 084HH1NDCB, 08BPSC6YTE, 0VK5V9P8G3, 0S7Y9Q990Q]
sources:
  - url: https://en.wikipedia.org/wiki/Conjugacy_class
    locator: Conjugacy class equation
---

## Proof

We reduce the class equation modulo $p$. Let $e$ be the identity of $G$.

1. First, $\abs{G} = p^r$ with $r \geq 1$. Let $q$ be a prime that divides $\abs{G}$; one exists since $\abs{G} > 1$. By [[Cauchy's theorem|0JM7PA288B]], some element of $G$ has order $q$.
2. Since $G$ is a [[$p$-group|06DAH3VS6M]], that order is a power of $p$. As $q$ is prime, $q = p$.
3. So $p$ is the only prime factor of $\abs{G}$, and $\abs{G} = p^r$ by the [[fundamental theorem of arithmetic|084HH1NDCB]]. Since $\abs{G} > 1$, $r \geq 1$.
4. Each positive divisor $d$ of $p^r$ is a power of $p$. Indeed, a prime factor of $d$ divides $p^r$. So it divides $p$ by [[Euclid's lemma|051VYKA1EX]], and it equals $p$.
5. By the [[class equation|08BPSC6YTE]], $\abs{G} = \abs{Z(G)} + \sum_{i=1}^{k} [G : C_G(a_i)]$, where $\operatorname{Cl}(a_1), \dots, \operatorname{Cl}(a_k)$ are the conjugacy classes with more than one element.
6. By the [[class size formula|0VK5V9P8G3]], $[G : C_G(a_i)] = \abs{\operatorname{Cl}(a_i)}$, which divides $\abs{G} = p^r$ and is greater than $1$.
7. By step 4, each $[G : C_G(a_i)]$ is $p^j$ with $j \geq 1$, so $p$ divides it. Also $p$ divides $\abs{G}$, by step 3.
8. Therefore $p$ divides $\abs{Z(G)} = \abs{G} - \sum_{i} [G : C_G(a_i)]$.
9. The [[centre|0S7Y9Q990Q]] contains $e$, so $\abs{Z(G)} \geq 1$. A positive multiple of $p$ is at least $p \geq 2$. So $Z(G) \neq \set{e}$.

## Idea

In the class equation every class outside the centre has size a positive power of $p$, and so does the whole group. Modulo $p$ these terms vanish, so the number of central elements is a multiple of $p$. It is not zero, because the identity is central, so it is at least $p$.
