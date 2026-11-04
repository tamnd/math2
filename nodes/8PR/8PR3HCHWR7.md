---
tag: 8PR3HCHWR7
kind: proof
name: Proof of Urysohn's lemma by dyadic open sets
msc: [54D15]
proves: 01EY3VR7ZD
uses: [0AJ646N339, 0G5AV9Q4RR, 0DRKT1QJR7, 0SHC6Z304Z, 0CNQXVBHCX, 0EDH403M21, 04KFTA34C5, 0A3GWZ86AY, 0YVRNEDSVG, 0D5YHQGDJY, 0A6YRNZB2R, 09CJ00H3NW, 0SY9ECQ19Q]
sources:
  - url: https://en.wikipedia.org/wiki/Urysohn%27s_lemma
    locator: Proof sketch
---

## Proof

We build open sets $U_r$ indexed by dyadic rationals and let $f(x)$ be the least index of a set that contains $x$. For $W \subseteq X$, write $\overline{W}$ for the [[closure|0DRKT1QJR7]]. By [[the closure is the smallest closed superset|0SHC6Z304Z]], $W \subseteq \overline{W}$, $\overline{W}$ is closed, and $\overline{W} \subseteq F$ for each closed $F \supseteq W$.

A shrinking lemma.

1. Claim: if $C$ is closed, $W$ is open and $C \subseteq W$, then some open $V$ has $C \subseteq V$ and $\overline{V} \subseteq W$.
2. The set $X \setminus W$ is [[closed|0G5AV9Q4RR]], since its complement $W$ is open. It is disjoint from $C$.
3. Since $X$ is [[normal|0AJ646N339]], there are disjoint open sets $V \supseteq C$ and $V' \supseteq X \setminus W$.
4. Then $V \subseteq X \setminus V'$, and $X \setminus V'$ is closed. So $\overline{V} \subseteq X \setminus V' \subseteq W$. This proves the claim.

The sets $U_r$.

5. For $n \ge 0$, let $D_n = \set{k / 2^n : k \in \Z, \ 0 \le k \le 2^n}$. Then $D_n \subseteq D_{n+1}$. Let $D$ be the union of all $D_n$.
6. Let $U_1 = X \setminus B$. It is open, and $A \subseteq U_1$ since $A \cap B = \varnothing$. Step 1 gives an open $U_0$ with $A \subseteq U_0$ and $\overline{U_0} \subseteq U_1$.
7. Let $P_n$ say: open sets $U_r$ are given for $r \in D_n$, with $\overline{U_r} \subseteq U_s$ whenever $r < s$ in $D_n$. Step 6 gives $P_0$.
8. Under $P_n$, if $r \le s$ in $D_n$, then $U_r \subseteq U_s$. For $r < s$ this is $U_r \subseteq \overline{U_r} \subseteq U_s$.
9. Assume $P_n$. Each $r \in D_{n+1} \setminus D_n$ has the form $r = (2k+1)/2^{n+1}$. Let $r^- = k / 2^n$ and $r^+ = (k+1)/2^n$, the neighbours of $r$ in $D_n$.
10. By $P_n$, $\overline{U_{r^-}} \subseteq U_{r^+}$. Step 1 gives an open $U_r$ with $\overline{U_{r^-}} \subseteq U_r$ and $\overline{U_r} \subseteq U_{r^+}$.
11. We check $P_{n+1}$. Let $r < s$ in $D_{n+1}$. If $r, s \in D_n$, use $P_n$.
12. If $r \notin D_n$ and $s \in D_n$, then $s \ge r^+$, since $r^+$ is the least element of $D_n$ above $r$. So $\overline{U_r} \subseteq U_{r^+} \subseteq U_s$ by steps 10 and 8.
13. If $r \in D_n$ and $s \notin D_n$, then $r \le s^-$. Also $\overline{U_r} \subseteq \overline{U_{s^-}}$, by $P_n$ when $r < s^-$. So $\overline{U_r} \subseteq \overline{U_{s^-}} \subseteq U_s$.
14. If $r, s \notin D_n$, then $s - r \ge 2 / 2^{n+1}$, since both are odd multiples of $1/2^{n+1}$. So $r^+ \le s^-$, and $\overline{U_r} \subseteq U_{r^+} \subseteq U_{s^-} \subseteq \overline{U_{s^-}} \subseteq U_s$.
15. By induction on $n$, $P_n$ holds for all $n$. Sets chosen at one stage are kept at later stages. So for all $r < s$ in $D$ we have $\overline{U_r} \subseteq U_s$, and $U_r \subseteq U_s$.

