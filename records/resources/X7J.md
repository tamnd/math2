---
records:
    - id: X7JWV4D7Z2
      kind: problem-set
      title: BMO Round 2 2000
      date: "2000-02-23"
      expressions:
        - key: e1
          kind: edition
          date: "2000-02-23"
          structure: X7JWV4D7Z2/e1.json
      relations:
        - kind: part_of
          to: 8XFPR5H74Q
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.4 scope/1
      catalogue:
        - source: bmo
          snapshot: blake3:68eb2251465334659a3c67c12bc8e13877594a5a11510cf9a756eaf0f62db81c
          native_id: bmo2-2000
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
---
