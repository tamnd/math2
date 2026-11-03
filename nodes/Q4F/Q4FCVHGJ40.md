---
tag: Q4FCVHGJ40
kind: proof
name: Proof of the formula for the order of a power
msc: [20A05]
proves: 0VVPQNVM8S
uses: [G5S1M9, 0JPYSD5E0B, 00DRK90Z6K, 0F5QC101Q7, 02WF878BH1, 03BAREW1Z5, 096PW7Q014]
sources:
  - url: https://proofwiki.org/wiki/Order_of_Power_of_Group_Element
---

## Proof

1. Let $G$ be a [[group|G5S1M9]] with identity $e$. Let $g \in G$ have [[order|0JPYSD5E0B]] $n \geq 1$, and let $k \in \Z$.
2. Let $d = \gcd(n, k)$ be the [[greatest common divisor|02WF878BH1]]. Since $n \neq 0$ and $1$ is a common divisor, $d \geq 1$.
3. Since $d$ [[divides|096PW7Q014]] $n$ and $k$, write $n = dt$ and $k = dk'$ with integers $t, k'$. Then $t = n/d \geq 1$.
4. Claim: $\gcd(t, k') = 1$. Let $c = \gcd(t, k')$. Since $t \neq 0$, we have $c \geq 1$.
5. Then $cd$ divides $dt = n$ and $dk' = k$. So $cd$ is a common divisor of $n$ and $k$, hence $cd \leq d$. So $c \leq 1$, and $c = 1$.
6. Let $s$ be a positive integer. By the [[laws of exponents|00DRK90Z6K]], $(g^k)^s = g^{ks}$.
7. By [[the divisibility criterion for powers|0F5QC101Q7]], $g^{ks} = e$ if and only if $n$ divides $ks$.
8. Since $n = dt$ and $ks = dk's$ with $d \neq 0$, $n$ divides $ks$ if and only if $t$ divides $k's$. Indeed, for $q \in \Z$, $ks = nq$ means $dk's = dtq$, which is $k's = tq$.
9. If $t$ divides $k's$, then $t$ divides $s$, by step 4 and the [[generalized Euclid's lemma|03BAREW1Z5]]. If $t$ divides $s$, then $t$ divides $k's$.
10. By steps 6 to 9, for each positive integer $s$, $(g^k)^s = e$ if and only if $t$ divides $s$.
11. In particular $(g^k)^t = e$. Each positive $s$ with $(g^k)^s = e$ is a positive multiple of $t$, so $s \geq t$.
12. So $t$ is the least positive integer $s$ with $(g^k)^s = e$. The order of $g^k$ is $t = n / \gcd(n, k)$.

## Idea

The power $(g^k)^s$ is $e$ exactly when $n$ divides $ks$. After removing the common factor $d = \gcd(n, k)$ from $n$ and $k$, the parts left are coprime. So the condition becomes "$n/d$ divides $s$", and the least such $s$ is $n/d$.
