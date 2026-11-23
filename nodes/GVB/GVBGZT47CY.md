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

Work in [[first-order logic with equality|Q1494G7FBM]] over any signature, and consider the [[sentences|DKFGQTRYZE]]
$$\lambda_2 = \exists x \, \exists y \, \neg (x = y), \qquad \mu_1 = \forall x \, \forall y \, (x = y).$$
For a formula $\varphi$ with the free variable $x$, and a variable $y$ that does not occur in $\varphi$, also consider
$$\exists ! x \, \varphi \;:=\; \exists x \, \big( \varphi \land \forall y \, (\varphi[y/x] \to y = x) \big).$$
We check what each says in a structure $\mathcal{M}$ with domain $M$.

1. $\mathcal{M} \models \lambda_2$ exactly when there are $a, b \in M$ with $a \neq b$, because $=$ means identity.
   So $\lambda_2$ says $|M| \ge 2$.
2. $\mathcal{M} \models \mu_1$ exactly when any two elements of $M$ are the same.
   Domains are nonempty, so $\mu_1$ says $|M| = 1$.
3. $\mu_1$ is logically equivalent to $\neg \lambda_2$.
   Push the negation inward: $\neg \exists x \, \exists y \, \neg (x = y)$ becomes $\forall x \, \neg \exists y \, \neg (x = y)$, then $\forall x \, \forall y \, \neg \neg (x = y)$, which is $\mu_1$.
4. $\mathcal{M} \models \exists ! x \, \varphi$ exactly when some $a$ satisfies $\varphi$ and every $b$ that satisfies $\varphi$ is $a$.
   So it says that exactly one element satisfies $\varphi$.
5. The condition on $y$ matters.
   If $y$ were free in $\varphi$, the quantifier $\forall y$ would capture it, and the formula would say something else.

So with $=$ a single sentence can give a lower bound, an upper bound or an exact finite size for the domain.

## Remarks

The [[uniqueness quantifier|0QAJHFGZZJ]] $\exists !$ is not a primitive symbol; it is short for the formula above.
For each $n \ge 2$ the sentence
$$\lambda_n = \exists x_1 \cdots \exists x_n \bigwedge_{1 \le i < j \le n} x_i \neq x_j$$
says $|M| \ge n$, and $\lambda_n \land \neg \lambda_{n+1}$ says $|M| = n$.
For $n = 3$ the conjunction has the three parts $x_1 \neq x_2$, $x_1 \neq x_3$ and $x_2 \neq x_3$.

What no set of sentences can say is "$M$ is finite".
If a set $\Sigma$ had exactly the finite structures as models, then $\Sigma \cup \{ \lambda_n : n \ge 2 \}$ would be finitely satisfiable, and the compactness theorem would give an infinite model of $\Sigma$.
Without equality even $\lambda_2$ has no equivalent, as [[the doubling construction|92DFZ28TR7]] shows.

## Explanations

### L1 human

With the equals sign you can count in logic.
"There are $x$ and $y$ that are not equal" means there are at least two things.
"Any two things are equal" means there is only one thing.
"There is exactly one solution" means "there is a solution, and every solution equals it".

### L2 human

We check $\exists ! x \, (x \cdot x = x)$ in two structures with domain $\{ 0, 1, 2, 3, 4, 5 \}$.

First read $\cdot$ as addition mod $6$.
The element $0$ works, since $0 + 0 = 0$.
If $a + a = a$, add $-a$ to both sides to get $a = 0$.
So exactly one element works, and the sentence is true.

Now read $\cdot$ as multiplication mod $6$.
Square each element:
$$0^2 = 0, \quad 1^2 = 1, \quad 2^2 = 4, \quad 3^2 = 9 \equiv 3, \quad 4^2 = 16 \equiv 4, \quad 5^2 = 25 \equiv 1.$$
So $0$, $1$, $3$ and $4$ satisfy $x \cdot x = x$, and the sentence is false.
The typical use of such sentences is in axioms like "the identity is unique" and in size conditions on models.
Watch out: $\exists x \, \exists y \, (x \neq y)$ says "at least two", not "exactly two".
