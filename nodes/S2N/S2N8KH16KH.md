---
tag: S2N8KH16KH
kind: proof
name: Proof of the existence of maximal ideals by Zorn's lemma
msc: [13A15]
proves: 02HJYT53F7
uses: [0894J980RK, 0MYSA6MYNA, 0DDA6CY7GJ, 09J6KGT65G, 04RXTQA5ZA, 011C29Q1S1, 0GP9ASVQ1X, 0H5J02P8S9, 0TZEEFTNCC, 05GK32H72H]
sources:
  - url: https://en.wikipedia.org/wiki/Krull%27s_theorem
---

## Proof

We use [[Zorn's lemma|04RXTQA5ZA]]. We write the proof for left [[ideals|0MYSA6MYNA]]. For [[two-sided ideals|0DDA6CY7GJ]], read "two-sided ideal" for "left ideal" throughout; step 6 explains the one extra check.

1. Let $R$ be a [[ring|0894J980RK]] and let $I$ be a left ideal of $R$ with $I \neq R$.
2. A left ideal $L$ of $R$ equals $R$ if and only if $1 \in L$. Indeed, if $1 \in L$, then $r = r \cdot 1 \in L$ for every $r \in R$.
3. Let $\mathcal{P}$ be the set of left ideals $L$ of $R$ with $I \subseteq L$ and $L \neq R$. Inclusion is a [[partial order|011C29Q1S1]] on $\mathcal{P}$. The set $\mathcal{P}$ is nonempty, since $I \in \mathcal{P}$.
4. Let $\mathcal{C} \subseteq \mathcal{P}$ be a [[chain|0GP9ASVQ1X]]. If $\mathcal{C}$ is empty, then $I$ is an [[upper bound|0H5J02P8S9]] of $\mathcal{C}$ in $\mathcal{P}$. So assume that $\mathcal{C}$ is nonempty, and let $U$ be the [[union|05GK32H72H]] of the members of $\mathcal{C}$.
5. The set $U$ is a left ideal. It contains $0$, since some $L \in \mathcal{C}$ exists and $0 \in L$. Let $a, b \in U$, say $a \in L_1$ and $b \in L_2$ with $L_1, L_2 \in \mathcal{C}$. Since $\mathcal{C}$ is a chain, we may assume $L_1 \subseteq L_2$. Then $a - b \in L_2 \subseteq U$. For $r \in R$, $r a \in L_1 \subseteq U$.
6. In the two-sided case, also $a r \in L_1 \subseteq U$ for $a \in L_1$ and $r \in R$. So $U$ is then a two-sided ideal.
7. Every member of $\mathcal{C}$ contains $I$, so $I \subseteq U$. No member contains $1$ by step 2, so $1 \notin U$, and $U \neq R$.
8. So $U \in \mathcal{P}$, and $U$ contains each member of $\mathcal{C}$. Thus every chain in $\mathcal{P}$ has an upper bound in $\mathcal{P}$.
9. By Zorn's lemma, $\mathcal{P}$ has a [[maximal element|0TZEEFTNCC]] $M$. Then $M$ is a left ideal with $I \subseteq M$ and $M \neq R$.
10. Let $L$ be a left ideal of $R$ with $M \subseteq L$ and $L \neq R$. Then $I \subseteq L$, so $L \in \mathcal{P}$. By the maximality of $M$ in $\mathcal{P}$, $L = M$.
11. So every left ideal $L \supseteq M$ satisfies $L = M$ or $L = R$. Hence $M$ is a [[maximal ideal|09J6KGT65G]] of $R$ that contains $I$.
12. Now let $R$ be a nonzero ring, so $1 \neq 0$. The set $\set{0}$ is an ideal, and $\set{0} \neq R$ since $1 \notin \set{0}$. Steps 1 to 11 with $I = \set{0}$ give a maximal ideal of $R$.

## Idea

A proper ideal is one that avoids $1$. A union of a chain of ideals that avoid $1$ is again an ideal that avoids $1$. So Zorn's lemma applies and gives a proper ideal containing $I$ that cannot be enlarged without reaching the whole ring.
