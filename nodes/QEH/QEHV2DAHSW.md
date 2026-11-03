---
tag: QEHV2DAHSW
kind: definition
name: Reductive Lie group
msc: ["22E46", "22E15"]
defines: 42ZCE14AD2
uses: [7JBRGCVJRB]
sources:
  - url: https://en.wikipedia.org/wiki/Reductive_group
---

## Definition

Let $G$ be a real or complex [[Lie group|7JBRGCVJRB]], and let $\mathfrak{g}$ be its [[Lie algebra|WKVBS76432]], with centre $\mathfrak{z}(\mathfrak{g})$ and derived algebra $[\mathfrak{g}, \mathfrak{g}]$.
The group $G$ is a *reductive Lie group* if $\mathfrak{g}$ is a [[reductive Lie algebra|T4S70DDW0A]], that is:
$$\mathfrak{g} = \mathfrak{z}(\mathfrak{g}) \oplus [\mathfrak{g}, \mathfrak{g}] \quad \text{and} \quad [\mathfrak{g}, \mathfrak{g}] \text{ is semisimple}.$$

## Remarks

Over a field of characteristic $0$, $\mathfrak{g}$ is reductive exactly when its adjoint representation is completely reducible.

Example: $G = GL_n(\R)$ with $n \ge 1$.
Here $\mathfrak{g} = \mathfrak{gl}_n(\R)$, whose centre is the scalar matrices $\R I_n$ and whose derived algebra is $\mathfrak{sl}_n(\R)$, the trace-zero matrices.
Every matrix $X$ is uniquely $\frac{\tr X}{n} I_n + \left(X - \frac{\tr X}{n} I_n\right)$, so $\mathfrak{g} = \R I_n \oplus \mathfrak{sl}_n(\R)$, and $\mathfrak{sl}_n(\R)$ is $0$ or simple, hence semisimple.

Non-example: the group $B$ of invertible real upper triangular $2 \times 2$ matrices.
Its Lie algebra $\mathfrak{b}$ of upper triangular matrices has centre $\R I_2$ and derived algebra $\mathfrak{n}$ of strictly upper triangular matrices.
Then $\mathfrak{z}(\mathfrak{b}) \oplus \mathfrak{n}$ has dimension $2$, not $3$, and $\mathfrak{n}$ is abelian and nonzero, so not semisimple; both conditions fail.

Many authors add further conditions, for example that $G$ has finitely many connected components, or that $G$ is the group of real points of a reductive algebraic group.
Under the definition above, connected semisimple Lie groups and compact Lie groups are reductive.
