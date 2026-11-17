---
tag: 1ZHGAPYG2H
kind: proof
name: Proof of general associativity
msc: [08A02, 20A05]
topics: [BAZT8JJ70S]
audience: ug1
proves: 8HEYE9EZMW
uses: [0K8F7PVDMX, 0ASJVEFA9J]
methods: [0ASJVEFA9J]
sources:
  - book: isbn:9780471433347
    locator: Section 1.1
---

## Proof

We use the notation of the [[statement|8HEYE9EZMW]]: $\ast$ is an [[associative|0K8F7PVDMX]] operation on $S$, and $[a_1 \cdots a_n]$ is the left product.

Lemma: for $n \geq 2$, $1 \leq k \leq n - 1$ and $a_1, \ldots, a_n \in S$, we have $[a_1 \cdots a_k] \ast [a_{k+1} \cdots a_n] = [a_1 \cdots a_n]$.

1. We prove the lemma by [[induction|0ASJVEFA9J]] on $m = n - k$, the length of the second part. The claim for $m$ is: the lemma holds for all $n$ and $k$ with $n - k = m$.
2. Case $m = 1$. Then $k = n - 1$, and $[a_n] = a_n$ by the definition of the left product. So the left side is $[a_1 \cdots a_{n-1}] \ast a_n$, which is $[a_1 \cdots a_n]$ by the definition.
3. Case $m \geq 2$. Assume the claim for $m - 1$. Since the second part $a_{k+1}, \ldots, a_n$ has $m \geq 2$ elements, the definition gives $[a_{k+1} \cdots a_n] = [a_{k+1} \cdots a_{n-1}] \ast a_n$.
4. Put $x = [a_1 \cdots a_k]$ and $y = [a_{k+1} \cdots a_{n-1}]$. By step 3, the left side of the lemma is $x \ast (y \ast a_n)$.
5. By associativity, $x \ast (y \ast a_n) = (x \ast y) \ast a_n$.
6. The sequence $a_1, \ldots, a_{n-1}$ is split after position $k$, and its second part has $(n - 1) - k = m - 1 \geq 1$ elements. By the claim for $m - 1$, $x \ast y = [a_1 \cdots a_{n-1}]$.
7. By steps 5 and 6, the left side is $[a_1 \cdots a_{n-1}] \ast a_n$, which is $[a_1 \cdots a_n]$ by the definition. This proves the claim for $m$, and so the lemma.

Proposition: each bracketing of $a_1, \ldots, a_n$ equals $[a_1 \cdots a_n]$.

8. We use strong induction on $n$. The claim for $n$ is: for all $a_1, \ldots, a_n \in S$, each bracketing of $a_1, \ldots, a_n$ equals $[a_1 \cdots a_n]$.
9. Case $n = 1$. The only bracketing is $a_1$, and $[a_1] = a_1$ by the definition.
10. Case $n \geq 2$. Assume the claim for all lengths smaller than $n$. Let $z$ be a bracketing of $a_1, \ldots, a_n$. By the definition of a bracketing, $z = x \ast y$, where $x$ is a bracketing of $a_1, \ldots, a_k$ and $y$ is a bracketing of $a_{k+1}, \ldots, a_n$, for some $k$ with $1 \leq k \leq n - 1$.
11. The lengths $k$ and $n - k$ are both smaller than $n$, because $1 \leq k \leq n - 1$. By the induction hypothesis, $x = [a_1 \cdots a_k]$ and $y = [a_{k+1} \cdots a_n]$.
12. So $z = [a_1 \cdots a_k] \ast [a_{k+1} \cdots a_n]$, and this is $[a_1 \cdots a_n]$ by the lemma.
13. This proves the claim for $n$. By strong induction, the claim holds for all $n \geq 1$, so all the bracketings of $a_1, \ldots, a_n$ are equal to one element, $[a_1 \cdots a_n]$.

## Idea

We compare each bracketing with one fixed bracketing, the left product $((a_1 a_2) a_3) \cdots a_n$.
A bracketing is a product $x \ast y$ of two shorter bracketings, and by induction these are left products.
The lemma then joins two left products into one left product, and its proof moves the factors of the second part to the left one at a time with the law $(xy)z = x(yz)$.

## Variants

A second proof uses the right product $a_1 \ast (a_2 \ast (\cdots \ast a_n))$ as the fixed bracketing, with the same structure.
A third proof uses a normal form.
It shows that a finite number of uses of the rewrite rule $x(yz) \to (xy)z$ changes each bracketing into the left product.
The induction is on the number of factors in the right part of the outer product.
