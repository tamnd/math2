---
tag: V43C5CQ7AK
kind: statement
role: proposition
name: The De Morgan laws in a Heyting algebra
sources:
  - wikipedia: en:309343@r1371256451
    locator: Heyting algebra, section Properties > The De Morgan laws in a Heyting algebra
    note: adopted
    mention: wikipedia://en/309343#J0FE
    sections: [Statement]
inventory: [J61PTAA8G1]
---

## Statement

One of the two De Morgan laws is satisfied in every Heyting algebra, namely

$$\forall x,y \in H: \qquad \lnot(x \vee y)=\lnot x \wedge \lnot y.$$

However, the other De Morgan law does not always hold. We have instead a weak de Morgan law:

$$\forall x,y \in H: \qquad \lnot(x \wedge y)= \lnot \lnot (\lnot x \vee \lnot y).$$

The following statements are equivalent for all Heyting algebras *H*:

1. *H* satisfies both De Morgan laws,
1. $$\lnot(x \wedge y)=\lnot x \vee \lnot y \mbox{ for all } x, y \in H,$$
1. $$\lnot(x \wedge y)=\lnot x \vee \lnot y \mbox{ for all regular } x, y \in H,$$
1. $$\lnot\lnot (x \vee y) = \lnot\lnot x \vee \lnot\lnot y \mbox{ for all } x, y \in H,$$
1. $$\lnot\lnot (x \vee y) = x \vee y \mbox{ for all regular } x, y \in H,$$
1. $$\lnot(\lnot x \wedge \lnot y) = x \vee y \mbox{ for all regular } x, y \in H,$$
1. $$\lnot x \vee \lnot\lnot x = 1 \mbox{ for all } x \in H.$$

Condition 2 is the other De Morgan law. Condition 6 says that the join operation ∨<sub>reg</sub> on the Boolean algebra *H*<sub>reg</sub> of regular elements of *H* coincides with the operation ∨ of *H*. Condition 7 states that every regular element is complemented, i.e., *H*<sub>reg</sub> = *H*<sub>comp</sub>.

We prove the equivalence. Clearly the metaimplications 1 ⇒ 2, 2 ⇒ 3 and 4 ⇒ 5 are trivial. Furthermore, 3 ⇔ 4 and 5 ⇔ 6 result simply from the first De Morgan law and the definition of regular elements. We show that 6 ⇒ 7 by taking ¬*x* and ¬¬*x* in place of *x* and *y* in 6 and using the identity *a* ∧ ¬*a* = 0. Notice that 2 ⇒ 1 follows from the first De Morgan law, and 7 ⇒ 6 results from the fact that the join operation ∨ on the subalgebra *H*<sub>comp</sub> is just the restriction of ∨ to *H*<sub>comp</sub>, taking into account the characterizations we have given of conditions 6 and 7. The metaimplication 5 ⇒ 2 is a trivial consequence of the weak De Morgan law, taking ¬*x* and ¬*y* in place of *x* and *y* in 5.

Heyting algebras satisfying the above properties are related to De Morgan logic in the same way Heyting algebras in general are related to intuitionist logic.
