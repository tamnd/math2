---
tag: 00N5FHP1CV
kind: statement
role: theorem
name: Change of variables in multiple integrals
aliases: [substitution-rule-several-variables, jacobian-change-of-variables]
msc: [26B15]
uses: [03W6Q1MFR5, 0Z1Y7JHGBR, 0TCBZMEYGN, 0NKBMFC18R]
sources:
  - url: https://en.wikipedia.org/wiki/Integration_by_substitution
    locator: Substitution for multiple variables
---

## Statement

Let $U \subseteq \mathbb{R}^n$ be open, and let $\varphi \colon U \to \mathbb{R}^n$ be injective and of [[class C^1|0TCBZMEYGN]] with $\det D\varphi(u) \ne 0$ for each $u \in U$.
Let $f \colon \varphi(U) \to \mathbb{R}$ be continuous with compact support in $\varphi(U)$.
Then
$$\int_{\varphi(U)} f(v) \, dv = \int_U f(\varphi(u)) \, \lvert \det D\varphi(u) \rvert \, du.$$

## Remarks

Here $\det D\varphi(u)$ is the [[Jacobian determinant|03W6Q1MFR5]] of $\varphi$ at $u$. Under these hypotheses, $\varphi(U)$ is open and $\varphi$ is a [[diffeomorphism|0Z1Y7JHGBR]] from $U$ onto $\varphi(U)$.
The factor $\lvert \det D\varphi(u) \rvert$ is the ratio by which $\varphi$ scales small volumes near $u$. A linear map $A$ maps the unit cube to a parallelepiped of volume $\lvert \det A \rvert$.
The formula extends to Lebesgue integrable $f$ on $\varphi(U)$, and to maps that fail the hypotheses only on a set of measure zero.
Important cases are [[integration in polar coordinates|0T89W1QZ9K]], cylindrical coordinates and [[spherical coordinates|05WKRC7HWT]].

## Explanations

### L1 human

In one variable, substitution needs the factor $\varphi'(u)$. In several variables, the Jacobian determinant plays this role.
It corrects for the way the change of coordinates stretches or squeezes small regions.
