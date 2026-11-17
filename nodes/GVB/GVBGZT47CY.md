---
tag: GVBGZT47CY
kind: example
name: Counting sentences with equality
msc: ["03B10"]
topics: [PSRDJXRW53]
audience: ug2
instance_of: [Q1494G7FBM]
uses: [Q1494G7FBM, DKFGQTRYZE, 0QAJHFGZZJ]
sources:
  - url: https://en.wikipedia.org/wiki/First-order_logic
    locator: Equality and its axioms
  - url: https://en.wikipedia.org/wiki/Uniqueness_quantification
    locator: lead section
---

## Example

Work in [[first-order logic with equality|Q1494G7FBM]] over any signature.
Consider the [[sentences|DKFGQTRYZE]]
$$\lambda_2 = \exists x \, \exists y \, \neg (x = y), \qquad \mu_1 = \forall x \, \forall y \, (x = y),$$
and, for a formula $\varphi$ with free variable $x$, the formula
$$\exists ! x \, \varphi := \exists x \, (\varphi \land \forall y \, (\varphi[y/x] \to y = x)),$$
where $y$ is a variable that does not occur in $\varphi$.
We check what these say in a structure $\mathcal{M}$ with domain $M$.

1. $\mathcal{M} \models \lambda_2$ exactly when there are $a, b \in M$ with $a \neq b$, because $=$ means identity. So $\lambda_2$ says $\abs{M} \ge 2$.
2. $\mathcal{M} \models \mu_1$ exactly when all $a, b \in M$ are equal. Since domains are nonempty, $\mu_1$ says $\abs{M} = 1$.
3. $\mu_1$ is logically equivalent to $\neg \lambda_2$: pushing $\neg$ through the quantifiers turns $\neg \exists x \, \exists y \, \neg (x = y)$ into $\forall x \, \forall y \, (x = y)$.
4. $\mathcal{M} \models \exists ! x \, \varphi$ exactly when some $a$ satisfies $\varphi$, and every $b$ that satisfies $\varphi$ equals $a$. So it says that exactly one element satisfies $\varphi$.
5. The condition on $y$ is needed. If $y$ were free in $\varphi$, then $\forall y$ would capture it and the formula would say something else.

So with $=$ a single sentence fixes a lower bound, an upper bound or an exact finite size of the domain.

## Remarks

The [[uniqueness quantifier|0QAJHFGZZJ]] $\exists !$ is not a primitive symbol: it abbreviates the formula in the example.
For each $n$, the sentence $\lambda_n = \exists x_1 \cdots \exists x_n \bigwedge_{i < j} \neg (x_i = x_j)$ says $\abs{M} \ge n$, and $\lambda_n \land \neg \lambda_{n+1}$ says $\abs{M} = n$.
No set of sentences says "$M$ is finite", by the compactness theorem.

## Explanations

### L1 human

With the equals sign, one can count in logic.
"There are $x$ and $y$ that are not equal" means there are at least two things.
"Any two things are equal" means there is only one thing.
"There is exactly one solution" is "there is a solution, and every solution equals it".

### L2 human

We check $\exists ! x \, (x \cdot x = x)$ in the group $\Z / 6 \Z$ under addition, written with $\cdot$ for the group operation.

1. The element $0$ satisfies $0 + 0 = 0$.
2. If $a + a = a$, then adding $-a$ gives $a = 0$.
3. So exactly one element satisfies $x \cdot x = x$, and the sentence is true.
4. In the monoid $(\Z / 6 \Z, \cdot)$ with multiplication, the elements $0$, $1$, $3$ and $4$ satisfy $x \cdot x = x$, so the sentence is false there.

The typical use of these sentences is in axioms such as "the identity is unique" and in size conditions on models.
A trap: $\exists x \, \exists y \, (x \neq y)$ says "at least two", not "exactly two".
