---
tag: W8AH11V0NN
kind: proof
name: Proof of Kolmogorov's zero–one law
msc: [60F20]
proves: 073Q8Z94KG
uses: [0XCE070V8B, 09T8ZHST1V, 04WSW8T3SY, AQN6ZN66NK, 69460Z6DMW, BBHM1A36M7, 0X8HBKCSYB]
sources:
  - url: https://sites.math.duke.edu/~rtd/PTE/PTE5_011119.pdf
    locator: Theorem 2.5.3 and Theorem 2.1.7
---

## Proof

We show that each tail event is independent of itself. The tool is Dynkin's π-λ theorem.

1. For each $i$, let $X_i$ take values in a measurable space $(E_i, \mathcal{E}_i)$. For $k \ge 0$, let $\mathcal{F}_k = \sigma(X_1, \dots, X_k)$, with $\mathcal{F}_0 = \set{\varnothing, \Omega}$, and let $\mathcal{G}_k = \sigma(X_{k+1}, X_{k+2}, \dots)$.
2. Lemma: let $\mathcal{P}, \mathcal{Q} \subseteq \mathcal{F}$ be [[π-systems|AQN6ZN66NK]] with $P(A \cap B) = P(A) P(B)$ for all $A \in \mathcal{P}$ and $B \in \mathcal{Q}$. Then the same holds for all $A \in \sigma(\mathcal{P})$ and $B \in \sigma(\mathcal{Q})$.
3. Proof of the lemma: fix $B \in \mathcal{Q}$ and let $\mathcal{D}_B = \set{A \in \mathcal{F} : P(A \cap B) = P(A) P(B)}$. It contains $\Omega$, since $P(\Omega \cap B) = P(B)$.
4. If $A \subseteq A'$ are in $\mathcal{D}_B$, then $(A' \setminus A) \cap B = (A' \cap B) \setminus (A \cap B)$. So $P((A' \setminus A) \cap B) = (P(A') - P(A)) P(B) = P(A' \setminus A) P(B)$.
5. If $A_1 \subseteq A_2 \subseteq \cdots$ are in $\mathcal{D}_B$ with union $A$, then $A_j \cap B$ increase to $A \cap B$. By the [[continuity of probability|0X8HBKCSYB]], $P(A \cap B) = \lim_j P(A_j) P(B) = P(A) P(B)$.
6. By steps 3 to 5, $\mathcal{D}_B$ is a [[Dynkin system|69460Z6DMW]]. It contains $\mathcal{P}$ by hypothesis. By [[Dynkin's π-λ theorem|BBHM1A36M7]], $\sigma(\mathcal{P}) \subseteq \mathcal{D}_B$.
7. Now fix $A \in \sigma(\mathcal{P})$ and let $\mathcal{D}'_A = \set{B \in \mathcal{F} : P(A \cap B) = P(A) P(B)}$. By step 6, it contains $\mathcal{Q}$. The argument of steps 3 to 5, with the roles exchanged, shows that it is a Dynkin system.
8. By the π-λ theorem, $\sigma(\mathcal{Q}) \subseteq \mathcal{D}'_A$. This proves the lemma.
9. Fix $k \ge 0$. Let $\mathcal{P}_k$ be the family of sets $\bigcap_{i=1}^{k} \set{X_i \in B_i}$ with $B_i \in \mathcal{E}_i$, where the empty intersection is $\Omega$.
10. $\mathcal{P}_k$ is a π-system, since $\set{X_i \in B} \cap \set{X_i \in B'} = \set{X_i \in B \cap B'}$. It lies in $\mathcal{F}_k$, and it contains each set $\set{X_i \in B}$ with $i \le k$, by taking the other $B_j = E_j$.
11. So each $X_i$ with $i \le k$ is measurable for $\sigma(\mathcal{P}_k)$. By the minimality of $\mathcal{F}_k$, $\mathcal{F}_k \subseteq \sigma(\mathcal{P}_k) \subseteq \mathcal{F}_k$, so $\sigma(\mathcal{P}_k) = \mathcal{F}_k$.
12. Let $\mathcal{Q}_k$ be the family of sets $\bigcap_{i=k+1}^{k+j} \set{X_i \in B_i}$ with $j \ge 1$ and $B_i \in \mathcal{E}_i$. Two such sets can be written with the same $j$, by adding factors with $B_i = E_i$.
13. So, as in steps 10 and 11, $\mathcal{Q}_k$ is a π-system with $\sigma(\mathcal{Q}_k) = \mathcal{G}_k$.
14. For $A = \bigcap_{i \le k} \set{X_i \in B_i} \in \mathcal{P}_k$ and $B = \bigcap_{i = k+1}^{k+j} \set{X_i \in B_i} \in \mathcal{Q}_k$, the [[independence|0XCE070V8B]] of $X_1, \dots, X_{k+j}$ gives $P(A \cap B) = \prod_{i=1}^{k+j} P(X_i \in B_i) = P(A) P(B)$.
15. By steps 14 and 2, $P(A \cap B) = P(A) P(B)$ for all $A \in \mathcal{F}_k$ and $B \in \mathcal{G}_k$.
16. Let $\mathcal{T}$ be the tail σ-algebra. By definition, $\mathcal{T} \subseteq \mathcal{G}_k$ for every $k$. So step 15 gives $P(A \cap B) = P(A) P(B)$ for $A \in \bigcup_k \mathcal{F}_k$ and $B \in \mathcal{T}$.
17. Let $\mathcal{U} = \bigcup_{k \ge 0} \mathcal{F}_k$. The $\mathcal{F}_k$ increase, so two sets of $\mathcal{U}$ lie in a common $\mathcal{F}_k$, and so does their intersection. Thus $\mathcal{U}$ is a π-system.
18. Each $\set{X_m \in B}$ lies in $\mathcal{F}_m \subseteq \mathcal{U}$, and $\mathcal{U} \subseteq \mathcal{G}_0 = \sigma(X_1, X_2, \dots)$. As in step 11, $\sigma(\mathcal{U}) = \mathcal{G}_0$.
19. $\mathcal{T}$ is a [[σ-algebra|04WSW8T3SY]], as an intersection of σ-algebras. So it is a π-system with $\sigma(\mathcal{T}) = \mathcal{T}$.
20. By steps 16 to 19 and the lemma, $P(A \cap B) = P(A) P(B)$ for all $A \in \mathcal{G}_0$ and $B \in \mathcal{T}$. So $\mathcal{G}_0$ and $\mathcal{T}$ are [[independent σ-algebras|09T8ZHST1V]].
21. Let $A \in \mathcal{T}$. Since $\mathcal{T} \subseteq \mathcal{G}_0$, step 20 applies with $B = A$, and gives $P(A) = P(A \cap A) = P(A)^2$.
22. The only real solutions of $p = p^2$ are $p = 0$ and $p = 1$. Hence $P(A) \in \set{0, 1}$.

## Idea

A tail event does not depend on any finite group $X_1, \dots, X_k$, so it is independent of all of them. The π-λ theorem upgrades this to independence from the whole σ-algebra $\sigma(X_1, X_2, \dots)$. That σ-algebra contains the tail event itself, so the event is independent of itself, and $P(A) = P(A)^2$.
