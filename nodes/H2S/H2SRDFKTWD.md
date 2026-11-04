---
tag: H2SRDFKTWD
kind: proof
name: Proof of Euler's criterion by counting quadratic residues
msc: [11A15]
proves: 0M7DEDKSYB
uses: [01J8AMV9RS, 0SQDB87Z3T, 0M25PRN3WQ, 051VYKA1EX, 0R8YXRC9AJ, 0KJVQV3E0F, 0J5VGJYYC3, 0TPW25CBN6]
sources:
  - url: https://en.wikipedia.org/wiki/Euler%27s_criterion
    locator: Proof
---

## Proof

1. Let $p$ be an odd prime and $a$ an integer. Let $\left(\frac{a}{p}\right)$ be the [[Legendre symbol|01J8AMV9RS]]. Note that $(p-1)/2 \ge 1$ is an integer.
2. If $p \mid a$, then $p \mid a^{(p-1)/2}$. So $a^{(p-1)/2} \equiv 0 = \left(\frac{a}{p}\right) \pmod p$. Assume from now on that $p \nmid a$.
3. Let $x = a^{(p-1)/2}$. By [[Fermat's little theorem|0M25PRN3WQ]], $x^2 = a^{p-1} \equiv 1 \pmod p$. So $p \mid (x - 1)(x + 1)$.
4. By [[Euclid's lemma|051VYKA1EX]], $x \equiv 1$ or $x \equiv -1 \pmod p$. These two cases exclude each other, because $p \nmid 2$.
5. Suppose $a$ is a [[quadratic residue|0SQDB87Z3T]], so $a \equiv y^2 \pmod p$ for an integer $y$. Then $p \nmid y$, since $p \nmid a$.
6. Then $x \equiv (y^2)^{(p-1)/2} = y^{p-1} \equiv 1 \pmod p$, using [[powers of congruences|0J5VGJYYC3]] and Fermat's little theorem. So $x \equiv 1 = \left(\frac{a}{p}\right)$.
7. Now we count residues. Let $Q$ be the set of nonzero classes in $\mathbb{Z}/p\mathbb{Z}$ that are squares. Each such class is $\overline{y}^2$ with $1 \le y \le p - 1$.
8. Since $(p - y)^2 \equiv y^2 \pmod p$, each class in $Q$ is $\overline{y}^2$ for some $y$ with $1 \le y \le (p-1)/2$.
9. Let $1 \le y < z \le (p-1)/2$. If $y^2 \equiv z^2$, then $p \mid (z - y)(z + y)$. But $0 < z - y < p$ and $0 < z + y < p$, so this contradicts Euclid's lemma.
10. So the classes $\overline{y}^2$ with $1 \le y \le (p-1)/2$ are distinct, and $Q$ has exactly $(p-1)/2$ elements.
11. By steps 5 and 6, every class in $Q$ is a root of the polynomial $X^{(p-1)/2} - 1$ over $\mathbb{Z}/p\mathbb{Z}$.
12. The ring $\mathbb{Z}/p\mathbb{Z}$ [[is a field|0R8YXRC9AJ]]. So this polynomial has [[at most $(p-1)/2$ roots|0KJVQV3E0F]]. By steps 10 and 11, its roots are exactly the elements of $Q$.
13. Suppose $a$ is a quadratic nonresidue. Then $\overline{a} \notin Q$, so $\overline{a}$ is not a root, and $x \not\equiv 1 \pmod p$.
14. By step 4, $x \equiv -1 = \left(\frac{a}{p}\right) \pmod p$.
15. In all cases, $a^{(p-1)/2} \equiv \left(\frac{a}{p}\right) \pmod p$.

## Idea

The number $x = a^{(p-1)/2}$ squares to $1$, so it is $\pm 1$ modulo $p$. Residues give $+1$ at once by Fermat. There are exactly $(p-1)/2$ nonzero residues, and they already fill all the roots of $X^{(p-1)/2} - 1$, so a nonresidue must give $-1$.
