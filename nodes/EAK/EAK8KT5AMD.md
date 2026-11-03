---
tag: EAK8KT5AMD
kind: concept
name: Quaternions and spatial rotation
msc: [70B10, 15B10, "22E70"]
sources:
  - url: https://en.wikipedia.org/wiki/Quaternions_and_spatial_rotation
same_as:
  wikidata: Q2634405
  wikipedia: Quaternions and spatial rotation
---

## Summary

Unit [[quaternions|0GE4DVQKR8]] describe [[rotations|0HFREYRSZP]] of three-dimensional space.
A unit quaternion $q$ acts on a vector $v$, viewed as a pure quaternion, by $v \mapsto q v \bar q$, and this map is a rotation.
The quaternion $\cos(\theta/2) + \sin(\theta/2)(u_1 i + u_2 j + u_3 k)$ gives the rotation by $\theta$ about the unit axis $u$, and $q$ and $-q$ give the same rotation.
This description avoids the gimbal lock of [[Euler angles|7WGBNTRQ2S]] and is used in mechanics, robotics, computer graphics and spacecraft attitude control.

## Explanations

### L1 human

A rotation in space is fixed by an axis and an angle, which makes four numbers once the axis is a unit vector.
Quaternions pack these four numbers into one object, and multiplying quaternions composes rotations.
The half angle is a surprise: turning by $360$ degrees corresponds to the quaternion $-1$, and only a turn by $720$ degrees brings back $1$.
For example, the quaternion $(1 + k)/\sqrt{2}$ turns space by a quarter turn about the vertical axis, sending the direction $i$ to the direction $j$.
