---
tag: 9ZK3H3XEP9
kind: proof
name: Proof of the closed formula for Catalan numbers by the reflection principle
msc: [05A15]
proves: 0NNDQVJ54Q
uses: [017SRZ7NE9, 0R9JR0465V, 092DRBFKMG, 092GEF38YD, 0BFMR2FQ8B, 033KTKKRV6, 03QC59M99B, 0GV2573FP4, 0WFCGVMRRC]
sources:
  - url: https://en.wikipedia.org/wiki/Catalan_number
    locator: Proof of the formula, Second proof
---

## Proof

We count Dyck words as all balanced words minus the bad ones, and count the bad ones by reflection.

1. Let $n$ be a natural number. By [[Dyck words are counted by Catalan numbers|017SRZ7NE9]], the [[Catalan number|092DRBFKMG]] $C_n$ is the number of [[Dyck words|0R9JR0465V]] of semilength $n$.
2. If $n = 0$, then $C_0 = 1$, and $\frac{1}{1} \binom{0}{0} = 1 = \frac{0!}{1!\, 0!}$. From now on let $n \ge 1$.
3. For a word $p$ over $\set{U, D}$, let $h(p)$ be its number of letters $U$ minus its number of letters $D$.
4. Let $A$ be the set of words with $n$ letters $U$ and $n$ letters $D$. Such a word is fixed by the set of positions of its letters $U$, an $n$-element subset of $\set{1, \dots, 2n}$.
5. So by the [[number of $k$-element subsets|0BFMR2FQ8B]], $|A|$ is the [[binomial coefficient|092GEF38YD]] $\binom{2n}{n}$. Similarly, the set $A'$ of words with $n - 1$ letters $U$ and $n + 1$ letters $D$ has $|A'| = \binom{2n}{n-1}$.
6. A word of $A$ is a Dyck word unless some prefix $p$ has $h(p) < 0$. Call such words bad, and let $A_{\mathrm{bad}}$ be their set.
7. Let $w \in A_{\mathrm{bad}}$, and let $w_{\le t}$ be its prefix of length $t$. Each letter changes $h$ by $\pm 1$, and $h$ of the empty prefix is $0$. Take the least $t$ with $h(w_{\le t}) < 0$. Then $h(w_{\le t-1}) \ge 0$, so $h(w_{\le t}) = -1$.
8. Define $\rho(w)$ by exchanging $U$ and $D$ in all letters after position $t$. The suffix after $t$ has $h$ equal to $h(w) - h(w_{\le t}) = 1$, and the exchange turns this into $-1$.
9. So $h(\rho(w)) = -1 - 1 = -2$. Since $\rho(w)$ has length $2n$, it has $n - 1$ letters $U$ and $n + 1$ letters $D$. Thus $\rho(w) \in A'$.
10. Conversely, let $v \in A'$. Then $h(v) = -2 < 0$, so as in step 7 the least $t$ with $h(v_{\le t}) < 0$ has $h(v_{\le t}) = -1$. Exchanging $U$ and $D$ after position $t$ gives a word with $h = -1 + 1 = 0$, which is in $A_{\mathrm{bad}}$.
11. Both operations keep the first $t$ letters, and $t$ is defined from these letters alone. So they find the same $t$. Hence they are inverse to each other.
12. By the [[bijection principle|0GV2573FP4]], $|A_{\mathrm{bad}}| = |A'| = \binom{2n}{n-1}$.
13. By the [[complement principle|03QC59M99B]], $C_n = |A| - |A_{\mathrm{bad}}| = \binom{2n}{n} - \binom{2n}{n-1}$.
14. By the [[factorial formula|033KTKKRV6]], $\binom{2n}{n} = \frac{(2n)!}{n!\, n!}$ and $\binom{2n}{n-1} = \frac{(2n)!}{(n-1)!\, (n+1)!}$.
15. By the definition of the [[factorial|0WFCGVMRRC]], $n! = n \cdot (n-1)!$ and $(n+1)! = (n+1) \cdot n!$. So $\binom{2n}{n-1} = \frac{n}{n+1} \cdot \frac{(2n)!}{n!\, n!} = \frac{n}{n+1} \binom{2n}{n}$.
16. By steps 13 and 15, $C_n = \left(1 - \frac{n}{n+1}\right) \binom{2n}{n} = \frac{1}{n+1} \binom{2n}{n}$.
17. By step 14 and $(n+1) \cdot n! = (n+1)!$, this equals $\frac{(2n)!}{(n+1)!\, n!}$.

## Idea

Among the $\binom{2n}{n}$ words with $n$ letters of each kind, the bad ones first reach level $-1$ somewhere. Flipping every letter after that point is a bijection onto all words with $n - 1$ letters $U$, so there are $\binom{2n}{n-1}$ bad words. The difference simplifies to $\frac{1}{n+1}\binom{2n}{n}$.
