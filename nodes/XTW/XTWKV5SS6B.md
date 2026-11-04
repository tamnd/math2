---
tag: XTWKV5SS6B
kind: proof
name: Proof of the well-ordering theorem from Zorn's lemma
msc: ["03E25"]
proves: 0N109NG5ZX
uses: [04RXTQA5ZA, 0F1D6PK9RZ, 0316AYH1SC, 011C29Q1S1, 0T2NTJCV83, 0GP9ASVQ1X, 0H5J02P8S9, 0TZEEFTNCC, 05GK32H72H]
sources:
  - url: https://math.berkeley.edu/~gbergman/grad.hndts/AC+Zorn+.pdf
---

## Proof

We apply Zorn's lemma to the well-ordered subsets of $A$, ordered by extension at the top.

1. Let $A$ be a set. Let $W$ be the set of pairs $(B, R)$ with $B \subseteq A$ and $R \subseteq B \times B$ a [[well-order|0F1D6PK9RZ]] on $B$. Write $x \mathrel{R} y$ for $(x, y) \in R$.
2. Define $(B, R) \preceq (B', R')$ when three conditions hold: $B \subseteq B'$; $R = R' \cap (B \times B)$; and $b \mathrel{R'} b'$ for all $b \in B$ and $b' \in B' \setminus B$.
3. The relation $\preceq$ is a [[partial order|011C29Q1S1]]. It is reflexive. If $(B, R) \preceq (B', R')$ and $(B', R') \preceq (B, R)$, then $B = B'$ and $R = R' \cap (B \times B) = R'$.
4. Transitivity: let $(B, R) \preceq (B', R') \preceq (B'', R'')$. Then $B \subseteq B''$ and $R = R' \cap (B \times B) = R'' \cap (B \times B)$, since $B \subseteq B'$.
5. Let $b \in B$ and $b'' \in B'' \setminus B$. If $b'' \in B'$, then $b \mathrel{R'} b''$, so $b \mathrel{R''} b''$. If $b'' \notin B'$, then $b \mathrel{R''} b''$, since $b \in B'$. So $(B, R) \preceq (B'', R'')$.
6. The set $W$ is nonempty, since $(\emptyset, \emptyset) \in W$. So the empty [[chain|0GP9ASVQ1X]] has an [[upper bound|0H5J02P8S9]].
7. Let $K$ be a nonempty chain of $(W, \preceq)$. Put $B^* = \bigcup_{(B, R) \in K} B$ and $R^* = \bigcup_{(B, R) \in K} R$, two [[unions|05GK32H72H]].
8. For $(B, R) \in K$, we have $R^* \cap (B \times B) = R$. One inclusion is clear. If $x, y \in B$ and $x \mathrel{R'} y$ with $(B', R') \in K$, then $(B', R') \preceq (B, R)$ gives $R' \subseteq R$, and $(B, R) \preceq (B', R')$ gives $R = R' \cap (B \times B)$. Either way $x \mathrel{R} y$.
9. Finitely many elements of $B^*$ lie in finitely many members of $K$. These are comparable, so all the elements lie in the largest of these members, $B$ say.
10. By steps 8 and 9, any three elements of $B^*$ lie in some $B$ where $R^*$ agrees with the total order $R$. So $R^*$ is a [[total order|0316AYH1SC]] on $B^*$.
11. Let $(B, R) \in K$, $b \in B$ and $y \in B^* \setminus B$. Pick $(B', R') \in K$ with $y \in B'$. Then $(B', R') \preceq (B, R)$ fails, as $y \notin B$. So $(B, R) \preceq (B', R')$, and $b \mathrel{R'} y$, hence $b \mathrel{R^*} y$.
12. The order $R^*$ is a well-order. Let $S \subseteq B^*$ be nonempty, and pick $(B, R) \in K$ with $S \cap B \neq \emptyset$. Let $m$ be the [[least element|0T2NTJCV83]] of $S \cap B$ for $R$.
13. Let $t \in S$. If $t \in B$, then $m \mathrel{R} t$, so $m \mathrel{R^*} t$. If $t \notin B$, then $m \mathrel{R^*} t$ by step 11. So $m$ is the least element of $S$.
14. So $(B^*, R^*) \in W$. By steps 8 and 11, $(B, R) \preceq (B^*, R^*)$ for each $(B, R) \in K$. So every chain of $W$ has an upper bound.
15. By [[Zorn's lemma|04RXTQA5ZA]], $W$ has a [[maximal element|0TZEEFTNCC]] $(M, R_M)$.
16. Suppose that $M \neq A$, and pick $a \in A \setminus M$. Put $M' = M \cup \{a\}$ and $R' = R_M \cup \{(x, a) : x \in M'\}$.
17. Then $R'$ is a total order on $M'$ with $a$ as largest element. A nonempty $S \subseteq M'$ has a least element: the least element of $S \cap M$ if this set is nonempty, and $a$ otherwise.
18. So $(M', R') \in W$, and $(M, R_M) \preceq (M', R')$ with $M \neq M'$. This contradicts maximality. Hence $M = A$, and $R_M$ is a well-order on $A$.

## Idea

Look at all ways to well-order part of $A$, where one is below another when the bigger one only adds new elements on top. A chain of such orders glues into one well-order, because new elements never slip in below old ones. Zorn's lemma gives a maximal one, and it must cover all of $A$, since otherwise we could add a new element on top.
