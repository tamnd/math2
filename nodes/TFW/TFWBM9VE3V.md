---
tag: TFWBM9VE3V
kind: proof
name: Proof of the recurrence for Stirling numbers of the first kind
msc: [11B73]
proves: 0C5BFX94J9
uses: [0Z22VQH17V, 0BQMWCNS8S, 0YWDAZPRPQ, 0EE2V3CHFK, 0GV2573FP4]
sources:
  - url: https://en.wikipedia.org/wiki/Stirling_numbers_of_the_first_kind
    locator: Recurrence relation
---

## Proof

We remove the last element from its cycle and count each case by a bijection.

1. Let $\sigma$ be a [[permutation|0BQMWCNS8S]] of a finite set $X$. For $x \in X$, the cycle of $\sigma$ through $x$ is the set $\set{\sigma^t(x) : t \ge 0}$.
2. By the [[decomposition into disjoint cycles|0YWDAZPRPQ]], these sets are the moved sets of the cycles of $\sigma$, together with the singletons of fixed points. They partition $X$, and their number is the number of cycles of $\sigma$ in the definition of the [[Stirling numbers of the first kind|0Z22VQH17V]].
3. If $x$ lies in a cycle with $L$ elements, then $x, \sigma(x), \dots, \sigma^{L-1}(x)$ are its elements, all distinct, and $\sigma^L(x) = x$.
4. Let $n$ and $k$ be natural numbers. Let $X = \set{1, \dots, n + 1}$, let $z = n + 1$, and let $Y = \set{1, \dots, n}$. We count the permutations of $X$ with $k + 1$ cycles.
5. Case $\sigma(z) = z$. Then $\set{z}$ is a cycle, and $\sigma$ restricts to a permutation of $Y$. Its cycles are the other $k$ cycles of $\sigma$.
6. Conversely, a permutation of $Y$ with $k$ cycles, extended by $z \mapsto z$, gives such a $\sigma$. These maps are inverse to each other, so this case has $c(n, k)$ permutations.
7. Case $\sigma(z) \ne z$. Let $j = \sigma^{-1}(z)$, so $j \in Y$. Define $\tau : Y \to Y$ by $\tau(j) = \sigma(z)$ and $\tau(x) = \sigma(x)$ for $x \in Y \setminus \set{j}$.
8. The map $\tau$ is a bijection of $Y$. Indeed, $\sigma$ maps $Y \setminus \set{j}$ onto $X \setminus \set{z, \sigma(z)}$, and $\tau(j) = \sigma(z)$ supplies the missing value.
9. Let $C$ be the cycle of $\sigma$ through $z$, with $L$ elements. Write $a_t = \sigma^t(z)$ for $1 \le t \le L - 1$. Since $\sigma(z) \ne z$, $L \ge 2$, and $a_{L-1} = j$ because $\sigma(a_{L-1}) = z$.
10. For $1 \le t < L - 1$, $a_t \ne j$, so $\tau(a_t) = a_{t+1}$. Also $\tau(a_{L-1}) = \tau(j) = a_1$.
11. So $C \setminus \set{z} = \set{a_1, \dots, a_{L-1}}$ is a cycle of $\tau$, with $L - 1 \ge 1$ elements.
12. Any other cycle $C'$ of $\sigma$ avoids $z$ and $j$, since $j \in C$. On $C'$ the maps $\tau$ and $\sigma$ agree, so $C'$ is also a cycle of $\tau$.
13. The sets of steps 11 and 12 partition $Y$, so they are all the cycles of $\tau$. Hence $\tau$ has as many cycles as $\sigma$, namely $k + 1$.
14. Map $\sigma$ to the pair $(\tau, j)$, where $\tau$ is a permutation of $Y$ with $k + 1$ cycles and $j \in Y$.
15. Conversely, let $\tau$ be a permutation of $Y$ with $k + 1$ cycles, and let $j \in Y$. Define $\sigma$ on $X$ by $\sigma(j) = z$, $\sigma(z) = \tau(j)$, and $\sigma(x) = \tau(x)$ for the other $x$.
16. This $\sigma$ is a permutation of $X$, because $\tau$ maps $Y \setminus \set{j}$ onto $Y \setminus \set{\tau(j)}$. Also $\sigma(z) = \tau(j) \ne z$ and $\sigma^{-1}(z) = j$. Applying step 7 to it gives back $\tau$, because $\tau(j) = \sigma(z)$. So by step 13, $\sigma$ has $k + 1$ cycles.
17. Starting from $\sigma$, step 15 applied to $(\tau, j)$ gives back $\sigma$, since $\sigma(j) = z$ and $\sigma(z) = \tau(j)$. So the maps of steps 14 and 15 are inverse to each other.
18. By the [[bijection principle|0GV2573FP4]] and the [[rule of sum|0EE2V3CHFK]] over the $n$ choices of $j$, this case has $n\, c(n, k + 1)$ permutations.
19. The two cases are disjoint and cover all permutations of $X$ with $k + 1$ cycles. By the rule of sum,
$$c(n + 1, k + 1) = n\, c(n, k + 1) + c(n, k).$$

## Idea

Delete $z$ from the permutation: if $z$ is a fixed point, one cycle disappears. Otherwise, link the element before $z$ directly to the element after $z$, which keeps the number of cycles. This element before $z$ can be any of the $n$ other elements, which gives the factor $n$.
