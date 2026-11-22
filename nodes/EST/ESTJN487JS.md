---
tag: ESTJN487JS
kind: proof
name: Proof of the counts of vectors and ordered bases over a finite field
msc: ["15A03", "05A10"]
topics: [MVH97H8B2J]
audience: ug1
proves: PHTBCRD6WS
methods: [0NTF6DMVAP, 0ASJVEFA9J]
uses: [059THXBRBB, H75GS7QVPB, 096V7H13H9, 0VTQTPQGAV, 0EVHJFTG9Z]
sources:
  - url: https://en.wikipedia.org/wiki/General_linear_group
    locator: Over finite fields
---

## Proof

We count vectors through coordinates, and then we count independent lists by choosing one vector at a time.

1. Let $B = (b_1, \dots, b_n)$ be a [[basis|0VTQTPQGAV]] of $V$. By the [[isomorphism with the coordinate space|059THXBRBB]], the map $v \mapsto [v]_B$ is a bijection from $V$ onto $\mathbb{F}_q^n$.
2. A vector of $\mathbb{F}_q^n$ is a list of $n$ entries, each with $q$ possible values, so $|\mathbb{F}_q^n| = q^n$ by the product rule. By step 1, $|V| = q^n$, which proves part 1.
3. For part 2, let $N_k$ be the number of [[linearly independent|0EVHJFTG9Z]] lists $(c_1, \dots, c_k)$ in $V$, for $0 \le k \le n$. We prove by induction on $k$ that
$$N_k = \prod_{i = 0}^{k - 1} (q^n - q^i).$$
4. For $k = 0$, the empty list is independent and it is the only list of length $0$, so $N_0 = 1$, which is the empty product.
5. Let $(c_1, \dots, c_k)$ be independent with $k < n$, and let $S$ be its span. The list is a basis of $S$, so $|S| = q^k$ by part 1 applied to $S$.
6. If $c \in S$, then $c$ is a combination of $c_1, \dots, c_k$, so $(c_1, \dots, c_k, c)$ is dependent.
7. If $c \notin S$, suppose $a_1 c_1 + \dots + a_k c_k + a c = 0$. If $a \ne 0$, then $c = -a^{-1}(a_1 c_1 + \dots + a_k c_k)$ lies in $S$, which is false. So $a = 0$, and then all $a_i = 0$ because $(c_1, \dots, c_k)$ is independent. So $(c_1, \dots, c_k, c)$ is independent.
8. By steps 6 and 7, each independent list of length $k$ has exactly $q^n - q^k$ extensions to an independent list of length $k + 1$, and every independent list of length $k + 1$ arises once in this way from its first $k$ vectors. So $N_{k + 1} = N_k (q^n - q^k)$, which completes the induction.
9. In a space of dimension $n$, a list of $n$ vectors is a basis exactly when it is independent, by the [[right-size criterion|096V7H13H9]]. So the number of ordered bases is $N_n = \prod_{i = 0}^{n - 1} (q^n - q^i)$, which proves part 2.

## Idea

Coordinates turn each vector into a list of $n$ entries from $\mathbb{F}_q$, and that gives $q^n$ at once.
For the bases, we build a basis one vector at a time.
At each stage the forbidden vectors are exactly those in the span of the vectors already chosen, and that span has $q^k$ elements, so $q^n - q^k$ choices remain.
Step 7 is the [[linear dependence lemma|H75GS7QVPB]] in the special case that we need.

## Variants

Part 2 can also be read as the order of $\mathrm{GL}_n(\mathbb{F}_q)$, counted column by column: an $n \times n$ matrix is invertible exactly when each column lies outside the span of the earlier ones.
The counting is the same, with columns in place of basis vectors.
