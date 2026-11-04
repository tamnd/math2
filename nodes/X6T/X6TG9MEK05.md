---
tag: X6TG9MEK05
kind: proof
name: Proof of the Chapman–Kolmogorov equation
msc: [60J10]
proves: 01APZ8GDQH
uses: [033TJBZDG0, 0F1KBVY161, 0HB8SXHPFA, 0FJB06AD2P, 067SYD2J4B, 076JGP6R3T]
sources:
  - url: https://en.wikipedia.org/wiki/Chapman–Kolmogorov_equation
    locator: Application to time-dilated Markov chains
---

## Proof

We show by induction on $n$ that the $n$-step transition probabilities are the entries of the matrix power $P^n$. The equation then follows from $P^{m+n} = P^m P^n$.

1. Let $P = (p_{ij})$ be the [[transition matrix|0F1KBVY161]] of the [[Markov chain|033TJBZDG0]], with $p_{ij} = P(X_{r+1} = j \mid X_r = i)$ whenever $P(X_r = i) > 0$. A row $i$ with $P(X_r = i) = 0$ for all $r$ is not determined by the chain; we fix it as any probability distribution on $S$.
2. For matrices $A, B$ on $S$ with nonnegative entries, the [[product|076JGP6R3T]] $(AB)_{ij} = \sum_{k \in S} a_{ik} b_{kj}$ is a sum of nonnegative terms. Let $P^0$ be the identity matrix and $P^{n+1} = P^n P$.
3. By induction, each $P^n$ has nonnegative entries and rows that sum to $1$: $\sum_j (P^n P)_{ij} = \sum_k (P^n)_{ik} \sum_j p_{kj} = 1$. Exchanging the two sums is allowed for nonnegative terms, by [[Tonelli's theorem|067SYD2J4B]] for counting measure.
4. For nonnegative matrices $A, B, C$ on $S$, $((AB)C)_{ij} = \sum_l \sum_k a_{ik} b_{kl} c_{lj} = (A(BC))_{ij}$, again by exchanging sums of nonnegative terms. By induction on $n$ with this rule, $P^{m+n} = P^m P^n$ for all $m, n \ge 0$.
5. Lemma: let $m \le r$ and $i, k, j \in S$. Then $P(X_m = i, X_r = k, X_{r+1} = j) = P(X_m = i, X_r = k) \, p_{kj}$.
6. Proof of the lemma: the event $\set{X_m = i, X_r = k}$ is the countable disjoint union of the events $H = \set{X_0 = i_0, \dots, X_r = i_r}$ over the histories with $i_m = i$ and $i_r = k$.
7. If $P(H) > 0$, then $P(X_r = k) > 0$. The [[Markov property|0HB8SXHPFA]] in the definition of the chain and time-homogeneity give $P(H \cap \set{X_{r+1} = j}) = P(H) \, P(X_{r+1} = j \mid X_r = k) = P(H) \, p_{kj}$.
8. If $P(H) = 0$, both sides of the equation in step 7 are $0$. Summing over all histories $H$, by countable additivity, proves the lemma.
9. Claim: for $m, n \ge 0$ and $i \in S$ with $P(X_m = i) > 0$, $P(X_{m+n} = j \mid X_m = i) = (P^n)_{ij}$ for all $j$. We argue by induction on $n$.
10. For $n = 0$, $P(X_m = j \mid X_m = i)$ is $1$ if $j = i$ and $0$ otherwise. This is the entry $(P^0)_{ij}$ of the identity matrix.
11. Assume the claim for $n$. By countable additivity over the value $k$ of $X_{m+n}$, $P(X_m = i, X_{m+n+1} = j) = \sum_{k} P(X_m = i, X_{m+n} = k, X_{m+n+1} = j)$.
12. By the lemma with $r = m + n$, this equals $\sum_k P(X_m = i, X_{m+n} = k) \, p_{kj}$.
13. By the definition of [[conditional probability|0FJB06AD2P]] and the induction hypothesis, $P(X_m = i, X_{m+n} = k) = P(X_m = i) \, (P^n)_{ik}$.
14. So $P(X_m = i, X_{m+n+1} = j) = P(X_m = i) \sum_k (P^n)_{ik} p_{kj} = P(X_m = i) \, (P^{n+1})_{ij}$. Divide by $P(X_m = i)$ to get the claim for $n + 1$.
15. By step 9, the $n$-step transition probability $p^{(n)}_{ij}$ does not depend on $m$, and $p^{(n)}_{ij} = (P^n)_{ij}$. Where no $m$ has $P(X_m = i) > 0$, we set $p^{(n)}_{ij} = (P^n)_{ij}$, as in step 1. So $P^{(n)} = P^n$.
16. By step 4, $p^{(m+n)}_{ij} = (P^{m+n})_{ij} = (P^m P^n)_{ij} = \sum_{k \in S} p^{(m)}_{ik} \, p^{(n)}_{kj}$. In matrix form, $P^{(m+n)} = P^{(m)} P^{(n)}$.

## Idea

To go from $i$ to $j$ in $m + n$ steps, the chain must pass through some state $k$ at time $m$. The Markov property says that the chain forgets how it reached $k$. So the probabilities of the two parts of the path multiply, and summing over $k$ is a matrix product.