The function $f$.

16. For $x \in X$, let $S(x) = \set{r \in D : x \in U_r} \cup \set{1}$. It is nonempty and contained in $[0, 1]$. By the [[existence of the infimum|0EDH403M21]], let $f(x) = \inf S(x)$. Then $0 \le f(x) \le 1$.
17. Let $a \in A$. Then $a \in U_0$, so $0 \in S(a)$ and $f(a) = 0$.
18. Let $b \in B$. Then $b \notin U_1$, and $U_r \subseteq U_1$ for all $r \in D$ by step 15. So $S(b) = \set{1}$ and $f(b) = 1$.
19. Fact (i): if $r \in D$ and $x \notin U_r$, then $f(x) \ge r$. Indeed, if $s \in D$ and $x \in U_s$, then $s > r$, since $s \le r$ would give $x \in U_r$. Also $1 \ge r$. So $r$ is a lower bound of $S(x)$, and $r \le f(x)$ by the definition of the [[infimum|04KFTA34C5]].
20. Density: if $0 \le c < e \le 1$, some $s \in D$ has $c < s < e$. Since [[the reals are Archimedean|0A3GWZ86AY]], choose $n$ with $n (e - c) > 1$. Then $2^n \ge n$ gives $2^{-n} < e - c$.
21. Let $k = \floor{2^n c} + 1$, using the [[floor|0YVRNEDSVG]]. Then $c < k / 2^n \le c + 2^{-n} < e$. Since $0 \le c$ and $e \le 1$, we get $0 < k \le 2^n$. So $s = k / 2^n \in D_n$ works.
22. Fact (ii): if $r \in D$ and $x \in \overline{U_r}$, then $f(x) \le r$. This is clear for $r = 1$. Let $r < 1$ and suppose $f(x) > r$.
23. By step 20 with $c = r$ and $e = f(x)$, some $s \in D$ has $r < s < f(x)$. By step 15, $x \in \overline{U_r} \subseteq U_s$, so $s \in S(x)$ and $f(x) \le s$. This is a contradiction.

Continuity of $f$.

24. Give $[0, 1]$ the [[subspace topology|0D5YHQGDJY]] of the [[metric topology|0A6YRNZB2R]] of $\R$. Let $O$ be open in $[0, 1]$, let $x_0 \in f^{-1}(O)$ and let $t = f(x_0)$.
25. Write $O = [0, 1] \cap O'$ with $O'$ open in $\R$. There is $\varepsilon > 0$ with $(t - \varepsilon, t + \varepsilon) \subseteq O'$. So $(t - \varepsilon, t + \varepsilon) \cap [0, 1] \subseteq O$.
26. Upper side. If $t + \varepsilon > 1$, let $W_1 = X$; then $f(x) \le 1 < t + \varepsilon$ on $W_1$. Otherwise step 20 gives $q \in D$ with $t < q < t + \varepsilon$.
27. In that case, $f(x_0) < q$, so $x_0 \in U_q$ by fact (i). Let $W_1 = U_q$. For $x \in W_1$, $x \in \overline{U_q}$, so $f(x) \le q < t + \varepsilon$ by fact (ii).
28. Lower side. If $t - \varepsilon < 0$, let $W_2 = X$; then $f(x) \ge 0 > t - \varepsilon$ on $W_2$. Otherwise step 20 gives $p \in D$ with $t - \varepsilon < p < t$.
29. In that case, $f(x_0) > p$, so $x_0 \notin \overline{U_p}$ by fact (ii). Let $W_2 = X \setminus \overline{U_p}$, which is open. For $x \in W_2$, $x \notin U_p$, so $f(x) \ge p > t - \varepsilon$ by fact (i).
30. Let $W = W_1 \cap W_2$. It is open by the axioms of a [[topology|0CNQXVBHCX]], and $x_0 \in W$. By steps 25 to 29, $f(W) \subseteq (t - \varepsilon, t + \varepsilon) \cap [0, 1] \subseteq O$.
31. So $f^{-1}(O)$ is a [[neighbourhood|09CJ00H3NW]] of each of its points, hence open. Thus $f \colon X \to [0, 1]$ is [[continuous|0SY9ECQ19Q]], with $f = 0$ on $A$ and $f = 1$ on $B$ by steps 17 and 18.

## Idea

Normality lets us fit an open set, with its closure, strictly between a closed set and an open set around it. Repeating this at every dyadic level gives a nested family $U_r$ that grows from around $A$ to the complement of $B$. Then $f(x)$ records the first level at which $x$ enters the family. The strict nesting of closures makes $f$ continuous.
