---
records:
    - id: RY7ED9B8MB
      kind: problem-set
      title: BMO Round 2 2023
      date: "2023-01-25"
      expressions:
        - key: e1
          kind: edition
          date: "2023-01-25"
          structure: RY7ED9B8MB/e1.json
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
          native_id: bmo2-2023
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
