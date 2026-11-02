---
tag: MXRCPAH09H
kind: statement
role: theorem
name: Mordell–Weil theorem
msc: [11G10, 14K15, 14G05]
uses: [R7W03TXRS9, MWBDFS2KJ5, SWJYG87QQH, 082DWWXMRJ, 082GHNPJ53, F1FF505PWH]
about: [R7W03TXRS9, SWJYG87QQH]
sources:
  - url: https://en.wikipedia.org/wiki/Mordell%E2%80%93Weil_theorem
same_as:
  wikidata: Q284960
  wikipedia: Mordell–Weil theorem
---

## Statement

Let $K$ be an [[algebraic number field|MWBDFS2KJ5]] and let $A$ be an [[abelian variety|R7W03TXRS9]] over $K$.
Then the group $A(K)$ of $K$-[[rational points|SWJYG87QQH]] of $A$ is a [[finitely generated|082DWWXMRJ]] [[abelian group|082GHNPJ53]].

## Remarks

The proof has two parts.
The weak Mordell–Weil theorem says that $A(K)/mA(K)$ is finite for an integer $m \ge 2$.
It is proved with Kummer theory and the finiteness of the class group and of the unit group modulo $m$-th powers.
Then a [[height function|F1FF505PWH]] on $A(K)$ has finitely many points of bounded height and satisfies $h(mP) \approx m^2 h(P)$.
A descent with it shows that representatives of $A(K)/mA(K)$ and the points of small height generate $A(K)$.
Mordell proved the case of an elliptic curve over $\Q$, which is [[Mordell's theorem|BZHGKN6Q3K]]; Weil proved the general case.
So $A(K) \cong \Z^r \oplus T$ with $T$ finite; the integer $r$ is the rank of $A$ over $K$.
The hypothesis on $K$ matters.
Over $\overline{\Q}$ the group $E(\overline{\Q})$ of an [[elliptic curve|427N6S6QQW]] contains points of every finite order, so its torsion subgroup is infinite and it is not finitely generated.
Over $\R$ the group $E(\R)$ is uncountable.

## Explanations

### L1 human

An abelian variety, such as an elliptic curve, has a group law on its points.
The theorem says that over a number field all rational points are built from finitely many of them with this group law.
So an infinite set of solutions to a system of equations has a finite description.

### L2 human

The theorem gives the rank and the torsion subgroup as the basic invariants of $A(K)$.
The rank is hard to compute: the descent gives only an upper bound through the Selmer group, and the gap is measured by the Tate–Shafarevich group.
The [[Birch and Swinnerton-Dyer conjecture|ZWEFBG40H9]] predicts the rank from an $L$-function.
Let $C$ be a curve of genus at least $2$ embedded in its Jacobian.
The theorem places $C(K)$ inside a finitely generated group, and [[Faltings's theorem|H0DB07WM20]] shows that $C(K)$ is finite.
