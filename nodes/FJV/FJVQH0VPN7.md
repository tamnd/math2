---
tag: FJVQH0VPN7
kind: definition
name: Instanton
msc: [53C07, 81T13, "58E15"]
defines: YWBTGC7MFA
uses: [7CBT4SM83Y, 913WEQERBE, 8E37E74XVP, NJ21PN5ZGJ, ZAJFW1S078, 1Y4WX4XQWJ]
sources:
  - url: https://en.wikipedia.org/wiki/Instanton
---

## Definition

Let $(X, g)$ be an [[oriented|913WEQERBE]] [[Riemannian manifold|7CBT4SM83Y]] of dimension $4$, and let $\star$ be its [[Hodge star|1Y4WX4XQWJ]], which maps 2-forms to 2-forms.
Let $G$ be a compact [[Lie group|7JBRGCVJRB]] with Lie algebra $\mathfrak{g}$, and let $P \to X$ be a [[principal|8E37E74XVP]] $G$-bundle.
Let $A$ be a [[connection|NJ21PN5ZGJ]] on $P$ with [[curvature|ZAJFW1S078]] $F_A$, a 2-form on $X$ with values in the adjoint bundle $P \times_G \mathfrak{g}$.
The connection $A$ is an *instanton*, or anti-self-dual connection, if
$$\star F_A = -F_A.$$

## Remarks

Some authors use the opposite orientation and call self-dual connections, with $\star F_A = F_A$, instantons.
Anti-self-dual connections satisfy the Yang–Mills equations $d_A \star F_A = 0$, because $d_A \star F_A = -d_A F_A = 0$ by the Bianchi identity.
On a compact $X$, they minimize the Yang–Mills functional $\int_X \abs{F_A}^2$ among connections on $P$, the minimum being a topological constant times the absolute value of a characteristic number of $P$.

Example: a flat connection, with $F_A = 0$, is an instanton.
The BPST instanton on $\R^4$ for $G = SU(2)$ has curvature that is nowhere zero and anti-self-dual for one choice of orientation.

Non-example: on the trivial $U(1)$-bundle over $\R^4$ with coordinates $x_1, \dots, x_4$, let $A = i \, x_1 \, dx_2$.
Then $F_A = i \, dx_1 \wedge dx_2$ and $\star F_A = i \, dx_3 \wedge dx_4 \ne -F_A$, so $A$ is not an instanton.
