---
tag: FYQY3KVC7D
kind: proof
name: Proof of Bertrand's ballot theorem by reflection
msc: [05A15]
proves: 0FS972T0ZH
uses: [0AKNPYQ04R, 092GEF38YD, 0BFMR2FQ8B, 033KTKKRV6, 03QC59M99B, 0EE2V3CHFK, 0GV2573FP4, 0WFCGVMRRC]
sources:
  - url: https://en.wikipedia.org/wiki/Bertrand's_ballot_theorem
    locator: Proof by reflection
---

## Proof

We count the bad counting orders with André's reflection argument.

1. Let $p > q \ge 0$ be integers and $N = p + q$. A counting order gives a word $w = w_1 \cdots w_N$ with $p$ letters $A$ and $q$ letters $B$. Let $\Omega$ be the set of such words.
2. Each word arises from exactly $p!\, q!$ orders of the individual ballots. So a uniformly random order gives each word of $\Omega$ the same probability, and we may use the [[classical definition of probability|0AKNPYQ04R]] on $\Omega$.
3. A word is fixed by the positions of its $q$ letters $B$. By the [[number of $k$-element subsets|0BFMR2FQ8B]], $|\Omega|$ is the [[binomial coefficient|092GEF38YD]] $\binom{N}{q}$.
4. For $0 \le k \le N$, let $d_k$ be the number of letters $A$ minus the number of letters $B$ among $w_1, \dots, w_k$. Then $d_0 = 0$, $d_N = p - q > 0$, and $|d_{k+1} - d_k| = 1$.
5. The word is good if $d_k > 0$ for all $1 \le k \le N$, and bad otherwise.
6. If $q = 0$, the only word is $A \cdots A$, with $d_k = k > 0$. So the probability is $1 = \frac{p - 0}{p + 0}$. From now on let $q \ge 1$.
7. We claim that $w$ is bad exactly when $d_k = 0$ for some $k \ge 1$. If $d_k = 0$ with $k \ge 1$, then $w$ is bad by step 5.
8. Conversely, let $w$ be bad. If $w_1 = B$, then $d_1 = -1 < 0 < d_N$. Let $k$ be the least index with $d_k > 0$. Then $k \ge 2$ and $d_{k-1} \le 0$. Also $d_{k-1} \ge d_k - 1 \ge 0$, so $d_{k-1} = 0$ with $k - 1 \ge 1$.
9. If $w_1 = A$, then $d_1 = 1$, and some $j \ge 1$ has $d_j \le 0$. Let $k$ be the least such $j$. Then $d_{k-1} \ge 1$ and $d_k \ge d_{k-1} - 1 \ge 0$, so $d_k = 0$.
10. For a bad word $w$, let $k \ge 1$ be the least index with $d_k = 0$. Let $\rho(w)$ be the word obtained by exchanging $A$ and $B$ in $w_1, \dots, w_k$.
11. Since $d_k = 0$, the first $k$ letters have as many $A$ as $B$. So $\rho(w) \in \Omega$. Its differences are $-d_j$ for $j \le k$ and $d_j$ for $j \ge k$.
12. So $\rho(w)$ is bad, and $k$ is again its least index $\ge 1$ with difference $0$. Hence $\rho(\rho(w)) = w$, and $\rho$ is a bijection of the set of bad words to itself.
13. Since $k \ge 1$, $\rho$ changes the first letter. So $\rho$ maps the bad words that start with $A$ bijectively onto the bad words that start with $B$.
14. Every word that starts with $B$ is bad, because $d_1 = -1$. Such a word is fixed by the positions of its other $q - 1$ letters $B$ among $N - 1$ places. So there are $\binom{N-1}{q-1}$ of them.
15. By the [[bijection principle|0GV2573FP4]] and the [[rule of sum|0EE2V3CHFK]], there are $2 \binom{N-1}{q-1}$ bad words.
16. By the [[factorial formula|033KTKKRV6]] and $N! = N \cdot (N - 1)!$, $q! = q \cdot (q-1)!$ from the definition of the [[factorial|0WFCGVMRRC]],
$$\binom{N-1}{q-1} = \frac{(N-1)!}{(q-1)!\, p!} = \frac{q}{N} \cdot \frac{N!}{q!\, p!} = \frac{q}{N} \binom{N}{q}.$$
17. By the [[complement principle|03QC59M99B]], the number of good words is $\binom{N}{q} - \frac{2q}{N} \binom{N}{q} = \frac{p - q}{p + q} \binom{N}{q}$.
18. Dividing by $|\Omega| = \binom{N}{q}$, the probability that $A$ stays strictly ahead throughout the count is $\frac{p - q}{p + q}$.

## Idea

A bad count must reach a tie at some moment. Swapping the votes up to the first tie turns a bad count that starts with $A$ into one that starts with $B$, and back. Every count that starts with $B$ is bad, so the bad counts are twice those starting with $B$, a fraction $\frac{2q}{p+q}$.
