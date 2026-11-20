---
tag: Q7AQ1YK7BV
kind: proof
name: Proof outline of the representation theorems for cylindric algebras
msc: ["03G15"]
topics: [QYA4H5Y7VR]
audience: research
proves: WZ1BZYVD5G
uses: [RKCSWWVYTC, CQM84EW10G, AGYBSTD7BG, AX9Q86GB8M, RY8KRKR097]
methods: [0NTF6DMVAP, 0J0XBKG64S, JZQVJ9XT63]
sources:
  - book: isbn:9780720420432
  - book: isbn:9780444876799
---

## Proof

We prove part 3 from Monk's construction, and part 2 for countable algebras of dimension $\omega$ up to a routine check; parts 1 and 2 in general are cited from Henkin, Monk and Tarski, Part II.
For $\kappa \ne \lambda$ write $s^\kappa_\lambda x := c_\kappa(d_{\kappa\lambda} \cdot x)$, the substitution of $v_\lambda$ for $v_\kappa$; see [[the definition|RKCSWWVYTC]].

**Part 3, from Monk's algebras.**

1. Fix a finite $\alpha \ge 3$. Monk constructed algebras $A_k \in \mathbf{CA}_\alpha$, $k \in \omega$, none representable, such that a nonprincipal [[ultraproduct|AX9Q86GB8M]] $A^* = \prod_k A_k / D$ is representable.
2. Suppose a finite set $\Sigma$ of first-order sentences axiomatizes $\mathbf{RCA}_\alpha$, and let $\sigma$ be their conjunction.
3. Each $A_k$ is not representable, so $A_k \models \neg \sigma$.
4. By [[Łoś's theorem|AGYBSTD7BG]], $A^* \models \neg \sigma$, so $A^*$ is not representable. This contradicts step 1.
5. Part 4 follows: $\mathbf{CA}_\alpha$ is defined by finitely many equations when $\alpha$ is finite.

**Part 2 for a countable $A \in \mathbf{Lf}_\omega$.**

6. Claim: $c_\kappa y$ is the least upper bound of $\set{s^\kappa_\lambda y : \lambda \ne \kappa}$.
7. Each $s^\kappa_\lambda y \le c_\kappa y$, by monotonicity of $c_\kappa$.
8. Let $z \ge s^\kappa_\lambda y$ for all $\lambda \ne \kappa$. Pick $\lambda \notin \Delta y \cup \Delta z \cup \set{\kappa}$, which exists since $A$ is locally finite.
9. By axiom 6 and the identity $d_{\kappa\lambda} = d_{\lambda\kappa}$, which holds in $\mathbf{CA}_\alpha$, $c_\lambda d_{\kappa\lambda} = d_{\kappa\kappa} = 1$. As $c_\lambda y = y$, axiom 3 gives $c_\lambda(d_{\kappa\lambda} \cdot y) = c_\lambda d_{\kappa\lambda} \cdot y = y$.
10. So, with axiom 4, $c_\lambda s^\kappa_\lambda y = c_\kappa c_\lambda(d_{\kappa\lambda} \cdot y) = c_\kappa y$, and $c_\kappa y \le c_\lambda z = z$. This proves the claim.
11. Fix $x \ne 0$. The claim gives countably many joins in a countable Boolean algebra. By the Rasiowa-Sikorski lemma, there is an [[ultrafilter|CQM84EW10G]] $F \ni x$ such that $c_\kappa y \in F$ implies $s^\kappa_\lambda y \in F$ for some $\lambda$.
12. Put $\kappa \approx \lambda$ iff $d_{\kappa\lambda} \in F$. The identities $d_{\kappa\lambda} = d_{\lambda\kappa}$ and $d_{\kappa\lambda} \cdot d_{\lambda\mu} \le d_{\kappa\mu}$ hold in $\mathbf{CA}_\alpha$, so $\approx$ is an equivalence on $\omega$. Let $U = \omega / {\approx}$.
13. For $y \in A$, let $h(y)$ be the set of $s \in U^\omega$ such that $y$, with $v_\kappa$ replaced by a variable in the class $s_\kappa$ for each $\kappa \in \Delta y$, lies in $F$. This depends only on $s$ restricted to the finite set $\Delta y$.
14. Then $h$ preserves the Boolean operations because $F$ is an ultrafilter, the diagonals because of step 12, and $c_\kappa$ because of step 11. The check is the one of the [[Henkin construction|RY8KRKR097]].
15. Since the identity assignment $\kappa \mapsto [\kappa]$ lies in $h(x)$, $h(x) \ne \emptyset$. The product of these maps over all $x \ne 0$ represents $A$. $\blacksquare$

## Idea

Part 3 is a compactness argument: a finite axiomatization would be preserved by ultraproducts in both directions.
Part 2 is Henkin's proof of the completeness theorem in algebraic dress: an ultrafilter with witnesses for all existential elements is a complete theory with witnesses, and its term model is the representation.

## Variants

1. For uncountable $A$, or $\alpha > \omega$, one first adds new dimensions to make room for witnesses, and then argues as above; see Henkin, Monk and Tarski, Part II.
2. For part 1, Tarski showed that a homomorphic image of a subdirect product of set algebras is again of this form; the proof uses ultraproducts and is in Part II of the monograph.
