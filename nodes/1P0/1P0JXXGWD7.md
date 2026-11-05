---
tag: 1P0JXXGWD7
kind: statement
role: proposition
name: Kleiman's criterion
sources:
  - wikipedia: en:1186896@r1373926196
    locator: Ample line bundle, section Criteria for ampleness of line bundles > Kleiman's criterion
    note: adopted
    mention: wikipedia://en/1186896#F4HH
    sections: [Statement]
inventory: [E5Z0R45GQ2]
---

## Statement

To state **Kleiman's criterion** (1966), let *X* be a projective scheme over a field. Let $N_1(X)$ be the [[real|08J2M1JYAG]] vector space of 1-cycles (real linear combinations of curves in *X*) modulo numerical equivalence, meaning that two 1-cycles *A* and *B* are equal in $N_1(X)$ if and only if every line bundle has the same degree on *A* and on *B*. By the Néron–Severi theorem, the real vector space $N_1(X)$ has finite dimension. Kleiman's criterion states that a line bundle *L* on *X* is ample if and only if *L* has positive degree on every nonzero element *C* of the [[closure|0QEAJB91GZ]] of the cone of curves NE(*X*) in $N_1(X)$. (This is slightly stronger than saying that *L* has positive degree on every curve.) Equivalently, a line bundle is ample if and only if its class in the dual vector space $N^1(X)$ is in the interior of the nef cone.

Kleiman's criterion fails in general for proper (rather than projective) schemes *X* over a field, although it holds if *X* is smooth or more generally **Q**-factorial.

A line bundle on a projective variety is called **strictly nef** if it has positive degree on every curve. (Nagata 1959) and David Mumford constructed line bundles on smooth projective surfaces that are strictly nef but not ample. This shows that the condition $c_1(L)^2>0$ cannot be omitted in the Nakai–Moishezon criterion, and it is necessary to use the closure of NE(*X*) rather than NE(*X*) in Kleiman's criterion. Every nef line bundle on a surface has $c_1(L)^2\geq 0$, and Nagata and Mumford's examples have $c_1(L)^2=0$.

C. S. Seshadri showed that a line bundle *L* on a proper scheme over an algebraically closed field is ample if and only if there is a positive real number ε such that deg(*L*|<sub>*C*</sub>) ≥ ε*m*(*C*) for all (irreducible) curves *C* in *X*, where *m*(*C*) is the maximum of the multiplicities at the points of *C*.

Several characterizations of ampleness hold more generally for line bundles on a proper algebraic space over a field *k*. In particular, the Nakai-Moishezon criterion is valid in that generality. The Cartan-Serre-Grothendieck criterion holds even more generally, for a proper algebraic space over a Noetherian ring *R*. (If a proper algebraic space over *R* has an ample line bundle, then it is in fact a projective scheme over *R*.) Kleiman's criterion fails for proper algebraic spaces *X* over a field, even if *X* is smooth.
