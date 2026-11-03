---
tag: XADN5F6SCP
kind: definition
name: Knuth–Morris–Pratt algorithm
msc: [68W32, 68R15, 68W40]
defines: PM11BAWMM6
uses: [RABRP2KG81, 1P6EP01HZF, TQ3YZDGCHM]
sources:
  - url: https://en.wikipedia.org/wiki/Knuth%E2%80%93Morris%E2%80%93Pratt_algorithm
---

## Definition

Let $P = p_1 \cdots p_m$ and $T = t_1 \cdots t_n$ be [[strings|1P6EP01HZF]] over a finite [[alphabet|RABRP2KG81]], with $m \ge 1$.
The *failure function* of $P$ is the map $\pi \colon \set{1, \dots, m} \to \set{0, \dots, m - 1}$ such that $\pi(q)$ is the largest $k < q$ with $p_1 \cdots p_k = p_{q - k + 1} \cdots p_q$.
The *Knuth–Morris–Pratt algorithm* is the [[string-searching algorithm|TQ3YZDGCHM]] that computes $\pi$ and then runs these steps.

1. Set $q = 0$.
2. For $i = 1, \dots, n$: while $q > 0$ and $p_{q + 1} \ne t_i$, set $q = \pi(q)$.
3. Still for this $i$: if $p_{q + 1} = t_i$, increase $q$ by $1$.
4. Still for this $i$: if $q = m$, report an occurrence at position $i - m + 1$ and set $q = \pi(m)$.

After step 3 for index $i$, $q$ is the length of the longest prefix of $P$ that is a suffix of $t_1 \cdots t_i$.

## Remarks

Example: for $P = abab$ the failure function is $\pi(1) = 0$, $\pi(2) = 0$, $\pi(3) = 1$, $\pi(4) = 2$.
For instance $\pi(4) = 2$ because $ab$ is both a prefix and a suffix of $abab$, while $aba$ is not a suffix of it.
On the text $T = ababab$ the algorithm reports positions $1$ and $3$.

Non-example: the value $k = q$ is excluded in the failure function.
Allowing it would give $\pi(q) = q$, and step 2 would never move the pattern.

The failure function itself is computed by the same scan applied to $P$ against itself, in time $O(m)$.
Each step 2 loop lowers $q$, and $q$ rises by at most $1$ per character, so the search takes time $O(n)$ and the whole algorithm $O(n + m)$.
