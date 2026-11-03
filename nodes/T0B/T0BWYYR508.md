---
tag: T0BWYYR508
kind: statement
role: proposition
name: Equivalent definition with relaxed axioms
sources:
  - wikipedia: en:19447@r1375700306
    locator: Group (mathematics), section Elementary consequences of the group axioms > Equivalent definition with relaxed axioms
    note: adopted
    mention: wikipedia://en/19447#V50Y
    sections: [Statement]
inventory: [VAVGXVYCT4]
---

## Statement

The group axioms for identity and inverses may be "weakened" to assert only the existence of a left identity and left inverses. From these *one-sided axioms*, one can prove that the left identity is also a right identity and a left inverse is also a right inverse for the same element. Since they define exactly the same structures as groups, collectively the axioms are not weaker.

In particular, assuming associativity and the existence of a left identity $e$ (that is, $e\cdot f=f$) and a left inverse $f^{-1}$ for each element $f$ (that is, $f^{-1}\cdot f=e$), it follows that every left inverse is also a right inverse of the same element as follows. Indeed, one has

$$\begin{aligned} f \cdot f^{-1} &=e \cdot (f \cdot f^{-1}) && \text{(left identity)}\\ &=((f^{-1})^{-1} \cdot f^{-1}) \cdot (f \cdot f^{-1}) && \text{(left inverse)}\\ &=(f^{-1})^{-1} \cdot ((f^{-1} \cdot f) \cdot f^{-1}) && \text{(associativity)}\\ &=(f^{-1})^{-1} \cdot (e \cdot f^{-1}) && \text{(left inverse)}\\ &=(f^{-1})^{-1} \cdot f^{-1} && \text{(left identity)}\\ &=e && \text{(left inverse)} \end{aligned}$$

Similarly, the left identity is also a right identity:

$$\begin{aligned} f\cdot e &= f \cdot ( f^{-1} \cdot f) && \text{(left inverse)}\\ &= (f \cdot f^{-1}) \cdot f && \text{(associativity)}\\ &= e \cdot f && \text{(right inverse)}\\ &= f && \text{(left identity)} \end{aligned}$$

These results do not hold if any of these axioms (associativity, existence of left identity and existence of left inverse) is removed. For a structure with a looser definition (like a [[semigroup|0XMEM406JM]]) one may have, for example, that a left identity is not necessarily a right identity.

The same result can be obtained by only assuming the existence of a right identity and a right inverse.

However, only assuming the existence of a *left* identity and a *right* inverse (or vice versa) is not sufficient to define a group. For example, consider the set $G = \{ e,f \}$ with the operator $\,\!\cdot$ satisfying $e \cdot e = f \cdot e = e$ and $e \cdot f = f \cdot f = f$. This structure does have a left identity (namely, $e$), and each element has a right inverse (which is $e$ for both elements). Furthermore, this operation is associative (since the product of any number of elements is always equal to the rightmost element in that product, regardless of the order in which these operations are applied). However, $( G , \cdot )$ is not a group, since it lacks a right identity.
