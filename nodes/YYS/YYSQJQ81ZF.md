---
tag: YYSQJQ81ZF
kind: proof
name: Proof that independence means the joint law is the product of the marginals
msc: [60A05]
proves: 08QCA2F1NX
uses: [0E9502NT92, 0QAR0XDZH4, 0AXP2Z5N9H, 0TST4MHA3A, 0DKRR22AEQ, 9ZP4ER2N65, M8X6VZD91K, WEBBT18D4X, 0VGMEBVW1M, 04WSW8T3SY, 0FGCFY1AZX]
sources:
  - url: https://www.math.cmu.edu/~ttkocz/teaching/1920/prob-grad-notes.pdf
---

## Proof

1. Let $(\Omega, \mathcal{F}, P)$ be the probability space. Let $X$ and $Y$ be [[random variables|0DKRR22AEQ]] with values in $(E_1, \mathcal{E}_1)$ and $(E_2, \mathcal{E}_2)$.
2. Let $Z \colon \Omega \to E_1 \times E_2$ be $Z(\omega) = (X(\omega), Y(\omega))$. Let $\pi_1$ and $\pi_2$ be the coordinate projections of $E_1 \times E_2$.
3. Let $\mathcal{G}$ be the family of sets $C \subseteq E_1 \times E_2$ whose [[preimage|0FGCFY1AZX]] $Z^{-1}(C)$ lies in $\mathcal{F}$.
4. $\mathcal{G}$ is a [[σ-algebra|04WSW8T3SY]]. Indeed $Z^{-1}(E_1 \times E_2) = \Omega$, preimages commute with complements, and the preimage of a union is the union of the preimages.
5. For $A \in \mathcal{E}_1$, $\pi_1^{-1}(A) = A \times E_2$ and $Z^{-1}(A \times E_2) = X^{-1}(A) \in \mathcal{F}$. In the same way $Z^{-1}(\pi_2^{-1}(B)) = Y^{-1}(B) \in \mathcal{F}$ for $B \in \mathcal{E}_2$.
6. So $\mathcal{G}$ contains the generators of the [[product σ-algebra|M8X6VZD91K]] $\mathcal{E}_1 \otimes \mathcal{E}_2$. Hence $\mathcal{E}_1 \otimes \mathcal{E}_2 \subseteq \mathcal{G}$.
7. By step 6 the [[joint law|0QAR0XDZH4]] $\mu_{(X, Y)}(C) = P(Z^{-1}(C))$ is defined for all $C \in \mathcal{E}_1 \otimes \mathcal{E}_2$.
8. $\mu_{(X, Y)}$ is a [[probability measure|0VGMEBVW1M]]. Its total mass is $P(\Omega) = 1$. Disjoint sets have disjoint preimages, and preimages respect unions, so countable additivity of $P$ passes to $\mu_{(X, Y)}$.
9. The same argument shows that the [[laws|0TST4MHA3A]] $\mu_X(A) = P(X \in A)$ and $\mu_Y(B) = P(Y \in B)$ are probability measures.
10. They are the [[marginal laws|0AXP2Z5N9H]] of $\mu_{(X, Y)}$: by step 5, $\mu_{(X, Y)}(A \times E_2) = \mu_X(A)$ and $\mu_{(X, Y)}(E_1 \times B) = \mu_Y(B)$.
11. Let $A \in \mathcal{E}_1$ and $B \in \mathcal{E}_2$. Then $A \times B = \pi_1^{-1}(A) \cap \pi_2^{-1}(B)$ lies in $\mathcal{E}_1 \otimes \mathcal{E}_2$, and $Z^{-1}(A \times B) = X^{-1}(A) \cap Y^{-1}(B)$.
12. So $\mu_{(X, Y)}(A \times B) = P(X \in A, \, Y \in B)$ for all $A \in \mathcal{E}_1$ and $B \in \mathcal{E}_2$.
13. The measures $\mu_X$ and $\mu_Y$ are finite, so they are [[σ-finite|WEBBT18D4X]]. Hence the [[product measure|9ZP4ER2N65]] $\mu_X \otimes \mu_Y$ exists.
14. By its definition, $\mu_X \otimes \mu_Y$ is the unique measure on $\mathcal{E}_1 \otimes \mathcal{E}_2$ with $(\mu_X \otimes \mu_Y)(A \times B) = P(X \in A) \, P(Y \in B)$ for all $A$ and $B$.
15. Suppose that $X$ and $Y$ are [[independent|0E9502NT92]]. Then step 12 gives $\mu_{(X, Y)}(A \times B) = P(X \in A) \, P(Y \in B)$ for all $A \in \mathcal{E}_1$ and $B \in \mathcal{E}_2$.
16. So $\mu_{(X, Y)}$ is a measure on $\mathcal{E}_1 \otimes \mathcal{E}_2$ with the property of step 14. By the uniqueness in step 14, $\mu_{(X, Y)} = \mu_X \otimes \mu_Y$.
17. Conversely, suppose that $\mu_{(X, Y)} = \mu_X \otimes \mu_Y$. Evaluating both sides at $A \times B$ and using steps 12 and 14 gives $P(X \in A, \, Y \in B) = P(X \in A) \, P(Y \in B)$.
18. This holds for all $A \in \mathcal{E}_1$ and $B \in \mathcal{E}_2$, so $X$ and $Y$ are independent.

## Idea

On a rectangle $A \times B$, the joint law gives $P(X \in A, Y \in B)$ and the product measure gives $P(X \in A) P(Y \in B)$. Independence says exactly that these agree. A measure on the product σ-algebra is determined by its values on rectangles, so agreement on rectangles is the same as equality of the measures.
