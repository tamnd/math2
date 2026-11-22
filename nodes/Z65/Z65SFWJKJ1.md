---
tag: Z65SFWJKJ1
kind: proof
name: Proof of the Frobenius and Sylvester rank inequalities
msc: ["15A03"]
topics: [S6559D61BP]
audience: ug2
proves: GS8WE1ZYV9
uses: [0EWQEYRVA8, 0F0RPPJ2TT, 0PQ2GGY1QV, 0W4FSW1TVB, 073E4XC016, 0QW084460E]
methods: [0NTF6DMVAP]
sources:
  - url: https://en.wikipedia.org/wiki/Rank_(linear_algebra)
    locator: Properties
---

## Proof

We measure how much rank the map $x \mapsto Ax$ loses on a subspace, and we compare the loss on two nested subspaces.
Let $A$ be $m \times n$, $B$ be $n \times p$ and $C$ be $p \times q$ over a field $F$.

1. For a subspace $W \subseteq F^n$, let $A(W) = \{Aw : w \in W\}$, and let $L_W \colon W \to F^m$ be the linear map $L_W(w) = Aw$.
Its image is $A(W)$, and its kernel is $W \cap \operatorname{Null}(A)$, where $\operatorname{Null}(A)$ is the [[null space|0PQ2GGY1QV]] of $A$.
2. The [[rank-nullity theorem|0W4FSW1TVB]] for $L_W$ gives
$$\dim W - \dim A(W) = \dim\bigl(W \cap \operatorname{Null}(A)\bigr).$$
3. The [[column space|0F0RPPJ2TT]] of $B$ is $\{Bx : x \in F^p\}$, so $A(\operatorname{Col}(B)) = \{ABx : x \in F^p\} = \operatorname{Col}(AB)$.
4. In the same way, by [[associativity|073E4XC016]], $A(\operatorname{Col}(BC)) = \{(ABC)y : y \in F^q\} = \operatorname{Col}(ABC)$.
5. Put $W_1 = \operatorname{Col}(B)$ and $W_2 = \operatorname{Col}(BC)$.
Since $BCy = B(Cy)$, every vector of $W_2$ lies in $W_1$, so $W_2 \subseteq W_1$.
6. Steps 2 and 3 with $W = W_1$ and the [[definition of rank|0EWQEYRVA8]] give $\rank B - \rank(AB) = \dim(W_1 \cap \operatorname{Null}(A))$.
7. Steps 2 and 4 with $W = W_2$ give $\rank(BC) - \rank(ABC) = \dim(W_2 \cap \operatorname{Null}(A))$.
8. By step 5, $W_2 \cap \operatorname{Null}(A) \subseteq W_1 \cap \operatorname{Null}(A)$, so its dimension is not larger, by the [[dimension of a subspace|0QW084460E]].
9. Steps 6, 7 and 8 give
$$\rank(BC) - \rank(ABC) \le \rank B - \rank(AB),$$
which rearranges to part 1, $\rank(AB) + \rank(BC) \le \rank B + \rank(ABC)$.
10. For part 2, apply part 1 to the three matrices $A$, $I_n$ and $B$, of sizes $m \times n$, $n \times n$ and $n \times p$.
This gives $\rank A + \rank B \le \rank I_n + \rank(AB)$.
11. The columns of $I_n$ are the standard basis of $F^n$, so $\rank I_n = n$, and step 10 becomes $\rank A + \rank B - n \le \rank(AB)$.

## Idea

The rank that $A$ destroys on a subspace is the dimension of the part of that subspace that $A$ sends to zero.
A smaller subspace has a smaller such part, so it loses less rank.
Applied to $\operatorname{Col}(BC) \subseteq \operatorname{Col}(B)$, this is the Frobenius inequality.
With the identity matrix in the middle, $\operatorname{Col}(I_n)$ is all of $F^n$, the largest possible subspace, and we get Sylvester's inequality.

## Variants

Part 2 also follows from step 6 alone, without part 1.
The intersection $W_1 \cap \operatorname{Null}(A)$ lies in $\operatorname{Null}(A)$, so
$$\rank B - \rank(AB) \le \dim \operatorname{Null}(A) = n - \rank A,$$
by the [[rank-nullity theorem for matrices|TR48YQGCCA]] for $A$.
This short proof is the one to remember for Sylvester's inequality, while the nested version is needed for the Frobenius inequality.
