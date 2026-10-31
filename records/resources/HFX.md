---
records:
    - id: HFXC13NNG1
      kind: problem-set
      title: BMO Round 1 2023
      date: "2022-11-16"
      expressions:
        - key: e1
          kind: edition
          date: "2022-11-16"
          structure: HFXC13NNG1/e1.json
      relations:
        - kind: part_of
          to: 8XFPR5H74Q
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.2 scope/1
      catalogue:
        - source: bmo
          snapshot: blake3:68eb2251465334659a3c67c12bc8e13877594a5a11510cf9a756eaf0f62db81c
          native_id: bmo1-2023
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
    - id: HFXR5QG1FT
      kind: monograph
      title: Singular Homology Theory
      creators:
        - name: William S. Massey
          role: author
      date: "1980"
      expressions:
        - key: e1
          kind: edition
          date: "1980"
          ids:
            doi: 10.1007/978-1-4684-9231-6
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "1980"
              ids:
                isbn:
                    - "9781468492330"
                    - "9781468492316"
      relations:
        - kind: part_of
          to: 7ME1ABA6H5
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.2 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4684-9231-6
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
