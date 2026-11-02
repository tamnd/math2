---
tag: X9F8SQFQGP
kind: definition
name: Adjoint state method
msc: [49M41, 65K10, 49K20]
defines: YD8SA6WS01
uses: [0ABK9V9Y64, 047NDTEPCV, 0BXBADR94C, 0RXX2PT1MQ]
sources:
  - url: https://en.wikipedia.org/wiki/Adjoint_state_method
---

## Definition

Let $F \colon \R^n \times \R^p \to \R^n$ and $j \colon \R^n \times \R^p \to \R$ be continuously differentiable, written $F(u, \theta)$ and $j(u, \theta)$.
Let $\theta_0 \in \R^p$ and let $u(\theta)$ be a continuously differentiable map defined near $\theta_0$ with $F(u(\theta), \theta) = 0$.
Assume that the [[Jacobian matrix|047NDTEPCV]] $F_u = \partial F / \partial u$ is invertible at $(u(\theta), \theta)$.
Let $J(\theta) = j(u(\theta), \theta)$ be the reduced objective.
The *adjoint state* at $\theta$ is the vector $\lambda \in \R^n$ that solves the *adjoint equation*
$$F_u(u(\theta), \theta)^T \lambda = \nabla_u j(u(\theta), \theta).$$
The *adjoint state method* computes the [[gradient|0ABK9V9Y64]] of $J$ by the formula
$$\nabla J(\theta) = \nabla_\theta j(u(\theta), \theta) - F_\theta(u(\theta), \theta)^T \lambda.$$

## Remarks

The formula follows from the [[chain rule|0RXX2PT1MQ]].
Differentiating $F(u(\theta), \theta) = 0$ gives $F_u \, u'(\theta) = -F_\theta$, so $\nabla J^T = j_u u'(\theta) + j_\theta = -j_u F_u^{-1} F_\theta + j_\theta = -\lambda^T F_\theta + j_\theta$.
By the [[implicit function theorem|0BXBADR94C]], invertibility of $F_u$ at a solution gives the smooth map $u(\theta)$ locally.
The forward method needs $p$ linear solves with $F_u$, one for each column of $u'(\theta)$; the adjoint method needs one solve with $F_u^T$.
For a time-dependent state equation the adjoint equation runs backward in time; in optimal control it is the [[costate equation|WS9MRAZMFW]].

Example: $F(u, \theta) = A u - \theta$ with $A$ an invertible $n \times n$ matrix and $p = n$, and $j(u, \theta) = \frac{1}{2} \abs{u - d}^2$ for a fixed $d \in \R^n$.
Then $F_u = A$, $F_\theta = -I$ and $\nabla_\theta j = 0$, so $A^T \lambda = u - d$ and $\nabla J(\theta) = \lambda$.
Directly, $J(\theta) = \frac{1}{2} \abs{A^{-1} \theta - d}^2$ has gradient $A^{-T} (A^{-1} \theta - d) = \lambda$, as it should.

Non-example: let $n = p = 1$ and $F(u, \theta) = u^2 - \theta$, at the point $u = \theta = 0$, where $F_u = 0$ is singular.
The adjoint equation $0 \cdot \lambda = j_u$ need not have a solution, and the state is not a differentiable function of $\theta$ there.

## Explanations

### L1 human

The gradient of an objective constrained by an equation is found from one extra linear solve with the transposed Jacobian, whatever the number of parameters.
