---
records:
    - id: NBBCWFCDW2
      kind: monograph
      title: Functional Analysis in Mechanics
      creators:
        - name: Leonid P. Lebedev
          role: author
        - name: Iosif I. Vorovich
          role: author
        - name: Michael J. Cloud
          role: author
      date: "2003"
      expressions:
        - key: e1
          kind: edition
          date: "2003"
          ids:
            doi:
                - 10.1007/978-1-4614-5868-5
                - 10.1007/b98851
          manifestations:
            - key: m1
              kind: print
              publisher: Springer New York
              date: "2013"
              ids:
                isbn:
                    - "9781461458678"
                    - "9781461458685"
            - key: m2
              kind: print
              publisher: Springer New York
              date: "2003"
              ids:
                isbn:
                    - "9781441930354"
                    - "9780387227252"
      relations:
        - kind: part_of
          to: FA5PXCH6G7
          source: cluster/1
      scope:
        value: in
        rule: S4
        by: m2 v0.6.2 scope/1
      catalogue:
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/978-1-4614-5868-5
          level: work
        - source: springer-series
          snapshot: blake3:09492c429ae54789c72bd081d21b950751ebbf0910012c1957fb140a008b7b5e
          native_id: 10.1007/b98851
          level: work
      history:
        - op: add
          at: "2026-10-31"
          by: m2 v0.6.2 cluster/1
        - op: scope
          at: "2026-10-31"
          by: m2 v0.6.2 scope/1
          note: to in
    - id: NBBZ4MME4T
      kind: problem-set
      title: BMO Round 1 1998
      date: "1998-01-14"
      expressions:
        - key: e1
          kind: edition
          date: "1998-01-14"
          structure: NBBZ4MME4T/e1.json
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
          native_id: bmo1-1998
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
